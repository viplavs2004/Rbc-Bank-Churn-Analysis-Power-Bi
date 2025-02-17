# Bank Customer Churn Analysis

## Overview
This Power BI project analyzes customer churn for a bank by identifying the key factors influencing whether a customer stays or leaves the bank. By examining customer attributes like credit score, balance, tenure, and more, this project aims to uncover insights that can help the bank improve its retention strategies and reduce churn.

The project integrates data from various sources, including customer demographics, transaction data, and account details, and provides interactive visualizations to track churn over time, segmented by various customer attributes.

---

## Table of Contents
1. [Project Description](#project-description)
2. [Data Sources](#data-sources)
3. [Key Metrics and Measures](#key-metrics-and-measures)
4. [Power BI Visualizations](#power-bi-visualizations)
5. [How to Use](#how-to-use)
6. [Installation](#installation)
7. [Contributing](#contributing)
8. [License](#license)
9. [Acknowledgements](#acknowledgements)

---

## Project Description
The **Bank Churn Analysis** project is designed to help businesses identify key indicators for customer churn. The analysis helps answer the following questions:

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
The project contains the following visualizations:

### 1. Churn Rate Trends
This line chart displays the **churn rate over time**, helping users identify periods with higher customer churn.

![Churn Rate Trends](https://github.com/viplavs2004/Rbc-Bank-Churn-Analysis-Power-Bi/blob/main/RBc%20bank%20Churn%20analysis%20dashboard.png)

### 2. Retention vs. Exited Customers
This pie chart shows the proportion of **retained vs. exited customers**, providing a quick overview of customer loyalty.

![Retention vs. Exited Customers](https://github.com/viplavs2004/Rbc-Bank-Churn-Analysis-Power-Bi/blob/main/RBc%20bank%20Churn%20analysis%20dashboard%202.png)

### 3. Churn by Customer Demographics
These bar charts segment **churn data by customer attributes** such as Age, Balance, Credit Score, Tenure, and Geography.

![Churn by Demographics](https://github.com/viplavs2004/Rbc-Bank-Churn-Analysis-Power-Bi/blob/main/RBc%20bank%20Churn%20active%20customer%20exited%202.png)

### 4. Cohort Analysis
This visualization shows **how customer churn behavior changes based on the year they joined the bank**, allowing businesses to target specific customer groups.

### 5. Average Customer Attributes
This section displays average metrics like **Balance, Credit Score, and Tenure** for both exited and retained customers, helping in understanding key differences.

---

## How to Use
To interact with the Power BI report and gain insights, follow these steps:

1. **Clone or Download the Repository:** Clone this repository or download it as a ZIP file to your local machine.
2. **Open Power BI:** Open the Power BI Desktop application.
3. **Import the Power BI File:** Open the `BankChurn.pbix` file in Power BI.
4. **Explore the Report:** Use the built-in slicers and filters to interact with the visualizations. You can segment data by demographics such as Age, Geography, Credit Score, etc.
5. **Customize Visuals:** Modify or extend the Power BI report as needed to meet your specific business needs.

### Applying Filters
- **Date Filter:** Allows users to analyze churn trends for a specific time range.
- **Geography Filter:** Helps in comparing churn rates across different regions.
- **Credit Score Filter:** Enables understanding of how credit scores impact churn behavior.
- **Balance Filter:** Helps visualize how account balances relate to retention.
- **Tenure Filter:** Identifies how long-term customers behave differently compared to new customers.

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

1. Fork the repository.
2. Create a new branch (e.g., `feature-branch`).
3. Make your changes or add new features.
4. Commit your changes with a descriptive message.
5. Push the changes to your forked repository.
6. Open a Pull Request to merge your changes.

Please ensure that your changes are well-documented and add tests for any new features if applicable.

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

## Acknowledgements
- **Power BI** for enabling powerful data visualizations and analysis.
- **GitHub** for version control and collaboration.
- **Open Source Community** for contributing to various tools and resources used in this project.

