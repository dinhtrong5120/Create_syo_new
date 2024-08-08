import pandas as pd
# import time

# import streamlit
from src.app.edit_syo_new import logic_add, process_dataframe


def create_syo(form_syo, data_for_create):
                        # global class_option
    data_spec, col_option, col_start_config, col_attribute, col_option_code, col_end_config = data_for_create
    form_syo = form_syo.fillna("")
                        # form_syo.to_excel(r'C:\Users\KNT21617\Documents\New folder (3)\form_syo_1.xlsx')
    data_spec = data_spec.fillna("")
                        # data_spec.to_excel(r'C:\Users\KNT21617\Documents\New folder (3)\data_spec_1.xlsx')
                        # Kết hợp các biến thành một chuỗi
                        # content = f"{col_option}, {col_start_config}, {col_attribute}, {col_option_code}, {col_end_config}"
                        # Tên file để ghi
                        # # file_name = r"C:\Users\KNT21617\Documents\New folder (3)\output_1.txt"
                        #
                        # # Mở file để ghi
                        # with open(file_name, 'w') as file:
                        #     file.write(content)
    form_syo = form_syo.reset_index(drop=True)
    # streamlit.write('data_spec: ', data_spec)

    df_insert = form_syo[['group_key_map', 'default']]
    # streamlit.write('df_insert: ', df_insert)
    form_syo = form_syo.drop(columns=['group_key_map', 'default'])
    # streamlit.write('form_syo: ', form_syo)




    column_name = list(range(data_spec.shape[1]))
    data_spec.columns = column_name

    col_option = col_option - 1
    col_start_config = col_start_config  # in spec
    col_end_config = col_end_config  # in spec
    col_option_code = col_option_code - 1  # in spec
    col_attribute = col_attribute - 1  # in spec

    dict_option_code = {}
    # Determine the starting point
    index_start = form_syo[form_syo["auto"] == "X01_VISIBILITY"].index
    index_option_code = form_syo[form_syo["CADICS ID"] == "OptionCode"].index

    # Determine optioncode
    for index in range(4, len(form_syo.columns)):
        config = form_syo.columns[index]
        header = form_syo.columns[index]
        dict_option_code[config] = str(form_syo[header][int(index_option_code[0])])

    for index in range(int(index_start[0]), index_option_code[0]):
        option = form_syo["CADICS ID"][index]
        # Determine class_option
        if len(option) == 0:
            class_option = form_syo["auto"][index]
        else:
            # Search option in column A in Speclist
            result = data_spec[data_spec[col_option] == option]
            if len(result) > 0:  # Case option is found
                result = result.reset_index(drop=True)
                list_data = option_in_A(result, dict_option_code, col_start_config, col_end_config,
                                        col_option_code, col_attribute, 1)
            else:
                # Search option in column D in Speclist
                result = data_spec[data_spec[column_name[-1]] == class_option]  # 1 là cột class
                list_data = option_in_D(option, result, dict_option_code, col_start_config, col_end_config,
                                        col_option_code, col_attribute, col_option)

            col_start = 4
            for item in list_data:
                try:
                    form_syo.iat[index, col_start] = item
                except:
                    form_syo[col_start] = None
                    form_syo.iat[index, col_start] = item
                finally:
                    col_start = col_start + 1

    df_combined = pd.concat([form_syo, df_insert], axis=1)
    df_1 = logic_add(df_combined)
    df_2 = process_dataframe(df_1)
    return df_2


def option_in_A(result, dict_option_code, col_start_config, col_end_config,
                col_option_code, col_attribute, flag):
    # gia lap ca tham so dau vao
    # col_start_config=9    #in spec
    # col_end_config=15     #in spec
    # col_option_code=7     #in spec
    # col_attribute=5       #in spec
    # =========================

    dict_config_value = {}
    list_option_code_all = []
    list_attribute = []
    index_config = 1
    for address_config in range(col_start_config, col_end_config):

        if index_config < 10:
            config = "conf-00" + str(index_config)
        if 9 < index_config < 100:
            config = "conf-0" + str(index_config)

        list_option_code = []
        index_attribute_o = result[result[address_config] == "Opt."].index
        attribute = "-"
        # =============================Get optioncode===================================
        if len(index_attribute_o) > 0:
            for index in range(len(index_attribute_o)):
                option_code = result[col_option_code][index_attribute_o[index]]
                if isinstance(option_code, str):
                    list_option_code.append(option_code)
            # =============================== Case ==========================================

            syo_option_code = str(dict_option_code[config]).split(",")
            has_option = set(list_option_code).issubset(set(syo_option_code))
            if has_option:
                list_option_code_all = list_option_code_all + list_option_code
                attribute = result[col_attribute][index_attribute_o[0]]
                if attribute not in list_attribute:
                    list_attribute.append(attribute)

        if attribute == "-":
            index_attribute_d = result[result[address_config] == "D"].index

            if len(index_attribute_d) > 0:
                attribute = result[col_attribute][index_attribute_d[0]]
                if attribute not in list_attribute and attribute != "-":
                    list_attribute.append(attribute)
            else:
                index_attribute_s = result[result[address_config] == "S"].index
                if len(index_attribute_s) > 0:
                    attribute = result[col_attribute][index_attribute_s[0]]
                if attribute not in list_attribute and attribute != "-":
                    list_attribute.append(attribute)

        index_config = index_config + 1
        dict_config_value[config] = attribute

    # Convert Attribute to S, S2, S3 .....
    if flag == 1:
        for config, attribute in dict_config_value.items():
            if attribute != "-":
                index = list_attribute.index(attribute)
                dict_config_value[config] = "S" + str(index + 1)

        for index in range(len(list_attribute)):
            list_attribute[index] = "S" + str(index + 1) + ": " + str(list_attribute[index])

        list_option_code_all = list(dict.fromkeys(list_option_code_all))
        comment_option = str(list_option_code_all)
        for sys in ["[", "]", "'"]:
            comment_option = comment_option.replace(sys, "")
        list_attribute.insert(0, comment_option)

        values_list = list(dict_config_value.values())
        list_data = values_list + list_attribute
        return list_data
    else:
        return dict_config_value

def option_in_D(attribute, result, dict_option_code, col_start_config, col_end_config,
                col_option_code, col_attribute, col_option):
    # gia lap ca tham so dau vao
    # col_start_config=9    #in spec
    # col_end_config=15     #in spec
    # col_option_code=7     #in spec
    # col_attribute=5       #in spec
    # col_option=2          #in spec
    # =========================

    filter_attribute = result[result[col_attribute].str.contains(attribute, regex=False, na=False)]
    if len(filter_attribute) > 0:
        dict_check = {}
        list_option = filter_attribute[col_option].dropna().unique()

        for option in list_option:
            sub_result = result[result[col_option] == option]
            sub_result = sub_result.reset_index(drop=True)

            dict_config_value = option_in_A(sub_result, dict_option_code, col_start_config, col_end_config,
                                            col_option_code, col_attribute, 0)

            for config, value in dict_config_value.items():
                if config not in dict_check.keys():
                    dict_check[config] = value
                else:
                    dict_check[config] = dict_check[config] + " + " + value

        for config, value in dict_check.items():

            if attribute in value:
                dict_check[config] = "w"
            else:
                dict_check[config] = "w/o"

        list_data = list(dict_check.values())

    else:
        list_data = ["-"] * (col_end_config - col_start_config)
    return list_data


if __name__ == '__main__':
    form_syo = pd.read_excel(r'C:\Users\KNT21617\Documents\New folder (3)\form_syo.xlsx')
    data_spec = pd.read_excel(r'C:\Users\KNT21617\Documents\New folder (3)\data_spec.xlsx')
    data_for_create = [data_spec, 1, 9, 6, 8, 29]
    df = create_syo(form_syo, data_for_create)
    df.to_excel(r'C:\Users\KNT21617\Documents\New folder (3)\dataxxx.xlsx',index=False)
