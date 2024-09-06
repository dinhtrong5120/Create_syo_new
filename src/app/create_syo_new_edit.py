import re
import pandas as pd
from src.app.edit_syo_new import logic_add, process_dataframe
from src.app.check_filed_information import normalize_japanese_text


def create_syo(form_syo, data_for_create):
    # form_syo.to_excel(fr"C:\Users\KNT21617\Documents\New folder (3)\30_8_2024\form_syo_3008.xlsx", index=False)
    class_option = ''
    value_in_cadics_columns = ''
    value_in_auto_columns = ''
    data_spec, col_option, col_start_config, col_attribute, col_option_code, col_end_config = data_for_create
    # data_spec.to_excel(fr"C:\Users\KNT21617\Documents\New folder (3)\30_8_2024\data_spec_3008.xlsx", index=False)
    form_syo = form_syo.fillna("")
    data_spec = data_spec.fillna("")
    data_spec = data_spec.applymap(lambda x: normalize_japanese_text(x) if isinstance(x, str) else x)
    form_syo = form_syo.applymap(lambda x: normalize_japanese_text(x) if isinstance(x, str) else x)
    form_syo = form_syo.reset_index(drop=True)

    df_insert = form_syo[['group_key_map', 'default']]
    form_syo = form_syo.drop(columns=['group_key_map', 'default'])

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
        keyword_col_C = form_syo["keyword"][index]
        keyword_col_C = keyword_col_C.replace('\n', "")
        if keyword_col_C == '':
            value_in_cadics_columns = form_syo["CADICS ID"][index].upper()
            value_in_auto_columns = form_syo["auto"][index].upper()
            if value_in_cadics_columns == '' and value_in_auto_columns != '':
                class_option = form_syo["auto"][index].upper()
        else:
            if keyword_col_C == 'ALL' or keyword_col_C == 'w,w/o':
                LIST_HIENTHI = ["w", "w/o"]
                if keyword_col_C == 'ALL':
                    LIST_HIENTHI = ["ALL", "-"]

                option = form_syo["CADICS ID"][index].upper()
                nhap(form_syo, data_spec, index, col_option, dict_option_code, col_start_config, col_end_config,
                     col_option_code, col_attribute, column_name, class_option, option, LIST_HIENTHI)
            elif '(ALL)' in keyword_col_C or '(w,w/o)' in keyword_col_C:
                LIST_HIENTHI = ["w", "w/o"]
                if '(ALL)' in keyword_col_C:
                    LIST_HIENTHI = ["ALL", "-"]
                option = keyword_col_C.replace("(ALL)", "")
                option = option.replace("(w,w/o)", "").upper()
                nhap(form_syo, data_spec, index, col_option, dict_option_code, col_start_config, col_end_config,
                     col_option_code, col_attribute, column_name, class_option, option, LIST_HIENTHI)
            else:
                parts = custom_split(keyword_col_C)
                for item in parts:
                    item = item.strip()
                    try:
                        result_yes = re.search(r'\(([^()]+)\)$', item).group(1)
                        result_yes_split = result_yes.split(",")
                        if len(result_yes_split) == 1:
                            LIST_HIENTHI = [result_yes_split[0], "-"]
                        else:
                            LIST_HIENTHI = [result_yes_split[0], result_yes_split[1]]
                        option = re.sub(r'\([^()]+\)$', '', item).strip().upper()

                        nhap(form_syo, data_spec, index, col_option, dict_option_code, col_start_config, col_end_config,
                             col_option_code, col_attribute, column_name, class_option, option, LIST_HIENTHI)

                    except:
                        LIST_HIENTHI = [item, "-"]
                        option = item.strip().upper()
                        nhap(form_syo, data_spec, index, col_option, dict_option_code, col_start_config,
                             col_end_config,
                             col_option_code, col_attribute, column_name, class_option, option, LIST_HIENTHI)
    df_combined = pd.concat([form_syo, df_insert], axis=1)
    # df_1 = logic_add(df_combined)
    df_2 = process_dataframe(df_combined)
    return df_2


def custom_split(s):
    parts = []
    in_parentheses = False
    current_part = ""

    for char in s:
        if char == "(":
            in_parentheses = True
        elif char == ")":
            in_parentheses = False

        if char == "," and not in_parentheses:
            parts.append(current_part)
            current_part = ""
        else:
            current_part += char

    parts.append(current_part)

    return parts


def nhap(form_syo, data_spec, index, col_option, dict_option_code, col_start_config, col_end_config,
         col_option_code, col_attribute, column_name, class_option, option, LIST_HIENTHI):
    result = data_spec[data_spec[col_option] == option]
    if len(result) > 0:  # Case option is found
        result = result.reset_index(drop=True)
        list_data = option_in_A(result, dict_option_code, col_start_config, col_end_config,
                                col_option_code, col_attribute, 1)
        if LIST_HIENTHI != ["ALL", "-"]:
            replacement_value = LIST_HIENTHI[0]
            for i in range(len(list_data)):
                if list_data[i] != '-' and list_data[i] != '' and ':' not in list_data[i]:
                    list_data[i] = replacement_value
                else:
                    try:
                        if list_data[i] != '' and ':' not in list_data[i]:
                            list_data[i] = LIST_HIENTHI[1]
                        if ':' in list_data[i]:
                            list_data[i] = ''
                    except:
                        pass
    else:
        result = data_spec[data_spec[column_name[-1]] == class_option]  # 1 là cột class
        if LIST_HIENTHI == ["ALL", "-"]:
            LIST_HIENTHI = ["w", "w/o"]
        list_data = option_in_D(option, result, dict_option_code, col_start_config, col_end_config,
                                col_option_code, col_attribute, col_option, LIST_HIENTHI)
    col_start = 4

    for item in list_data:

        try:
            if form_syo.iat[index, col_start] == "" or form_syo.iat[index, col_start] == "-":
                form_syo.iat[index, col_start] = item
        except:
            form_syo[col_start] = ''
            form_syo.iat[index, col_start] = item
        finally:
            col_start = col_start + 1


def option_in_A(result, dict_option_code, col_start_config, col_end_config,
                col_option_code, col_attribute, flag):
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
                if isinstance(option_code, str) and option_code != "":
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
                col_option_code, col_attribute, col_option, LIST_HIENTHI):
    list_vip = []
    if '✚' in attribute or '+' in attribute:
        list_attribute = re.split(r"[✚+]", attribute)
        dict_check = {}
        dict_check_1 = {}
        for item in list_attribute:
            filter_attribute = result[result[col_attribute].str.contains(item, regex=False, na=False)]
            if len(filter_attribute) > 0:

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
                            dict_check[config] = dict_check[config] + "+" + value
                for config_1, value_1 in dict_check.items():
                    if item in value_1:
                        if item not in list_vip:
                            list_vip.append(item)
                        if len(list_vip) == 1:
                            dict_check_1[config_1] = item
                        elif len(list_vip) > 1:
                            dict_check_1[config_1] += ('✚' + item)
                    else:
                        dict_check_1[config_1] = '-'

            else:
                list_data = [LIST_HIENTHI[1]] * (col_end_config - col_start_config)
                return list_data
        list_data = list(dict_check_1.values())
        if LIST_HIENTHI == ['w', 'w/o']:
            for i in range(len(list_data)):
                if list_data[i] != '-' and list_data[i] != '' and ':' not in list_data[i]:
                    list_data[i] = LIST_HIENTHI[0]
                if list_data[i] == '-':
                    list_data[i] = LIST_HIENTHI[1]
                if ':' in list_data[i]:
                    list_data[i] = ''
        return list_data

    else:
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
                    dict_check[config] = LIST_HIENTHI[0]
                else:
                    dict_check[config] = LIST_HIENTHI[1]

            list_data = list(dict_check.values())

        else:
            list_data = [LIST_HIENTHI[1]] * (col_end_config - col_start_config)
        return list_data


if __name__ == '__main__':
    # a = ['Sheet1', 'Sheet2', 'Sheet3', 'Sheet4']
    a = ['Sheet1']
    data_spec = pd.read_excel(r"C:\Users\KNT21617\Documents\New folder (3)\30_8_2024\data_spec_3008.xlsx",
                              sheet_name='Sheet1')
    for sheet in a:
        form_syo = pd.read_excel(r"C:\Users\KNT21617\Documents\New folder (3)\30_8_2024\form_syo_3008.xlsx",
                                 sheet_name=sheet)
        data_for_create = [data_spec, 1, 9, 6, 8, 29]
        df = create_syo(form_syo, data_for_create)
        df.to_excel(fr"C:\Users\KNT21617\Documents\New folder (3)\30_8_2024\output\{sheet}_web.xlsx", index=False)
