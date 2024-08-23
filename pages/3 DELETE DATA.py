from src.delete.DELETE_DATABASE import delete_database
from src.delete.DELETE_INPUT_FILES import delete_input_file
from src.delete.DELETE_INPUT_FOLDERS import delete_input_folder
from src.delete.DELETE_OUTPUT_FOLDERS import delete_output
from src.delete.DELETE_OUTPUT_ALL import delete_all_output
import streamlit as st
from streamlit_extras.grid import grid

st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":smiley:",
    layout="wide"
)
# try :
if 'position' in st.session_state:
    if st.session_state.position == "admin" or st.session_state.position == "master":
        delete_database()
        st.write("")
        st.write("")
        st.write("")

        st.markdown(
            '<h1 style="text-align: center;background-color: #CCE9D9;border: 2px solid #4CAF50; padding: 10px;">INPUT</h1>',
            unsafe_allow_html=True)
    # st.subheader("")
        st.write("")
        col1, col2 = st.columns(2)
        with col1:


            delete_input_folder()
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
        # delete_output(
        with col2:
            try:
                delete_input_file()
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
            except:
                st.warning("Input is empty!")
        st.markdown(
            '<h1 style="text-align: center;background-color: #CCE9D9;border: 2px solid #4CAF50; padding: 10px;">OUTPUT</h1>',
            unsafe_allow_html=True)
        st.write("")
        col3, col4 = st.columns(2)
        with col3:
            delete_output()
        with col4:
            delete_all_output()

    else:
        st.warning("Permission Deny!")
else:
    st.warning("Please login before running app!!!")
# except:
#     st.warning("Please login before running app!!!")
