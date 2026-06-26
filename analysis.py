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
lt.show()
print("Chart 3 saved!")

# ============================================
# STEP 8: AVERAGE HAPPINESS BY YEAR (TREND)
# ============================================

yearly_avg = df_all.groupby('Year')['Score'].mean()

plt.figure(figsize=(10, 6))
plt.plot(yearly_avg.index, yearly_avg.values, marker='o',
         color='#2a9d8f', linewidth=2.5, markersize=8)
plt.title('Average Global Happiness Score 2015-2019', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Average Happiness Score')
plt.xticks([2015, 2016, 2017, 2018, 2019])
plt.ylim(5.0, 5.6)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('Visuals/happiness_trend_2015_2019.png')
plt.show()
print("Chart 4 saved!")

# ============================================
# STEP 9: AVERAGE HAPPINESS BY REGION
# ============================================

df_2015_original = pd.read_csv("data/2015.csv")
region_avg = df_2015_original.groupby('Region')['Happiness Score'].mean().sort_values(ascending=True)

plt.figure(figsize=(12, 8))
bars = plt.barh(region_avg.index, region_avg.values, color='#2a9d8f')

for bar, value in zip(bars, region_avg.values):
    plt.text(value + 0.05, bar.get_y() + bar.get_height()/2,
             f'{value:.2f}', va='center', fontsize=10)

plt.title('Average Happiness Score by Region (2015)', fontsize=16)
plt.xlabel('Average Happiness Score')
plt.ylabel('Region')
plt.xlim(0, 8)
plt.tight_layout()
plt.savefig('Visuals/happiness_by_region.png')
plt.show()
print("Chart 5 saved!")

# ============================================
# STEP 10: GDP vs HAPPINESS SCATTER PLOT
# ============================================

plt.figure(figsize=(10, 7))
sns.scatterplot(data=df_all, x='GDP', y='Score', alpha=0.5, color='#2a9d8f')
sns.regplot(data=df_all, x='GDP', y='Score',
            scatter=False, color='#1a5c5c', line_kws={'linewidth': 2})
plt.title('GDP per Capita vs Happiness Score (2015-2019)', fontsize=16)
plt.xlabel('GDP per Capita')
plt.ylabel('Happiness Score')
plt.tight_layout()
plt.savefig('Visuals/gdp_vs_happiness.png')
plt.show()
print("Chart 6 saved!")

# ============================================
# STEP 11: NORDIC COUNTRIES TREND
# ============================================

countries = ['Finland', 'Denmark', 'Norway', 'Iceland', 'Switzerland']
colors = ['#2a9d8f', '#264653', '#4a9e8f', '#1a5c5c', '#80b3ac']

plt.figure(figsize=(12, 7))

for country, color in zip(countries, colors):
    country_data = df_all[df_all['Country'] == country]
    plt.plot(country_data['Year'], country_data['Score'],
             marker='o', linewidth=2, label=country, color=color)

plt.title('Happiness Score Trends - Top Nordic Countries (2015-2019)', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Happiness Score')
plt.xticks([2015, 2016, 2017, 2018, 2019])
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('Visuals/nordic_trends.png')
plt.show()
print("Chart 7 saved!")

# ============================================
# STEP 12: FINLAND CONTEXT NOTE
# ============================================

print("""
==============================================
KEY INSIGHT: FINLAND'S ONGOING DOMINANCE
==============================================
Our dataset shows Finland rising from 5th to 1st
between 2015 and 2019. This was just the beginning.

Finland has ranked #1 every year from 2018 to 2026, nine consecutive years as of the latest report.

The factors our analysis identifies as strongest
predictors of happiness (GDP: 0.79, Health: 0.74,
Social Support: 0.65) are exactly the areas where
Finland consistently outperforms other nations.
==============================================
""")