# GreenPrint AI – Carbon Footprint Estimator

A Streamlit web application to estimate and visualize individual carbon footprints using machine learning, custom charts, and actionable reduction tips.

---

## Purpose

This project aims to help common people understand the carbon impact they are making through their daily activities. It provides personalized suggestions that can be easily adopted in their daily routine without any out-of-the-way efforts, supporting a transition towards a sustainable future.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset Creation](#dataset-creation)
- [Model Training](#model-training)
- [Model & Data Sources](#model--data-sources)
- [Conclusion](#conclusion)

---

## Features

- Estimate your annual carbon footprint from lifestyle and home activity data.
- Get personalized reduction tips based on your inputs.
- Interactive Pie chart visualization of emission sources.
- Built-in machine learning model for predictions.
- Modern UI with custom styling.

---

## Installation

1. **Clone the repository:**

    ```
    git clone https://github.com/your-username/carbon-footprint-app.git
    cd carbon-footprint-app
    ```

2. **Create and activate a Python virtual environment:**

    ```
    python -m venv env
    # Windows
    .\env\Scripts\activate
    # macOS/Linux
    source env/bin/activate
    ```

3. **Install requirements:**

    ```
    pip install -r requirements.txt
    ```

---

## Usage

1. **Run the Streamlit app:**

    ```
    streamlit run streamlit_app.py
    ```

2. **Open your browser** and go to [http://localhost:8501](http://localhost:8501) (auto-opens by default).

---

## Dataset Creation

The synthetic dataset is generated in the `Creating_Dataset.ipynb` notebook. It simulates lifestyle and household activities influencing carbon emissions, including:

- Car travel, public transport, flights per year.
- Electricity and natural gas consumption.
- Renewable energy use percentage.
- Diet type and meat consumption.
- Waste produced and recycling habits.
- Household size and house size.

The resulting data includes a calculated carbon footprint value (`carbon_footprint_kgCO2_per_year`). This dataset is saved as `synthetic_carbon_footprint.csv` and used for model training.

---

## Model Training

Model training is performed within the `Running_Model.ipynb` notebook with the following steps:

- Loading and preprocessing the synthetic dataset.
- Encoding categorical features (like diet type).
- Splitting data into training and test sets (80/20).
- Training a **Random Forest Regressor** with 200 estimators to predict carbon footprint.
- Evaluating model performance using mean absolute error and R² metrics.
- Saving the trained model as `carbon_model.pkl` and feature columns as `model_columns.pkl` for use in the app.

---

## Model & Data Sources

- The app uses the trained Random Forest model (`carbon_model.pkl`) to provide carbon footprint predictions based on user input.
- Feature columns order and names from `model_columns.pkl` maintain input consistency.
- Dataset and training notebooks document reproducibility and methodology.

## Conclusion
GreenPrint AI empowers individuals to understand the carbon impact of their daily choices and offers simple, actionable suggestions to help reduce their footprint. By making sustainability accessible without major lifestyle changes, this app encourages gradual but meaningful progress toward a greener and more sustainable future for all.











