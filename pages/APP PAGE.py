import streamlit as st
# from user_read_only import user_read_only
from src.ux_ui.user_read_only_prokan import user_read_only_prokan
# from admin import admin
from src.ux_ui.admin_prokan import admin_prokan

st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":smiley:",
    layout="wide"
)


def reset_data():
    if st.session_state.get('data_pro') is not None:
        st.session_state['data_pro'] = {}


if 1 == 1:
    try:
        if st.session_state.position == "admin" or st.session_state.position == "master":  # st.session_state.mail:
            # ------------MAIN APP-----------x
            # try:
            admin_prokan()
            # except Exception as e:
            #     st.error(f"Error: {e}")
        elif st.session_state.position == "staff":
            try:
                user_read_only_prokan()
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please login before running app!!!")
    except:
        st.warning("Please login before running app!!!")
else:
    if st.session_state.position == "admin" or st.session_state.position == "master":  # st.session_state.mail:
        # ------------MAIN APP-----------x
        admin_prokan()
    elif st.session_state.position == "staff":
        user_read_only_prokan()


    # if st.session_state.position == "admin" or st.session_state.position == "master":  # st.session_state.mail:
    #     admin_prokan()
