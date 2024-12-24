import pandas as pd

df = pd.read_csv('wine-project/wines/wines.csv')

# How many wines have been given a rating of 100 points?
max_rating = len(df.loc[df['points'] == 100])
print(max_rating)

# What is the name of the most expensive wine?
most_expensive = df.loc[df['price'] == df['price'].max()]['name'].squeeze()
print(most_expensive)

# Calculate a new column where you show the ratings in a scale from 0 to 5. Floats are allowed.
rating_scale = df["rate"] = df["points"] / 20
print(rating_scale[:10])

# Create a price histogram for wins that cost less than 100
df.loc[df['price'] < 100]['price'].hist()

# Plot price horizontally against points vertically. Do you think ratings increase by price?
df.plot(x='price', y='points', figsize=(15, 3), kind='scatter')