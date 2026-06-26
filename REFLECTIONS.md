# Project Reflections: World Happiness Analysis

*A critical look at what this analysis does well, where it falls short,
and what I would do differently.*

---

## What Worked Well

The decision to combine five years of data into one unified dataset was the
right call. It allowed trend analysis that a single-year snapshot would never
reveal, most importantly, Finland's rise from 5th to 1st between 2015 and
2019, which turned out to be the most compelling story in the data.

Standardising inconsistent column names across five separately formatted
datasets was the most technically demanding part of this project and the
most valuable lesson. Real-world data is messy, and the ability to clean
and unify it is something I now feel confident doing from scratch.

The correlation heatmap was the single most informative visualisation.
It answered the central question of the project in one chart: GDP and
health matter most, generosity barely matters at all.

---

## Limitations

**The data stops at 2019.**
There is a 7-year gap between where this dataset ends and today. Given
that Finland has continued to rank 1st every year from 2018 to 2026,
extending the analysis to include 2020–2024 would paint a much more
complete picture. It would also capture the impact of COVID-19
pandemic on global happiness, a dimension that would be fascinating
to analyse.

**The Region column was only available in 2015 and 2016.**
This limited the regional analysis to a single-year snapshot rather
than a trend over time. A more complete dataset would allow tracking
how entire regions shifted across the five years.

**Correlation does not explain causation.**
GDP and happiness are strongly correlated (r = 0.79), but this data
alone cannot tell us that wealth causes happiness. It is equally
possible that happier societies build stronger economies. A more
rigorous analysis would use regression modelling to quantify how
much each factor independently contributes to the happiness score,
controlling for the others.

**The happiness score is self-reported.**
The score is based entirely on how people rate their own lives, not
on objective quality of life metrics. Two countries with identical GDP
and healthcare could score differently based purely on cultural
attitudes toward expressing satisfaction or dissatisfaction. This is
a known limitation of the World Happiness Report itself, not just
this analysis, and it is worth keeping in mind when interpreting
any finding.

---

## What I Would Do Differently

**Extend the dataset to 2024.**
The most obvious improvement. Five years of data tells a partial story.
Nine years would tell a complete one, and would make the Finland
narrative far more powerful with actual data rather than external
references.

**Build a regression model.**
A multiple linear regression would allow me to quantify how much each 
factor independently predicts happiness, controlling for all the others.
Right now, I can say GDP correlates most strongly, but I cannot say
by how much it matters relative to health or social support when
Both are considered together.

**Investigate the outliers.**
The countries that sit furthest from the regression line are often where
the most interesting stories live. Why does Costa Rica score so high
despite a modest GDP? Why do Gulf states like Qatar underperform relative
to their enormous wealth? Digging into those specific cases would add
real depth to the analysis.

**Build an interactive dashboard.**
A static chart can only show one angle at a time. An interactive Tableau
A Power BI dashboard would let someone explore the data themselves,
filtering by region, year, or factor, which would make the findings
far more accessible and engaging.

**Add statistical significance testing.**
Correlation coefficients tell you the strength of a relationship but
not whether it is statistically significant. Adding p-values would
make the analysis more rigorous and credible.

---

## What This Project Taught Me

Beyond the technical skills: pandas, matplotlib, seaborn, data wrangling
across inconsistently formatted datasets. This project taught me to think
about data as a story with a beginning, a narrative, and open questions at
the end.

The Finland finding was not something I set out to investigate. It emerged
from the data, and following that thread, connecting it to nine years of
real-world reports beyond the dataset, is what turned a standard EDA
exercise into something I can speak about with genuine enthusiasm.

That, I think, is what data analysis is actually about.

---

*Salma Ayoubi — June 2026*
