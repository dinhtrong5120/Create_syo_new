import pandas as pd
import math


def check_key_spec_new(file_name):
    list_key_check_row_15 = ['Class', 'Attributes', 'Option Package', 'ZONE', 'BODY', 'ENGINE', 'AXLE', 'HANDLE',
                             'GRADE', 'TRANS', 'YEAR', 'INTAKE', 'SEAT/EQUIP', 'NUMBER']
    list_end = []
    df_ = pd.read_excel(file_name, header=None)
    list_key_word_1 = df_.iloc[14].tolist()
    list_key_word_1_processed = [x for x in list_key_word_1 if not (isinstance(x, float) and math.isnan(x))]
    name_column = df_.iloc[14].eq('NAME').idxmax()
    list_key_word_2 = df_.iloc[:, name_column].tolist()
    list_key_word_2_processed = [x for x in list_key_word_2 if not (isinstance(x, float) and math.isnan(x))]
    list_key_word = list_key_word_1_processed + list_key_word_2_processed
    dict_sub = {'file_name': None, 'Class': None, 'Attributes': None, 'Option Package': None, 'ZONE': None,
                'BODY': None, 'ENGINE': None, 'AXLE': None, 'HANDLE': None,
                'GRADE': None, 'TRANS': None, 'YEAR': None, 'INTAKE': None, 'SEAT/EQUIP': None, 'NUMBER': None}
    for item in list_key_check_row_15:
        if item not in list_key_word:
            if dict_sub['file_name'] is None:
                dict_sub['file_name'] = file_name.name
            dict_sub[item] = '✕'
    if list(set(dict_sub.values())) != [None]:
        list_end.append(dict_sub)
    df_output = pd.DataFrame(list_end)
    flg_check_fail = False
    if not df_output.empty:
        flg_check_fail = True
    return df_output, flg_check_fail


def check_syo(df_):
    list_error_ = []
    for item in ['auto', 'Gr', 'Keyword', 'CADICS ID']:
        if item not in df_.columns:
            list_error_.append(item)
    df_['CADICS ID'] = df_['CADICS ID'].str.strip()
    valid_df = df_[df_['CADICS ID'].notna() & (df_['CADICS ID'] != '')]
    duplicated_elements_ = valid_df[valid_df.duplicated('CADICS ID', keep=False)]['CADICS ID'].unique().tolist()
    return list_error_, duplicated_elements_


if __name__ == "__main__":
    df = pd.read_excel(r"C:\Users\KNT21617\Downloads\newken\project\data\input_syo\CAR 1.xlsx")
    print(df['CADICS ID'])
    list_error, duplicated_elements = check_syo(df)
    print(list_error, duplicated_elements)
