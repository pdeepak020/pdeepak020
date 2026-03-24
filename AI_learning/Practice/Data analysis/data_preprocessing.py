#data preprocessing
#data wrangaling, eda, feature engineering, data processing

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import scipy.stats as stats
warnings.filterwarnings('ignore')

#pre processing - missing value treatment, outlier treatment, data transformation, data scaling, data encoding

#drop the null data or fill the null data with mean, median, mode, or any other value
#mean and median is used for numerical data and mode is used for categorical data
#when we replace the null values with mean, median, mode, we are assuming that the data is normally distributed
#also the mean and median should be grouped by categorical data

