# =====================================================
# POWER BI TASKS PAGE
# =====================================================

import streamlit as st
from PIL import Image
import os 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run_powerbi_tasks():


    powerbi_task = st.selectbox(
        "Select Power BI Task",
        [
            "Publish dashboard for executives",
            "Dashboard: revenue, cost, profit trends",
            "Slicers for product categories",
            "YoY growth visualization",
            "Drill-through for regional analysis",
            "KPI cards for profitability",
            "Forecasting visuals for revenue",
            "Scenario-based dashboards"    
            
        ]
    )

    # ==========================================
    # QUESTION 1
    # ==========================================

    if powerbi_task == "Dashboard: revenue, cost, profit trends":

        st.subheader(" Revenue, Cost, Profit Trends")

        image_path = os.path.join(BASE_DIR, "Assets", "s1.png")
        image = Image.open(image_path)

        st.image(
            image,
            use_container_width=True
        )

        
    # ==========================================
    # QUESTION 2
    # ==========================================

    elif powerbi_task == "Slicers for product categories":

        st.subheader(" Product Category Slicers")

        image_path = os.path.join(BASE_DIR, "Assets", "s2.png")
        image = Image.open(image_path)

        st.image(
            image,
            use_container_width=True
        )

       
    # ==========================================
    # QUESTION 3
    # ==========================================

    elif powerbi_task == "YoY growth visualization":

        st.subheader(" YoY Growth Visualization")

        image_path = os.path.join(BASE_DIR, "Assets", "s3.png")
        image = Image.open(image_path)

        st.image(
            image,
            use_container_width=True
        )

    # ==========================================
    # QUESTION 4
    # ==========================================

    elif powerbi_task == "Drill-through for regional analysis":

        st.subheader(" Drill-through Regional Analysis")

        image_path = os.path.join(BASE_DIR, "Assets", "s4.png")
        image = Image.open(image_path)

        st.image(
            image,
            use_container_width=True
        )


    # ==========================================
    # QUESTION 5
    # ==========================================

    elif powerbi_task == "KPI cards for profitability":

        st.subheader(" KPI Cards")

        image_path = os.path.join(BASE_DIR, "Assets", "s5.png")
        image = Image.open(image_path)

        st.image(
            image,
            use_container_width=True
        )

       

    # ==========================================
    # QUESTION 6
    # ==========================================

    elif powerbi_task == "Forecasting visuals for revenue":

        st.subheader(" Revenue Forecasting")

        image_path = os.path.join(BASE_DIR, "Assets", "s6.png")
        image = Image.open(image_path)

        st.image(
            image,
            use_container_width=True
        )


    # ==========================================
    # QUESTION 7
    # ==========================================

    elif powerbi_task == "Scenario-based dashboards":

        st.subheader(" Scenario Based Dashboard")

        image_path = os.path.join(BASE_DIR, "Assets", "s7.png")
        image = Image.open(image_path)

        st.image(
            image,
            use_container_width=True
        )

        



    # ==========================================
    # QUESTION 8
    # ==========================================

    elif powerbi_task == "Publish dashboard for executives":

        st.subheader("Published Executive Dashboard")

        image_path = os.path.join(BASE_DIR, "Assets", "s8.png")
        image = Image.open(image_path)

        st.markdown("<br><br>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 4, 1])

        with col2:
         st.image(image, width=850)

       