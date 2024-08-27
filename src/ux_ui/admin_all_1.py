import streamlit
import streamlit as st
import pandas as pd
from streamlit_extras.grid import grid
from src.ux_ui.read_data_view import *
from src.ux_ui.user_read_only_all import view_prokan
from src.app.update_file import get_csrf_token, update_file_into_server_new
from src.app.create_cadics import create_cadics_old
from src.app.cadic_test import create_cadics_new
from src.app.create_document_step2 import create_doc
from src.app.classify_group import *
from src.app.update_file import update_file_after_edit
from src.db.function_database_new import querry_data_syo_hyo, update_and_querry_form_data, update_syo, \
    add_function_from_admin, get_gray_blue, update_data_new, update_syo_form
from src.app.check_filed_information import check_key_spec_new, check_optioncode
from src.app.all_process_spec_not_protected import main_process_spec_not_protected
from src.app.create_syo_new_edit import create_syo
import numpy as np
from tests.convert_data_syo import dataframe_convert
from streamlit_modal import Modal
import time


def long_running_function():
    # Giả sử hàm này chạy trong 5 giây
    time.sleep(2)


def reset_data():
    if st.session_state.get('data_pro') is None:
        st.session_state['data_pro'] = {}


def set_data(key: str, value):
    st.session_state['data_pro'][key] = value


def get_data(key):
    return st.session_state['data_pro'].get(key)


def admin_all_1():
    reset_data()
    # set_data("list_group",["ALL"])
    csrf_token = get_csrf_token()
    # st.markdown(
    #     '<h1 style="text-align: center;background-color: #CCE9D9;border: 2px solid #4CAF50; padding: 10px;">INPUT</h1>',
    #     unsafe_allow_html=True)
    col_left, col_right = st.columns([1, 3])

    # Initialize the modal with a key
    modal_load_file = Modal(key="modal_loading", title="Loading...")
    modal_view = Modal(key="modal_viewing", title="Viewing...")
    modal_create_form = Modal(key="modal_create_form", title="仕様表FORM...")
    modal_create_syo = Modal(key="modal_create_syo", title="仕様表作成...")
    modal_create_cadics = Modal(key="modal_create_cadics", title="Create cadics...")
    modal_create_output = Modal(key="modal_create_output", title="Create output...")

    with col_left:
        if 'view_complete' not in st.session_state:
            st.session_state.view_complete = False
        if 'load_complete' not in st.session_state:
            st.session_state.load_complete = False
        if 'create_form_complete' not in st.session_state:
            st.session_state.create_form_complete = False
        if 'create_syo_complete' not in st.session_state:
            st.session_state.create_syo_complete = False
        if 'create_cadics_complete' not in st.session_state:
            st.session_state.create_cadics_complete = False
        if 'create_output_complete' not in st.session_state:
            st.session_state.create_output_complete = False
        try:    
            with st.form('input_form'):
                # PROJECT BOX
                col_left_prj_grid = grid(1, 2, 2, 2, 2, vertical_align="top")
                # Row 1:
                col_left_prj_grid.header("Project")
                # Row 2:
                col_left_prj_grid.text_input("Model Code", key="code")
                col_left_prj_grid.selectbox("PowerTrain", ['EV', 'e-Power', 'ICE'], key="pwt")
                # Row 3:
                col_left_prj_grid.selectbox("Case", ['CASE1', 'CASE1.5', 'CASE2'], key="case")
                col_left_prj_grid.selectbox("Plant", ['JPN', 'US', 'EUR', 'PRC'], key="plant")
                # Row 4:
                try:
                    list_group, notice = get_name_group(st.session_state.code)
                    list_group = ["ALL"] + list_group
                except:
                    list_group = ["ALL"]
                col_left_prj_grid.multiselect("Dev", list_group, default=["ALL"], key="dev")
                col_left_prj_grid.selectbox("Lot", ["ALL", 'DS', 'DC', 'PFC', 'VC', 'PT1', 'PT2'], key="lot")

                st.header("Spec box")
                files = st.file_uploader("", accept_multiple_files=True)
                col_left_spec_grid = grid(2, 2, vertical_align="top")
                set_data("running", 0)

                # ==============================================================================================================================
                if files is not None and col_left_spec_grid.form_submit_button("仕様表FORM",
                                                                            use_container_width=True) and get_data(
                    "running") == 0:
                    set_data("running", 1)
                    st.session_state.view_complete = False
                    st.session_state.load_complete = False
                    st.session_state.create_syo_complete = False
                    st.session_state.create_cadics_complete = False
                    st.session_state.create_output_complete = False
                    modal_create_form.open()
                # ==============================================================================================================================
                if col_left_spec_grid.form_submit_button("VIEW", use_container_width=True) and get_data(
                    "running") == 0:
                    set_data("running", 1)
                    st.session_state.load_complete = False
                    st.session_state.create_form_complete = False
                    st.session_state.create_syo_complete = False
                    st.session_state.create_cadics_complete = False
                    st.session_state.create_output_complete = False
                    modal_view.open()
                # ==============================================================================================================================

                if files is not None and col_left_spec_grid.form_submit_button("LOAD FILE",
                                                                           use_container_width=True) and get_data(
                    "running") == 0:
                    set_data("running", 1)
                    st.session_state.view_complete = False
                    st.session_state.create_syo_complete = False
                    st.session_state.create_form_complete = False
                    st.session_state.create_cadics_complete = False
                    st.session_state.create_output_complete = False
                    modal_load_file.open()            
                # ==============================================================================================================================
                if files is not None and col_left_spec_grid.form_submit_button("仕様表作成",
                                                                           use_container_width=True) and get_data(
                    "running") == 0:
                    set_data("running", 1)
                    set_data("link_2", "cadics_off_delete")
                    st.session_state.view_complete = False
                    st.session_state.load_complete = False
                    st.session_state.create_form_complete = False
                    st.session_state.create_cadics_complete = False
                    st.session_state.create_output_complete = False
                    modal_create_syo.open()

                if col_left_spec_grid.form_submit_button("CREATE CADICS",
                                                     use_container_width=True) and get_data("running") == 0:
                    set_data("running", 1)
                    st.session_state.view_complete = False
                    st.session_state.load_complete = False
                    st.session_state.create_form_complete = False
                    st.session_state.create_syo_complete = False
                    st.session_state.create_output_complete = False

                    modal_create_cadics.open()

                if col_left_spec_grid.form_submit_button("CREATE OUTPUTS", use_container_width=True) and get_data(
                        "running") == 0:
                    set_data("running", 1)
                    st.session_state.view_complete = False
                    st.session_state.load_complete = False
                    st.session_state.create_form_complete = False
                    st.session_state.create_syo_complete = False
                    st.session_state.create_cadics_complete = False
                    modal_create_output.open()

            if modal_load_file.is_open():
                with modal_load_file.container():
                    with st.spinner(text="In progress..."):
                        if len(files) > 0:
                            update_file_into_server_new(st.session_state.code, files, csrf_token)

                            notice = update_file_after_edit(st.session_state.code, st.session_state.pwt,
                                                        st.session_state.plant,
                                                        st.session_state.case, files, csrf_token,
                                                        st.session_state.name_user)
                            st.session_state.message_3 = notice
                            update_syo()
                            update_syo_form(files)
                            if 'message_5' in st.session_state:
                                del st.session_state['message_5']
                        else:
                            # st.error("file has not been uploaded yet!!!")
                            st.session_state.message_5 = "file has not been uploaded yet!!!"
                            if 'message_4' in st.session_state:
                                del st.session_state['message_4']
                            if 'message_10' in st.session_state:
                                del st.session_state['message_10']
                        st.session_state.load_complete = True
                        modal_load_file.close()
            if modal_view.is_open():
                with modal_view.container():
                    with st.spinner(text="In progress..."):
                        session, data, project_id, app_list = query_data(str(st.session_state.code).upper(),
                                                                     st.session_state.plant, st.session_state.pwt,
                                                                     st.session_state.case, st.session_state.dev,
                                                                     st.session_state.lot)
                        # st.write(data)
                        set_data("data_cadics", data)

                        list_file, folder_output, name_zip = check_file_out(st.session_state.code, st.session_state.pwt,
                                                                        st.session_state.plant, st.session_state.case)

                        data_syo, unique_list_max, unique_list_submax = querry_data_syo_hyo(st.session_state.code)
                        set_data("data_syo", data_syo)
                        set_data("device_group", unique_list_max)
                        set_data("device", unique_list_submax)
                        df_1, merged_df_4_optioncode, unique_list_max, unique_list_submax = update_and_querry_form_data()
                        form_df = pd.concat([df_1, merged_df_4_optioncode], axis=0)
                        form_df = form_df.fillna('')
                        form_df = form_df.drop(columns=['device_name'])
                        set_data("form", form_df)
                        st.session_state.view_complete = True
                        set_state(list_file, folder_output, name_zip)
                        set_state_db(session, project_id, app_list)
                        modal_view.close()

            if modal_create_form.is_open():
                with modal_create_form.container():
                    with st.spinner(text="In progress..."):
                        if files is not None and files != []:
                            code = str(st.session_state.code).lower()
                            if code not in str(files[0].name).lower() or 'Spec_List' not in files[0].name:
                                st.error("Model code or Spec incorrect")
                                st.session_state.message_6 = "Model code or Spec incorrect"
                                set_data("仕様表", frame_empty())
                            elif code == '':
                                st.error('Model code is blank')
                                st.session_state.message_6 = 'Model code is blank'
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
                                    st.session_state.message_6 = "Form Speclist is incorrect"
                                else:
                                    df_end_region3, data_for_create = main_process_spec_not_protected(files[0],
                                                                                                  str(st.session_state.code).upper())
                                    # st.write('df_end_region3: ', df_end_region3)
                                    merger_end, unique_list_max, unique_list_submax = add_function_from_admin(
                                        df_end_region3, files)
                                    merger_end = merger_end.reset_index(drop=True)
                                    set_data("device_group", unique_list_max)
                                    set_data("device", unique_list_submax)
                                    set_data('data_for_create', data_for_create)
                                # st.write('data_for_create: ', data_for_create[1:])
                                # merger_end = merger_end.astype(str)
                                    set_data("form+spec", merger_end)
                                    st.success("Create Completed!!!")
                                    st.session_state.message_6 = "Create Completed!!!"
                            # set_state()
                        else:
                            set_data("仕様表", frame_empty())
                            st.warning("file has not been uploaded yet")
                            st.session_state.message_6 = "file has not been uploaded yet"
                        set_data("running", 0)
                        st.session_state.create_form_complete = True
                        modal_create_form.close()

            if modal_create_syo.is_open():

                with modal_create_syo.container():
                    with st.spinner(text="In progress..."):
                        if not get_data("flag_check_fail") and get_data(
                                "flag_check_fail") is not None and 'data_frame_combine' in st.session_state:
                            if st.session_state.data_frame_combine.shape[1] > 4:
                                check_optioncode(st.session_state.data_frame_combine)

                                if not check_optioncode(st.session_state.data_frame_combine):
                                    # st.write('ok')
                                    if st.session_state.code != '':
                                        form_syo = create_syo(st.session_state.data_frame_combine,
                                                          get_data("data_for_create"))

                                        form_syo.replace({np.nan: ''}, inplace=True)
                                        # st.write('form_syo: ',form_syo)
                                        set_data("仕様表", form_syo)
                                        result_querry_region_4_gray, result_querry_region_4_blue = get_gray_blue(
                                            st.session_state.code)
                                        df, df_1 = dataframe_convert(form_syo, st.session_state.code,
                                                                 result_querry_region_4_gray,
                                                                 result_querry_region_4_blue)
                                        # st.write('df: ',df)
                                        # update_data_new_online(st.session_state.code, df, df_1)
                                        # if isinstance()
                                        update_data_new(st.session_state.code, df, df_1)
                                        set_data("link_1", "syo_hyo")
                                        set_data("link_syo", "syo_hyo")
                                        st.success("Completed")
                                        st.session_state.message_7 = 'Completed'
                                    else:
                                        st.warning("Model code can not be left blank")
                                        st.session_state.message_7 = 'Model code can not be left blank'
                                else:
                                    # st.write('OptionCode empty')
                                    st.session_state.message_7 = 'OptionCode empty'
                                    time.sleep(1.5)
                            else:
                                # st.write('ok')
                                st.warning("OptionCode empty")
                                st.session_state.message_7 = 'OptionCode empty'
                        else:
                            set_data("仕様表", frame_empty())
                            st.warning("Please create Form zxxx")
                            st.session_state.message_7 = 'Please create Form'
                            st.warning(st.session_state.message_7)
                        set_data("running", 0)
                        st.session_state.create_syo_complete = True
                        modal_create_syo.close()

            if modal_create_cadics.is_open():
                with modal_create_cadics.container():
                    with st.spinner(text="In progress..."):
                        notice, session, data, project_id, app_list = create_cadics_new(st.session_state.case,
                                                                                    st.session_state.plant,
                                                                                    st.session_state.pwt,
                                                                                    st.session_state.code,
                                                                                    st.session_state.dev)
                        # notice,session, data, project_id, app_list=[None,None,None,None,None]
                        set_data("data_cadics", data)
                        set_state_db(session, project_id, app_list)
                        list_file, folder_output, name_zip = check_file_out(st.session_state.code, st.session_state.pwt,
                                                                        st.session_state.plant, st.session_state.case)
                        set_state(list_file, folder_output, name_zip)
                        set_data("running", 0)
                        st.write("notice: ", notice)
                        st.session_state.message_8 = notice
                        st.session_state.create_cadics_complete = True
                        # modal_create_cadics.close()
            if modal_create_output.is_open():
                with modal_create_output.container():
                    with st.spinner(text="In progress..."):
                        notice = create_doc(st.session_state.case, st.session_state.plant, st.session_state.pwt,
                                        st.session_state.code)
                        list_file, folder_output, name_zip = check_file_out(st.session_state.code, st.session_state.pwt,
                                                                        st.session_state.plant, st.session_state.case)
                        set_state(list_file, folder_output, name_zip)
                        set_data("running", 0)
                    st.write(notice)
                    st.session_state.message_9 = notice
                    st.session_state.create_output_complete = True
                    modal_create_output.close()

            # ******************************************************
            if st.session_state.view_complete:
                if 'message_1' in st.session_state:
                    st.error(st.session_state.message_1)
                if 'Project' in st.session_state.message_2:
                    st.error(st.session_state.message_2)
                elif st.session_state.message_2 != '':
                    st.success(st.session_state.message_2)
            # ******************************************************
            if st.session_state.load_complete:
                if 'Completed' in st.session_state.message_3:
                    st.success(st.session_state.message_3)
                elif st.session_state.message_3 != '':
                    st.error(st.session_state.message_3)
                if 'message_4' in st.session_state:
                    if 'Update' in st.session_state.message_4:
                        st.success(st.session_state.message_4)
                        if 'message_10' in st.session_state:
                            del st.session_state['message_10']
                    elif st.session_state.message_4 != '':
                        st.error(st.session_state.message_4)
                if 'message_5' in st.session_state:
                    if 'Updated' in st.session_state.message_5:
                        st.success(st.session_state.message_5)
                    elif st.session_state.message_5 != '':
                        st.error(st.session_state.message_5)
                if 'message_10' in st.session_state:
                    if 'Updated' in st.session_state.message_10:
                        st.success(st.session_state.message_10)
                    else:
                        st.error(st.session_state.message_10)

            # ******************************************************
            if st.session_state.create_form_complete:
                if 'Completed!!!' in st.session_state.message_6:
                    st.success(st.session_state.message_6)
                else:
                    st.error(st.session_state.message_6)
            # ******************************************************
            if st.session_state.create_syo_complete:
                if 'message_7' in st.session_state:
                    if 'Completed' in st.session_state.message_7:
                        st.success(st.session_state.message_7)
                    else:
                        st.error(st.session_state.message_7)
            # ******************************************************
            if st.session_state.create_cadics_complete:
                if 'Completed' in st.session_state.message_8:
                    st.success(st.session_state.message_8)
                else:
                    st.warning(st.session_state.message_8)
            # ******************************************************
            if st.session_state.create_output_complete:
                if 'Completed' in st.session_state.message_9:
                    st.success(st.session_state.message_9)
                else:
                    st.warning(st.session_state.message_9)
            # ******************************************************
        except Exception as e:
            print(e)
            st.write(e)
            # st.write('st.session_state.selected_option: ',st.session_state.selected_option)
    with col_right:
        # BANNER RIGHT
        col_r1, col_r2 = st.columns([2, 1])
        with col_r1:
            st.markdown(
                '<h1 style="text-align: center;border: 2px solid #4CAF50; padding: 10px;">プロ管集約業務1本化システム</h1>',
                unsafe_allow_html=True)
            #    st.markdown(
        # '<h1 style="text-align: center;background-color: #CCE9D9;border: 2px solid #4CAF50; padding: 10px;">INPUT</h1>',
        # unsafe_allow_html=True)
        with col_r2:
            # st.markdown(f'<p style="text-align: center;">{st.session_state.name_user}.</p>', unsafe_allow_html=True)
            # st.markdown(f'<p style="text-align: center;">{st.session_state.position}</p>', unsafe_allow_html=True)
            st.markdown(
                f'<p style="text-align: center;'
                # f'background-color: #CCE9D9;'
                f'border: 2px solid #4CAF50; '
                f'padding: 10px">{st.session_state.name_user}<br>{st.session_state.position}</p>',
                unsafe_allow_html=True)
        view_prokan("admin")


def set_state(list_file, folder_output, name_zip):
    set_data("folder_output", folder_output)
    set_data("name_zip", name_zip)
    list_link = ["Car配車要望表", "WTC仕様用途一覧表", "WTC要望集約兼チェックリスト", "実験部品", "特性管理部品リスト",
                 "File Log"]
    for index in range(len(list_link)):
        set_data(list_link[index], list_file[index])
    set_data("flag_view", 1)


def set_state_db(session, project_id, app_list):
    set_data("session", session)
    set_data("project_id", project_id)
    set_data("app_list", app_list)
