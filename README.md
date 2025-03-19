# Car Price Prediction Project

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Analysis & Model Training](#data-analysis--model-training)
- [API Usage](#api-usage)
- [Data Exploration Insights](#data-exploration-insights)
- [Model Performance](#model-performance)
- [API Documentation](#api-documentation)
- [Future Improvements](#future-improvements)
- [Software and Tools Required](#software-and-tools-required)
- [Git Configuration](#git-configuration)
- [Commit and Push Changes](#commit-and-push-changes)

---

## Overview

This project provides an end-to-end machine learning solution for predicting car prices based on various features such as brand, model, year, engine size, mileage, and more. The solution includes data exploration, preprocessing, model training, evaluation, and a REST API for serving predictions.

### Key Features:
- Predict car prices using a **Random Forest Regressor**.
- Comprehensive **exploratory data analysis**.
- Handling of **categorical features** and **feature engineering**.
- Model tuning and evaluation for optimal performance.

---

## Project Structure

- `app.py`: Main Python application for running the API.
- `car_price_prediction_usage.ipynb`: Jupyter Notebook demonstrating model usage.
- `README.md`: Project documentation.
- `requirements.txt`: List of project dependencies.
- `scaling.pkl`: Pre-trained scaler for data preprocessing.
- `templates/home.html`: HTML template for the web interface.

---

## Installation

### Prerequisites:
1. Install [Python 3.7+](https://www.python.org/downloads/).
2. Install [Git CLI](https://git-scm.com/downloads).
3. Install [VS Code](https://code.visualstudio.com/).

### Steps:
1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd car_price_pred
    ```
2. Create a virtual environment:
    ```bash
    conda create -p venv python==3.7 -y
    conda activate venv/
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

1. Run the application:
    ```bash
    python app.py
    ```
2. Open your browser and navigate to `http://127.0.0.1:5000`.

---

## Data Analysis & Model Training

The project uses the following features for car price prediction:
- Brand
- Model
- Year of manufacture
- Engine size
- Fuel type
- Transmission type
- Mileage
- Number of doors
- Number of previous owners

### Steps:
1. Perform **exploratory data analysis** to understand the dataset.
2. Preprocess the data:
    - Handle missing values.
    - Encode categorical features.
    - Scale numerical features.
3. Train the model using **Random Forest Regressor**.
4. Evaluate the model using metrics like **R² score** and **Mean Absolute Error (MAE)**.

---

## API Usage

The project includes a REST API for serving predictions. Use the following endpoint:

- **POST /predict**: Submit car details in JSON format to get the predicted price.

Example request:
```json
{
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2015,
  "engine_size": 1.8,
  "fuel_type": "Petrol",
  "transmission": "Automatic",
  "mileage": 50000,
  "doors": 4,
  "previous_owners": 1
}
```

---

## Data Exploration Insights

- **Correlation Analysis**: Identified key features influencing car prices.
- **Outlier Detection**: Removed anomalies to improve model performance.
- **Feature Importance**: Determined the most impactful features using the trained model.

---

## Model Performance

- **R² Score**: 0.92
- **Mean Absolute Error (MAE)**: $1,200
- **Cross-Validation**: Ensured model generalization across different data splits.

---

## API Documentation

Refer to the `app.py` file for detailed API documentation and usage examples.

---

## Future Improvements s

- Add support for additional car features like **color** and **region**.
- Implement a **mobile-friendly UI** for the web application.
- Explore **deep learning models** for improved accuracy.
- Deploy the application on **Heroku** or **AWS** for public access.
