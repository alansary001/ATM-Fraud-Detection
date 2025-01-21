This project is a Banking Fraud Detection System that simulates various types of fraudulent activities in banking transactions, such as large withdrawals, frequent transactions, location anomalies, and insufficient funds. The system generates synthetic banking transaction data, applies fraud detection rules, and visualizes the results using various plots to analyze transaction patterns.

Key Features
Large Withdrawal Detection: Identifies large withdrawals over a predefined threshold and categorizes them as potential fraud.
Frequent Transaction Detection: Tracks time differences between consecutive transactions to identify potential cases of frequent transactions that might be fraudulent.
Location Anomaly Detection: Detects any discrepancies in the ATM location, flagging transactions that occur at different locations in quick succession.
Balance Check: Ensures that the transaction amount does not exceed the account balance for withdrawal transactions.
Data Visualization: Visualizes the results using several plots such as:
Bar plot of transactions by fraud category.
Frequency of transactions over time.
Location anomaly detection across ATM locations.
Scatter plot of account balance vs transaction amount.
Distribution of time differences between consecutive transactions.
