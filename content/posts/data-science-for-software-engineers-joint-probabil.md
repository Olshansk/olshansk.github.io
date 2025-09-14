---
title: "Data Science for Software Engineers — Joint Probability Matrices"
date: 2020-05-25T23:31:48-07:00
draft: false
tags: ["ai", "data-science", "machine-learning", "python"]
categories: ["Data Science", "Technology", "AI"]
summary: "Joint Probability Matrices — An 'Extension of the Confusion Matrix' for Continuous Variables"
medium_url: "https://medium.com/@olshansky/data-science-for-software-engineers-joint-probability-matrices-f4fcb94d1483"
ShowToc: true
---

_If you're just interested in the code, the Jupyter notebook is available [here](https://github.com/Olshansk/data_science_for_swe/blob/master/transition_matrix/Transition%20Matrix.ipynb). Big thanks to [Albert Altarovici](https://www.linkedin.com/in/altarovici/) for explaining fundamental Data Science concepts and reviewing this article._

When measuring the performance of a prediction model (i.e. a Machine Learning classification algorithm), there are 4 metrics you are likely to measure and reference: [Precision, Recall](https://en.wikipedia.org/wiki/Precision_and_recall), Accuracy and [F-score](https://en.wikipedia.org/wiki/F1_score). A common visual method to interpret these results is via a [Confusion Matrix](https://en.wikipedia.org/wiki/Confusion_matrix). A lot of great articles have already been [written](https://towardsdatascience.com/understanding-confusion-matrix-a9ad42dcfd62) about these topics, so I won't delve into too many details.

For a binary classification problem, the ground truth data (also referred to as target values) are binary (0 or 1), and the predicted value is some value between 0 and 1. There are a few things to keep in mind here:

- A threshold needs to be selected to determine if a predicted value should be rounded up or down. This threshold needs to be chosen based on some cutoff that balances tradeoffs in your model.
- For categorical data (more than two options), we need to use [one-hot encoding](https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/) and perform multiple pairwise analyses.
- Classification metrics (accuracy, prediction, recall, f1-score) are only defined for discrete values. When predicting a continuous value, we are generally more interested in regression metrics (e.g. RMSE, MAE) as described well in this [Stack Overflow answer](https://stackoverflow.com/questions/49103139/calculating-accuracy-scores-of-predicted-continuous-values).

I was recently introduced to joint probability matrices, which can be thought of as an extension to confusion matrices when your data is non-categorical, but you still want to visualize the data patterns in a similar fashion. Most importantly, it can be used to easily identify outliers in your data, which will lead you to specific examples where a large discrepancy occurs between your target values and predicted values, which will hopefully help you fine tune your model. This is easiest to illustrate via an example.

## Example: Student Grades Prediction

Consider a class of 30 students who took a test and received a grade between 0 and 100 that is normally distributed. Let's assume that the mean and standard deviation are 80% and 20% respectively; this will be our ground truth data. Our model will predict a grade for each student that is also between 0 and 100. For simplicity, we'll model our predictions using a random set of numbers that has the same distribution as the actual data.

The following snippet of code will generate our mocked data:

```python
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, explained_variance_score
import matplotlib.pyplot as plt
import seaborn as sns

# Generate ground truth data
np.random.seed(42)
n_students = 30
grades_GT = np.random.normal(80, 20, n_students)
grades_GT = np.clip(grades_GT, 0, 100)  # Ensure grades are between 0 and 100

# Generate predicted data (random for demonstration)
grades_P = np.random.normal(80, 20, n_students)
grades_P = np.clip(grades_P, 0, 100)
```

Next, we illustrate a few methods of comparing our ground truth data to our predicted data using regression analysis methods. The following snippet of code will output several regression metric values, plot the [Probability Density Function](https://en.wikipedia.org/wiki/Probability_density_function), as well as a histogram showing the frequency distribution of the grades. [Fritz AI](https://heartbeat.fritz.ai/) has a [fantastic article](https://heartbeat.fritz.ai/5-regression-loss-functions-all-machine-learners-should-know-4fb140e9d4b0) about the different regression analysis methods and their tradeoffs, so we won't delve into the details.

```python
# Calculate regression metrics
mse = mean_squared_error(grades_GT, grades_P)
mae = mean_absolute_error(grades_GT, grades_P)
evs = explained_variance_score(grades_GT, grades_P)

print(f"mean_squared_error:  {mse:.1f}")
print(f"mean_absolute_error:  {mae:.2f}")
print(f"explained_variance_score:  {evs:.2f}")

# Plot distributions
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Probability density function
ax1.hist(grades_GT, alpha=0.7, label='Ground Truth', bins=10)
ax1.hist(grades_P, alpha=0.7, label='Predicted', bins=10)
ax1.set_xlabel('Grade')
ax1.set_ylabel('Frequency')
ax1.set_title('Grade Distribution Comparison')
ax1.legend()

# Scatter plot
ax2.scatter(grades_GT, grades_P)
ax2.plot([0, 100], [0, 100], 'r--', label='Perfect Prediction')
ax2.set_xlabel('Ground Truth Grade')
ax2.set_ylabel('Predicted Grade')
ax2.set_title('Predicted vs Ground Truth')
ax2.legend()

plt.tight_layout()
plt.show()
```

The code snippet above will generate the following output:

```
mean_squared_error:  733.4
mean_absolute_error:  21.54
explained_variance_score:  -1.15
```

![Grade Distribution Comparison and Scatter Plot](https://cdn-images-1.medium.com/max/800/1*O_W3XR3dDvAT73YwpdvehQ.png)

From the graphs above, we see that the two data sets follow a similar pattern, which is expected because they're both normally distributed with the same mean and standard deviation. However, the regression analysis metrics (i.e. Mean Squared Error) are showing that our data is essentially senseless, which is also expected because we generated our data randomly. This means that while our on aggregate, the distribution is similar, individual values (e.g. predicted grade of Student A vs actual grade of StudentA) are very different.

In order to determine where the biggest variations lie, we can use a joint probability matrix.

## Joint Probability Matrix

The joint probability matrix for the data above will look as follows:

![Joint Probability Matrix Heatmap](https://cdn-images-1.medium.com/max/800/1*1JPRowHYciToCXH36VqdaQ.png)

How do we interpret this data? For example, the red title on the 2nd last row, with a value of 0.07 means that 7% of the students (2 in our case) who actually received a grade between 80%-90%, were predicted to receive a grade between 50%-60% by our model. Next, one would manually inspect this small portion of hand-picked outliers and start drawing conclusions about changes that need to be made to the prediction model. This sort of analysis could lead to interesting followup investigations, but was obfuscated by the regression analysis done above. Perhaps the model is is very biased to under-predict the grade of high performers, perhaps it is just a bug in the code, etc…

The table above can be generated using the following code snippet:

```python
def create_joint_probability_matrix(ground_truth, predicted, bins):
    # Create categorical buckets for continuous data
    gt_cut = pd.cut(ground_truth, bins, include_lowest=True)
    pred_cut = pd.cut(predicted, bins, include_lowest=True)

    # Create DataFrames with bucket assignments
    df_gt = pd.DataFrame({'ground_truth_bucket': gt_cut})
    df_pred = pd.DataFrame({'predicted_bucket': pred_cut})

    # Add index to merge on
    df_gt['student_id'] = df_gt.index
    df_pred['student_id'] = df_pred.index

    # Merge the dataframes
    df_merged = df_gt.merge(df_pred, on='student_id')

    # Create cross-tabulation (joint frequency matrix)
    joint_freq = pd.crosstab(
        df_merged['ground_truth_bucket'],
        df_merged['predicted_bucket'],
        normalize=True
    )

    # Format and display as heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(joint_freq, annot=True, fmt='.2f', cmap='Reds')
    plt.title('Joint Probability Matrix')
    plt.xlabel('Predicted Grade Bucket')
    plt.ylabel('Ground Truth Grade Bucket')
    plt.show()

    return joint_freq
```

By making the following function call:

```python
bins = np.linspace(0, 100, 11)
create_joint_probability_matrix(grades_GT, grades_P, bins)
```

All you need to provide is a list of the target values, the predicted values, and a list of bins of how you want to discretize the data.

In the ideal scenario, where our model is 100% accurate in predicting our ground truth data, all of the values in the joint probability matrix will lie across the diagonal. For example, building a joint probability between the the same set of values will produce the following output:

```python
create_joint_probability_matrix(grades_GT, grades_GT, bins)
```

![Perfect Diagonal Joint Probability Matrix](https://cdn-images-1.medium.com/max/800/1*rv5AU7L9NM4fcaO_DB_vhQ.png)

For example, the table above shows that 27% of students who had an actual grade between 60–70%, were also predicted to have a grade between 60–70%. More importantly, all cells outside of the diagonal above are 0, meaning our model made no mistakes (because we're comparing the exact same set of values).

That's all there is to it. This doesn't replace anything in your toolbox, but simply provides an additional method to inspect discrepancies in your predicted data for continuous variables, which can hopefully lead you down the right path in tuning your model.

_Feel free to stop reading now if you're not interested in a breakdown of the create_joint_probability_matrix function above._

## Implementation Details

For those who are less familiar with Pandas, like myself, this section will describe some of the operations we performed above.

Once we have our data, we need to split it into 10 equally sized buckets. This decision is kind of arbitrary and up to the discretion of the analyst.

```python
# Create bins for discretizing continuous data
bins = np.linspace(0, 100, 11)  # Creates 10 equally-sized buckets
gt_cut = pd.cut(grades_GT, bins, include_lowest=True)
pred_cut = pd.cut(grades_P, bins, include_lowest=True)
```

The output of the the cut function will simply assign a range (i.e. a bucket) to each value. The output of the above code snippet will output:

![Bucket Assignments Table](https://cdn-images-1.medium.com/max/800/1*nxWf05lxYsnHXJch19JGVw.png)

Next, we need to transform the DataFrames so they can be merged together:

```python
# Create DataFrames with student IDs
df_gt = pd.DataFrame({
    'student_id': range(len(grades_GT)),
    'ground_truth_bucket': gt_cut
})

df_pred = pd.DataFrame({
    'student_id': range(len(grades_P)),
    'predicted_bucket': pred_cut
})

# Merge on student ID
df_merged = df_gt.merge(df_pred, on='student_id')
```

I personally found it easiest to understand what the commands above do by inspecting small portions of the DataFrame at each step.

1. Assign a student ID (i.e. index) to each student and associate it with the bucket that their grade is in; both in the predicted and ground truth tables.
2. Merge the two tables based on the student ID.
3. Create a multi-leveled pandas DataFrame that provides a count of the number of students

![DataFrame Screenshot](https://cdn-images-1.medium.com/max/800/1*Gr4WqRcm1mt6rv1VDpJJEw.png)

Next, we take the 2D array and convert the count values to percentages based on the total number of students in our dataset:

```python
# Create joint probability matrix using crosstab with normalization
joint_prob = pd.crosstab(
    df_merged['ground_truth_bucket'],
    df_merged['predicted_bucket'],
    normalize=True  # This converts counts to probabilities
)
```

This will produce the following output:

![Probability Matrix Table](https://cdn-images-1.medium.com/max/800/1*BtQ7bTImSg8vp2PJUf7Gmg.png)

A quick check to make sure this step is correct is by verifying that the sum of all values in your DataFrame add up to 1.

Lastly, we simply want to format the output table so it's more readable by rounding our values, and applying a background gradient to easily see where the outlier cells are. The following code snippet:

```python
# Format and visualize the joint probability matrix
styled_matrix = joint_prob.round(2).style.background_gradient(cmap='Reds')
display(styled_matrix)
```

Will format the table above into this one:

![Final Formatted Heatmap](https://cdn-images-1.medium.com/max/800/1*iOSRMdGfWEoTVqHvv2c0IA.png)
