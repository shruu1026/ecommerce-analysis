import pandas as pd

df = pd.read_csv("olist_orders_dataset.csv")

# convert date
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# create new columns
df['year'] = df['order_purchase_timestamp'].dt.year
df['month'] = df['order_purchase_timestamp'].dt.month

# analysis
print("\nOrder Status:\n", df['order_status'].value_counts())
print("\nYearly Orders:\n", df['year'].value_counts())
print("\nMonthly Orders:\n", df['month'].value_counts().sort_index())

# delivery performance
print("\nDelivered vs Not Delivered:")
print("Delivered:", df[df['order_status']=='delivered'].shape[0])
print("Not Delivered:", df[df['order_status']!='delivered'].shape[0])

# cleaning
df_clean = df.dropna()
print("\nAfter Cleaning:", df_clean.shape)