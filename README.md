Machine Learning System for Residential Property Valuation

Author: Priyanka MS

House Price Prediction is a rapid prototyping project aimed at estimating residential property prices using machine learning techniques. The system leverages real estate features such as property size, location, construction status, and seller type to generate accurate price predictions.

This repository contains the complete end-to-end workflow, including data preprocessing, exploratory analysis, model training, evaluation, and deployment through a web-based application.

📦 Project Components

This repository includes:

Dataset preprocessing and feature selection

Exploratory Data Analysis (EDA) and visualization

Machine Learning models (Linear Regression, Random Forest, XGBoost)

Model evaluation and selection using R² score

Serialized trained model

Streamlit-based web application for real-time predictions

🧠 Model Summary

Final Model: Random Forest Regressor

Evaluation Metric: R² Score

Best Performance: ~0.71

Random Forest was selected after comparing multiple models based on predictive performance on unseen data.

🚀 Web Application

A lightweight Streamlit web app allows users to:

Enter property details

Get instant house price predictions

Interact with a clean and user-friendly interface

🔮 Future Enhancements

Hyperparameter tuning using GridSearchCV

Integration of map-based visualizations

Cloud deployment (HuggingFace / Render)

Inclusion of additional real estate features

