import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


df = pd.read_excel("Tab.xlsx")

print(df.head())
print(df.describe())
print(df)


X = df[
    [
        "Area_m2",
        "Rooms",
        "Age_years",
        "Floor",
        "Parking",
        "Elevator"
    ]
]

y = df["Current_Price_Billion_Toman"]

X = X.fillna(X.mean())


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(predictions)


result = pd.DataFrame({
    "Real": y_test.values,
    "Predicted": predictions
})

print(result)


plt.figure(figsize=(8, 5))

sns.histplot(
    df["Current_Price_Billion_Toman"],
    bins=10
)

plt.title("Distribution of House Prices")
plt.xlabel("House Price (Billion Toman)")
plt.ylabel("Count")

plt.show()

