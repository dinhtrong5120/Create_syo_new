# import streamlit as st
# import pandas as pd
#
# A = ['default', 'cat', 'dog', 'bird', 'ppp']
# df = pd.DataFrame({'A': [True, False, True], 'B': ['cat', 'cat', 'dog']})
# df['B'] = df['B'].astype(pd.CategoricalDtype(A))
#
# df_1 = st.data_editor(df, num_rows='dynamic')
#
# st.write(df_1)
#
#
#
#
# data_df = pd.DataFrame(
#     {
#         "category": [
#             "📊 Data Exploration",
#             "📈 Data Visualization",
#             "🤖 LLM",
#             "📊 Data Exploration",
#         ],
#     }
# )
#
# st.data_editor(
#     data_df,
#     column_config={
#         "category": st.column_config.SelectboxColumn(
#             "App Category",
#             help="The category of the app",
#             width="medium",
#             options=[
#                 "📊 Data Exploration",
#                 "📈 Data Visualization",
#                 "🤖 LLM",
#                 1,
#             ],
#             required=True,
#         )
#     },
#     hide_index=True,
#     num_rows='dynamic'
# )
