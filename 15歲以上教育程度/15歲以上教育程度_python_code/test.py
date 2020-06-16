'''
for i in range(row_len):
    try:
        year_all = Original_data.iloc[i,0].split(',', 1)[1]
    except:
            None
    if int(year_all) < 2001:
        year_bf_2001.append(year_all)
print(year_bf_2001)
'''
#target = target.set_index(target["按年月別分_Year_and_month"])

