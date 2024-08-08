
import streamlit as st
from streamlit_extras.grid import grid
from .user_read_only_syo_hyo import view_syo_hyo
from ..db.function_database_new import querry_data_syo_hyo, update_data_new, add_function_from_admin, \
    update_and_querry_form_data, get_gray_blue, frame_empty, querry_to_show_project
from tests.convert_data_syo import *
from ..app.all_process_spec_not_protected import main_process_spec_not_protected
from ..app.create_syo import create_syo
from ..app.check_filed_information import check_key_spec_new, check_optioncode
import numpy as np


def reset_data():
    if st.session_state.get('data') is None:
        st.session_state['data'] = {}


def set_data(key: str, value):
    st.session_state['data'][key] = value


def get_data(key):
    return st.session_state['data'].get(key)


def admin_syo_hyo():
    reset_data()
    col_left, col_right = st.columns([1, 3])
    with col_left:
        with st.form('仕様表作成_form'):

            col_left_prj_grid = grid(1, 1, 2, 2, 1, vertical_align="top")
            # Row 1:
            col_left_prj_grid.header("仕様表作成")
            # Row 2:
            col_left_prj_grid.header("Project Infor")
            # Row 3:
            col_left_prj_grid.text_input("Model Code", key="code")
            col_left_prj_grid.selectbox("PowerTrain", ['EV', 'e-Power', 'ICE'], key="pwt")
            # Row 4:
            col_left_prj_grid.selectbox("Case", ['CASE1', 'CASE1.5', 'CASE2'], key="case")
            col_left_prj_grid.selectbox("Plant", ['JPN', 'US', 'EUR', 'PRC'], key="plant")

            files = st.file_uploader("", accept_multiple_files=False)
            col_left_spec_grid = grid(2, vertical_align="top")
            set_data("running", 0)
            # ==============================================================================================================================

            if col_left_spec_grid.form_submit_button("View", use_container_width=True) and get_data(
                    "running") == 0:
                set_data("link_1", "syo_hyo")
                set_data("link_2", "cadics_off_delete")
                with st.spinner(text="In progress..."):
                    set_data("running", 1)

                    set_state()
                    if st.session_state.code == '':
                        st.warning("Model code cannot be left blank")
                        # set_data("link_syo", "cadics_z")
                        set_data("link_1", "cadics_off_save")
                        set_data("仕様表", frame_empty())
                    else:
                        data, unique_list_max, unique_list_submax = querry_data_syo_hyo(st.session_state.code)
                        data = data.fillna("")
                        set_data("仕様表", data)
                        set_data("device_group", unique_list_max)
                        set_data("device", unique_list_submax)
                        set_data("link_syo", "syo_hyo")
                        if not data.empty:
                            print()
                    set_data("running", 0)
                set_data("flag_check_fail", True)

            # ==============================================================================================================================

            if col_left_spec_grid.form_submit_button("仕様表FORM", use_container_width=True) and get_data(
                    "running") == 0:
                set_data("link_syo", "cadics_zzz")
                set_data("link_1", "cadics_off_save")
                set_data("link_2", "cadics_off_delete")
                set_data("running", 1)
                with st.spinner(text="In progress..."):
                    if files is not None:
                        code = str(st.session_state.code).lower()
                        if code not in str(files.name).lower() or 'Spec_List' not in files.name:
                            st.error("Model code or Spec incorrect")
                            set_data("仕様表", frame_empty())
                        elif code == '':
                            st.error('Model code is blank')
                            set_data("仕様表", frame_empty())
                        else:
                            df_check_log, flg_check_fail = check_key_spec_new(files)
                            set_data("flag_check_fail", flg_check_fail)
                            if flg_check_fail:
                                df_1, merged_df_4_optioncode, unique_list_max, unique_list_submax = update_and_querry_form_data()
                                merged_df_fail = pd.concat([df_1, merged_df_4_optioncode], axis=0)
                                set_data("device_group", unique_list_max)
                                set_data("device", unique_list_submax)
                                set_data("仕様表", merged_df_fail)
                                st.write(df_check_log)
                                st.warning("Form Speclist is incorrect")
                            else:
                                df_end_region3, data_for_create = main_process_spec_not_protected(files,
                                                                                                  str(st.session_state.code).upper())
                                merger_end, unique_list_max, unique_list_submax = add_function_from_admin(
                                    df_end_region3, files)
                                merger_end = merger_end.reset_index(drop=True)
                                set_data("device_group", unique_list_max)
                                set_data("device", unique_list_submax)
                                set_data('data_for_create', data_for_create)
                                set_data("仕様表", merger_end)
                                st.success("Create Completed!!!")
                        set_state()
                    else:
                        set_data("仕様表", frame_empty())
                        st.warning("file has not been uploaded yet")
                    set_data("running", 0)
            # ==============================================================================================================================
            if col_left_spec_grid.form_submit_button("仕様表作成",
                                                     use_container_width=True) == True and get_data("running") == 0:
                set_data("running", 1)
                set_data("link_2", "cadics_off_delete")
                with st.spinner(text="In progress..."):
                    if not get_data("flag_check_fail") and get_data("flag_check_fail") is not None and st.session_state.data_frame.shape[1] > 4:
                        if not check_optioncode(st.session_state.data_frame):
                            if st.session_state.code != '':
                                form_syo = create_syo(st.session_state.data_frame, get_data("data_for_create"))
                                form_syo.replace({np.nan: ''}, inplace=True)
                                set_data("仕様表", form_syo)
                                result_querry_region_4_gray, result_querry_region_4_blue = get_gray_blue(
                                    st.session_state.code)
                                df, df_1 = dataframe_convert(form_syo, st.session_state.code,
                                                             result_querry_region_4_gray,
                                                             result_querry_region_4_blue)
                                # update_data_new_online(st.session_state.code, df, df_1)
                                update_data_new(st.session_state.code, df, df_1)
                                set_data("link_1", "syo_hyo")
                                set_data("link_syo", "syo_hyo")
                                st.success("Completed")
                            else:
                                st.warning("Model code can not be left blank")
                        else:
                            st.warning("OptionCode empty")
                    else:
                        set_data("仕様表", frame_empty())
                        st.warning("Please create Form")
                    set_data("running", 0)

            # ==============================================================================================================================
            if col_left_spec_grid.form_submit_button("LIST PROJECT",
                                                     use_container_width=True) == True and get_data("running") == 0:
                set_data("running", 1)
                set_data("link_1", "cadics_off_save")
                set_data("link_2", "cadics_on_delete")
                with st.spinner(text="In progress..."):
                    all_project = querry_to_show_project()
                    set_data("仕様表", all_project)
                    set_state()
                    set_data("link_syo", "cadics_xzxx")
                    st.success("Completed")
                    set_data("running", 0)

        with st.form('仕様表の Format Update'):

            col_left_prj_grid = grid(1, vertical_align="top")

            col_left_prj_grid.header("仕様表の Format Update")
            files_update = st.file_uploader("", accept_multiple_files=True)
            col_left_spec_grid = grid(2, vertical_align="top")
            # set_data("running", 0)

            # ==============================================================================================================================

            if col_left_spec_grid.form_submit_button("Update", use_container_width=True) and get_data("running") == 0:
                set_data("link_1", "cadics_off_save")
                set_data("link_2", "cadics_off_delete")
                set_data("running", 1)
                with st.spinner(text="In progress..."):
                    set_state()
                    if files_update is not None and len(files_update) > 0:
                        for file_update in files_update:
                            filename = file_update.name
                            code = filename.split('.')[0]
                            if "仕様表_" ==  code[0:4]:
                                code = code.replace("仕様表_", "")
                                df, df_1 = dataframe_convert(file_update, code, [], [])
                                if not isinstance(df, pd.DataFrame):
                                    if df_1:
                                        st.error(df + str(df_1))
                                        set_data("仕様表", frame_empty())
                                    else:
                                        st.error(df)
                                        set_data("仕様表", frame_empty())
                                    continue
                                update_data_new(code, df, df_1)
                                if df.shape[1] != 7:
                                    data, unique_list_max, unique_list_submax = querry_data_syo_hyo(code)
                                    data = data.fillna("")
                                    set_data("仕様表", data)
                                else:
                                    df_1, merged_df_4_optioncode, unique_list_max, unique_list_submax = update_and_querry_form_data()
                                    form_df = pd.concat([df_1, merged_df_4_optioncode], axis=0)
                                    set_data("device_group", unique_list_max)
                                    set_data("device", unique_list_submax)
                                    set_data("仕様表", form_df)
                                    st.success('Updated!')
                            else:
                                set_data("仕様表", frame_empty())
                                st.error('Upload file name is incorrect')
                    elif len(files_update) == 0:
                        set_data("仕様表", frame_empty())
                        st.warning('Please upload file')
                    set_data("device_group", [])
                    set_data("device", [])
                    set_data("link_syo", "syo_hyo")
                    set_data("running", 0)
            # ==============================================================================================================================

            if col_left_spec_grid.form_submit_button("View Form", use_container_width=True) and get_data(
                    "running") == 0:
                set_data("link_syo", "syo_hyo")
                set_data("link_1", "cadics_off_save")
                set_data("link_2", "cadics_off_delete")
                set_data("running", 1)
                with st.spinner(text="In progress..."):
                    df_1, merged_df_4_optioncode, unique_list_max, unique_list_submax = update_and_querry_form_data()
                    form_df = pd.concat([df_1, merged_df_4_optioncode], axis=0)
                    set_data("device_group", unique_list_max)
                    set_data("device", unique_list_submax)
                    set_data("仕様表", form_df)
                    set_state()
                    set_data("running", 0)

    with col_right:
        col_r1, col_r2 = st.columns([5, 1])
        with col_r1:
            st.markdown(
                '<h1 style="text-align: center;'
                'background-color: #CCE9D9;'
                'border: 2px solid #4CAF50; '
                'padding: 10px;">仕様表自動作成</h1>',
                unsafe_allow_html=True)
        with col_r2:
            st.markdown(
                f'<p style="text-align: center;'
                f'background-color: #CCE9D9;'
                f'border: 2px solid #4CAF50; '
                f'padding: 10px">{st.session_state.name_user}<br>{st.session_state.position}</p>',
                unsafe_allow_html=True)
        view_syo_hyo(st.session_state.code)


def set_state():
    set_data("flag_view", 1)


def set_state_db(session, project_id, app_list):
    set_data("session", session)
    set_data("project_id", project_id)
    set_data("app_list", app_list)
