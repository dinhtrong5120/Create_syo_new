import streamlit as st
from src.ux_ui.user_read_only_syo_hyo import user_read_only_syo_hyo
from src.ux_ui.admin_all_1 import admin_all_1

st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":smiley:",
    layout="wide"
)
# light = '''
# <style>
#     .stApp {
#         background-color: white;
#     }
#     # .stButton > button { /* Thay đổi màu nền của nút */
#     #     background-color: gray;
#     # }
#     # .stTextInput > div > div > input { /* Thay đổi màu nền của input text */
#     #     background-color: darkgray;
#     # }
#     # /* ... và tiếp tục cho các thành phần khác */
# </style>
# '''
# st.markdown(light, unsafe_allow_html=True)
#
# page_bg_img = '''
#     <style>
#     .stApp {
#       background-image:
#         linear-gradient(to bottom, rgba(20,20,20,0.4), rgba(20,20,20,0.9)),
#         url("https://www-asia.nissan-cdn.net/content/dam/Nissan/jp/vehicles/ariya/2203/cruising-distance_charge/ariya_2203_cruising-distance_charge_01.jpg.ximg.l_12_m.smart.jpg");
#       background-size: cover;
#       background-repeat: no-repeat;
#       opacity: 0.95;
#     }
#     </style>
# '''
#
# st.markdown(page_bg_img, unsafe_allow_html=True)


def reset_data():
    if st.session_state.get('data') is not None:
        st.session_state['data'] = {}


if 1 == 1:
    try:
        if st.session_state.position == "admin" or st.session_state.position == "master":
            try:
                admin_all_1()
            except Exception as e:
                st.error(f"Error: {e}")
        elif st.session_state.position == "staff":
            try:
                user_read_only_syo_hyo()
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please login before running app!!!")
    except:
        if 'position' not in st.session_state:
            st.warning("Please login before running app!!!")
        else:
            try:
                st.rerun()
            except Exception as e:
                st.error(f"Error : {e}")
else:
    if st.session_state.position == "admin" or st.session_state.position == "master":
        admin_all_1()
    elif st.session_state.position == "staff":
        user_read_only_syo_hyo()
