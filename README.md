# Bank Customer Churn Analysis

## Overview
This Power BI project analyzes customer churn for a bank by identifying the key factors influencing whether a customer stays or leaves the bank. By examining customer attributes like credit score, balance, tenure, and more, this project aims to uncover insights that can help the bank improve its retention strategies and reduce churn.

The project integrates data from various sources, including customer demographics, transaction data, and account details, and provides interactive visualizations to track churn over time, segmented by various customer attributes.

---

## Table of Contents
- [Project Description](#project-description)
- [Data Sources](#data-sources)
- [Key Metrics and Measures](#key-metrics-and-measures)
- [Power BI Visualizations](#power-bi-visualizations)
- [How to Use](#how-to-use)
- [Installation](#installation)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

---

## Project Description
The Bank Churn Analysis project is designed to help businesses identify key indicators for customer churn. The analysis helps answer the following questions:

- What factors contribute to customers leaving the bank?
- How does customer behavior vary with attributes like age, balance, and credit score?
- What retention strategies can be implemented to reduce churn?

This project combines data wrangling, exploration, and analysis in Power BI to visualize churn trends, cohort analysis, and the impact of various customer demographics on churn.

---

## Data Sources
The analysis uses data from the following sources:

- **ActiveCustomer:** Contains data on customers who are currently active with the bank.
- **Bank_Churn:** Contains data on customers who have exited the bank.
- **CreditCard:** Information on whether customers have a credit card.
- **CustomerInfo:** Includes general customer data such as name, age, and other personal details.
- **ExitCustomer:** Data for customers who have left the bank.
- **Gender:** Customer gender information.
- **Geography:** Customer location data, which can help segment churn by region.

The data is consolidated into a single table named `BankChurn`, which includes customer information and whether they have exited the bank (`Exited` column). A `Date` table is also used to provide time-based analysis on churn trends.

---

## Key Metrics and Measures
The following DAX measures were created to facilitate churn analysis:

- **Churn Rate:** Percentage of customers who have exited the bank.
- **Total Customers:** Total number of customers in the bank.
- **Retained Customers:** Number of customers who have stayed with the bank.
- **Exited Customers:** Number of customers who have left the bank.
- **Average Credit Score of Exited Customers:** Shows the average credit score of customers who left.
- **Average Balance of Retained Customers:** Shows the average balance of customers who stayed.
- **Customer Churn by Year:** Churn statistics segmented by the year of customer acquisition.
- **Monthly Churn Trend:** Churn trends tracked monthly.

These measures help uncover important patterns, such as the relationship between credit score and churn, the impact of customer tenure on retention, and how churn trends evolve over time.

---

## Power BI Visualizations

### 1. Customer Churn Dashboard
![Customer Churn Dashboard](https://github.com/viplavs2004/Rbc-Bank-Churn-Analysis-Power-Bi/blob/main/RBc%20bank%20Churn%20analysis%20dashboard.png)

- This dashboard provides an overview of customer churn.
- Displays key metrics such as total customers, retained customers, and churn rate.
- Includes a **geographical churn analysis**, showing churn rates across different regions.
- Users can filter by **Age, Gender, Geography, and Credit Score** to see how different demographics contribute to churn.

### 2. Churn Rate and Active vs. Exited Customers
![Churn Analysis](https://github.com/viplavs2004/Rbc-Bank-Churn-Analysis-Power-Bi/blob/main/RBc%20bank%20Churn%20analysis%20dashboard%202.png)

- Compares the number of active and exited customers.
- Displays **monthly churn trends** using a line graph.
- Provides insights into **customer tenure** and how long customers stay before leaving.
- Users can interact with slicers to filter churn data by **year, region, and credit score**.

### 3. Active vs. Exited Customer Comparison
![Active vs Exited Customers](https://github.com/viplavs2004/Rbc-Bank-Churn-Analysis-Power-Bi/blob/main/RBc%20bank%20Churn%20active%20customer%20exited%202.png)

- Displays side-by-side comparisons of **active vs. exited customers** based on attributes such as balance, tenure, and credit score.
- Helps identify patterns in the behavior of churned customers vs. retained customers.
- Users can apply filters for a deeper dive into specific demographics.

---

## How to Use
To interact with the Power BI report and gain insights, follow these steps:

1. **Clone or Download the Repository:**
   - Clone this repository or download it as a ZIP file to your local machine.

2. **Open Power BI:**
   - Open the Power BI Desktop application.

3. **Import the Power BI File:**
   - Open the `BankChurn.pbix` file in Power BI.

4. **Explore the Report:**
   - Use the built-in slicers and filters to interact with the visualizations.
   - Segment data by demographics such as Age, Geography, and Credit Score.

5. **Customize Visuals:**
   - Modify or extend the Power BI report as needed to meet your specific business needs.

---

## Installation
### Prerequisites:
- **Power BI Desktop:** Ensure that you have Power BI Desktop installed on your machine.
- **Data Source Access:** The data source files (e.g., CSV, Excel, or database access) should be available and properly linked within the Power BI file.

### Steps to Install:
1. Clone or download this repository.
2. Open the `BankChurn.pbix` file in Power BI.
3. Refresh the data source connections if needed (based on the format of your data files).
4. Review the `Date` table and `BankChurn` table to ensure all data has been loaded correctly.

---

## Contributing
We welcome contributions to enhance the project further. If you would like to contribute, follow these steps:

1. **Fork the Repository.**
2. **Create a new branch** (e.g., `feature-branch`).
3. **Make your changes** or add new features.
4. **Commit your changes** with a descriptive message.
5. **Push the changes** to your forked repository.
6. **Open a Pull Request** to merge your changes.

Please ensure that your changes are well-documented, and add tests for any new features if applicable.

---

## Acknowledgements
- **Power BI** for enabling powerful data visualizations and analysis.
- **GitHub** for version control and collaboration.
- **Open Source Community** for contributing to various tools and resources used in this project.

