import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Creating the DataFrame
np.random.seed(42)

data = {
    'TransactionID': range(1, 6),
    'ATM_ID': np.random.randint(1000, 9999, size=5),
    'CardNumber': np.random.randint(1000000000000000, 9999999999999999, size=5 , dtype='int64'),
    'Amount': np.random.randint(100, 5000, size=5),
    'Time': pd.date_range(start='2023-01-01', periods=5, freq='h'), 
    'Location': np.random.choice(['Location A', 'Location B', 'Location C'], size=5),
    'AccountBalance': np.random.randint(1000, 50000, size=5),
    'TransactionType': np.random.choice(['Withdrawal', 'Deposit', 'Transfer'], size=5)
}

df = pd.DataFrame(data)

# Fraud Detection Rules
def detect_large_withdrawals(row):
    if row['TransactionType'] == 'Withdrawal' and row['Amount'] > 1000:
        return 'Large Withdrawal'
    return 'Normal'

def detect_frequent_transactions(df):
    df['Time'] = pd.to_datetime(df['Time'])
    df['TimeDiff'] = df['Time'].diff().dt.total_seconds().fillna(0)
    return df

df['FraudCategory'] = df.apply(detect_large_withdrawals, axis=1)
df = detect_frequent_transactions(df)

# Simulating ATM Location Anomalies (for demo purposes)
def check_location_anomalies(df):
    df['LocationAnomaly'] = np.where(df['Location'] != df['Location'].shift(), 'Anomaly', 'Normal')
    return df

df = check_location_anomalies(df)

def check_account_balance(row):
    if row['TransactionType'] == 'Withdrawal' and row['Amount'] > row['AccountBalance']:
        return 'Insufficient Funds'
    return 'Normal'

df['BalanceCheck'] = df.apply(check_account_balance, axis=1)

# Visualizations

# 1. Bar plot for Fraud Categories
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='FraudCategory', hue='FraudCategory', palette='Set2')  # Set hue to FraudCategory
plt.title('Count of Transactions by Fraud Category')
plt.xlabel('Fraud Category')
plt.ylabel('Number of Transactions')
plt.show()

# 2. Plot transaction frequency over time
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Time', hue='FraudCategory', palette='Set1')
plt.title('Transaction Frequency Over Time')
plt.xlabel('Time')
plt.ylabel('Transaction Count')
plt.xticks(rotation=45)
plt.show()

# 3. Bar plot for Location Anomalies
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='LocationAnomaly', hue='Location', palette='coolwarm')
plt.title('Location Anomalies Across ATM Locations')
plt.xlabel('Location Anomaly')
plt.ylabel('Number of Transactions')
plt.show()

# 4. Scatter plot for Account Balance vs Transaction Amount
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='AccountBalance', y='Amount', hue='BalanceCheck', palette='coolwarm', style='FraudCategory', s=100)
plt.title('Account Balance vs Transaction Amount')
plt.xlabel('Account Balance')
plt.ylabel('Transaction Amount')
plt.show()

# 5. Histogram for Time Differences (Frequency of Transactions)
plt.figure(figsize=(8, 6))
sns.histplot(df['TimeDiff'], kde=True, bins=10, color='blue')
plt.title('Distribution of Time Between Transactions')
plt.xlabel('Time Difference (seconds)')
plt.ylabel('Frequency')
plt.show()
