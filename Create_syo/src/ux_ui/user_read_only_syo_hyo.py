import streamlit as st
from streamlit_extras.grid import grid
import io
import pandas as pd
from ..db.function_database_new import get_gray_blue, delete_project_syo, frame_empty, \
    update_data_new
from tests.convert_data_syo import dataframe_convert


def reset_data_syo_hyo():
    if st.session_state.get('data') is None:
        st.session_state['data'] = {}


def set_data_syo_hyo(key: str, value):
    st.session_state['data'][key] = value


def get_data_syo_hyo(key):
    return st.session_state['data'].get(key)


def user_read_only_syo_hyo():
    reset_data_syo_hyo()
    col_left, col_right = st.columns([1, 3])
    with col_left:
        with st.form('input_form'):
            # PROJECT BOX
            col_left_prj_grid = grid(1, 2, 2, vertical_align="top")
            # Row 1:
            col_left_prj_grid.header("Project")
            # Row 2:
            col_left_prj_grid.text_input("Model Code", key="code")
            col_left_prj_grid.selectbox("PowerTrain", ['EV', 'e-Power', 'ICE'], key="pwt")
            # Row 3:
            col_left_prj_grid.selectbox("Case", ['CASE1', 'CASE1.5', 'CASE2'], key="case")
            col_left_prj_grid.selectbox("Plant", ['JPN', 'US', 'EUR', 'PRC'], key="plant")

            st.header("View Box")
            col_left_spec_grid = grid(1, vertical_align="top")
            if col_left_spec_grid.form_submit_button("View", use_container_width=True):
                set_data_syo_hyo("link_syo", "syo_hyo")
            with col_right:
                col_r1, col_r2 = st.columns([2, 1])
                with col_r1:
                    st.markdown(
                        '<h1 style="text-align: center;background-color: #CCE9D9;border: 2px solid #4CAF50; padding: 10px;">仕様表自動作成</h1>',
                        unsafe_allow_html=True)
                with col_r2:
                    st.markdown(
                        f'<p style="text-align: center;">{st.session_state.name_user}<br>{st.session_state.position}</p>',
                        unsafe_allow_html=True)

                view_syo_hyo(st.session_state.code)


def view_syo_hyo(project_name):
    button_select_caout_grid = grid(1, 1, 1, vertical_align="top")
    row_butt = st.columns(6)

    if get_data_syo_hyo("flag_view") == 1:

        st.session_state.data_frame = button_select_caout_grid.data_editor(get_data_syo_hyo("仕様表"), height=710,
                                                                           width=10000,
                                                                           disabled=['auto', 'gr', 'keyword',
                                                                                     'CADICS ID', 'project_name'])

        css = """
            <style>
                .stButton > button, .stDownloadButton > button {
                    width: 100%;  /* Đặt chiều rộng 100% */
                    #background-color: rgba(0, 0, 255, 0.5);  /* Màu xanh lam với độ trong suốt 50% */
                    #color: white !important;     
                    #border: 1px solid black;
                }
                #.stButton > button:hover, .stDownloadButton > button:hover {
                    #background-color: darkorange;
                    #color: white !important;
                #}
            </style>
        """
        st.markdown(css, unsafe_allow_html=True)
        with row_butt[2]:
            if get_data_syo_hyo("link_1") == "syo_hyo":
                if st.button("SAVE"):
                    result_querry_region_4_gray, result_querry_region_4_blue = get_gray_blue(st.session_state.code)
                    df, df_1 = dataframe_convert(st.session_state.data_frame, st.session_state.code,
                                                 result_querry_region_4_gray,
                                                 result_querry_region_4_blue)
                    # update_data_new_online(st.session_state.code, df, df_1)
                    update_data_new(st.session_state.code, df, df_1)
                    st.success('Success')
        with row_butt[3]:
            if get_data_syo_hyo("link_2") == "cadics_on_delete":
                if st.button("DELETE"):
                    df_after_deleted = delete_project_syo(st.session_state.data_frame)
                    # st.write(df_after_deleted)
                    set_data_syo_hyo("仕様表", df_after_deleted)
                    st.session_state.data_frame = df_after_deleted
                    # st.success("Delete Completed")
                    # st.experimental_rerun()
                    # st.rerun()

        with row_butt[4]:
            if get_data_syo_hyo("link_syo") == "syo_hyo":

                df = get_data_syo_hyo("仕様表")
                if df is None or df.equals(frame_empty()):
                    print('ggg')
                else:
                    num_columns = df.shape[1]
                    device_group = get_data_syo_hyo("device_group")
                    device = get_data_syo_hyo("device")
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                        df.to_excel(writer, index=False, sheet_name='Sheet1')
                        workbook = writer.book
                        worksheet = writer.sheets['Sheet1']
                        highlight_format_device_group = workbook.add_format(
                            {'bg_color': '#535353', 'font_color': '#FFFFFF'})
                        highlight_format_device = workbook.add_format({'bg_color': '#245269', 'font_color': '#FFFFFF'})
                        # _____________________________ Áp dụng cho toàn bộ dòng_____________________________
                        # Áp dụng định dạng màu vàng cho hàng chứa giá trị 'X01_VISIBILITY' trong cột A
                        # for row_num, value in enumerate(df['auto'], start=1):
                        #     if str(value) is not None:
                        #         if str(value) in device_group:
                        #             worksheet.set_row(row_num, None, highlight_format_device_group)
                        #         if str(value) in device:
                        #             worksheet.set_row(row_num, None, highlight_format_device)
                        # _____________________________ Áp dụng đến cột cần tô màu _____________________________
                        for row_num, value in enumerate(df['auto'], start=1):
                            if str(value) is not None:

                                if str(value) in device_group:
                                    for col_num in range(num_columns):
                                        worksheet.write(row_num, col_num, df.iloc[row_num - 1, col_num],
                                                        highlight_format_device_group)
                                if str(value) in device:
                                    for col_num in range(num_columns):
                                        worksheet.write(row_num, col_num, df.iloc[row_num - 1, col_num],
                                                        highlight_format_device)

                    output.seek(0)
                    if st.session_state.data_frame.shape[1] != 4:
                        file_name = f"仕様表_{project_name.upper()}.xlsx"
                    else:
                        file_name = "仕様表_FORM.xlsx"
                    st.download_button(
                        label="Download File",
                        data=output,
                        # file_name=f"仕様表_{project_name.upper()}.xlsx",
                        file_name=file_name,
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        use_container_width=True,
                    )
    else:
        data_empty = pd.DataFrame([[""] * 30] * 30)
        column_names = [f'{i + 1}' for i in range(30)]
        data_empty = pd.DataFrame(data_empty, columns=column_names)
        data_empty = data_empty.fillna("")
        button_select_caout_grid.dataframe(data_empty, height=725, width=1000000)


def set_state_db_syo_hyo(session, project_id, app_list):
    set_data_syo_hyo("session", session)
    set_data_syo_hyo("project_id", project_id)
    set_data_syo_hyo("app_list", app_list)
