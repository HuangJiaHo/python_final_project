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
data = pd.read_csv('C:\\Users\\IRVING\Desktop\\python_final_project\\data\\歷年15歲以上民間人口之教育程度.csv')
Original_data = pd.DataFrame(data)
#------------------------#


#------Data_position-----#
row_len = len(Original_data.iloc[0:])

for i in range(row_len):
    try:
        year_split = Original_data.iloc[i, 0].split(',', 1)[1]
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

            
#---Senior_high_compare_MF--#
Senior_high_compare_MF = Original_data.copy()
Senior_high_compare_MF = Senior_high_compare_MF.iloc[pos_1978:]
Senior_high_compare_MF = Senior_high_compare_MF.drop(labels=range(41, 53))
Senior_high_compare_MF = Senior_high_compare_MF.drop(labels=(range(54, 66)))
Senior_high_compare_MF.iloc[0:, 0] = year_af_1978
Senior_high_compare_MF.rename(columns={'按年月別分_Year_and_month': '年_Year'}, inplace=True)
Senior_high_compare_MF = Senior_high_compare_MF.set_index(Senior_high_compare_MF["年_Year"])
Senior_high_compare_MF = Senior_high_compare_MF.drop(["年_Year", "總計_Total","男_Male", "女_Female",
                                  "國中及以下_合計_Junior_high_and_below_Total",
                                  "國中及以下_男_Junior_high_and_below_Male",
                                  "國中及以下_女_Junior_high_and_below_Female",
                                  "國中及以下_國小及以下_小計_Junior_high_and_below_Primary_school_and_below_Total",
                                  "國中及以下_國小及以下_男_Junior_high_and_below_Primary_school_and_below_Male",
                                  "國中及以下_國小及以下_女_Junior_high_and_below_Primary_school_and_below_Female",
                                  "國中及以下_國中_小計_Junior_high_and_below_Junior_high_Total",
                                  "國中及以下_國中_男_Junior_high_and_below_Junior_high_Male",
                                  "國中及以下_國中_女_Junior_high_and_below_Junior_high_Female",
                                  "高中職_合計_Senior_high_and_vocational_Total",
                                  "高中職_高中_小計_Senior_high_and_vocational_Senior_high_Total",
                                  "高中職_高職_小計_Senior_high_and_vocational_Vocational_Total",
                                  "大專及以上_合計_Junior_college_and_above_Total",
                                  "大專及以上_男_Junior_college_and_above_Male",
                                  "大專及以上_女_Junior_college_and_above_Female",
                                  "大專及以上_專科_小計_Junior_college_and_above_Junior_college_Total",
                                  "大專及以上_專科_男_Junior_college_and_above_Junior_college_Male",
                                  "大專及以上_專科_女_Junior_college_and_above_Junior_college_Female",
                                  "大專及以上_大學_小計_Junior_college_and_above_University_Total",
                                  "大專及以上_大學_男_Junior_college_and_above_University_Male",
                                  "大專及以上_大學_女_Junior_college_and_above_University_Female",
                                  "大專及以上_研究所_小計_Junior_college_and_above_Graduate_school_Total",
                                  "大專及以上_研究所_男_Junior_college_and_above_Graduate_school_Male",
                                  "大專及以上_研究所_女_Junior_college_and_above_Graduate_school_Female"                                
                                  ], axis=1)
try:
    Senior_high_compare_MF = Senior_high_compare_MF.replace({'-': 0})
except:
        None

Senior_high_compare_MF = Senior_high_compare_MF.reindex(columns=['高中職_男_Senior_high_and_vocational_Male',
                                                                 '高中職_高中_男_Senior_high_and_vocational_Senior_high_Male',
                                                                 '高中職_高職_男_Senior_high_and_vocational_Vocational_Male',
                                                                 '高中職_女_Senior_high_and_vocational_Female',
                                                                 '高中職_高中_女_Senior_high_and_vocational_Senior_high_Female',
                                                                 '高中職_高職_女_Senior_high_and_vocational_Vocational_Female'])
#------------------------#


#------Save_to_csv-------#
Senior_high_compare_MF.to_csv('C:\\Users\\IRVING\\Desktop\\python_final_project\\15歲以上教育程度\\15歲以上教育程度_process_csv\\升高中與高職的比例變化\\男女升高中及高職的比例變化\\Senior_high_compare_MF.csv')
#------------------------#


#------Show_all_img------#
for i in range(0, 42, 2):
    year_af_1978_xticks.append(year_af_1978[i])
Senior_high_compare_MF.plot.bar(ylim=(0,4000), fontsize=15)
plt.xticks(np.arange(0, 42, step = 2), year_af_1978_xticks)
plt.yticks(np.arange(0,4500, step = 500))
plt.title("男女升高中職的比例 1978年 ~ 2019年", fontsize=50)
plt.legend(loc='upper left', fontsize=15)
plt.xlabel('年度', fontsize=25)
plt.ylabel('人數', fontsize=25)
plt.show()

#------------------------#