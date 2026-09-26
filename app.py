import streamlit as st

from src.common import page_header, PRODUCT

st.set_page_config(page_title="Bellabeat | Overview", page_icon="🌿", layout="wide")

page_header(
    "Bellabeat Smart Device Usage Analysis",
    "How consumers use their fitness trackers, and what it means for Bellabeat's marketing strategy.",
)

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Business task")
    st.markdown(
        f"""
Bellabeat is a high-tech company that makes health-focused smart devices for women.
Co-founder and Chief Creative Officer **Urška Sršen** wants to know **how consumers
are already using their smart devices**, so that Bellabeat's marketing team can turn
those habits into growth opportunities.

This app analyzes public Fitbit fitness-tracker data as a proxy for smart-device
usage, and focuses the resulting recommendations on one Bellabeat product,
the **{PRODUCT}**.
        """
    )

    st.subheader("Guiding questions")
    st.markdown(
        """
1. What are the trends in smart device usage (steps, activity, sleep) across the week and across the day?
2. How does activity relate to sleep, and how consistently do people wear their device?
3. How can these trends inform Bellabeat's marketing strategy?
        """
    )

with col2:
    st.subheader("Stakeholders")
    st.markdown(
        """
**Primary**
- Urška Sršen — co-founder, Chief Creative Officer
- Sando Mur — co-founder, executive team

**Secondary**
- Bellabeat marketing analytics team
        """
    )
    st.info(
        "Use the sidebar to move through the report: Data & Cleaning → "
        "SQL Analysis → Dashboard → Recommendations.",
        icon="👈",
    )

st.divider()
st.subheader("Report deliverables covered by this app")
st.markdown(
    """
| # | Deliverable | Page |
|---|---|---|
| 1 | Summary of the business task | Overview (this page) |
| 2 | Description of all data sources | Data & Cleaning |
| 3 | Documentation of cleaning and manipulation | Data & Cleaning |
| 4 | Summary of the analysis | SQL Analysis |
| 5 | Supporting visualizations and key findings | Dashboard |
| 6 | Top high-level content recommendations | Recommendations |
    """
)
