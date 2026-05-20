import streamlit as st
import pandas as pd
import plotly.express as px
import os

# =====================================================
# BASE PATHS
# =====================================================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

EXCEL_FILE = os.path.join(
    BASE_DIR,
    "FinalExcelSureTrust.xlsx"
)

ASSETS_DIR = os.path.join(
    BASE_DIR,
    "Assets"
)

# =====================================================
# SAFE READ EXCEL
# =====================================================

def safe_read_excel(*args, **kwargs):

    try:

        return pd.read_excel(
            EXCEL_FILE,
            *args,
            **kwargs
        )

    except FileNotFoundError:

        st.error(
            "Excel file not found: FinalExcelSureTrust.xlsx"
        )

        st.stop()

    except Exception as e:

        st.error(
            f"Excel loading error: {e}"
        )

        st.stop()

# =====================================================
# MAIN FUNCTION
# =====================================================

def run_excel_tasks(df):

    excel_task = st.selectbox(
        "Select Excel Task",
        [
            "Build P&L, Balance Sheet, Cash Flow models",
            "Pivot Revenue by Product",
            "INDEX MATCH Lookup",
            "Waterfall Profit Breakdown",
            "Forecast Sales",
            "Scenario Analysis",
            "Automate quarterly reports with macros",
            "KPI Dashboard",
            "Link Excel outputs to SQL queries.",
            "Export data for Python analysis"
        ]
    )

    # =====================================================
    # QUESTION 1
    # =====================================================

    if excel_task == "Build P&L, Balance Sheet, Cash Flow models":

        st.subheader("Question-1 Data")

        # =================================================
        # P&L
        # =================================================

        st.markdown(
            '<div class="q3-label">Build Profit & Loss Statement</div>',
            unsafe_allow_html=True
        )

        q1_df = safe_read_excel(
            sheet_name="Dataset & All Question",
            usecols="P:Q",
            skiprows=6,
            nrows=3,
            header=None
        )

        q1_df.columns = [
            "Particulars",
            "Amount"
        ]

        left, center, right = st.columns([1, 2, 1])

        with center:

            st.dataframe(
                q1_df,
                width=1500,
                hide_index=True
            )

        # =================================================
        # BALANCE SHEET
        # =================================================

        st.markdown(
            '<div class="q3-label">Balance Sheet</div>',
            unsafe_allow_html=True
        )

        q1_df = safe_read_excel(
            sheet_name="Dataset & All Question",
            usecols="P:Q",
            skiprows=11,
            nrows=3,
            header=None
        )

        q1_df.columns = [
            "Particulars",
            "Amount"
        ]

        left, center, right = st.columns([1, 2, 1])

        with center:

            st.dataframe(
                q1_df,
                width=1500,
                hide_index=True
            )

        # =================================================
        # CASH FLOW
        # =================================================

        st.markdown(
            '<div class="q3-label">Cash Flow Statement</div>',
            unsafe_allow_html=True
        )

        q1_df = safe_read_excel(
            sheet_name="Dataset & All Question",
            usecols="P:Q",
            skiprows=16,
            nrows=3,
            header=None
        )

        q1_df.columns = [
            "Particulars",
            "Amount"
        ]

        left, center, right = st.columns([1, 2, 1])

        with center:

            st.dataframe(
                q1_df,
                width=1500,
                hide_index=True
            )

    # =====================================================
    # QUESTION 2
    # =====================================================

    elif excel_task == "Pivot Revenue by Product":

        st.subheader("Question-2 Pivot Report")

        q2_df = safe_read_excel(
            sheet_name="Question-2",
            skiprows=3
        )

        q2_df.columns = [
            "Quarter",
            "Sum of Sales",
            "Sum of Profit"
        ]

        st.dataframe(
            q2_df,
            use_container_width=True
        )

        fig = px.bar(
            q2_df,
            x="Quarter",
            y=["Sum of Sales", "Sum of Profit"],
            barmode="group",
            title="Quarter-wise Sales & Profit"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # =====================================================
    # QUESTION 3
    # =====================================================

    elif excel_task == "INDEX MATCH Lookup":

        st.markdown(
            '<div class="q3-container">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="q3-title">3. INDEX-MATCH (Dynamic Lookup)</div>',
            unsafe_allow_html=True
        )

        product_df = safe_read_excel(
            sheet_name="Dataset & All Question",
            usecols="C",
            skiprows=4,
            header=None
        )

        product_list = product_df.iloc[:, 0].dropna().tolist()

        data_df = safe_read_excel(
            sheet_name="Dataset & All Question",
            usecols="C,H,I,J",
            skiprows=4,
            header=None
        )

        data_df.columns = [
            "Product Name",
            "Cost",
            "Sales",
            "Profit"
        ]

        col1, col2, col3, col4 = st.columns([6, 1.5, 1.5, 1.5])

        with col1:

            st.markdown(
                '<div class="q3-label">Product Name From Dropdown List</div>',
                unsafe_allow_html=True
            )

            selected_product = st.selectbox(
                "",
                product_list,
                label_visibility="collapsed"
            )

        matched_row = data_df[
            data_df["Product Name"] == selected_product
        ]

        cost = matched_row.iloc[0]["Cost"]
        sales = matched_row.iloc[0]["Sales"]
        profit = matched_row.iloc[0]["Profit"]

        with col2:

            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Cost</div>
                <div class="metric-value">{cost}</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:

            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Sales</div>
                <div class="metric-value">{sales}</div>
            </div>
            """, unsafe_allow_html=True)

        with col4:

            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Profit</div>
                <div class="metric-value">{profit}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

    # =====================================================
    # QUESTION 4
    # =====================================================

    elif excel_task == "Waterfall Profit Breakdown":

        st.subheader("Question-4 Waterfall Chart")

        st.markdown(
            '<div class="q3-label">Waterfall Chart (Profit Flow)</div>',
            unsafe_allow_html=True
        )

        q4_df = safe_read_excel(
            sheet_name="Dataset & All Question",
            usecols="P:Q",
            skiprows=41,
            nrows=3,
            header=None
        )

        q4_df.columns = [
            "Category",
            "Amount"
        ]

        left, right = st.columns([1, 2])

        with left:

            st.dataframe(
                q4_df,
                width=400,
                hide_index=True
            )

        colors = [
            "#00E5FF",
            "#FF4B4B",
            "#00FF9C"
        ]

        fig = px.bar(
            q4_df,
            x="Category",
            y="Amount",
            text="Amount",
            color="Category",
            color_discrete_sequence=colors,
            title="Profit Flow Analysis"
        )

        fig.update_layout(
            plot_bgcolor="#071426",
            paper_bgcolor="#071426",
            font_color="white",
            title_font_size=26,
            title_x=0.25,
            xaxis_title="",
            yaxis_title="Amount",
            showlegend=False,
            height=550
        )

        fig.update_traces(
            texttemplate='%{text:.0f}',
            textposition='outside',
            marker_line_color="white",
            marker_line_width=2
        )

        fig.update_yaxes(
            showgrid=True,
            gridcolor="rgba(255,255,255,0.1)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # =====================================================
    # QUESTION 5
    # =====================================================

    elif excel_task == "Forecast Sales":

        st.subheader(
            "Forecast Sales using Exponential Smoothing"
        )

        forecast_df = safe_read_excel(
            sheet_name="Question-5"
        )

        forecast_df = forecast_df.loc[
            :,
            ~forecast_df.columns.str.contains("^Unnamed")
        ]

        forecast_df["Order Date"] = pd.to_datetime(
            forecast_df["Order Date"]
        ).dt.strftime("%d-%m-%Y")

        st.dataframe(
            forecast_df,
            height=400,
            use_container_width=True
        )

        st.subheader("Exact Excel Forecast Chart")

        image_path = os.path.join(
            ASSETS_DIR,
            "forecast_chart.png"
        )

        if os.path.exists(image_path):

            st.image(
                image_path,
                use_container_width=True
            )

        else:

            st.warning(
                "Forecast chart image not found."
            )