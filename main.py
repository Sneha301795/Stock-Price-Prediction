"""
Main Streamlit application entry point.

Big Stock Price Prediction Using Apache Spark
Frontend dashboard powered by Streamlit and PySpark backend.
"""

import streamlit as st
import logging

from utils.cookies import cookies
from streamlit_cookies_controller import CookieController
from frontend.components.sidebar import render_sidebar
from frontend.pages import login, dashboard, stock_search, portfolio, technical_analysis, model_performance

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def initialize_session_state() -> None:
    """Initialize Streamlit session state keys."""
    # Check for persistent login from cookies
    if cookies.ready():
        saved_login = cookies.get("logged_in")
        saved_username = cookies.get("username")
        saved_theme = cookies.get("theme", "Dark")
        
        if "logged_in" not in st.session_state:
            st.session_state.logged_in = saved_login == "true"
        
        if "username" not in st.session_state:
            st.session_state.username = saved_username
        
        if "theme" not in st.session_state:
            st.session_state.theme = saved_theme

    if "token" not in st.session_state:
        st.session_state.token = None

    if "portfolio" not in st.session_state:
        st.session_state.portfolio = []


    # Ensure default values if cookies not available
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "username" not in st.session_state:
        st.session_state.username = None

    if "theme" not in st.session_state:
        st.session_state.theme = "Dark"


def apply_global_theme() -> None:
    """Apply custom styling to the dashboard based on selected theme."""
    theme = st.session_state.get("theme", "Light")
    # light vs dark colors
    if theme == "Dark":
        app_bg = "#1e1e1e"
        sidebar_bg = "#2e2e2e"
        text_color = "#ffffff"
        header_color = "#ffffff"
    else:
        app_bg = "#f8f9fa"
        sidebar_bg = "#ffffff"
        text_color = "#1f2937"
        header_color = "#1f2937"

    st.markdown(
        f"""
        <style>
        /* Global styling */
        .stApp {{
            background-color: {app_bg};
            color: {text_color};
        }}

        /* Main content container */
        .main .block-container {{
            padding-top: 1.5rem;
            padding-bottom: 1.5rem;
            max-width: 1400px;
        }}

        /* Sidebar styling */
        [data-testid="stSidebar"] {{
            background-color: {sidebar_bg};
            border-right: 1px solid #e0e0e0;
        }}

        /* Metric styling */
        .metric-label {{
            font-weight: 600;
            font-size: 14px;
        }}

        /* Chart styling */
        .plotly-chart {{
            border-radius: 8px;
        }}

        /* Button styling */
        .stButton > button {{
            border-radius: 6px;
            font-weight: 500;
        }}

        /* Header styling */
        h1, h2, h3 {{
            color: {header_color};
            font-weight: 600;
        }}

        /* Info boxes */
        .stInfo, .stSuccess, .stWarning, .stError {{
            border-radius: 6px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_footer() -> None:
    """Render application footer."""
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.caption("📈 Big Stock Price Prediction")
    with col2:
        st.caption("Powered by Apache Spark & Streamlit")
    with col3:
        st.caption("© 2024 - All Rights Reserved")


def main() -> None:
    """Main application entry point."""
    st.set_page_config(
        page_title="Big Stock Price Prediction Dashboard",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    initialize_session_state()
    apply_global_theme()

    # If user is not logged in, show login page
    if not st.session_state.logged_in:
        login.render()
        return

    # Render sidebar and get selected page
    selected_page = render_sidebar()

    # Route to the selected page
    try:
        if selected_page == "Dashboard":
            dashboard.render()
        
        elif selected_page == "Stock Search":
            stock_search.render()
        
        elif selected_page == "Technical Analysis":
            technical_analysis.render()
        
        elif selected_page == "Portfolio Tracker":
            portfolio.render()
        
        elif selected_page == "Model Performance":
            model_performance.render()
        
        elif selected_page == "Login":
            # User clicked logout or login page is shown
            st.session_state.logged_in = False
            st.session_state.token = None
            st.session_state.username = None
            st.rerun()
        
        else:
            st.error(f"❌ Page '{selected_page}' not found.")
    
    except Exception as e:
        logger.error(f"Error rendering page: {e}")
        st.error(f"❌ An error occurred: {str(e)}")
        st.info("Please try refreshing the page or navigating to another section.")
    
    # Render footer
    render_footer()


if __name__ == "__main__":
    main()

