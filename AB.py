import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import chi2_contingency

# Load the dataset
df = pd.read_csv('C:/Users/Jacqy/Documents/AB/smart.csv')

# Streamlit app title and description
st.title("A/B Testing Analysis")
st.write("""
This app performs an A/B test analysis on conversion rates and displays relevant statistics and visualizations.
""")

# Show first 5 rows of the dataset
st.subheader("Dataset Preview")
st.write(df.head())

# Missing values
st.subheader("Missing Values")
st.write(df.isnull().sum())

# First 100 rows
st.subheader("First 100 Rows")
st.write(df.head(100))

# Check for duplicates
st.subheader("Duplicate Records")
st.write(f"Number of duplicate records: {df.duplicated().sum()}")

# Descriptive statistics
st.subheader("Descriptive Statistics")
st.write(df.describe())

# Group by Region for Conversion Sum
st.subheader("Conversion Sum by Region")
st.write(df.groupby('Region')['Conversion'].sum())

# Group by Device for Conversion Sum
st.subheader("Conversion Sum by Device")
st.write(df.groupby('Device')['Conversion'].sum())

# Group by Group and Device for Conversion Sum
st.subheader("Conversion Sum by Group and Device")
st.write(df.groupby(['Group', 'Device'])['Conversion'].sum())

# Conversion rate by group
conversion_rate = df.groupby('Group')['Conversion'].mean()
st.subheader("Conversion Rate by Group")
st.write(conversion_rate)

# Bar plot of conversion rates by group
st.subheader("Conversion Rate by Group - Bar Plot")
fig, ax = plt.subplots()
conversion_rate.plot(kind='bar', color=['skyblue', 'salmon'], ax=ax)
ax.set_title('Conversion Rate by Group')
ax.set_ylabel('Conversion Rate')
ax.set_xlabel('Group')
st.pyplot(fig)

# Group A and Group B conversion rate
group_a_conversion = df[df['Group'] == 'A']['Conversion'].mean()
group_b_conversion = df[df['Group'] == 'B']['Conversion'].mean()

st.subheader("Conversion Rate for Group A and Group B")
st.write(f"Group A Conversion Rate: {group_a_conversion}")
st.write(f"Group B Conversion Rate: {group_b_conversion}")

# Time Spent histogram by group
st.subheader("Time Spent Histogram by Group")
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Plot separate histograms for Group A and Group B
df[df['Group'] == 'A']['Time Spent (s)'].hist(bins=20, alpha=0.6, ax=ax[0])
ax[0].set_title("Group A - Time Spent")
ax[0].set_xlabel("Time Spent (s)")
ax[0].set_ylabel("Frequency")

df[df['Group'] == 'B']['Time Spent (s)'].hist(bins=20, alpha=0.6, ax=ax[1])
ax[1].set_title("Group B - Time Spent")
ax[1].set_xlabel("Time Spent (s)")
ax[1].set_ylabel("Frequency")

st.pyplot(fig)

# Z-test for conversion rate between Group A and Group B
st.subheader("Z-test for Conversion Rates")

# Number of conversions and total participants in each group
conversions_A = df[df['Group'] == 'A']['Conversion'].sum()
conversions_B = df[df['Group'] == 'B']['Conversion'].sum()
n_A = df[df['Group'] == 'A'].shape[0]
n_B = df[df['Group'] == 'B'].shape[0]

# Perform the z-test
z_stat, p_value = proportions_ztest([conversions_A, conversions_B], [n_A, n_B])

# Output the result of the z-test
st.write(f"Z-statistic: {z_stat}")
st.write(f"P-value: {p_value}")

# Chi-square test for independence
st.subheader("Chi-square Test for Independence")

# Create a contingency table
contingency_table = pd.crosstab(df['Group'], df['Conversion'])

# Perform the chi-square test
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Output the result
st.write(f"Chi-square statistic: {chi2}")
st.write(f"P-value: {p}")
