# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#Importarea bibliotecilor necesare
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import statsmodels.formula.api as smf
import statsmodels.api as sm

#incarcare date
df = pd.read_excel(r"C:\Users\mariu\OneDrive\Desktop\anul 2 sem 1\maican\winequality-red.xlsx")

#verificare valori lipsa
print(df.isnull().sum())

# calcul statistici descriptive
desc_stats = df.describe().transpose()

# adaugare skewness, kurtosis, median si mode
desc_stats['skewness'] = df.skew()
desc_stats['kurtosis'] = df.kurtosis()
desc_stats['median'] = df.median()
desc_stats['mode'] = df.mode().iloc[0]
desc_stats = desc_stats[['count', 'mean', 'std', 'min', '25%', '50%', 'median', '75%', 'max', 'skewness', 'kurtosis', 'mode']]

# specificare fisier
file_path = r'C:\Users\mariu\OneDrive\Desktop\anul 2 sem 1\maican\desc_stats_red.xlsx'

# scrie datele in excel
desc_stats.to_excel(file_path, index=True)


# Histograme pentru intelegerea tuturor distributiilor
df.hist(bins=30, figsize=(20,20))
plt.show()

# corelatie variabile

df_rounded = df.round(2)

corr = df_rounded.corr()
print(corr)
# specificare fisier pentru scriere
file_path = r'C:\Users\mariu\OneDrive\Desktop\anul 2 sem 1\maican\corr_matrix.xlsx'

# scrie matricea de corelatie
corr.to_excel(file_path, index=True)

#afiseaza matricea de corelatie
fig, ax = plt.subplots(figsize=(12, 12))
sns.heatmap(corr, annot=True, annot_kws={"size": 10}, fmt='.2f',
            xticklabels=['I' + str(i) for i in range(1, corr.shape[0] + 1)],
            yticklabels=['I' + str(i) for i in range(1, corr.shape[0] + 1)],
            ax=ax)
plt.show()


#incarcare date
df2 = pd.read_excel(rC:\Users\mariu\OneDrive\Desktop\anul 2 sem 1\maican\winequality-white.xlsx")

#verificare valori lipsa
print(df2.isnull().sum())

# calcul statistici descriptive
desc_stats2 = df2.describe().transpose()

# adaugare skewness, kurtosis, median si mode
desc_stats2['skewness'] = df2.skew()
desc_stats2['kurtosis'] = df2.kurtosis()
desc_stats2['median'] = df2.median()
desc_stats2['mode'] = df2.mode().iloc[0]
desc_stats2 = desc_stats2[['count', 'mean', 'std', 'min', '25%', '50%', 'median', '75%', 'max', 'skewness', 'kurtosis', 'mode']]

# specificare fisier
file_path = r'C:\Users\mariu\OneDrive\Desktop\anul 2 sem 1\maican\desc_stats_white.xlsx'

# scrie datele in excel
desc_stats2.to_excel(file_path, index=True)

# Histograme pentru intelegerea tuturor distributiilor
df2.hist(bins=30, figsize=(20,20))
plt.show()


# corelatie variabile
df_rounded = df2.round(2)

corr = df_rounded.corr()
print(corr)

#specifica fisier
file_path = r'C:\Users\mariu\OneDrive\Desktop\anul 2 sem 1\maican\corr_matrix2.xlsx'

# scrie date in fisier
corr.to_excel(file_path, index=True)

#afiseaza

fig, ax = plt.subplots(figsize=(12, 12))
sns.heatmap(corr, annot=True, annot_kws={"size": 10}, fmt='.2f',
            xticklabels=['I' + str(i) for i in range(1, corr.shape[0] + 1)],
            yticklabels=['I' + str(i) for i in range(1, corr.shape[0] + 1)],
            ax=ax)
plt.show()



### analiza de regresie

#incarcare date
df = pd.read_excel(r"C:\Users\mariu\OneDrive\Desktop\anul 2 sem 1\maican\winequality-red.xlsx")

#selectie variabila dependenta, selectie variabile independente

X = df.drop(["quality"], axis=1)
y = df["quality"]

regressor = LinearRegression()
regressor.fit(X, y)

# regresie OLS (Ordinary Least Squares)

model = sm.OLS(y, X).fit()
print(model.summary())

#eliminare variabile cu p-value mai mic de 0.05
p_values = model.pvalues
significant_variables = [col for col, p_val in zip(X.columns, p_values) if p_val < 0.05]
X = df[significant_variables]
model = sm.OLS(y, X).fit()
print(model.summary())



p_values = model.pvalues
significant_variables = [col for col, p_val in zip(X.columns, p_values) if p_val < 0.05]
X = df[significant_variables]
model = sm.OLS(y, X).fit()
print(model.summary())

#incarcare date
df = pd.read_excel(r"C:\Users\mariu\OneDrive\Desktop\anul 2 sem 1\maican\winequality-white.xlsx")
#seteaza variabile independente / variabila dependenta
X = df.drop(["quality"], axis=1)
y = df["quality"]

regressor = LinearRegression()
regressor.fit(X, y)
# regresie OLS (Ordinary Least Squares)

model = sm.OLS(y, X).fit()
print(model.summary())

#elimina variabile cu p-value mai mic decat 0.05
p_values = model.pvalues
significant_variables = [col for col, p_val in zip(X.columns, p_values) if p_val < 0.05]



X=df[significant_variables]
regressor = LinearRegression()
regressor.fit(X, y)

model = sm.OLS(y, X).fit()
print(model.summary())
    


    



    
    

