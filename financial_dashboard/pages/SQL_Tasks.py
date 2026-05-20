# =====================================================
# SQL TASKS PAGE (MYSQL BASED)
# =====================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector


def run_sql_tasks():

    st.title("🛢️ SQL Tasks Dashboard")

    sql_task = st.selectbox(
        "Select SQL Task",
        [
            "Create tables for sales, costs, profits",
            "Query quarterly revenue growth",
            "JOIN product and region tables",
            "GROUP BY profitability by segment",
            "Stored procedures for financial KPIs",
            "Window functions for YoY growth",
            "Query top 5 profitable products",
            "Trigger alerts for cost overruns",
            "Export SQL results to Excel",
            "Link SQL outputs to Python"
        ]
    )

    # ==========================================
    # MYSQL CONNECTION
    # ==========================================

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="231632043006",
        database="financial_db"
    )

    # ==========================================
    # QUESTION 1
    # ==========================================

    if sql_task == "Create tables for sales, costs, profits":

        st.subheader("Question-1 Create Table")

        query = """
        DESCRIBE datasetsuretrust
        """

        result = pd.read_sql(
            query,
            conn
        )

        st.dataframe(
            result,
            use_container_width=True
        )

        st.success("datasetsuretrust Table Loaded Successfully")

    # ==========================================
    # QUESTION 2
    # ==========================================

    elif sql_task == "Query quarterly revenue growth":

        st.subheader("Question-2 Quarterly Revenue Growth")

        query = """
        SELECT
            YEAR(`Order Date`) AS year,
            QUARTER(`Order Date`) AS quarter,
            SUM(Sales) AS revenue
        FROM datasetsuretrust
        GROUP BY year, quarter
        ORDER BY year, quarter
        """

        result = pd.read_sql(
            query,
            conn
        )

        st.dataframe(
            result,
            use_container_width=True
        )

        fig = px.line(
            result,
            x="quarter",
            y="revenue",
            color="year",
            markers=True,
            title="Quarterly Revenue Growth"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # QUESTION 3
    # ==========================================

    elif sql_task == "JOIN product and region tables":

        st.subheader("Question-3 JOIN Product & Region")

        query = """
        SELECT
            d.`Product Name`,
            d.Category,
            d.Region,
            d.Sales
        FROM datasetsuretrust d
        JOIN datasetsuretrust r
        ON d.Region = r.Region
        LIMIT 50
        """

        result = pd.read_sql(
            query,
            conn
        )

        st.dataframe(
            result,
            use_container_width=True
        )

    # ==========================================
    # QUESTION 4
    # ==========================================

    elif sql_task == "GROUP BY profitability by segment":

        st.subheader("Question-4 Profitability by Segment")

        query = """
        SELECT
            Category,
            Region,
            SUM(Sales) AS total_sales,
            SUM(Profit) AS total_profit
        FROM datasetsuretrust
        GROUP BY Category, Region
        ORDER BY total_profit DESC
        """

        result = pd.read_sql(
            query,
            conn
        )

        st.dataframe(
            result,
            use_container_width=True
        )

        fig = px.bar(
            result,
            x="Category",
            y="total_profit",
            color="Region",
            title="Profitability by Segment"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # QUESTION 5
    # ==========================================

    elif sql_task == "Stored procedures for financial KPIs":

        st.subheader("Question-5 Financial KPI")

        query = """
        CALL Financial_KPI()
        """

        result = pd.read_sql(
            query,
            conn
        )

        st.dataframe(
            result,
            use_container_width=True
        )

        st.metric(
            "Total Revenue",
            round(result.iloc[0]["Total_Revenue"], 2)
        )

        st.metric(
            "Total Profit",
            round(result.iloc[0]["Total_Profit"], 2)
        )

    # ==========================================
    # QUESTION 6
    # ==========================================

    elif sql_task == "Window functions for YoY growth":

        st.subheader("Question-6 YoY Growth")

        query = """
        SELECT
            year,
            revenue,
            LAG(revenue) OVER (ORDER BY year) AS previous_year,

            (
                (revenue - LAG(revenue) OVER (ORDER BY year))
                / LAG(revenue) OVER (ORDER BY year)
            ) * 100 AS growth_percent

        FROM (
            SELECT
                YEAR(`Order Date`) AS year,
                SUM(Sales) AS revenue
            FROM datasetsuretrust
            GROUP BY year
        ) t
        """

        result = pd.read_sql(
            query,
            conn
        )

        st.dataframe(
            result,
            use_container_width=True
        )

        fig = px.line(
            result,
            x="year",
            y="growth_percent",
            markers=True,
            title="Year over Year Growth"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # QUESTION 7
    # ==========================================

    elif sql_task == "Query top 5 profitable products":

        st.subheader("Question-7 Top 5 Profitable Products")

        query = """
        SELECT
            `Product Name`,
            SUM(Profit) AS total_profit
        FROM datasetsuretrust
        GROUP BY `Product Name`
        ORDER BY total_profit DESC
        LIMIT 5
        """

        result = pd.read_sql(
            query,
            conn
        )

        st.dataframe(
            result,
            use_container_width=True
        )

        fig = px.bar(
            result,
            x="Product Name",
            y="total_profit",
            color="total_profit",
            title="Top 5 Profitable Products"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # QUESTION 8
    # ==========================================

    elif sql_task == "Trigger alerts for cost overruns":

        st.subheader("Question-8 Cost Overrun Alert")

        query = """
        SELECT
            `Product Name`,
            Cost,
            Profit
        FROM datasetsuretrust
        WHERE Cost > 5000
        """

        result = pd.read_sql(
            query,
            conn
        )

        st.dataframe(
            result,
            use_container_width=True
        )

        st.error("⚠️ Cost exceeds allowed limit")

    # ==========================================
    # QUESTION 9
    # ==========================================

    elif sql_task == "Export SQL results to Excel":

        st.subheader("Question-9 Export SQL Results")

        query = """
        SELECT *
        FROM datasetsuretrust
        LIMIT 100
        """

        result = pd.read_sql(
            query,
            conn
        )

        result.to_excel(
            "SQL_Export.xlsx",
            index=False
        )

        st.success("SQL Results Exported Successfully")

        st.dataframe(
            result,
            use_container_width=True
        )

    # ==========================================
    # QUESTION 10
    # ==========================================

    elif sql_task == "Link SQL outputs to Python":

        st.subheader("Question-10 SQL + Python Integration")

        query = """
        SELECT
            Region,
            SUM(Sales) AS Revenue,
            SUM(Profit) AS Profit
        FROM datasetsuretrust
        GROUP BY Region
        """

        result = pd.read_sql(
            query,
            conn
        )

        st.dataframe(
            result,
            use_container_width=True
        )

        fig = px.scatter(
            result,
            x="Revenue",
            y="Profit",
            color="Region",
            size="Profit",
            title="SQL Output Linked to Python"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # CLOSE CONNECTION
    # ==========================================

    conn.close()