# =====================================================
# ADVANCED PYTHON / DATA SCIENCE TASKS
# =====================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    mean_squared_error
)

from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

from statsmodels.tsa.arima.model import ARIMA

import os 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run_advanced_python_tasks():

    st.title(" Advanced Python & Data Science Tasks")

    task = st.selectbox(
        "Select Advanced Task",
        [
            "Feature engineering: profit margin drivers",
            "Clustering for product segmentation",
            "Classification models for high vs. low profit",
            "Random Forest for cost prediction",
            "PCA for dimensionality reduction",
            "Cross-validation for forecasting models",
            "Compare regression vs. ARIMA",
            "Confusion matrix for classification",
            "Predictive insights for CFO",
            "Export results to Power BI"
        ]
    )

    # ==========================================
    # LOAD DATASET
    # ==========================================

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    csv_path = os.path.join(BASE_DIR, "DatasetSureTrust.csv")

    df = pd.read_csv(csv_path, encoding="latin1")

    # ==========================================
    # DATA CLEANING
    # ==========================================

    df.dropna(inplace=True)

    # ==========================================
    # TASK 1
    # ==========================================

    if task == "Feature engineering: profit margin drivers":

        st.subheader("Profit Margin Drivers")

        df["Profit Margin"] = (
            df["Profit"] / df["Sales"]
        ) * 100

        result = df[
            ["Sales", "Profit", "Profit Margin"]
        ].head(20)

        st.dataframe(
            result,
            use_container_width=True
        )

        fig = px.scatter(
            df,
            x="Sales",
            y="Profit",
            color="Profit Margin",
            title="Profit Margin Drivers"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # TASK 2
    # ==========================================

    elif task == "Clustering for product segmentation":

        st.subheader("K-Means Product Segmentation")

        cluster_df = df[
            ["Sales", "Profit"]
        ]

        model = KMeans(
            n_clusters=3,
            random_state=42
        )

        df["Cluster"] = model.fit_predict(cluster_df)

        fig = px.scatter(
            df,
            x="Sales",
            y="Profit",
            color="Cluster",
            title="Product Segmentation"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # TASK 3
    # ==========================================

    elif task == "Classification models for high vs. low profit":

        st.subheader("Profit Classification")

        df["Profit_Class"] = np.where(
            df["Profit"] > df["Profit"].median(),
            1,
            0
        )

        X = df[["Sales", "Quantity"]]
        y = df["Profit_Class"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        clf = DecisionTreeClassifier()

        clf.fit(X_train, y_train)

        predictions = clf.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        st.write(
            "Classification Accuracy:",
            round(accuracy, 2)
        )

    # ==========================================
    # TASK 4
    # ==========================================

    elif task == "Random Forest for cost prediction":

        st.subheader("Random Forest Cost Prediction")

        X = df[["Sales", "Quantity"]]
        y = df["Profit"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        rf = RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )

        rf.fit(X_train, y_train)

        predictions = rf.predict(X_test)

        result_df = pd.DataFrame({
            "Actual Profit": y_test.values,
            "Predicted Profit": predictions
        })

        st.dataframe(
            result_df.head(20),
            use_container_width=True
        )

    # ==========================================
    # TASK 5
    # ==========================================

    elif task == "PCA for dimensionality reduction":

        st.subheader("PCA Visualization")

        pca_df = df[
            ["Sales", "Profit", "Quantity"]
        ]

        pca = PCA(n_components=2)

        components = pca.fit_transform(pca_df)

        pca_result = pd.DataFrame(
            components,
            columns=["PC1", "PC2"]
        )

        fig = px.scatter(
            pca_result,
            x="PC1",
            y="PC2",
            title="PCA Dimensionality Reduction"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # TASK 6
    # ==========================================

    elif task == "Cross-validation for forecasting models":

        st.subheader("Cross Validation")

        X = df[["Sales", "Quantity"]]
        y = df["Profit"]

        model = LinearRegression()

        scores = cross_val_score(
            model,
            X,
            y,
            cv=5
        )

        st.write(
            "Cross Validation Scores:",
            scores
        )

        st.write(
            "Average Score:",
            scores.mean()
        )

    # ==========================================
    # TASK 7
    # ==========================================

    elif task == "Compare regression vs. ARIMA":

        st.subheader("Regression vs ARIMA")

        # Linear Regression
        X = df[["Sales"]]
        y = df["Profit"]

        reg = LinearRegression()

        reg.fit(X, y)

        reg_pred = reg.predict(X)

        reg_mse = mean_squared_error(
            y,
            reg_pred
        )

        # ARIMA
        sales_series = df["Sales"]

        arima_model = ARIMA(
            sales_series,
            order=(2, 1, 2)
        )

        arima_fit = arima_model.fit()

        forecast = arima_fit.forecast(steps=10)

        st.write(
            "Regression MSE:",
            reg_mse
        )

        st.write("ARIMA Forecast")

        st.dataframe(
            forecast.to_frame(),
            use_container_width=True
        )

    # ==========================================
    # TASK 8
    # ==========================================

    elif task == "Confusion matrix for classification":

        st.subheader("Confusion Matrix")

        df["Profit_Class"] = np.where(
            df["Profit"] > df["Profit"].median(),
            1,
            0
        )

        X = df[["Sales", "Quantity"]]
        y = df["Profit_Class"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        clf = DecisionTreeClassifier()

        clf.fit(X_train, y_train)

        pred = clf.predict(X_test)

        cm = confusion_matrix(
            y_test,
            pred
        )

        fig, ax = plt.subplots()

        sns.heatmap(
            cm,
            annot=True,
            fmt="d",
            cmap="Blues",
            ax=ax
        )

        st.pyplot(fig)

    # ==========================================
    # TASK 9
    # ==========================================

    elif task == "Predictive insights for CFO":

        st.subheader("Predictive Insights")

        total_sales = df["Sales"].sum()
        total_profit = df["Profit"].sum()

        avg_profit = df["Profit"].mean()

        st.metric(
            "Total Sales",
            round(total_sales, 2)
        )

        st.metric(
            "Total Profit",
            round(total_profit, 2)
        )

        st.metric(
            "Average Profit",
            round(avg_profit, 2)
        )

    # ==========================================
    # TASK 10
    # ==========================================

    elif task == "Export results to Power BI":

        st.subheader("Export Data")

        export_df = df.head(100)

        export_df.to_csv(
            "PowerBI_Advanced_Export.csv",
            index=False
        )

        st.success(
            "CSV Exported Successfully"
        )

        st.dataframe(
            export_df,
            use_container_width=True
        )