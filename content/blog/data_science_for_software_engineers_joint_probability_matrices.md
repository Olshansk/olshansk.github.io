
# Data Science for Software Engineers — Joint Probability Matrices

Joint Probability Matrices — An “Extension of the Confusion Matrix” for Continuous Variables

*If you’re just interested in the code, the Jupyter notebook is available [here](https://github.com/Olshansk/data_science_for_swe/blob/master/transition_matrix/Transition%20Matrix.ipynb). Big thanks to [Albert Altarovici](https://www.linkedin.com/in/altarovici/) for explaining fundamental Data Science concepts and reviewing this article.*

When measuring the performance of a prediction model (i.e. a Machine Learning classification algorithm), there are 4 metrics you are likely to measure and reference: [Precision, Recall](https://en.wikipedia.org/wiki/Precision_and_recall), Accuracy and [F-score.](https://en.wikipedia.org/wiki/F1_score) A common visual method to interpret these results is via a [Confusion Matrix](https://en.wikipedia.org/wiki/Confusion_matrix). A lot of great articles have already been [written](https://towardsdatascience.com/understanding-confusion-matrix-a9ad42dcfd62) about these topics, so I won’t delve into too many details.

For a binary classification problem, the ground truth data (also referred to as target values) are binary (0 or 1), and the predicted value is some value between 0 and 1. There are a few things to keep in mind here:

* A threshold needs to be selected to determine if a predicted value should be rounded up or down. This threshold needs to be chosen based on some cutoff that balances tradeoffs in your model.

* For categorical data (more than two options), we need to use [one-hot encoding](https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/) and perform multiple pairwise analyses.

* Classification metrics (accuracy, prediction, recall, f1-score) are only defined for discrete values. When predicting a continuous value, we are generally more interested in regression metrics (e.g. RMSE, MAE) as described well in this [Stack Overflow answer](https://stackoverflow.com/questions/49103139/calculating-accuracy-scores-of-predicted-continuous-values).

I was recently introduced to joint probability matrices, which can be thought of as an extension to confusion matrices when your data is non-categorical, but you still want to visualize the data patterns in a similar fashion. Most importantly, it can be used to easily identify outliers in your data, which will lead you to specific examples where a large discrepancy occurs between your target values and predicted values, which will hopefully help you fine tune your model. This is easiest to illustrate via an example.

Consider a class of 30 students who took a test and received a grade between 0 and 100 that is normally distributed. Let’s assume that the mean and standard deviation are 80% and 20% respectively; this will be our ground truth data. Our model will predict a grade for each student that is also between 0…
