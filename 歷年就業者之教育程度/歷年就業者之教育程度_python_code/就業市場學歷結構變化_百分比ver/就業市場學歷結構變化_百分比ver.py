#---------import---------#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#------------------------#


#--------Variable--------#
year_af_1978 = []
year_af_1978_xticks = []
year_bf_2000 = []
year_bf_2013 = []
year_bf_2019 = []
#------------------------#


#------Setting_font------#
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
#------------------------#


#------Read_csv_file-----#
data = pd.read_csv('C:\\Users\\IRVING\\Desktop\\python_final_project\\data\\問題三.csv')
Original_data = pd.DataFrame(data)
#------------------------#


#------Data_position-----#
row_len = len(Original_data.iloc[0:])

for i in range(row_len):
    try:
        year_split = Original_data.iloc[i, 0]
    except:
            year_split = None
    try:
        if int(year_split) == 1978:
            pos_1978 = i
        if int(year_split) == 2001:
            pos_2001 = i
        if int(year_split) == 2013:
            pos_2013 = i
        if int(year_split) == 2018:
            pos_2018 = i
        if int(year_split) == 2019:
            pos_2019 = i
        if int(year_split) >= 1978:
            year_af_1978.append(year_split)
        if int(year_split) <= 2000:
            year_bf_2000.append(year_split)
        if int(year_split) >= 2001 and int(year_split) <= 2013:
            year_bf_2013.append(year_split)
        if int(year_split) >= 2014 and int(year_split) <= 2019:
            year_bf_2019.append(year_split)
    except:
            None
#------------------------#
           
#---Senior_high_compare--#
Senior_high_compare = Original_data.copy()
Senior_high_compare = Senior_high_compare.iloc[pos_1978:]
Senior_high_compare = Senior_high_compare.set_index(Senior_high_compare["年份"])
Senior_high_compare = Senior_high_compare.drop(["年份"], axis=1)
try:
    Senior_high_compare['國中及以下佔就業人口比率'] = Senior_high_compare['國中及以下佔就業人口比率'].map(lambda x: str(x)[:-1])
    Senior_high_compare['高中佔就業人口比率'] = Senior_high_compare['高中佔就業人口比率'].map(lambda x: str(x)[:-1])
    Senior_high_compare['高職佔就業人口比率'] = Senior_high_compare['高職佔就業人口比率'].map(lambda x: str(x)[:-1])
    Senior_high_compare['專科佔就業人口比率'] = Senior_high_compare['專科佔就業人口比率'].map(lambda x: str(x)[:-1])
    Senior_high_compare['大學佔就業人口比率'] = Senior_high_compare['大學佔就業人口比率'].map(lambda x: str(x)[:-1])
    Senior_high_compare['研究所佔就業人口比率'] = Senior_high_compare['研究所佔就業人口比率'].map(lambda x: str(x)[:-1])
    Senior_high_compare = Senior_high_compare.replace({'-': 0})
    Senior_high_compare=Senior_high_compare.astype(float)
except:
        None    
''' 
#------Save_to_csv-------#
Senior_high_compare.to_csv('C:\\Users\\IRVING\\Desktop\\python_final_project\\15歲以上教育程度\\15歲以上教育程度_process_csv\\升高中與高職的比例變化\\Senior_high_compare.csv')
#------------------------#
'''
 
#------Show_all_img------# 
Senior_high_compare.plot.barh(stacked = True, xlim = (0, 100), fontsize=15)
plt.yticks(np.arange(0, 42, step = 1))
plt.xticks(np.arange(0, 110, step = 10))
plt.title("就業市場學歷結構變化 1978年 ~ 2019年", fontsize=50)
plt.legend(loc='best', fontsize=15, facecolor='white', framealpha=1)
plt.xlabel('占比率 %', fontsize=25)
plt.ylabel('年度', fontsize=25)
plt.show()
#------------------------#

