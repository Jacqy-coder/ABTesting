# A/B Testing Analysis

This project analyzes an A/B test experiment using Python. The dataset compares two groups (A and B) based on user conversion behavior. The objective is to determine if there's a statistically significant difference in conversion rates and whether group assignment influences conversion outcomes.

---

##  Code Overview

### 1. **Data Loading & Inspection**
- Loads the dataset using `pandas`.
- Displays the first few rows, checks for missing or duplicate values.
- Provides descriptive statistics for quick insights.

### 2. **Grouped Analysis**
- Aggregates conversion data by:
  - `Region`
  - `Device`
  - `Group` + `Device`
- Computes and displays the **conversion rate per group**.

### 3. **Visualizations**
- **Bar chart** comparing conversion rates between Group A and Group B.
- **Histograms** showing distribution of time spent per group.

### 4. **Statistical Testing**
- **Z-test for proportions**: Determines if the conversion rates between Group A and Group B are significantly different.
- **Chi-square test for independence**: Checks if conversion is dependent on group assignment.

---

##  Results

### Z-Test
- Used to compare conversion rates between groups.
- Output includes the Z-statistic and p-value.

### Chi-Square Test
- **Chi-square statistic**: `0.0041`  
- **P-value**: `0.9492`

---

## Conclusion

The **p-value of 0.949** from the chi-square test is much higher than the 0.05 threshold. This means there is **no statistically significant relationship** between the group assignment and conversion. The conversion behavior appears to be **independent of the group**.

---

## Recommendation

- Since there is no significant difference between the two groups, **either group can be maintained** without impacting conversion.
- It is advisable to:
  - Continue monitoring with a larger or segmented dataset.
  - Explore additional factors like device type, time spent, and user region.
  - Consider qualitative feedback or business context before making final decisions.

---

##  Tools Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- SciPy  
- Statsmodels  

---

## Author

**Jacqueline Wanjiku**  
Data Analyst focused on leveraging data to inform business strategy and performance optimization.
