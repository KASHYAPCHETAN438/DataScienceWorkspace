import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run_python_tasks():

    st.title("🐍 Python Tasks")

    python_task = st.selectbox(
        "Select Python Task",
        [
            "Import SQL financial data into Pandas",
            "Clean and preprocess revenue data",
            "EDA on profitability trends",
            "Regression models for revenue forecasting",
            "ARIMA for time-series forecasting",
            "Visualize profit margins with seaborn",
            "Automate quarterly reporting",
            "ML model for cost prediction",
            "Export results to CSV for Power BI",
            "Link Python outputs to Data Science"
        ]
    )

    # ==========================================
    # LOAD DATASET
    # ==========================================

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    csv_path = os.path.join(BASE_DIR, "DatasetSureTrust.csv")

    df = pd.read_csv(csv_path, encoding="latin1")






    # ==========================================
    # TASK 1
    # ==========================================

    if python_task == "Import SQL financial data into Pandas":

        st.subheader("SQL Financial Data Imported into Pandas")

        st.dataframe(
            df.head(20),
            use_container_width=True
        )

        st.success("Dataset Successfully Imported")

    # ==========================================
    # TASK 2
    # ==========================================

    elif python_task == "Clean and preprocess revenue data":

        st.subheader("Revenue Data Cleaning")

        clean_df = df.copy()

        clean_df.dropna(inplace=True)

        clean_df.columns = clean_df.columns.str.strip()

        st.write("Shape After Cleaning:", clean_df.shape)

        st.dataframe(
            clean_df.head(20),
            use_container_width=True
        )

    # ==========================================
    # TASK 3
    # ==========================================

    elif python_task == "EDA on profitability trends":

        st.subheader("Profitability Trend Analysis")

        profit_region = df.groupby("Region")["Profit"].sum().reset_index()

        fig = px.bar(
            profit_region,
            x="Region",
            y="Profit",
            color="Region",
            title="Region-wise Profit Analysis"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # TASK 4
    # ==========================================

    elif python_task == "Regression models for revenue forecasting":

        st.subheader("Revenue Forecasting using Regression")

        regression_df = df[["Sales", "Profit"]].dropna()

        X = regression_df[["Sales"]]
        y = regression_df["Profit"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=0.2,
            random_state=42
        )

        model = LinearRegression()

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        mse = mean_squared_error(y_test, predictions)

        st.write("Mean Squared Error:", mse)

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

    elif python_task == "ARIMA for time-series forecasting":

        st.subheader("ARIMA Time-Series Forecasting")

        sales_series = df["Sales"].dropna()

        model = ARIMA(
            sales_series,
            order=(2, 1, 2)
        )

        model_fit = model.fit()

        forecast = model_fit.forecast(steps=10)

        forecast_df = pd.DataFrame({
            "Forecasted Sales": forecast
        })

        st.dataframe(
            forecast_df,
            use_container_width=True
        )

        fig = px.line(
            forecast_df,
            y="Forecasted Sales",
            title="Future Sales Forecast"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # TASK 6
    # ==========================================

    elif python_task == "Visualize profit margins with seaborn":

        st.subheader("Profit Margin Visualization")

        fig, ax = plt.subplots(figsize=(10, 5))

        sns.histplot(
            df["Profit"],
            kde=True,
            ax=ax
        )

        st.pyplot(fig)

    # ==========================================
    # TASK 7
    # ==========================================

    elif python_task == "Automate quarterly reporting":

        st.subheader("Quarterly Reporting")

        quarterly_report = df.groupby("Region")[["Sales", "Profit"]].sum()

        st.dataframe(
            quarterly_report,
            use_container_width=True
        )

        st.success("Quarterly Report Generated Successfully")

    # ==========================================
    # TASK 8
    # ==========================================

    elif python_task == "ML model for cost prediction":

        st.subheader("Cost Prediction ML Model")

        ml_df = df[["Sales", "Profit", "Quantity"]].dropna()

        X = ml_df[["Sales", "Quantity"]]
        y = ml_df["Profit"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=0.2,
            random_state=42
        )

        model = LinearRegression()

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        result_df = pd.DataFrame({
            "Actual Profit": y_test.values,
            "Predicted Profit": predictions
        })

        st.dataframe(
            result_df.head(20),
            use_container_width=True
        )

    # ==========================================
    # TASK 9
    # ==========================================

    elif python_task == "Export results to CSV for Power BI":

        st.subheader("Export CSV File")

        export_df = df.head(100)

        export_df.to_csv(
            "PowerBI_Export.csv",
            index=False
        )

        st.success("CSV Exported Successfully")

        st.dataframe(
            export_df,
            use_container_width=True
        )

    # ==========================================
    # TASK 10
    # ==========================================

    elif python_task == "Link Python outputs to Data Science":

        st.subheader("Python + Data Science Integration")

        summary_df = df.describe()

        st.dataframe(
            summary_df,
            use_container_width=True
        )

        corr = df.corr(numeric_only=True)

        fig = px.imshow(
            corr,
            text_auto=True,
            title="Correlation Matrix"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )