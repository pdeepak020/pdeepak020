#inferential statistics
#based on 2 parameters - population and sample
#population - entire group of individuals
#sample - subset of population

#estimation is the process of inferring the value of a population parameter from a sample statistic
#means population mean - sample mean should be equal to 0 to get the best estimate of the population mean
#point estimation - single value estimate of a population parameter or mean of mean of all the sample subset data
#interval estimation - range of values within which the population parameter is expected to lie with a certain level of confidence
#confidence interval - range of values within which the population parameter is expected to lie with a certain level of confidence
#confidence level - probability that the confidence interval contains the population parameter
#confidence level = 1 - alpha (alpha is the level of significance)
#practical method- confidence interval = sample mean +/- (z * standard error) (for large sample size)(sample mean can be PE like mean of mean of all the sample subset data) (z is 3 or 2 for 99% and 95% confidence level respectively)
#classical method- confidence interval = sample mean +/- (z * standard deviation) (for large sample size)(sample mean can be PE like mean of mean of all the sample subset data) (z is 3 or 2 for 99% and 95% confidence level respectively)



#central limit theorem - states that the sampling distribution of the sample mean approaches a normal distribution as the sample size increases, regardless of the shape of the population distribution
#standard error - measure of how much the sample mean is expected to vary from the population mean
#standard error = standard deviation / square root of sample size

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import warnings
warnings.filterwarnings('ignore')


num=np.random.randn(1000) #generate 1000 random numbers from normal distribution
num2=np.random.uniform(0, 1, 1000) #generate 1000 random numbers from uniform distribution

#normal dist - will range from -3sigma to +3sigma ie 99.7% of the data will be within 3 standard deviation from the mean
#formaula for normalixed distribution is (x-mean)/std deviation


#hypothesis testing - process of making decisions about a population based on a sample/ to test the claim given is correct pr not/

#null hypothesis - no difference between the sample and population mean (H0)
#alternative hypothesis - there is a difference between the sample and population mean (H1)/ statement to test or prove is alternate hypothesis
#type 1 error - rejecting the null hypothesis when it is true (false positive)
#type 2 error - failing to reject the null hypothesis when it is false (false negative)

#null and alternative hypothesis for correlation test - no correlation between the two variables (H0) and there is a correlation between the two variables (H1)

#for normal distribution the mean and median should be same

#if pvalue is less than alpha (level of significance) then we reject the null hypothesis and accept the alternative hypothesis
#pvalue is the probability of getting the observed value or more extreme value if the null hypothesis is true
#pvalue is the area under the curve of the normal distribution for the given value


#t test or sample test is for numeric data/ where we compare the average values of two groups to see if they are significantly different from each other
#proportion test is for categorical data/ where we compare the proportion of two groups to see if they are significantly different from each other
data=pd.read_csv("HR_newdata.csv")

data.head()

count = data['Gender'].value_counts() #count of unique

groupm=data[data['Gender']==1]['MonthlyIncome'] #count of unique
groupf=data[data['Gender']==2]['MonthlyIncome']

print(count)
print(groupm)

sns.distplot(groupm)
sns.distplot(groupf)
plt.show()

z,pvalue = stats.ttest_ind(groupm, groupf) #t test for independent samples
print(z,pvalue) #t test statistic and p value
print(np.mean(groupm), np.mean(groupf)) #mean of groupm and groupf







