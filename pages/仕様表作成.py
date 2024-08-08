import streamlit as st
from src.ux_ui.user_read_only_syo_hyo import user_read_only_syo_hyo
from src.ux_ui.admin_syo_hyo import admin_syo_hyo

st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":smiley:",
    layout="wide"
)


def reset_data():
    if st.session_state.get('data') is not None:
        st.session_state['data'] = {}


if 1 == 2:
    try:
        if st.session_state.position == "admin" or st.session_state.position == "master":
            admin_syo_hyo()
        elif st.session_state.position == "staff":
            try:
                user_read_only_syo_hyo()
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please login before running app!!!")
    except:
        st.warning("Please login before running app!!!")
else:
    if st.session_state.position == "admin" or st.session_state.position == "master":
        admin_syo_hyo()
    elif st.session_state.position == "staff":
        user_read_only_syo_hyo()
