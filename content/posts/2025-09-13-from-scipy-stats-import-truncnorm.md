---
title: "from scipy.stats import truncnorm"
date: 2025-09-13T12:00:00-07:00
draft: true
description: ""
tags: []
categories: []
medium_url: ""
substack_url: ""
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

* * *

###   


from scipy.stats import truncnorm

# <https://stackoverflow.com/a/43641446/768439>

def background_gradient(s, m=None, M=None, cmap=’Reds’, low=0, high=0):

if m is None:

m = s.min().min()

if M is None:

M = s.max().max()

rng = M — m

norm = colors.Normalize(m — (rng * low), M + (rng * high))

normed = s.apply(lambda x: norm(x.values))

cm = plt.cm.get_cmap(cmap)

c = normed.applymap(lambda x: colors.rgb2hex(cm(x)))

ret = c.applymap(lambda x: ‘background-color: %s’ % x)

return ret

# Firstly, we’ll be using scipy’s truncnorm instead of numpy random to avoid

# values < 0 or > 100

# Using: <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.truncnorm.html>

mean = 70

std = 20

min_clip = 0

max_clip = 100

a, b = (min_clip — mean) / std, (max_clip — mean) / std

# Generate marks for two classes (note that they’re of different sizes)

classA = pd.Series(truncnorm.rvs(a, b, loc=mean, scale=std, size=30))

classB = pd.Series(truncnorm.rvs(a, b, loc=mean, scale=std, size=30))

# I’m adding these to make sure we handle our edge cases correctly (more on it later)

idx = max(classA.index)

classA = classA.append(pd.Series([100, 0], index=[idx+1, idx+2]), verify_integrity=True)

# Quickly visualize the data

df = pd.DataFrame({‘classA’: classA, ‘classB’: classB})

df.plot.hist(alpha=0.5)

# display(df)

# Many binning strategies, but here we are using 10 bins between 0 and 100 explicitly. Look at docs for more

num_bins = 10

bins = [i * num_bins for i in range(num_bins + 1)]

# Figure out which bin every value is in

outA = pd.cut(classA, bins=bins, include_lowest=True, right=True)

outB = pd.cut(classB, bins=bins, include_lowest=True, right=True)

# Verify for personal understanding and validate the edge cases

# for idx, grade in classA.iteritems():

# print(idx, grade, outA[idx])

# Show the output of this

# <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.groupby.html>

# If a dict or Series is passed, the Series or dict VALUES will be used to determine the groups (the Series’ values are first aligned; see .align() method)

# type(out)

# pandas.core.series.Series

# Probability distribution analysis

classACounts = classA.groupby(outA).count()

classBCounts = classB.groupby(outB).count()

classATotalCount = classACounts.values.sum()

classBTotalCount = classACounts.values.sum()

totalCount = classATotalCount + classBTotalCount

classAPD = classACounts.apply(lambda c: c / classATotalCount)

classBPD = classBCounts.apply(lambda c: c / classBTotalCount)

pdProduct = np.matrix.round(np.multiply(classAPD.values.reshape(1,num_bins), classBPD.values.reshape(num_bins,1)), 2)

# Goal: Most of the weight is around the diagonal

df = pd.DataFrame(pdProduct, columns=axis, index=axis)

df.columns.name = “Class A”

df.index.name = “Class B”

df = df.style.set_caption(“Probability distribution product”).apply(background_gradient, high=1, axis=None)

display(df)

# Counts analysis

trans_matrix = [[0] * num_bins for _ in range(num_bins)]

for bA, cA in enumerate(classACounts.values.tolist()):

for bB, cB in enumerate(classBCounts.values.tolist()):

trans_matrix[bA][bB] = cA + cB

np_trans_matrix = np.matrix(trans_matrix)

delta_matrix = abs(np_trans_matrix — np_trans_matrix.transpose())

other_matrix = np.round(abs(np_trans_matrix — np_trans_matrix.transpose()) / (abs(np_trans_matrix + np_trans_matrix.transpose())), 2)

# Goal: Small numbers wherever possible

df = pd.DataFrame(np_trans_matrix, columns=axis, index=axis)

df.columns.name = “Class A”

df.index.name = “Class B”

df = df.style.set_caption(“Counts matrix abs(original — transpose)”).apply(background_gradient, high=1, axis=None)

display(df)

  

