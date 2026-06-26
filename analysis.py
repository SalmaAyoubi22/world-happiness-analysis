# ============================================
# WORLD HAPPINESS ANALYSIS
# Author: Salma Ayoubi
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================
# STEP 1: LOAD DATA
# ============================================

df_2015 = pd.read_csv("data/2015.csv")
df_2016 = pd.read_csv("data/2016.csv")
df_2017 = pd.read_csv("data/2017.csv")
df_2018 = pd.read_csv("data/2018.csv")
df_2019 = pd.read_csv("data/2019.csv")

print("Shape:", df_2015.shape)
print("\nColumns:", df_2015.columns.tolist())
print("\nFirst 5 rows:")
print(df_2015.head())

# ============================================
# STEP 2: DATA CLEANING & EXPLORATION
# ============================================

print("Missing values in 2015:")
print(df_2015.isnull().sum())

print("\nBasic statistics:")
print(df_2015.describe())

# ============================================
# STEP 3: ADD YEAR COLUMN
# ============================================

df_2015['Year'] = 2015
df_2016['Year'] = 2016
df_2017['Year'] = 2017
df_2018['Year'] = 2018
df_2019['Year'] = 2019

# ============================================
# STEP 4: STANDARDISE COLUMN NAMES
# ============================================

df_2015 = df_2015.rename(columns={
    'Happiness Rank': 'Rank',
    'Happiness Score': 'Score',
    'Economy (GDP per Capita)': 'GDP',
    'Family': 'Social Support',
    'Health (Life Expectancy)': 'Health',
    'Trust (Government Corruption)': 'Corruption',
})

df_2016 = df_2016.rename(columns={
    'Happiness Rank': 'Rank',
    'Happiness Score': 'Score',
    'Economy (GDP per Capita)': 'GDP',
    'Family': 'Social Support',
    'Health (Life Expectancy)': 'Health',
    'Trust (Government Corruption)': 'Corruption',
})

df_2017 = df_2017.rename(columns={
    'Happiness.Rank': 'Rank',
    'Happiness.Score': 'Score',
    'Economy..GDP.per.Capita.': 'GDP',
    'Family': 'Social Support',
    'Health..Life.Expectancy.': 'Health',
    'Trust..Government.Corruption.': 'Corruption',
    'Country': 'Country',
})

df_2018 = df_2018.rename(columns={
    'Overall rank': 'Rank',
    'Country or region': 'Country',
    'GDP per capita': 'GDP',
    'Social support': 'Social Support',
    'Healthy life expectancy': 'Health',
    'Freedom to make life choices': 'Freedom',
    'Perceptions of corruption': 'Corruption',
})

df_2019 = df_2019.rename(columns={
    'Overall rank': 'Rank',
    'Country or region': 'Country',
    'GDP per capita': 'GDP',
    'Social support': 'Social Support',
    'Healthy life expectancy': 'Health',
    'Freedom to make life choices': 'Freedom',
    'Perceptions of corruption': 'Corruption',
})

cols = ['Country', 'Rank', 'Score', 'GDP', 'Social Support',
        'Health', 'Freedom', 'Generosity', 'Corruption', 'Year']

df_2015 = df_2015[cols]
df_2016 = df_2016[cols]
df_2017 = df_2017[cols]
df_2018 = df_2018[cols]
df_2019 = df_2019[cols]

df_all = pd.concat([df_2015, df_2016, df_2017, df_2018, df_2019], ignore_index=True)

print("Clean combined shape:", df_all.shape)
print("\nColumns:", df_all.columns.tolist())
print("\nFirst 5 rows:")
print(df_all.head())

# ============================================
# STEP 5: TOP 10 HAPPIEST COUNTRIES (2019)
# ============================================

top10 = df_all[df_all['Year'] == 2019].nlargest(10, 'Score')

plt.figure(figsize=(10, 6))
sns.barplot(data=top10, x='Score', y='Country', color='#2a9d8f')
plt.title('Top 10 Happiest Countries in 2019', fontsize=16)
plt.xlabel('Happiness Score')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('Visuals/top10_happiest_2019.png')
plt.show()
print("Chart 1 saved!")

# ============================================
# STEP 6: BOTTOM 10 UNHAPPIEST COUNTRIES (2019)
# ============================================

bottom10 = df_all[df_all['Year'] == 2019].nsmallest(10, 'Score')

plt.figure(figsize=(10, 6))
sns.barplot(data=bottom10, x='Score', y='Country', color='#1a5c5c')
plt.title('Bottom 10 Unhappiest Countries in 2019', fontsize=16)
plt.xlabel('Happiness Score')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('Visuals/bottom10_unhappiest_2019.png')
plt.show()
print("Chart 2 saved!")

# ============================================
# STEP 7: CORRELATION HEATMAP
# ============================================

factors = ['Score', 'GDP', 'Social Support', 'Health',
           'Freedom', 'Generosity', 'Corruption']

corr = df_all[factors].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='YlGnBu', fmt='.2f', linewidths=0.5)
plt.title('Correlation Between Happiness Factors', fontsize=16)
plt.tight_layout()
plt.savefig('Visuals/correlation_heatmap.png')
p