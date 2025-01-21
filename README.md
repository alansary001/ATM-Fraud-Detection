This project is a Banking Fraud Detection System that simulates various types of fraudulent activities in banking transactions, such as **large withdrawals,** **frequent transactions**, **location anomalies**, and **insufficient funds**.  
The system generates synthetic banking transaction data, applies fraud detection rules, and visualizes the results using various plots to analyze transaction patterns.

Key Features  
1. Large Withdrawal Detection: Identifies large withdrawals over a predefined threshold and categorizes them as potential fraud.
2. Frequent Transaction Detection: Tracks time differences between consecutive transactions to identify potential cases of frequent transactions that might be fraudulent.
3. Location Anomaly Detection: Detects any discrepancies in the ATM location, flagging transactions that occur at different locations in quick succession.
4. Balance Check: Ensures that the transaction amount does not exceed the account balance for withdrawal transactions.
5. Data Visualization: Visualizes the results using several plots such as:
6. Bar plot of transactions by fraud category.
7. Frequency of transactions over time.
8. Location anomaly detection across ATM locations.
9. Scatter plot of account balance vs transaction amount.
10. Distribution of time differences between consecutive transactions.
