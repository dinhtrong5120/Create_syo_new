import streamlit as st
import webbrowser

from src.db.funtion_database import log_in

st.set_page_config(
    page_title="Login Page",
    page_icon="👋",
)
st.header("# Welcome to Website プロ管集約業務1本化! 👋")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Sử dụng session state để lưu trạng thái của các nút
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

if st.button("Login"):
    st.session_state.button_clicked = True
    # Check if the username and password are correct
    name_user, position, project_query = log_in(username, password)
    if position is not None:
        st.session_state.position = position
        st.session_state.name_user = name_user
        st.session_state.project_query = project_query
        st.success("Login successful!")
        st.switch_page("pages/1 HOME.py")
    else:
        st.session_state.position = None
        st.error("Login failed. Please check your credentials.")


# Hàm để chuyển hướng đến một URL
def open_url(url):
    webbrowser.open_new_tab(url)


# Nếu nút login đã được bấm, hiển thị thêm 2 nút
#if st.session_state.button_clicked and st.session_state.position is not None:
    #col1, col2 = st.columns(2)
    #with col1:
        #if st.button("仕様表作成"):
            #st.switch_page("pages/仕様表作成.py")
    #with col2:
        #if st.button("プロ管集約"):
            #st.switch_page("pages/APP PAGE.py")
# import pandas as pd
# import streamlit as st
# from io import BytesIO
#
# def get_data(sheet_name):
#     # Đây chỉ là ví dụ, bạn có thể thay đổi hàm này để lấy dữ liệu từ nguồn thực tế của bạn
#     return pd.DataFrame({
#         'cột1': ['データ1', 'データ2'],
#         'cột2': ['データ3', 'データ4']
#     })
#
# project_name = "tên_project"  # Thay đổi cho phù hợp với tên project của bạn
#
# # Tạo buffer BytesIO
# buffer = BytesIO()
#
# # Lấy dữ liệu và ghi vào buffer với encoding 'utf-8-sig'
# get_data("仕様表").to_csv(buffer, index=False, header=True, encoding='utf-8-sig')
#
# # Đặt lại vị trí con trỏ của buffer về đầu
# buffer.seek(0)
#
# # Tạo nút download file với buffer dữ liệu
# st.download_button(
#     label="Download File",
#     data=buffer,
#     file_name=f"仕様表_{project_name.upper()}.csv",
#     mime="text/csv",
#     use_container_width=True,
# )
