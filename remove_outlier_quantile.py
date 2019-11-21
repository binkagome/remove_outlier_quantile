#get Q1 and Q3
Q1 = series.quantile(.25)
Q3 = series.quantile(.75)

#or
Q1 = series.describe()['25%']
Q3 = series.describe()['75%']


# detect the outlier or no outlier
IQR = Q3 - Q1
threshold = Q3 + 1.5 * IQR

df_outlier = df[df['A'].apply(lambda x:x > threshold)]
