import pandas as pd

"""fuction:check_optioncode_from_syo
-Description: Check OptionCode Name and OptionCode taked maru ? 
-Input: df_ (dataframe)
-Output: boolean 
"""


def check_optioncode(df_):
    opt_index = df_.index[df_['CADICS ID'] == 'OptionCode'].values[0]
    conf_columns = ['CADICS ID'] + [col for col in df_.columns if col.startswith('conf-')]
    # df_end = df_.loc[opt_index + 1:, conf_columns]
    first_row = df_.loc[opt_index, conf_columns]
    contains_non_nan = first_row[conf_columns].notna().any()
    if not contains_non_nan:
        # return "There isn't any OptionCode name"
        return False
    return True


if __name__ == '__main__':
    file_path = r"C:\Users\KNT21617\Downloads\newken\仕様表\仕様表_PZ1K_copy - Copy.xlsx"
    df = pd.read_excel(file_path)
    results = check_optioncode(df)
    print(results)
