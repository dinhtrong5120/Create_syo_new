import streamlit as st
import pandas as pd
from streamlit_extras.grid import grid
import io
# from read_data_view import *
# from funtion_database import *
from src.ux_ui.read_data_view import *
from src.db.funtion_database import *
from src.ux_ui.user_read_only_syo_hyo import get_data_syo_hyo
from src.db.function_database_new import get_gray_blue, update_data_new
from tests.convert_data_syo import dataframe_convert


def reset_data_prokan():
    if st.session_state.get('data_pro') is None:
        st.session_state['data_pro'] = {}


def set_data_prokan(key: str, value):
    st.session_state['data_pro'][key] = value


def get_data_prokan(key):
    return st.session_state['data_pro'].get(key)


def user_read_only_prokan():
    # st.session_state['data'] = {}
    reset_data_prokan()
    # set_data("flag_view",0)
    # APP
    col_left, col_right = st.columns([1, 3])
    with col_left:
        with st.form('input_form'):
            # PROJECT BOX
            col_left_prj_grid = grid(1, 2, 2, 2, vertical_align="top")
            # Row 1:
            col_left_prj_grid.header("Project")
            # Row 2:
            col_left_prj_grid.text_input("Model Code", key="code")
            col_left_prj_grid.selectbox("PowerTrain", ['EV', 'e-Power', 'ICE'], key="pwt")
            # Row 3:
            col_left_prj_grid.selectbox("Case", ['CASE1', 'CASE1.5', 'CASE2'], key="case")
            col_left_prj_grid.selectbox("Plant", ['JPN', 'US', 'EUR', 'PRC'], key="plant")
            # Row 4:
            col_left_prj_grid.selectbox("Dev", ['ALL', 'XQ4', 'XR2', 'XR3'], key="dev")
            col_left_prj_grid.selectbox("Lot", ["ALL", 'DS', 'DC', 'PFC', 'VC', 'PT1', 'PT2'], key="lot")
            st.header("View Box")
            col_left_spec_grid = grid(1, vertical_align="top")
            if col_left_spec_grid.form_submit_button("View Data", use_container_width=True):
                with st.spinner(text="In progress..."):
                    list_file, folder_output, name_zip = check_file_out(st.session_state.code, st.session_state.pwt,
                                                                        st.session_state.plant, st.session_state.case)
                    set_data_prokan("folder_output", folder_output)
                    set_data_prokan("name_zip", name_zip)
                    session, data, project_id, app_list = query_data(st.session_state.code, st.session_state.plant,
                                                                     st.session_state.pwt, st.session_state.case,
                                                                     st.session_state.dev, st.session_state.lot)
                    set_data_prokan("data_cadics", data)
                    set_state_db_prokan(session, project_id, app_list)
                    list_link = ["Car配車要望表", "WTC仕様用途一覧表", "WTC要望集約兼チェックリスト", "実験部品",
                                 "特性管理部品リスト", "File Log.xlsx"]
                    for index in range(len(list_link)):
                        set_data_prokan(list_link[index], list_file[index])
                        set_data_prokan("flag_view", 1)
                st.write("Completed!!!")
            # BANNER RIGHT
            with col_right:
                col_r1, col_r2 = st.columns([2, 1])
                with col_r1:
                    st.markdown('<h1 style="text-align: center;">プロ管集約業務システム</h1>', unsafe_allow_html=True)

                with col_r2:
                    st.markdown(f'<p style="text-align: center;">{st.session_state.name_user}.</p>',
                                unsafe_allow_html=True)
                    st.markdown(f'<p style="text-align: center;">{st.session_state.position}</p>',
                                unsafe_allow_html=True)

                view_prokan("staff")
                # Create button select output : Cadis or 5 output


def view_prokan(position):
    button_select_caout_grid = grid(2, 1, 4, vertical_align="top")
    row_butt = st.columns(6)
    selected_option_output_select = button_select_caout_grid.selectbox("SELECT OUTPUT",
                                                                       ["CADICS 項目", "仕様表", "FORM", "仕様表FORM",
                                                                        "Car配車要望表",
                                                                        "WTC仕様用途一覧表",
                                                                        "WTC要望集約兼チェックリスト",
                                                                        "実験部品", "特性管理部品リスト",
                                                                        "File Log"])
    # area for table output

    if get_data_prokan("flag_view") == 1:
        if selected_option_output_select == "CADICS 項目":
            button_select_caout_grid.selectbox("Select Sheet", ["CADICS"])
            if position == "staff":
                button_select_caout_grid.dataframe(get_data_prokan("data_cadics"), height=525, width=10000)
            if position != "staff":
                if get_data_prokan("session") is not None:
                    data_edit = button_select_caout_grid.data_editor(get_data_prokan("data_cadics"), height=525,
                                                                     width=10000)
                    with row_butt[3]:
                        if st.button("SAVE", use_container_width=True):
                            with st.spinner(text="In progress..."):
                                update_edit(data_edit, get_data_prokan("session"), get_data_prokan("data_cadics"),
                                            get_data_prokan("project_id"), get_data_prokan("app_list"))
                                set_data_prokan("data_cadics", data_edit)
                            st.write("Save Completed!!!")
                else:
                    button_select_caout_grid.dataframe(get_data_prokan("data_cadics"), height=525, width=10000)

            set_data_prokan("link", "cadics")

        if selected_option_output_select == "仕様表":
            Sheet_name = button_select_caout_grid.selectbox("Select Sheet", ["Sheet1"])
            if position == "staff":
                button_select_caout_grid.dataframe(get_data_prokan("data_syo"), height=525, width=10000)
            if position != "staff":
                st.session_state.data_frame = button_select_caout_grid.data_editor(get_data_prokan("data_syo"),
                                                                                   height=525, width=10000,
                                                                                   disabled=['auto', 'gr', 'keyword',
                                                                                             'CADICS ID'])
                with row_butt[3]:
                    if st.button("SAVE", use_container_width=True):
                        with st.spinner(text="In progress..."):
                            result_querry_region_4_gray, result_querry_region_4_blue = get_gray_blue(
                                st.session_state.code)
                            df, df_1 = dataframe_convert(st.session_state.data_frame, st.session_state.code,
                                                         result_querry_region_4_gray,
                                                         result_querry_region_4_blue)
                            update_data_new(st.session_state.code, df, df_1)
                            st.write("Save Completed!!!")
            set_data_prokan("link", "仕様表")
            set_data_prokan("仕様表", st.session_state.data_frame)

        if selected_option_output_select == "仕様表FORM":
            Sheet_name = button_select_caout_grid.selectbox("Select Sheet", ["Sheet1"])
            if position == "staff":
                button_select_caout_grid.dataframe(get_data_prokan("form+spec"), height=525, width=10000)
            if position != "staff":
                st.session_state.data_frame_combine = button_select_caout_grid.data_editor(get_data_prokan("form+spec"),
                                                                                           height=525, width=10000,
                                                                                           disabled=['auto', 'gr',
                                                                                                     'keyword',
                                                                                                     'CADICS ID'])

        if selected_option_output_select == "FORM":
            button_select_caout_grid.selectbox("Select Sheet", ["Sheet1"])
            if position == "staff":
                st.session_state.data_frame = button_select_caout_grid.dataframe(get_data_prokan("form"), height=525,
                                                                                 width=10000)
            if position != "staff":
                st.session_state.data_frame = button_select_caout_grid.data_editor(get_data_prokan("form"), height=525,
                                                                                   width=10000, disabled=['auto', 'gr',
                                                                                                     'keyword',
                                                                                                     'CADICS ID'])
            # set_data_prokan("link", "cadics")
            set_data_prokan("link", "仕様表")
            set_data_prokan("仕様表", st.session_state.data_frame)

        if selected_option_output_select == "Car配車要望表":
            Sheet_name = button_select_caout_grid.selectbox("Select Sheet", ["PFC", "VC", "PT1", "PT2"])
            data = read_output(get_data_prokan("Car配車要望表"), Sheet_name)
            button_select_caout_grid.dataframe(data, height=525, width=10000)
            set_data_prokan("link", get_data_prokan("Car配車要望表"))
            set_data_prokan("name", "Car配車要望表.xlsx")

        if selected_option_output_select == "WTC仕様用途一覧表":
            Sheet_name = button_select_caout_grid.selectbox("Select Sheet", ["PFC", "VC"])
            data = read_output(get_data_prokan("WTC仕様用途一覧表"), Sheet_name)
            button_select_caout_grid.dataframe(data, height=525, width=10000)
            set_data_prokan("link", get_data_prokan("WTC仕様用途一覧表"))
            set_data_prokan("name", "WTC仕様用途一覧表.xlsx")

        if selected_option_output_select == "WTC要望集約兼チェックリスト":
            Sheet_name = button_select_caout_grid.selectbox("Select Sheet", ["PFC", "VC"])
            data = read_output(get_data_prokan("WTC要望集約兼チェックリスト"), Sheet_name)
            button_select_caout_grid.dataframe(data, height=525, width=10000)
            set_data_prokan("link", get_data_prokan("WTC要望集約兼チェックリスト"))
            set_data_prokan("name", "WTC要望集約兼チェックリスト.xlsx")

        if selected_option_output_select == "実験部品":
            Sheet_name = button_select_caout_grid.selectbox("Select Sheet", ["PFC", "VC"])
            data = read_output(get_data_prokan("実験部品"), Sheet_name)
            button_select_caout_grid.dataframe(data, height=525, width=10000)
            set_data_prokan("link", get_data_prokan("実験部品"))
            set_data_prokan("name", "実験部品.xlsx")

        if selected_option_output_select == "特性管理部品リスト":
            Sheet_name = button_select_caout_grid.selectbox("Select Sheet", ["PFC", "VC"])
            data = read_output(get_data_prokan("特性管理部品リスト"), Sheet_name)
            button_select_caout_grid.dataframe(data, height=525, width=10000)
            set_data_prokan("link", get_data_prokan("特性管理部品リスト"))
            set_data_prokan("name", "特性管理部品リスト.xlsx")

        if selected_option_output_select == "File Log":
            Sheet_name = button_select_caout_grid.selectbox("Select Sheet",
                                                            ["COUNT", "関連表①", "関連表②", "関連表③", "関連表④"])
            data = read_output(get_data_prokan("File Log"), Sheet_name)
            button_select_caout_grid.dataframe(data, height=525, width=10000)
            set_data_prokan("link", get_data_prokan("File Log"))
            set_data_prokan("name", "File Log.xlsx")

        # button save and download
        button_select_caout_grid.header("")
        with row_butt[4]:
            if get_data_prokan("link") is not None and get_data_prokan("link") not in ["cadics", 'FORM', '仕様表']:
                with open(get_data_prokan("link"), "rb") as fp:
                    st.download_button(
                        label="Download File",
                        data=fp,
                        file_name=get_data_prokan("name"),
                        mime="text/plain",
                        use_container_width=True
                    )
            elif get_data_prokan("link") == "cadics" and len(get_data_prokan("data_cadics").columns) > 31:
                bool = st.download_button(
                    label="Download File",
                    data=get_data_prokan("data_cadics").to_csv(index=None, header=None),
                    file_name="CADICS_ALL.csv",
                    mime="text/csv",
                    use_container_width=True,
                )
                if bool and position == "admin":
                    write_cadic_temp(st.session_state.name_user, position, st.session_state.code, st.session_state.pwt,
                                     st.session_state.plant, st.session_state.case, get_data_prokan("data_cadics"))
                    bool = False
            elif get_data_prokan("link") == "仕様表":
                df = get_data_prokan("仕様表")
                if df is None or df.equals(frame_empty()) or df.shape[0] == 1:
                    print('ggg')
                else:
                    num_columns = df.shape[1]
                    device_group = get_data_prokan("device_group")
                    device = get_data_prokan("device")
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                        df.to_excel(writer, index=False, sheet_name='Sheet1')
                        workbook = writer.book
                        worksheet = writer.sheets['Sheet1']
                        highlight_format_device_group = workbook.add_format(
                            {'bg_color': '#535353', 'font_color': '#FFFFFF'})
                        highlight_format_device = workbook.add_format({'bg_color': '#245269', 'font_color': '#FFFFFF'})
                        for row_num, value in enumerate(df['auto'], start=1):
                            # st.write('value: ',value)
                            # st.write('str(value): ',str(value))
                            # st.write('device_group: ',device_group)
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
                    if st.session_state.data_frame.shape[1] != 6:
                        file_name = f"仕様表_{str(st.session_state.code).upper()}.xlsx"
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
        with row_butt[5]:
            try:
                # zip_folder(get_data("folder_output"),get_data("folder_output")+".zip")
                with open(get_data_prokan("folder_output") + ".zip", "rb") as fp:
                    st.download_button(
                        label="Download All",
                        data=fp,
                        file_name=get_data_prokan("name_zip"),
                        mime="application/zip",
                        use_container_width=True
                    )
            except:
                None
    else:
        Sheet_name = button_select_caout_grid.selectbox("Select Sheet", [])
        data_empty = pd.DataFrame([[""] * 30] * 20)
        column_names = [f'{i + 1}' for i in range(30)]
        data_empty = pd.DataFrame(data_empty, columns=column_names)
        data_empty = data_empty.fillna("")
        button_select_caout_grid.dataframe(data_empty, height=525, width=10000)


def set_state_db_prokan(session, project_id, app_list):
    set_data_prokan("session", session)
    set_data_prokan("project_id", project_id)
    set_data_prokan("app_list", app_list)
