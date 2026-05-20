# =====================================================
# POWER BI TASKS PAGE
# =====================================================

import streamlit as st
from PIL import Image


def run_powerbi_tasks():


    powerbi_task = st.selectbox(
        "Select Power BI Task",
        [
            "Dashboard: revenue, cost, profit trends",
            "Slicers for product categories",
            "YoY growth visualization",
            "Drill-through for regional analysis",
            "KPI cards for profitability",
            "Forecasting visuals for revenue",
            "Scenario-based dashboards"
            # "Publish dashboard for executives"
        ]
    )

    # ==========================================
    # QUESTION 1
    # ==========================================

    if powerbi_task == "Dashboard: revenue, cost, profit trends":

        st.subheader(" Revenue, Cost, Profit Trends")

        image = Image.open("Assests/s1.png")

        st.image(
            image,
            use_container_width=True
        )

        st.success("Revenue, Cost & Profit Dashboard Loaded Successfully")

    # ==========================================
    # QUESTION 2
    # ==========================================

    elif powerbi_task == "Slicers for product categories":

        st.subheader(" Product Category Slicers")

        image = Image.open("Assests/s2.png")

        st.image(
            image,
            use_container_width=True
        )

        st.success("Slicers Dashboard Loaded Successfully")

    # ==========================================
    # QUESTION 3
    # ==========================================

    elif powerbi_task == "YoY growth visualization":

        st.subheader(" YoY Growth Visualization")

        image = Image.open("Assests/s3.png")

        st.image(
            image,
            use_container_width=True
        )

        st.success("YoY Growth Dashboard Loaded Successfully")

    # ==========================================
    # QUESTION 4
    # ==========================================

    elif powerbi_task == "Drill-through for regional analysis":

        st.subheader(" Drill-through Regional Analysis")

        image = Image.open("Assests/s4.png")

        st.image(
            image,
            use_container_width=True
        )

        st.success("Regional Analysis Dashboard Loaded Successfully")

    # ==========================================
    # QUESTION 5
    # ==========================================

    elif powerbi_task == "KPI cards for profitability":

        st.subheader(" KPI Cards")

        image = Image.open("Assests/s5.png")

        st.image(
            image,
            use_container_width=True
        )

        st.success("KPI Dashboard Loaded Successfully")

    # ==========================================
    # QUESTION 6
    # ==========================================

    elif powerbi_task == "Forecasting visuals for revenue":

        st.subheader(" Revenue Forecasting")

        image = Image.open("Assests/s6.png")

        st.image(
            image,
            use_container_width=True
        )

        st.success("Forecasting Dashboard Loaded Successfully")

    # ==========================================
    # QUESTION 7
    # ==========================================

    elif powerbi_task == "Scenario-based dashboards":

        st.subheader(" Scenario Based Dashboard")

        image = Image.open("Assests/s7.png")

        st.image(
            image,
            use_container_width=True
        )

        st.success("Scenario Dashboard Loaded Successfully")

    # # ==========================================
    # # QUESTION 8
    # # ==========================================

    # elif powerbi_task == "Publish dashboard for executives":

    #     st.subheader("Question-8 Published Executive Dashboard")

    #     image = Image.open("Assests/s8.png")

    #     st.image(
    #         image,
    #         use_container_width=True
    #     )

        st.success("Executive Dashboard Published Successfully")