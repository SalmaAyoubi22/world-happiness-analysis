# World Happiness Analysis (2015–2019)
### *What makes a country happy, and why has Finland been #1 for 9 years straight?*

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![pandas](https://img.shields.io/badge/pandas-2.0-lightblue?style=flat-square)
![matplotlib](https://img.shields.io/badge/matplotlib-3.11-orange?style=flat-square)
![seaborn](https://img.shields.io/badge/seaborn-0.13-teal?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-green?style=flat-square)

</div>

---

## The Question Behind This Project

Finland is a small Nordic country of 5.5 million people. It has long winters,
months of near-total darkness, and some of the highest income tax rates in the
world. And yet, since 2018, it has been ranked the **happiest country on Earth,
every single year, without exception.**

By 2026, Finland has held the #1 spot for **nine consecutive years.**

That raised a question worth investigating: **what actually drives national
happiness?** Is it money? Health? Freedom? Trust in government? Strong
communities? And can data tell us why Finland keeps winning while far wealthier
nations fall behind?

This project analyses five years of the **World Happiness Report (2015–2019)**
across **158 countries**, using Python to explore the factors behind happiness
scores — and to trace the early signs of Finland's rise to the top.

---

## What the Data Covers

The World Happiness Report surveys citizens in over 150 countries annually,
asking them to rate their own lives on a scale of 0–10. That score is then
broken down into six contributing factors:

| Factor | What it measures |
|---|---|
| GDP per Capita | Economic wealth per person |
| Social Support | Having people to count on in difficult times |
| Health | Healthy life expectancy at birth |
| Freedom | Freedom to make key life choices |
| Generosity | Charitable giving and volunteering |
| Corruption | Trust (or lack of it) in government and business |

This analysis covers **782 data points** (158 countries x 5 years),
cleaned and standardised from five separately formatted annual datasets.

---

## Key Findings

### 1. Money matters most — but it is not everything
GDP per capita is the **strongest single predictor of happiness (r = 0.79)**.
Wealthier countries are significantly happier on average. But the relationship
is not perfect — several countries punch well above their economic weight,
and some wealthy nations underperform. This tells us wealth creates the
*conditions* for happiness, but does not guarantee it.

### 2. Health and social support are nearly as powerful
Life expectancy (r = 0.74) and having a strong social network (r = 0.65)
are close behind GDP. Countries where people live longer and feel supported
by family and community consistently score higher — regardless of income level.

### 3. Generosity is the great surprise
With a correlation of just **r = 0.14**, generosity has almost no measurable
relationship with national happiness. Countries whose citizens donate and
volunteer the most are not noticeably happier. This challenges the popular
assumption that giving makes societies flourish — at least at the national level.

### 4. The Nordic formula is real and consistent
5 of the top 10 happiest countries in 2019 are Nordic nations. They do not
just score well on one factor — they score in the top tier across GDP, health,
social support, freedom, AND low corruption simultaneously. It is the
combination, not any single element, that sets them apart.

### 5. The gap between top and bottom is enormous
Finland scores 7.77. South Sudan scores 2.85. That 5-point gap represents
the difference between a society built on stability, trust and welfare systems
— and one defined by conflict, poverty and institutional collapse. The bottom
10 countries are almost entirely active or recent war zones and the poorest
nations in Sub-Saharan Africa.

### 6. The Latin American Happiness Paradox
Latin America scores significantly higher than its GDP would predict —
ranking 4th regionally despite lower average incomes than Eastern Asia.
The data points to strong social support and freedom scores as the driver.
People in these countries report feeling deeply connected to family and
community, which partially compensates for lower economic wealth. This is
a well-documented finding in happiness research that our data confirms.

### 7. Global happiness is stable — with one dip
The worldwide average happiness score barely moved between 2015 and 2019
(range: 5.36–5.41). The one exception was a notable dip in 2017 —
a year marked by significant global political turbulence — before recovering
to its highest point in 2019. Big shifts happen at the country level,
not the global average.

---

## Finland — The Full Picture

<div align="center">

| Year | Finland Rank | Notes |
|------|-------------|-------|
| 2015 | 6th | Beginning of the rise |
| 2016 | 5th | Climbing steadily |
| 2017 | 5th | Holds position despite global dip |
| 2018 | **1st** | Takes the top spot for the first time |
| 2019 | **1st** | Dataset ends here |
| 2020 | **1st** | Holds through the pandemic |
| 2021 | **1st** | |
| 2022 | **1st** | |
| 2023 | **1st** | |
| 2024 | **1st** | 7th consecutive year (official report) |
| 2026 | **1st** | 9th consecutive year |

</div>

Our dataset captures the critical window, the years Finland was climbing.
By 2018, it had overtaken Switzerland, Norway and Denmark to claim #1,
and has never been displaced since.

What our correlation analysis reveals is *why* this makes sense. Finland
scores in the top tier across the four factors that matter most in the data:
GDP (0.79 correlation with happiness), Health (0.74), Social Support (0.65),
and Freedom (0.55). It also maintains one of the lowest corruption scores
in the world, and citizens report extremely high trust in public institutions.

Finland did not win by being the richest country, it was not. It won by
being **consistently strong across every dimension that drives happiness**,
while other wealthy nations fell short on trust, freedom or social cohesion.

As Finnish philosopher Frank Martela put it:
> *"It would be more accurate to say that Finland has the least unhappy
> people in the world."*

---

## Visualisations

| Chart | What it shows |
|---|---|
| Top 10 Happiest Countries (2019) | Which nations lead and by how much |
| Bottom 10 Unhappiest Countries (2019) | The stark contrast at the other end |
| Correlation Heatmap | Which factors drive happiness most (and least) |
| Global Happiness Trend 2015–2019 | How world happiness moved year by year |
| Happiness by Region | Which parts of the world are happiest on average |
| GDP vs Happiness Scatter Plot | 782-point visualisation of the wealth-happiness link |
| Nordic Countries Trend 2015–2019 | Finland's rise tracked against its closest rivals |

---

## Technical Summary

- **Language:** Python 3.11
- **Libraries:** pandas, matplotlib, seaborn
- **Key techniques:** data wrangling across inconsistently formatted datasets,
  EDA, Pearson correlation analysis, multi-year trend analysis,
  regression visualisation, groupby aggregation
- **Data points:** 782 rows across 5 years and 158 countries

---

## References & Data

| Source | Link |
|---|---|
| World Happiness Report Dataset | [Kaggle — Download here](https://www.kaggle.com/datasets/unsdsn/world-happiness) |
| Official World Happiness Report | [worldhappiness.report](https://worldhappiness.report) |
| Finland 9-year streak — 2024 Report | [World Happiness Report 2024](https://worldhappiness.report/news/world-happiness-report-2024-most-comprehensive-picture-yet-of-happiness-across-generations/) |

---

## Author

**Salma Ayoubi** — Data Analyst  
[GitHub Profile](https://github.com/SalmaAyoubi22)
