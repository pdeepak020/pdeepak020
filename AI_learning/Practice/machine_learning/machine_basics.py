
#machine learning = prediction based on data

#leran the patern using historuical data and do prediction based on the pattern learned from the historical data
#machine learning = using algorithms to learn from data and make predictions or decisions without being explicitly programmed


#supervised learning = training data with labels
#we data with input and output
#input = features, output = labels
#unsupervised learning = training data without labels - used for recommendations
#we data with input only
#input = features, output = none
#reinforcement learning = training data with feedback
#ensemble learning = combining multiple models to improve performance
#transfer learning = using a pre-trained model on a new task
#deep learning = using neural networks with many layers

#regression = predicting a continuous value
#classification = predicting a discrete value



#algortihms -
# ...existing code...

# Types of ML algorithms

# 1. Supervised Learning Algorithms
# - Linear Regression
# - Logistic Regression
# - Decision Trees
# - Random Forest
# - Support Vector Machines (SVM)
# - k-Nearest Neighbors (k-NN)
# - Naive Bayes

# 2. Unsupervised Learning Algorithms
# - K-Means Clustering
# - Hierarchical Clustering
# - Principal Component Analysis (PCA)
# - Association Rule Learning (e.g., Apriori)

# 3. Reinforcement Learning Algorithms
# - Q-Learning
# - Deep Q-Networks (DQN)
# - Policy Gradient Methods

# 4. Ensemble Methods
# - Bagging (e.g., Random Forest)
# - Boosting (e.g., AdaBoost, Gradient Boosting)
# - Stacking

# 5. Deep Learning Algorithms
# - Artificial Neural Networks (ANN)
# - Convolutional Neural Networks (CNN)
# - Recurrent Neural Networks (RNN)
# - Long Short-Term Memory (LSTM)
# - Generative Adversarial Networks (GAN)

# ...existing code...


#linear regression = predicting a continuous value based on a linear relationship between input features and output labels

#y = mx + b
#y = dependent variable (output)
#x = independent variable (input)
#m = slope of the line (coefficient) - feature coefficient
#b = y-intercept (constant term)

#we can use multiple features/columns in the dataset to predict the output
#y = m1x1 + m2x2 + m3x3 + ... + b - training data with multiple features/columns

#evaluation metrics for regression
#1. Mean Absolute Error (MAE) = average of absolute differences between predicted and actual values
#2. Mean Squared Error (MSE) = average of squared differences between predicted and actual values
#3. Root Mean Squared Error (RMSE) = square root of MSE - varies with the scale of the data -infinity to +infinity
#4. R-squared (R2) = proportion of variance in the dependent variable that can be explained by the independent variables - 0 to 1


#overfitting - traing data data performs well but test data does not perform well
#underfitting - training data and test data both perform poorly
#bias error - error due to assumptions made by the model - this happens for training data
#variance error - error due to sensitivity to small fluctuations in the training data - this happens for test data

#low bias and high variance - overfitting
#high bias and low variance - underfitting 
#underfitting is decided by baised on the client requirement, if requirement is 70% accuracy then 
# we can say that model is underfitting if it is giving 60% accuracy, if requirement is 90% accuracy then we can say that model is underfitting if it is giving 80% accuracy

#if traing and test data r2 score is 10% deviated then it is called overfitting

#optimal model - where the traing and test data both performe well

#change in randome state will change the model performance
#random state = seed value for random number generator - it is used to make the results reproducible

#cross validation = technique to evaluate the performance of a model by splitting the data into multiple subsets and training/testing the model on different combinations of these subsets
# Explanation:
# - cross_val_score splits the data into 5 parts (folds).
# - It trains the model on 4 folds and tests on the remaining fold.
# - This is repeated 5 times, each time using a different fold for testing.
# - The cv_scores array contains the R-squared score for each of the 5 iterations.
# - The mean cross-validation score is the average of these scores, giving an overall estimate of the model's performance.


#regularization = technique to prevent overfitting by adding a penalty term to the loss function
#lasso regression = linear regression with L1 regularization = yactual - (mx + b) + λ|m| (L1 regularization) where (mx + b) + λ|m| is predicted value
#ridge regression = linear regression with L2 regularization = yactual -  mx + b + λm^2 (L2 regularization)where (mx + b) + λm^2 is predicted value


#advantage of linear regression
#1. Simple to understand and interpret 
#2. Computationally efficient
#3. Works well with linearly separable data
#4. Can be used for both regression and classification tasks
#disadvantage of linear regression
#1. Assumes a linear relationship between input features and output labels
#2. Sensitive to outliers
#3. Cannot capture complex relationships in the data
#4. Can suffer from multicollinearity (when two or more independent variables are highly correlated)
#5. Assumes homoscedasticity (constant variance of errors)
#6. Assumes independence of errors (errors are not correlated)
#7. Assumes normality of errors (errors are normally distributed)
#8. Can be affected by multicollinearity (when two or more independent variables are highly correlated) 

#performation of linear regression can be improved by feature engineering, feature selection, and regularization techniques
#feature engineering = process of creating new features from existing features to improve the performance of the model
#feature selection = process of selecting the most important features from the dataset to improve the performance of the model
#regularization techniques = L1 and L2 regularization to prevent overfitting by adding a penalty term to the loss function

#performaace measure of linear regression can be done using evaluation metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared (R2)

#multicollinearity = when two or more independent variables are highly correlated, it can lead to unstable estimates of the coefficients and make it difficult to interpret the model

#polynomial regression = extension of linear regression where the relationship between the independent variable and dependent variable is modeled as an nth degree polynomial
#polynomial regression is used when the relationship between the independent variable and dependent variable is non-linear
#polynomial regression formula = y = b0 + b1*x + b2*x^2 + b3*x^3 + ... + bn*x^n

#classification - supervised learning task where the output variable is categorical (discrete) and the goal is to predict the class label of new data points based on the input features

#binary classification = classification task where the output variable has two classes (e.g., spam or not spam, positive or negative)
#multiclass classification = classification task where the output variable has more than two classes (e.g., classifying images of animals into categories like cat, dog, and bird)
#

#evaluation metrics for classification
#confusion matrix = table that summarizes the performance of a classification model by comparing the predicted class labels with the actual class labels
# True Positives (TP) = predicted positive and actual positive
# True Negatives (TN) = predicted negative and actual negative
# False Positives (FP) = predicted positive and actual negative
# False Negatives (FN) = predicted negative and actual positive

#1. Accuracy = (True Positives + True Negatives) / Total Samples
#2. Precision = True Positives / (True Positives + False Positives) - how many of the predicted positive cases were actually positive

#3. Recall (Sensitivity) = True Positives / (True Positives + False Negatives) - how many of the actual positive cases were predicted as positive
#4. F1 Score = 2 * (Precision * Recall) / (Precision + Recall) - harmonic mean of precision and recall
#5. ROC-AUC (Receiver Operating Characteristic - Area Under Curve) = measures the model's ability to distinguish between classes across different thresholds
#Best ROC Curve:

#The curve goes straight up the left side and then horizontally to the right, forming a right angle at the top-left corner.
#AUC is 1.0
#This indicates perfect discrimination; the model can perfectly separate the two classes.
#Worst ROC Curve:

#It is a diagonal line from the bottom-left to the top-right.
#AUC is 0.5
#This indicates no discrimination; the model performs no better than random guess

#logistic regression formula - z = mx + b 
#logistic regression = linear regression with a sigmoid function applied to the output to convert it into a probability between 0 and 1
#sigmoid function = 1 / (1 + e^(-z)) where z is the output of the linear regression model
#logistic regression is used for binary classification tasks, where the output variable has two classes (e.g., spam or not spam, positive or negative)
#logistic regression can be extended to multiclass classification tasks using techniques like One-vs-Rest (OvR) or Softmax regression
#logistic regression is a linear model, but it can be used for classification tasks by applying a non-linear activation function (sigmoid) to the output
#logistic regression is a probabilistic model, meaning it outputs probabilities for each class rather than just class labels
#logistic regression can be used for both binary and multiclass classification tasks, but it is primarily used for binary classification tasks

#class imbalance = when one class has significantly more samples than the other class(es) in a classification task
#class imbalance can lead to biased predictions towards the majority class, resulting in poor performance on the minority class
#to handle class imbalance, techniques like oversampling the minority class, undersampling the majority class, or using class weights can be applied
#oversampling = increasing the number of samples in the minority class by duplicating existing samples or generating synthetic samples
#undersampling = reducing the number of samples in the majority class by randomly removing samples

#KNN (k-Nearest Neighbors) or (lazzy learner) it is a light wieghted alogrithm,  instance-based learning algorithm that classifies a new data point based on the majority class of its k nearest neighbors in the feature space
#distance based algorithm = KNN uses distance metrics like Euclidean distance, Manhattan distance, or Minkowski distance to measure the similarity between data points
#KNN is a non-parametric algorithm, meaning it does not make any assumptions about the underlying data distribution
#KNN is a lazy learner, meaning it does not learn a model during training but instead stores the training data and makes predictions at the time of query
#KNN is sensitive to the choice of distance metric and the value of k (number of neighbors to consider)
#KNN can be used for both classification and regression tasks, but it is primarily used for classification tasks
#KNN algorithm steps:
#1. Choose the number of neighbors (k) to consider.
#2. Calculate the distance between the new data point and all training data points using a distance metric (e.g., Euclidean distance).
#3. Sort the distances in ascending order and select the k nearest neighbors.
#4. Determine the majority class among the k nearest neighbors.
#5. Assign the majority class as the predicted class for the new data point.


#bayes theorem = a mathematical formula that describes the probability of an event based on prior knowledge of conditions related to the event
#condition probability explaination = the probability of an event occurring given that another event has already occurred
#bayes theorem formula = P(A|B) = (P(B|A) * P(A)) / P(B)
#where: 
# P(A|B) = probability of event A given event B has occurred
# P(B|A) = probability of event B given event A has occurred
# P(A) = prior probability of event A
# P(B) = prior probability of event B
#example of conditional probability = the probability of a person having a disease given that they have a positive test result
#example of bayes theorem = the probability of a person having a disease given that they have a positive test result, given the prior probability of the disease and the accuracy of the test

#naive bayes = a family of probabilistic algorithms based on Bayes' theorem, assuming independence between features
#types of naive bayes algorithms
#1. Gaussian Naive Bayes = assumes that the features follow a Gaussian (normal) distribution    
#2. Multinomial Naive Bayes = used for discrete data, such as text classification, where features represent word counts or frequencies
#3. Bernoulli Naive Bayes = used for binary features, where features represent the presence or absence of a feature (e.g., word occurrence in text classification)

#naive bayes algorithm steps:
#1. Calculate the prior probabilities of each class based on the training data.
#2. For each feature, calculate the likelihood of the feature given each class using the training data.
#3. For a new data point, calculate the posterior probability for each class using Bayes' theorem.
#4. Assign the class with the highest posterior probability as the predicted class for the new data point.

#decision tree = lot mathematical calculations, it is a flowchart-like structure that splits the data into subsets based on feature values
#common words in decision tree
#1. Node = a point in the tree where a decision is made based on a feature value
#2. Leaf Node = a terminal node that represents a class label or prediction
#3. Root Node = the topmost node in the tree that represents the entire dataset
#4. Branch = a connection between nodes that represents a decision based on a feature value
#5. Split = the process of dividing the data into subsets based on a feature value
#6. Pruning = the process of removing unnecessary nodes from the tree to reduce complexity and improve generalization
#7. Depth = the length of the longest path from the root node to a leaf node
#8. Feature Importance = a measure of how much a feature contributes to the decision-making process in the tree
#9. Gini Impurity = a measure of how often a randomly chosen element from the set would be incorrectly labeled if it was randomly labeled according to the distribution of labels in the subset
#10. Information Gain = the reduction in entropy (uncertainty) achieved by splitting the data based on a feature
#11. Entropy = a measure of the uncertainty or randomness in a dataset, used to determine the best feature to split the data
#12. Overfitting = when the model learns the training data too well, capturing noise and leading to poor generalization on unseen data
#13. Underfitting = when the model is too simple to capture the underlying patterns in the data, leading to poor performance on both training and test data
#14. Hyperparameters = parameters that are set before training the model, such as the maximum depth of the tree, minimum samples per leaf, and splitting criteria
#15. Splitting Criteria = the method used to determine the best feature to split the data, such as Gini impurity or information gain
#16. Maximum Depth = the maximum number of levels in the tree, used to control overfitting
#17. Minimum Samples Split = the minimum number of samples required to split a node, used to control overfitting
#18. Minimum Samples Leaf = the minimum number of samples required to be at a leaf node, used to control overfitting
#19. Class Imbalance = when one class has significantly more samples than the other class(es) in a classification task, which can lead to biased predictions towards the majority class


#how to select root node in decision tree
#1. Calculate the Gini impurity or information gain for each feature. - varies from 0 to 0.5
#   - Gini impurity formula = 1 - Σ(p(x)^2) where p(x) is the probability of each class in the dataset
#2. Select the feature with the lowest Gini impurity or highest information gain as the root node.
#3. Split the data based on the selected feature's values.

#entropy = a measure of the uncertainty or randomness in a dataset, used to determine the best feature to split the data
#entropy varies from 0 to 1 
#entropy formula = -Σ(p(x) * log2(p(x))) where p(x) is the probability of each class in the dataset

#svm - supoort vector machine = a supervised learning algorithm used for classification and regression tasks, which finds the optimal hyperplane that separates different classes in the feature space
#hyperplane = a decision boundary that separates different classes in the feature space
#support vectors = the data points that are closest to the hyperplane and influence its position
#kernel = a function that transforms the input data into a higher-dimensional space to make it easier to find a hyperplane that separates the classes
#types of kernels in SVM - it basically converts the data into higher order digree so that the hyperplane can be found easily
#and the data can be separated easily
#1. Linear Kernel = used for linearly separable data, where the classes can be separated by a straight line (or hyperplane in higher dimensions)    
#2. Polynomial Kernel = used for non-linear data, where the classes can be separated by a polynomial function
#3. Radial Basis Function (RBF) Kernel = used for non-linear data, where the classes can be separated by a Gaussian function
#4. Sigmoid Kernel = used for non-linear data, where the classes can be separated by a sigmoid function
#5. Custom Kernel = user-defined kernel function for specific use cases
#SVM algorithm steps:
#1. Choose a kernel function based on the data distribution and problem requirements.
#2. Transform the input data into a higher-dimensional space using the chosen kernel function.
#3. Find the optimal hyperplane that maximizes the margin between the support vectors of different classes.
#4. Classify new data points based on their position relative to the hyperplane.
#5. Use techniques like cross-validation to tune hyperparameters (e.g., C parameter for regularization) and improve model performance.

#how to improve class imbalance  -
#techniques to improve class imbalance
#oversampling and undersampling
#1. Oversampling the minority class = increasing the number of samples in the minority class by duplicating existing samples or generating synthetic samples (e.g., using SMOTE - Synthetic Minority Over-sampling Technique (KNN-based method to generate synthetic samples for the minority class))
#   - SMOTE works by selecting a random sample from the minority class and finding its k nearest neighbors. It then generates synthetic samples by interpolating between the selected sample and its neighbors.
#2. Undersampling the majority class = reducing the number of samples in the majority class by randomly removing samples

#ensemble learning = a technique that combines multiple models to improve performance and robustness
#types of ensemble learning methods
#1. voting classifier= a technique that combines predictions from multiple models by taking the majority vote (for classification tasks) or averaging (for regression tasks)

#2. parallel ensemble - Bagging (Bootstrap Aggregating) = combines predictions from multiple models trained on different subsets of the training data, reducing variance and improving stability (e.g., Random Forest)  
#what is bootstrap aggregating = a technique that involves creating multiple subsets of the training data by randomly sampling with replacement, and then training a separate model on each subset
#why called parallel ensemble = because all the models are trained independently and in parallel, and their predictions are combined to make the final prediction
#3. sequential ensemble - Boosting = combines predictions from multiple models trained sequentially, where each model focuses on correcting the errors of the previous model (e.g., AdaBoost, Gradient Boosting, XGBoost)
#what is boosting = a technique that involves training multiple models sequentially, where each model is trained to correct the errors of the previous model
#why called sequential ensemble = because each model is trained based on the errors of the previous model, and their predictions are combined to make the final prediction

#oob score = out-of-bag score, a technique used in bagging methods like Random Forest to estimate the performance of the model without using a separate validation set
#it works by using the samples that were not included in the bootstrap sample (out-of-bag samples) to evaluate the model's performance
#oob score is calculated by averaging the predictions of the out-of-bag samples across all trees in the Random Forest
#ensemble learning is used to improve the performance of machine learning models by combining the strengths of multiple models and reducing the weaknesses of individual models

#staking ensemble = a technique that combines predictions from multiple models by training a meta-model on the predictions of the base models
#stacking ensemble steps:
#1. Train multiple base models on the training data.
#2. Generate predictions from each base model on the validation set or test set.
#3. Use the predictions from the base models as input features to train a meta-model.
#4. The meta-model learns to combine the predictions from the base models to make the final prediction.
#5. The final prediction is made by the meta-model based on the predictions from the base models.
#stacking ensemble is used to improve the performance of machine learning models by combining the strengths of multiple models and reducing the weaknesses of individual models



#USUPERVISED LEARNING - segmentation of data into clusters or groups based on similarity or distance metrics
#mainly used for markeing compaigns, customer segmentation, and recommendation systems. to predict the discount or offers based on the customer behavior
#no target variable or labels are provided, the algorithm learns patterns and structures from the input data without any supervision
#text segmentation = clustering text documents into groups based on similarity or distance metrics
#image segmentation = clustering image pixels into groups based on similarity or distance metrics   
#clustering = the process of grouping similar data points together based on their features or attributes
#asociation rule learning = a technique used to discover interesting relationships or patterns between variables in large datasets, often used in market basket analysis to find associations between products purchased together
#feature dimensionality reduction = a technique used to reduce the number of features in a dataset while preserving its important characteristics, often used to improve model performance and reduce computational complexity

#types of clustering algorithms
#1. K-Means Clustering (radial nature)= partitions the data into k clusters by minimizing the distance between data points and their assigned cluster centroids
#2. Hierarchical Clustering = creates a hierarchy of clusters by recursively merging or splitting clusters based on distance metrics
#3. DBSCAN (Density-Based Spatial Clustering of Applications with Noise) = groups data points based on their density, allowing for the identification of clusters of varying shapes and sizes
#4. Gaussian Mixture Models (GMM) = models the data as a mixture of multiple Gaussian distributions, allowing for soft clustering where data points can belong to multiple clusters with different probabilities
#5. Agglomerative Clustering = a bottom-up approach that starts with each data point as a separate cluster and merges them based on distance metrics
#6. Spectral Clustering = uses the eigenvalues of a similarity matrix to perform dimensionality reduction and clustering in a lower-dimensional space
#7. Mean Shift Clustering = a non-parametric clustering algorithm that iteratively shifts data points towards the mode of the data distribution to form clusters
#8. Affinity Propagation = a clustering algorithm that uses message passing between data points to identify exemplars and form clusters

#elbow method = a technique used to determine the optimal number of clusters (k) in K-Means clustering by plotting the within-cluster sum of squares (WCSS) against the number of clusters and looking for an "elbow" point where the rate of decrease slows down
#silhouette score = a measure of how similar a data point is to its own cluster compared to other clusters, ranging from -1 to 1, where higher values indicate better clustering quality
#silhouette score formula = (b - a) / max(a, b)

#dbscan = a density-based clustering algorithm that groups data points based on their density, allowing for the identification of clusters of varying shapes and sizes
#dbscan algorithm steps:
#1. Choose two parameters: epsilon (ε) - the maximum distance between two points to be considered as neighbors, and min_samples - the minimum number of points required to form a dense region.
#2. For each data point, find its neighbors within the epsilon distance.
#3. If the number of neighbors is greater than or equal to min_samples, mark the point as a core point and create a new cluster.
#4. Expand the cluster by recursively adding all reachable points (neighbors) to the cluster until no more points can be added.
#5. If a point is not a core point and has fewer neighbors than min_samples, it is marked as a noise point.
#6. Repeat the process for all data points until all points are assigned to a cluster or marked as noise.
#advantages of dbscan
#1. Can find clusters of varying shapes and sizes, making it suitable for complex datasets.
#2. Does not require the number of clusters to be specified in advance, unlike K-Means.
#3. Can handle noise and outliers effectively by marking them as noise points.
#disadvantages of dbscan
#1. Sensitive to the choice of epsilon (ε) and min_samples parameters, which can affect clustering results.
#2. Struggles with datasets with varying densities, as it may not be able to identify clusters with different densities.
#3. Not suitable for high-dimensional data due to the curse of dimensionality, which can lead to poor clustering performance.

#use below link for understanding
#https://www.naftaliharris.com/blog/visualizing-dbscan-clustering/

#hierarchical clustering = a clustering algorithm that creates a hierarchy of clusters by recursively merging or splitting clusters based on distance metrics
#hierarchical clustering algorithm steps:
#1. Calculate the distance between all pairs of data points using a distance metric (e.g., Euclidean distance).
#2. Create a distance matrix that represents the distances between all pairs of data points.
#3. Choose a linkage criterion (e.g., single linkage, complete linkage, average linkage) to determine how clusters are formed based on the distances.
#4. Start with each data point as a separate cluster.
#5. Merge the two closest clusters based on the chosen linkage criterion.
#6. Repeat the merging process until all data points are in a single cluster or until a stopping criterion is met (e.g., a specified number of clusters).
#7. The result is a dendrogram, which is a tree-like structure that represents the hierarchy of clusters.
#advantages of hierarchical clustering
#1. Does not require the number of clusters to be specified in advance, unlike K-Means.
#2. Provides a hierarchical structure that allows for different levels of granularity in clustering.
#3. Can handle different shapes and sizes of clusters, making it suitable for complex datasets.
#disadvantages of hierarchical clustering
#1. Computationally expensive, especially for large datasets, as it requires calculating distances between all pairs of data points.
#2. Sensitive to noise and outliers, which can affect the clustering results.
#3. The choice of linkage criterion can significantly impact the clustering results, and there is no one-size-fits-all solution.
#hierarchical clustering is often visualized using a dendrogram, which shows the hierarchy of clusters and allows for easy identification of the optimal number of clusters by cutting the dendrogram at a specific height

#hierarcial lustering
# calculated based on the distance between data points, which can be Euclidean distance, Manhattan distance, or any other distance metric
# distance matrix = a matrix that represents the distances between all pairs of data points, used to determine the closest clusters during the merging process
# linkage criterion = a method used to determine how clusters are formed based on the distances between data points, such as single linkage (minimum distance), complete linkage (maximum distance), or average linkage (average distance)
#dendrogram = a tree-like structure that represents the hierarchy of clusters, where the x-axis represents the data points and the y-axis represents the distance or dissimilarity between clusters
# agglomerative clustering = a bottom-up approach that starts with each data point as a separate cluster and merges them based on distance metrics
# divisive clustering = a top-down approach that starts with all data points in a single cluster and recursively splits them into smaller clusters based on distance metrics
# agglomerative clustering algorithm steps:
# 1. Calculate the distance between all pairs of data points using a distance metric (e.g., Euclidean distance).
# 2. Create a distance matrix that represents the distances between all pairs of data points.
# 3. Start with each data point as a separate cluster.
# 4. Merge the two closest clusters based on the chosen linkage criterion.
# 5. Repeat the merging process until all data points are in a single cluster or until a stopping criterion is met (e.g., a specified number of clusters).
# 6. The result is a dendrogram, which is a tree-like structure that represents the hierarchy of clusters.
# divisive clustering algorithm steps:
# 1. Start with all data points in a single cluster.
# 2. Calculate the distance between all pairs of data points using a distance metric (e.g., Euclidean distance).
# 3. Split the cluster into two smaller clusters based on the distance between data points.
# 4. Repeat the splitting process until each data point is in its own cluster or until a stopping criterion is met (e.g., a specified number of clusters).

#feature dimensionality reduction = a technique used to reduce the number of features in a dataset while preserving its important characteristics, often used to improve model performance and reduce computational complexity
#feature selection methods - correlation. backward elimination, forward selection, recursive feature elimination, and LASSO regression
#above methods were used to elemenate the features that are not important for the model
#feature extraction methods - PCA, t-SNE, and LDA
#PCA (Principal Component Analysis) = a linear dimensionality reduction technique that transforms the data into a lower-dimensional space by finding the principal components that capture the most variance in the data
#t-SNE (t-Distributed Stochastic Neighbor Embedding) = a non-linear dimensionality reduction technique that visualizes high-dimensional data in a lower-dimensional space by preserving local structure and relationships between data points
#LDA (Linear Discriminant Analysis) = a supervised dimensionality reduction technique that projects the data into a lower-dimensional space while maximizing class separability, often used for classification tasks


#association rule learning = a technique used to discover interesting relationships or patterns between variables in large datasets, often used in market basket analysis to find associations between products purchased together







