**README.md  PART1**
<br>**Project Overview**</br>
<div align="center">
  <img src="C:\Users\admin\Downloads\masai logo.jfif" width="400" />

  # Laptop_Data Analysis and Predictions
  
  **Name:** S.Geetha 
  **Student ID:** (iitp_aimltn_2602552 )
</div>

<div align="center">
  # Capstone Project-2026. **Laptop Analysis Prediction**
  AI & ML ESSENTIALS.
</div>
# Applied-AI-ML-Essentials-CAPSTONE-2026
Laptop Data Analysis &amp; Price prediction: This project is about analyzing and modelling a comprehensive dataset(Laptop_Data) to decode how technical components impact the overall market cost of a device.
**PROJECT OVER VIEW**:en
I would like to thank Masai by Vishlesan i-Hub, IIT Patna Indian Institute of Technology, Patna,for this wonderful opportunity given to built a capstone project. Dedicated to my beloved Lord and my parents, Industry mentors,Teaching assistants and Project Co-ordinator!
In this rapidly evolving electronics market, Laptop pricing is highly dynamic and dependent on complex hardware combinations.Consumers and retailers often find it challenging to determine whether a laptop is fairly priced based on hardware.
**About this project**
The Laptop price prediction dataset track various technical specifications and their market prices.Features like RAM, Memory written in text column are converted to numerical columns for machine learning purpose.Categorical column contain text labels eg-Apple , HP,Dell.
Each dataset maps critical technical physical attributes that include : Brand and Category-Manufactrer(company), Core Hardware-(CPU,Clock speed) Storage configuration - Storage type (ssd vs hdd) total capacity, Physical metrics-screen size,Display resolution and total weight.
**Key Project Objectives**
Data pre cleaning- Handle noise and mixed text
**Capstone Pipeline outline**
1.Environment Setup: Jupiter notebookenvironment(ipynb) Handles dynamic script path.
2.Data aquisition :Downloading Laptop price prediction datasetfrom a public respository via code and stored in ournote book.
3.Directory creation: Saving outputs to specific path which explicitly exist in workspace.
**Part 1 — Data Acquisition, Cleaning, and Exploratory**
**Task 1 & 2**: Dataset loaded(laptop_data).It has mixed columns. gb is converted to numerical column. Loaded and checked for missing and duplicate values.Null value analysis made,numeric columns filled using median because it is less affected by outliers than the mean.This makes the median relieable measure of central tendency for skewed numerical data . The memory column not numeric,It is an object-string columnsuch as 256gb ssd, 1tb hdd,128 ssd + 1TB HDD.String columns are not included in numerical columns,so missing values are not filled.
**Task 3**The number of rows removed was calculated by comparing the dataset size before and after duplicate removal.The percentage of missing values determine whether duplicate removal after the missing data distribution.Null percentage remains unchanged indicates removing duplicate rows did not alter the overall pattern of missing values.
**Task 4**  Check memory usage before conversion. Convert RAM from object to numeric-becomes integer/ float column. COMPANY to category.
GB suffix was removed and the column was converted into numeric type using** pd.tonumeric..., errors='coerce').
** The company column has repeated string values suitable for caegory conversion reduce memory usage because store only once and refer internally.memory usage was measured befor and after conversion using** df.memory usage(deep-true .sum())**
**Task 5** Descriptive statistics generated using df.describe().Skewness for each column calculated using **df.skew()**
Positive skewness has a long tail towards high values(right skewed).Negative skewes long tail towards lower values(left skewed).
**Effect on MEAN imputation** for highly skewed data mean influenced by extreme values(outliers)using median for imputing values more appropriate because it is less affected by skewness and outliers. Converting Ram to numeric ,**** PRICE & RAM are the best numeric 
**Task 6** Outlier detection: XX YY outliers are detected.The outliers are not removed because they represent valid high end laptop configurations,Removing will result in loss of important informations.In part 2 the outliers will be retained initially and evaluated.
**Task 7** Visualization: Five visualization plots are generated and saved as png in part1 folder.
**Line Plot** shows how laptop price varries across dataset.It helps to visualize trends and fluctuations in price values.
**Barchart** Barchart compares average laptop price across different companies.Company with taller bars have higher average prices.
**Histogram** shows most skewd numeric column indicates the distribution of values,right skewed distribution has most values concenterated at lower price with few high price laptops, creating long tail on the right.
**Scatter plot** Scatter plot between RAM and PRICE shows positive relationship appear moderately positive.
**Box plot** Compares the distribution of Laptop across different companies.Difference in the median  indicate different typical prices.
Difference in the spread shows how much price vary with each company,outlier point represents expensive and inexpensive laptops.
**Correlation heat map Created to visualize the relationship among the numeric variable range from -1 to +1.
+1 indicates strong positive correlation
-1 indicatestrong negative correlation
0 indicates little or no linear relationship.
which means with more RAM tend to have high rate or price.Correlation map computed using df.corr() visualized with heat map using sns heatmap.X and Y strongly correlated a plausible third variable explain the relationship of overall laptop configurations.
**Imputation strategy comparison** For positively skewed distribution mean is pulled upward, the medien remains closer to the center.
For a negatively skewed distribution the mean pulled downward whereas the medien represents the central tendency. So median is chosen for imputation ,it is more robust to skewness .After imputation isnull().sum() confirmed no missing values in the numeric columns.
If the column has no missing values produce exactly same output because fillna() has nothing to fill.No nan values to replace.
**Conclusion:** The two numeric columns did not contain missing values applying mean or median imputation produce identical result and no null values to replace.Median is the pure imputation strategy for skewed distribution because it is less affected by outliers than mean.
**Grouped aggregation** CATEGORICAL COLUMN:COMPANY
                        NUMERICAL COLUMN  :PRICE
Dataset grouped by COMPANY column and the mean standard deviation and count of price calculated.
Company with highest average price -High standard deviation indicates aptop price varies considerably within the company.
Ratio of highest group mean was ratio,Larger ratio shows company carries useful predictive information, average price differs across company. RAM CPU STORAGEneeded for accurate price distribution.grouby.agg['mean','standard','count']) Null % table printed for all column.
**Saved in part1 folder**
Laptop-Price-Prediction/
│
├── Part1/
│   ├── Part1.ipynb
│   ├── cleaned_data.csv
│   ├── laptop_data.csv          
│   ├── README.md
│   ├── line_plot.png
│   ├── bar_chart.png
│   ├── histogram.png
│   ├── scatter_plot.png
│   ├── box_plot.png
│   └── correlation_heatmap.png
│
└── .gitignore (optional)
