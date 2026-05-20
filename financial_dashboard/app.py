# =========================================================
# app.py
# =========================================================

import streamlit as st
import pandas as pd
import os

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Enterprise Financial Analytics",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# LOAD CSS
# =========================================================

def load_css(file_name):

    try:

        css_path = os.path.join(
            os.path.dirname(__file__),
            file_name
        )

        with open(css_path, encoding="utf-8") as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

    except FileNotFoundError:

        st.warning(
            f"CSS file not found: {file_name}"
        )

# LOAD CSS FILE

load_css("style.css")

# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():

    try:

        # EXCEL FILE PATH

        excel_path = os.path.join(
            os.path.dirname(__file__),
            "FinalExcelSureTrust.xlsx"
        )

        # READ EXCEL FILE

        df = pd.read_excel(
            excel_path,
            sheet_name="Dataset & All Question",
            header=3
        )

        # REMOVE UNNAMED COLUMNS

        df = df.loc[
            :,
            ~df.columns.str.contains("^Unnamed")
        ]

        # CLEAN COLUMN NAMES

        df.columns = df.columns.str.strip()

        # REQUIRED COLUMNS

        required_columns = [

            "Order Date",
            "Product Name",
            "Category",
            "Region",
            "Unit_cost",
            "Quantity",
            "Sales",
            "Profit"

        ]

        # CHECK MISSING COLUMNS

        missing_columns = [

            col for col in required_columns
            if col not in df.columns

        ]

        if missing_columns:

            st.error(
                f"Missing columns in dataset: {missing_columns}"
            )

            st.stop()

        # KEEP REQUIRED COLUMNS

        df = df[required_columns]

        # REMOVE NULL VALUES

        df = df.dropna()

        # DATE FORMAT

        df["Order Date"] = pd.to_datetime(
            df["Order Date"]
        ).dt.strftime("%d-%m-%Y")

        return df

    except FileNotFoundError:

        st.error(
            "Excel file not found: FinalExcelSureTrust.xlsx"
        )

        st.stop()

    except Exception as e:

        st.error(
            f"Error loading dataset: {e}"
        )

        st.stop()

# LOAD DATAFRAME

df = load_data()

# =========================================================
# MAIN TITLE
# =========================================================

st.markdown(
    """
    <div class="main-title">
        Corporate Financial Performance Dashboard
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="sub-title">
        Real-Time Sales • Profit Analysis • Business Insights • Forecasting
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# DATASET INFORMATION
# =========================================================

st.markdown(
    """
    <div class="section-title">
        📂 Dataset Information
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """

## Description
            
- ##### Superstore Dataset Final is a retail business dataset used for financial analytics, sales forecasting, and business intelligence projects.

- ##### It contains transactional records of products sold across different regions, including order date, product name, region, unit cost, quantity, sales, profit, category, and customer-related insights.

- ##### The dataset is highly useful for projects involving Excel, SQL, Python, Data Science, Machine Learning, and Power BI.

## Gathering Details

- ##### **Dataset Source:** Kaggle

- ##### **Dataset Name:** Superstore Dataset Final

- ##### **Format:** CSV / Excel

- ##### **Project Type:** Corporate Financial Analytics

"""
)

# =========================================================
# DATASET PREVIEW
# =========================================================

st.markdown(
    """
    <div class="section-title">
        📊 Dataset Preview
    </div>
    """,
    unsafe_allow_html=True
)

st.dataframe(
    df,
    height=450,
    use_container_width=True
)

# =========================================================
# MODULE SELECTOR
# =========================================================

st.markdown(
    """
    <div class="section-title">
         Select Module
    </div>
    """,
    unsafe_allow_html=True
)

module = st.selectbox(
    "Select module",
    [

        "📊 Excel Tasks",
        "🗄 SQL Tasks",
        "🐍 Python Tasks",
        "🤖 Data Science Tasks",
        "📈 Power BI Tasks"

    ],
    label_visibility="hidden"
)

# =========================================================
# SELECTED MODULE TITLE
# =========================================================

st.markdown(
    f"""
    <div class="selected-module-box">
        <div class="selected-module-text">
            {module}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# LOAD PAGES
# =========================================================

try:

    if module == "📊 Excel Tasks":

        from pages.Excel_Tasks import run_excel_tasks

        run_excel_tasks(df)

    elif module == "🗄 SQL Tasks":

        from pages.SQL_Tasks import run_sql_tasks

        run_sql_tasks()

    elif module == "🐍 Python Tasks":

        from pages.Python_Tasks import run_python_tasks

        run_python_tasks()

    elif module == "🤖 Data Science Tasks":

        from pages.DataScience_Tasks import (
            run_advanced_python_tasks
        )

        run_advanced_python_tasks()

    elif module == "📈 Power BI Tasks":

        from pages.PowerBI_Tasks import run_powerbi_tasks

        run_powerbi_tasks()

except ModuleNotFoundError as e:

    st.error(
        f"Module import error: {e}"
    )

except Exception as e:

    st.error(
        f"Unexpected error: {e}"
    )