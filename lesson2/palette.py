import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline 

df = pd.read_csv(‘advertising.csv’) 
sns.pairplot(df, hue=’age_group’, palette=’d’)