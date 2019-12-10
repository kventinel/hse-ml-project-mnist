# Task

## K-means

1. Choose 3 to 6 features. Explain the choice.
2. Apply K-means:
    1. At K=5
    2. At K=9
    3. In both cases: 10 or more random initializations, choose the best solution over the K-means criterion; present it in a table.
3. Interpret each found partition by using features from the data table – as instructed in the lecture slides. Explain why you consider one of them better than the other in this perspective.

## Bootstrap

Take one of the partitions found in the previous work.

1. Take a feature, find the 95% confidence interval for its grand mean by using bootstrap.
2. Compare the within-cluster means for one of the features between two clusters using bootstrap.
3. Take a cluster, and compare the grand mean with the within- cluster mean for the feature by using bootstrap.

Note: each application of bootstrap should be done in both, pivotal and non-pivotal, versions.

## Contigency Table

1. Consider three nominal features (one of them, not more, may be taken from nominal features in your data).
2. Build two contingency tables over them: present a conditional frequency table and Quetelet relative index tables. Make comments on relations between categories of the common (to both tables) feature and two others.
3. Compute and visualize the chi-square- summary_Quetelet_index over both tables. Comment on the meaning of the values in the data analysis context.
4. Tell what numbers of observations would suffice to see the features as associated at 95% confidence level; at 99% confidence level.

## PCA/SVD

1. In your data set, select a subset of 3-6 features related to the same aspect and explain your choice (may be the same subset that was used for k-means clustering).
2. Standardize the selected subset; compute its data scatter and SVD; determine contributions of all the principal components to the data scatter, naturally and per cent.
3. Compute and interpret a hidden ranking factor behind the selected features. The factor should be expressed in a 0-100 rank scale (as well as the features – ranking normalization).
4. Visualize the data using two first principal components at the standardization with two versions of normalization: (a) range normalization and (b) z-scoring. At these visualizations, use a distinct shape/color for points representing a pre-specified by you group of objects. Also, apply the conventional PCA for finding two first principal components and visualization; compare to the results at z-scoring. Comment on which of the
normalizations is better and why.

## Correlation Coefficient

1. Find two features in your dataset with more or less “linear-like” scatterplot.
2. Display the scatter-plot and comment how well it is suitable for building a linear regression.
3. Build a linear regression of one of the features over the other. Make a comment on the meaning of the slope.
4. Find the correlation and determinacy coefficients, and comment on the meaning of the latter.
5. Make a prediction of the target values for given two or three predictor’ values; make a comment.
6. Compare the mean relative absolute error of the regression on all points of your set and the determinacy coefficient and make comments.
