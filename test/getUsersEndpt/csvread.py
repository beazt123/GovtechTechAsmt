import pandas as pd

# csv.reader(
#     "success.csv", 
#     delimiter=',', 
#     skipinitialspace= True, 
#     strict=True
#     )

df = pd.read_csv('success.csv',
    sep=',',     # field separator
    comment='#', # comment
    header=0,
    skipinitialspace=True,
    skip_blank_lines=True,
    error_bad_lines=True,
    warn_bad_lines=True
    ).sort_index()
print(df)
# print(df.index)
# print(df.columns)