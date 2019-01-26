# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#path of the data file- path
#Code starts here 
data = pd.read_csv(path)
data['Gender'].replace('-','Agender', inplace=True)
gender_count = data['Gender'].value_counts()
print(gender_count)
plt.bar(np.arange(len(gender_count)),gender_count)


# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
plt.pie(alignment,labels= list(alignment.index))



# --------------
#Code starts here
sc_df = data[['Strength','Combat']].copy()
sc_covariance = np.matrix(sc_df.cov())[0,1]
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()
sc_pearson = sc_covariance/(sc_strength*sc_combat)
print(sc_pearson)

ic_df = data[['Intelligence','Combat']].copy()
ic_covariance = np.matrix(ic_df.cov())[0,1]
ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)
print(ic_pearson)


# --------------
#Code starts here

total_high = data['Total'].quantile(0.99)
print(total_high)
super_best = data[data['Total']>total_high]
super_best_names = list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here
fig = plt.figure()
ax_1 = fig.add_subplot(221)
ax_2 = fig.add_subplot(222)
ax_3 = fig.add_subplot(223)
ax_1.boxplot(super_best['Intelligence'])
ax_2.boxplot(super_best['Speed'])
ax_3.boxplot(super_best['Power'])


