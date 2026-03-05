<p align="center">
  <img src="./churnboardpic.png" alt="GrandStay Operations Dashboard" width="100%">
</p>

### <a href="https://veritasbank-churn-dashboard.streamlit.app/" target="_blank" rel="noopener noreferrer">Live Churn Dashboard Link</a>

# Veritas Bank: Customer Churn and Retention Analysis

[cite_start]This project analyzes customer attrition patterns for Veritas Bank, a UK-headquartered retail bank with major operations in Germany and France[cite: 4]. [cite_start]By utilizing SQL Server and Power BI, the study identifies key churn drivers and provides data-driven strategies for regional optimization and personalized engagement[cite: 22, 23, 77].

---

## Business Overview and Problem
[cite_start]Veritas Bank was established in the 1990s and has grown its customer base to over 3 million users[cite: 4, 5]. [cite_start]Despite its technology-driven approach and strong online banking capabilities, the bank is currently facing increased customer churn[cite: 6, 10]. 

The primary challenges include:
* [cite_start]Intense competition from neobanks and fintech startups[cite: 11].
* [cite_start]A perceived decrease in customer engagement within the German and French markets[cite: 12].
* [cite_start]An absence of real-time churn monitoring and targeted retention strategies based on behavioral insights[cite: 13, 14].

---

## Project Focus and Scope
[cite_start]The goal of this project is to build an operational baseline to quantify risk profiles and identify common characteristics among customers who have exited the bank[cite: 37, 41].

The project followed a four-phase analytical approach:
1. [cite_start]Database Design and Data Importation: Setting up the environment in SQL Server and performing data quality checks[cite: 86, 89].
2. [cite_start]Data Transformation and Feature Engineering: Creating derived columns and views specifically for churn analysis[cite: 97, 98, 99].
3. [cite_start]Power BI Modeling and Dashboard Development: Connecting to the SQL database to visualize customer demographics and churn metrics[cite: 91, 92, 95].
4. [cite_start]Strategic Reporting: Summarizing insights and recommendations to guide marketing and service policies[cite: 26, 101, 102].

---

## Technology Stack
* [cite_start]Database Management: Microsoft SQL Server for data processing and transformation[cite: 78, 80].
* [cite_start]Visualization: Microsoft Power BI for data modeling (DAX) and interactive dashboard development[cite: 81, 82, 93].
* [cite_start]Documentation: Microsoft PowerPoint for executive summaries[cite: 101].

---

## Analytical Insights from the Dashboard

Based on the analysis of 10,000 customers, the following insights were derived from the performance data:



### 1. Demographic Risk Factors
* Geography: Germany and France show the highest churn rates at 18.06% and 17.52% respectively, compared to only 9.93% in the UK.
* Age: Customers classified as "Young Adults" exhibit the highest churn rate at 14.89%, while "Older Adults" show the highest retention.
* Credit Score: The "Fair" credit score category accounts for the largest portion of churned customers at 34.09%.

### 2. Behavioral Insights
* Active Status: There is a significant correlation between inactivity and churn; inactive members are significantly more likely to exit (1,385 customers) than active members (510 customers).
* Product Engagement: Customers holding only one product ("Low Engagement") represent the highest risk group.
* Account Balance: The "Very Low" balance segment has the highest churn rate at 18.54%.

---

## Strategic Recommendations
* Regional Focus: Implement targeted retention campaigns specifically for the German and French markets to address the high regional attrition rates.
* Engagement Programs: Develop incentives to transition inactive members to "Active" status, as active membership is a primary driver for retention.
* Product Cross-Selling: Encourage "Low Engagement" customers to adopt additional products, as higher product holdings correlate with increased loyalty.
* High-Risk Monitoring: Establish a proactive monitoring system for customers in the "Fair" credit score and "Very Low" balance segments.

---
**Project Credits: Amdari | Veritas Bank Analytics**