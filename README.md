Bank Customer Churn Analysis
Overview
This Power BI project analyzes customer churn for a bank by identifying the key factors influencing whether a customer stays or leaves the bank. By examining customer attributes like credit score, balance, tenure, and more, this project aims to uncover insights that can help the bank improve its retention strategies and reduce churn.

The project integrates data from various sources, including customer demographics, transaction data, and account details, and provides interactive visualizations to track churn over time, segmented by various customer attributes.

Table of Contents
Project Description
Data Sources
Key Metrics and Measures
Power BI Visualizations
How to Use
Installation
Contributing
License
Project Description
The Bank Churn Analysis project is designed to help businesses identify key indicators for customer churn. The analysis helps answer the following questions:

What factors contribute to customers leaving the bank?
How does customer behavior vary with attributes like age, balance, and credit score?
What retention strategies can be implemented to reduce churn?
This project combines data wrangling, exploration, and analysis in Power BI to visualize churn trends, cohort analysis, and the impact of various customer demographics on churn.

Data Sources
The analysis uses data from the following sources:

ActiveCustomer: Contains data on customers who are currently active with the bank.
Bank_Churn: Contains data on customers who have exited the bank.
CreditCard: Information on whether customers have a credit card.
CustomerInfo: Includes general customer data such as name, age, and other personal details.
ExitCustomer: Data for customers who have left the bank.
Gender: Customer gender information.
Geography: Customer location data, which can help segment churn by region.
The data is consolidated into a single table named BankChurn, which includes customer information and whether they have exited the bank (Exited column). A Date table is also used to provide time-based analysis on churn trends.

Key Metrics and Measures
The following DAX measures were created to facilitate churn analysis:

Churn Rate: Percentage of customers who have exited the bank.
Total Customers: Total number of customers in the bank.
Retained Customers: Number of customers who have stayed with the bank.
Exited Customers: Number of customers who have left the bank.
Average Credit Score of Exited Customers: Shows the average credit score of customers who left.
Average Balance of Retained Customers: Shows the average balance of customers who stayed.
Customer Churn by Year: Churn statistics segmented by the year of customer acquisition.
Monthly Churn Trend: Churn trends tracked monthly.
These measures help uncover important patterns, such as the relationship between credit score and churn, the impact of customer tenure on retention, and how churn trends evolve over time.

Power BI Visualizations
The project contains the following visualizations:

Churn Rate Trends: Line charts displaying the churn rate over time (monthly/quarterly).
Retention vs. Exited Customers: Pie charts to show the proportion of retained vs. exited customers.
Churn by Customer Demographics: Bar charts segmented by Age, Balance, Credit Score, Tenure, and Geography.
Cohort Analysis: Visualizes how customers' churn behavior varies based on the year they joined the bank.
Average Customer Attributes: Displays average metrics like Balance, Credit Score, and Tenure for exited vs. retained customers.
These visualizations allow business stakeholders to explore key insights and make data-driven decisions.

How to Use
To interact with the Power BI report and gain insights, follow these steps:

Clone or Download the Repository: Clone this repository or download it as a ZIP file to your local machine.

Open Power BI: Open the Power BI Desktop application.

Import the Power BI File: Open the BankChurn.pbix file in Power BI.

Explore the Report: Use the built-in slicers and filters to interact with the visualizations. You can segment data by demographics such as Age, Geography, Credit Score, etc.

Customize Visuals: Modify or extend the Power BI report as needed to meet your specific business needs.

Installation
Prerequisites:
Power BI Desktop: Ensure that you have Power BI Desktop installed on your machine.
Data Source Access: The data source files (e.g., CSV, Excel, or database access) should be available and properly linked within the Power BI file.
Steps to Install:
Clone or download this repository.
Open the BankChurn.pbix file in Power BI.
Refresh the data source connections if needed (based on the format of your data files).
Review the Date table and BankChurn table to ensure all data has been loaded correctly.
Contributing
We welcome contributions to enhance the project further. If you would like to contribute, follow these steps:

Fork the Repository.
Create a new branch (e.g., feature-branch).
Make your changes or add new features.
Commit your changes with a descriptive message.
Push the changes to your forked repository.
Open a Pull Request to merge your changes.
Please ensure that your changes are well-documented, and add tests for any new features if applicable.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Power BI for enabling powerful data visualizations and analysis.
GitHub for version control and collaboration.
Open Source Community for contributing to various tools and resources used in this project
