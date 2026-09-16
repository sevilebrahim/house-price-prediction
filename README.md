# House Price Prediction 🏠

What if a few details about a house could give us an idea of its price?

That is what I explored in this project.

The program works with a housing dataset and uses information such as the size of the property, number of rooms, building age, floor, parking, and elevator availability to predict the current price of a house.

I used Linear Regression to learn the relationship between these features and the target price. Before training, the data is checked and missing values in the input features are replaced with the average value of their columns.

After that, the dataset is divided into training and testing parts. The model learns from the training data and then predicts prices for the test data. The actual prices and the predicted prices are displayed together so the results can be compared.

I also added a visualization of the house price distribution to get a quick look at how the prices are spread across the dataset.

## Features

The model uses:

* Area
* Number of Rooms
* Building Age
* Floor
* Parking
* Elevator

The target value is the current house price.

## Project Flow

```text
Housing Data
     ↓
Explore the Dataset
     ↓
Handle Missing Values
     ↓
Select Features
     ↓
Split the Data
     ↓
Train Linear Regression
     ↓
Predict House Prices
     ↓
Compare Actual and Predicted Values
     ↓
Visualize Price Distribution
```

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn
* Excel

## Running the Project

Install the required libraries:

```bash
pip install pandas scikit-learn matplotlib seaborn openpyxl
```

Then run:

```bash
python house_price_prediction.py
```

Make sure the Excel dataset is available and the file path in the Python code points to the correct location.

## What I Learned

This project helped me practice the complete basic workflow of a regression problem: loading a dataset, exploring it, handling missing data, selecting features, training a model, making predictions, and visualizing the results.

It also showed me how machine learning can be used for a practical problem where the output is a numerical value rather than a category.

## Future Ideas

This project could be developed further by adding more property features, evaluating the model with R² and MSE, and creating a simple interface where users can enter house details and get a predicted price.
