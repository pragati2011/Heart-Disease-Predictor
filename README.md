# ❤️ Heart Disease Prediction Using Machine Learning

## 📌 Project Overview

This project predicts the likelihood of heart disease using Machine Learning algorithms. The workflow covers the complete data science pipeline, including data cleaning, exploratory data analysis (EDA), preprocessing, model building, evaluation, and deployment through a Streamlit web application.

The goal is to assist users in assessing potential heart disease risk based on various medical attributes.

---

## 🎯 Objectives

* Analyze heart disease data to identify important patterns and trends.
* Clean and preprocess raw healthcare data.
* Train and compare multiple machine learning models.
* Select the best-performing model for prediction.
* Deploy the model using an interactive Streamlit web application.

---

## 📊 Exploratory Data Analysis (EDA)

The following analyses were performed:

* Dataset overview and structure analysis
* Missing value detection
* Duplicate record identification
* Statistical summary of features
* Distribution analysis using histograms
* Correlation heatmap
* Class distribution visualization
* Feature relationship analysis
* Outlier detection using boxplots

---

## 🧹 Data Cleaning

Data cleaning steps included:

* Handling missing values
* Removing duplicate records
* Checking inconsistent values
* Verifying data types
* Outlier inspection

---

## ⚙️ Data Preprocessing

The following preprocessing techniques were applied:

### Feature Encoding

Categorical features were converted into numerical format using One-Hot Encoding.

### Feature Scaling

Numerical features were standardized using StandardScaler to improve model performance.

### Feature Selection

Relevant features were retained for model training and prediction.

---

## 🤖 Machine Learning Models Used

### 1. Logistic Regression

A statistical classification algorithm used as a baseline model.

### 2. Decision Tree Classifier

A tree-based model that learns decision rules from the data.

### 3. Support Vector Machine (SVM)

A powerful classification algorithm that finds the optimal separating hyperplane.

### 4. K-Nearest Neighbors (KNN)

A distance-based algorithm that classifies samples based on neighboring data points.

---

## 📈 Model Evaluation

The models were evaluated using:

* Accuracy Score
* Precision
* Recall
* F1-Score
* Confusion Matrix

Model performances were compared to identify the most suitable algorithm for heart disease prediction.

---

## 🚀 Streamlit Web Application

An interactive web application was developed using Streamlit where users can:

* Enter patient health information
* Receive instant predictions
* View heart disease risk assessment
* Interact with a user-friendly interface

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit

---

## 📂 Project Structure

```text
Heart-Disease-Prediction/
│
├── heart_disease_prediction.ipynb
├── app.py
├── knn_heart_model.pkl
├── heart_scaler.pkl
├── heart_columns.pkl
├── requirements.txt
├── README.md
└── heart.csv
```

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/yourusername/Heart-Disease-Prediction.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

---

## 📋 Input Features

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate
* Exercise-Induced Angina
* Oldpeak
* ST Slope

---

## 🎯 Results

Multiple machine learning models were trained and evaluated. After comparing performance metrics, the best-performing model was selected and integrated into the Streamlit application for real-time predictions.

---

## 👩‍💻 Internship Project

This project was developed as part of the Python Programming / Machine Learning Internship Program.

---

## 📬 Connect With Me

If you found this project useful, feel free to star the repository and connect with me on LinkedIn.

⭐ Don't forget to star this repository if you like it!
