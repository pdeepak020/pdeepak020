#practice data analytics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import scipy.stats as stats
warnings.filterwarnings('ignore')

data=pd.read_csv("sales_data.csv")
#print(data.head())
#print(data.info())
print(data.describe())

#central tendency - mean, median, mode, quantile, covariance, co relation
num_data=data.select_dtypes(include=np.number)
char_data=data.select_dtypes(exclude=np.number)
#print(num_data, char_data)

num_data.mean() #mean of all columns
#sns.boxplot(num_data['Item_Outlet_Sales']) #box plot of Item_Outlet_Sales column show that outlier exists
#plt.show() #show the plot
#if data contains outliers, mean will be affected and won't give desired result. 
num_data.median() #median of all columns
#if data is not ditributed normally across the range, median will be a better choice than mean
#data is not normally distributed then median won't give correct middle value
sns.boxplot(num_data['Item_MRP'])
plt.show()

#if outlier is present on both ends almost equally, the it is nullified. both mean and median will be same

#trimmed mean
import scipy.stats as stats

stats.trim_mean(num_data['Item_Outlet_Sales'], proportiontocut=0.1) #10% of data is trimmed from both ends

res=pd.DataFrame()
per = num_data.quantile([0.25, 0.5, 0.75]).T #25%, 50%, 75% quantile of Item_Outlet_Sales column
res["mean"] = num_data.mean() #mean of Item_Outlet_Sales column
res["median"] = num_data.median() #median of Item_Outlet_Sales column
#res["mode"] = num_data.mode() #mode of Item_Outlet_Sales column
res["std"] = num_data.std() #standard deviation of Item_Outlet_Sales column
res["var"] = num_data.var() #variance of Item_Outlet_Sales column
res["coeff_var"] = num_data.std()/num_data.mean() #coefficient of variation of Item_Outlet_Sales column
res["range"] = num_data.max()-num_data.min() #range of Item_Outlet_Sales column
print(per) #print the quantile values
print(res)
#RANGE - max-min

print(num_data['Item_Outlet_Sales'].max()-num_data['Item_Outlet_Sales'].min()) #range of Item_Outlet_Sales column

#variance - how much data is spread out from the mean
#variance = sum of squares of difference between each data point and mean / number of data points
#variance = sum of squares of difference between each data point and mean / number of data points - 1 (sample variance)
#we do sumation of squares of difference between each data point and mean / number of data points - 1 (sample variance) to get unbiased estimate of population variance
#we do summation of each data point -mean and square it to eliminate negative effect of negative values

#standard deviation - square root of variance
#standard deviation = square root of sum of squares of difference between each data point and mean / number of data points - 1 (sample standard deviation)
#standard deviation = square root of sum of squares of difference between each data point and mean / number of data points (population standard deviation)

#coefficient of variation - standard deviation / mean
#coefficient of variation tells us the deviation of each data 

#bivariante analysis - covariance, correlation, regression
#covariance - measure of how much two random variables vary together / + or - relationship between two random variables
#covariance = sum of squares of difference between each data point and mean / number of data points - 1 (sample covariance)

#correlation - measure of how much two random variables are related to each other
#pearson correlation - measure of linear relationship between two random variables
#pearson correlation = covariance / (standard deviation of x * standard deviation of y)

#spearman correlation - measure of monotonic relationship between two random variables
#spearman correlation = 1 - (6 * sum of squares of difference between each data point and mean) / (n * (n^2 - 1))

pearson_corr = num_data.corr(method='pearson') #pearson correlation of all columns
spearman_corr = num_data.corr(method='spearman') #spearman

print(pearson_corr) #print the pearson correlation
print(spearman_corr) #print the spearman correlation
sns.heatmap(pearson_corr, annot=True) #heatmap of pearson correlation
plt.show() #show the plot


#measure of distribution - skewness, kurtosis
#skewness - measure of asymmetry of the distribution of data
#skewness = 0 - normal distribution, skewness > 0 - right skewed distribution, skewness < 0 - left skewed distribution
#skewness = summation (3 ** (mean - median)) / standard deviation
#when data has more outliers on one side, it is skewed to that side.
#skew is between +0.5 and -0.5 is considered normal, between +1 and -1 is moderately skewed, and greater than +1 or less than -1 is highly skewed.



#kurtosis - measure of peakedness of the distribution of data
#kurtosis = 0 - normal distribution, kurtosis > 0 - leptokurtic distribution, kurtosis < 0 - platykurtic distribution
#kurtosis = (sum of squares of difference between each data point and mean) / (number of data points * standard deviation^4) - 3

num_data.skew() #skewness of all columns
num_data.kurtosis() #kurtosis of all columns

sns.displot(num_data['Item_Outlet_Sales'], kde=True) #distribution plot of Item_Outlet_Sales column
plt.show() #show the plot

#transformations - log, square root, cube root, box-cox, y-box-cox, z-score
#log transformation - used to reduce the skewness of the data
#square root transformation - used to reduce the skewness of the data
#cube root transformation - used to reduce the skewness of the data
#box-cox transformation - used to reduce the skewness of the data

np.log(num_data['Item_Outlet_Sales']).plot(kind='kde') #log transformation of Item_Outlet_Sales column
plt.show() #show the plot
np.sqrt(num_data['Item_Outlet_Sales']).plot(kind='kde') #square root transformation of Item_Outlet_Sales column
plt.show() #show the plot
#this will convert data to normal distribution almost which can be used for hypothesis testing


