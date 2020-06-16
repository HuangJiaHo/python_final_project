#---------import---------#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#------------------------#


#--------Variable--------#
year_bf_2000 = []
year_bf_2013 = []
year_bf_2019 = []
#------------------------#


#------Setting_font------#
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
#------------------------#


#------Read_csv_file-----#
data = pd.read_csv('歷年15歲以上民間人口之教育程度.csv')
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
        if int(year_split) == 2001:
            pos_2001 = i
        if int(year_split) == 2013:
            pos_2013 = i
        if int(year_split) == 2018:
            pos_2018 = i
        if int(year_split) == 2019:
            pos_2019 = i
        if int(year_split) <= 2000:
            year_bf_2000.append(year_split)
        if int(year_split) >= 2001 and int(year_split) <= 2013:
            year_bf_2013.append(year_split)
        if int(year_split) >= 2014 and int(year_split) <= 2019:
            year_bf_2019.append(year_split)
    except:
            None
#------------------------#
            
            
#--bf_2000_data_process--#
bf_2000_data = Original_data.copy()
bf_2000_data = bf_2000_data.iloc[:pos_2001]
bf_2000_data.iloc[0:, 0] = year_bf_2000
bf_2000_data.rename(columns={'按年月別分_Year_and_month': '年_Year'}, inplace=True)
bf_2000_data = bf_2000_data.set_index(bf_2000_data["年_Year"])
bf_2000_data = bf_2000_data.drop(["年_Year", "男_Male", "女_Female",                                  
                                  "國中及以下_男_Junior_high_and_below_Male",
                                  "國中及以下_女_Junior_high_and_below_Female",
                                  "國中及以下_國小及以下_小計_Junior_high_and_below_Primary_school_and_below_Total",
                                  "國中及以下_國小及以下_男_Junior_high_and_below_Primary_school_and_below_Male",
                                  "國中及以下_國小及以下_女_Junior_high_and_below_Primary_school_and_below_Female",
                                  "國中及以下_國中_小計_Junior_high_and_below_Junior_high_Total",
                                  "國中及以下_國中_男_Junior_high_and_below_Junior_high_Male",
                                  "國中及以下_國中_女_Junior_high_and_below_Junior_high_Female",
                                  "高中職_男_Senior_high_and_vocational_Male",
                                  "高中職_女_Senior_high_and_vocational_Female",
                                  "高中職_高中_男_Senior_high_and_vocational_Senior_high_Male",
                                  "高中職_高中_女_Senior_high_and_vocational_Senior_high_Female",
                                  "高中職_高職_男_Senior_high_and_vocational_Vocational_Male",
                                  "高中職_高職_女_Senior_high_and_vocational_Vocational_Female",
                                  "大專及以上_男_Junior_college_and_above_Male",
                                  "大專及以上_女_Junior_college_and_above_Female",
                                  "大專及以上_專科_男_Junior_college_and_above_Junior_college_Male",
                                  "大專及以上_專科_女_Junior_college_and_above_Junior_college_Female",
                                  "大專及以上_大學_男_Junior_college_and_above_University_Male",
                                  "大專及以上_大學_女_Junior_college_and_above_University_Female",
                                  "大專及以上_研究所_男_Junior_college_and_above_Graduate_school_Male",
                                  "大專及以上_研究所_女_Junior_college_and_above_Graduate_school_Female"                                
                                  ], axis=1)
bf_2000_data = bf_2000_data.replace({'-': 0})
#------------------------#


#--bf_2013_data_process--#
bf_2013_data = Original_data.copy()
bf_2013_data = bf_2013_data.iloc[pos_2001:pos_2013 + 1]
bf_2013_data.iloc[:pos_2013, 0] = year_bf_2013
bf_2013_data.rename(columns={'按年月別分_Year_and_month': '年_Year'}, inplace=True)
bf_2013_data = bf_2013_data.set_index(bf_2013_data["年_Year"])
bf_2013_data = bf_2013_data.drop(["年_Year", "男_Male", "女_Female",                                  
                                  "國中及以下_男_Junior_high_and_below_Male",
                                  "國中及以下_女_Junior_high_and_below_Female",
                                  "國中及以下_國小及以下_小計_Junior_high_and_below_Primary_school_and_below_Total",
                                  "國中及以下_國小及以下_男_Junior_high_and_below_Primary_school_and_below_Male",
                                  "國中及以下_國小及以下_女_Junior_high_and_below_Primary_school_and_below_Female",
                                  "國中及以下_國中_小計_Junior_high_and_below_Junior_high_Total",
                                  "國中及以下_國中_男_Junior_high_and_below_Junior_high_Male",
                                  "國中及以下_國中_女_Junior_high_and_below_Junior_high_Female",
                                  "高中職_男_Senior_high_and_vocational_Male",
                                  "高中職_女_Senior_high_and_vocational_Female",
                                  "高中職_高中_男_Senior_high_and_vocational_Senior_high_Male",
                                  "高中職_高中_女_Senior_high_and_vocational_Senior_high_Female",
                                  "高中職_高職_男_Senior_high_and_vocational_Vocational_Male",
                                  "高中職_高職_女_Senior_high_and_vocational_Vocational_Female",
                                  "大專及以上_男_Junior_college_and_above_Male",
                                  "大專及以上_女_Junior_college_and_above_Female",
                                  "大專及以上_專科_男_Junior_college_and_above_Junior_college_Male",
                                  "大專及以上_專科_女_Junior_college_and_above_Junior_college_Female",
                                  "大專及以上_大學_男_Junior_college_and_above_University_Male",
                                  "大專及以上_大學_女_Junior_college_and_above_University_Female",
                                  "大專及以上_研究所_男_Junior_college_and_above_Graduate_school_Male",
                                  "大專及以上_研究所_女_Junior_college_and_above_Graduate_school_Female"                                
                                  ], axis=1)
bf_2013_data = bf_2013_data.replace({'-': 0})
#------------------------#


#--bf_2019_data_process--#
bf_2019_data = Original_data.copy()
bf_2019_data = bf_2019_data.iloc[(pos_2013 + 1):pos_2019+1,]
bf_2019_data = bf_2019_data.drop(labels=range(41, 53))
bf_2019_data.iloc[:pos_2013, 0] = year_bf_2019
bf_2019_data.rename(columns={'按年月別分_Year_and_month': '年_Year'}, inplace=True)
bf_2019_data = bf_2019_data.set_index(bf_2019_data["年_Year"])
bf_2019_data = bf_2019_data.drop(["年_Year", "男_Male", "女_Female",                                  
                                  "國中及以下_男_Junior_high_and_below_Male",
                                  "國中及以下_女_Junior_high_and_below_Female",
                                  "國中及以下_國小及以下_小計_Junior_high_and_below_Primary_school_and_below_Total",
                                  "國中及以下_國小及以下_男_Junior_high_and_below_Primary_school_and_below_Male",
                                  "國中及以下_國小及以下_女_Junior_high_and_below_Primary_school_and_below_Female",
                                  "國中及以下_國中_小計_Junior_high_and_below_Junior_high_Total",
                                  "國中及以下_國中_男_Junior_high_and_below_Junior_high_Male",
                                  "國中及以下_國中_女_Junior_high_and_below_Junior_high_Female",
                                  "高中職_男_Senior_high_and_vocational_Male",
                                  "高中職_女_Senior_high_and_vocational_Female",
                                  "高中職_高中_男_Senior_high_and_vocational_Senior_high_Male",
                                  "高中職_高中_女_Senior_high_and_vocational_Senior_high_Female",
                                  "高中職_高職_男_Senior_high_and_vocational_Vocational_Male",
                                  "高中職_高職_女_Senior_high_and_vocational_Vocational_Female",
                                  "大專及以上_男_Junior_college_and_above_Male",
                                  "大專及以上_女_Junior_college_and_above_Female",
                                  "大專及以上_專科_男_Junior_college_and_above_Junior_college_Male",
                                  "大專及以上_專科_女_Junior_college_and_above_Junior_college_Female",
                                  "大專及以上_大學_男_Junior_college_and_above_University_Male",
                                  "大專及以上_大學_女_Junior_college_and_above_University_Female",
                                  "大專及以上_研究所_男_Junior_college_and_above_Graduate_school_Male",
                                  "大專及以上_研究所_女_Junior_college_and_above_Graduate_school_Female"                                
                                  ], axis=1)
bf_2019_data = bf_2019_data.replace({'-': 0})
#------------------------#


#------Save_to_csv-------#
bf_2000_data.to_csv('C:\\Users\\IRVING\\Desktop\\python_final_project\\15歲以上教育程度\\15歲以上教育程度_process_csv\\bf_2000.csv')
bf_2013_data.to_csv('C:\\Users\\IRVING\\Desktop\\python_final_project\\15歲以上教育程度\\15歲以上教育程度_process_csv\\bf_2013.csv')
bf_2019_data.to_csv('C:\\Users\\IRVING\\Desktop\\python_final_project\\15歲以上教育程度\\15歲以上教育程度_process_csv\\bf_2019.csv')
#------------------------#


#------Show_all_img------#
bf_2000_data.plot.bar(ylim=(0,20000))
bf_2013_data.plot.bar(ylim=(0,25000))
bf_2019_data.plot.bar(ylim=(0,30000))
plt.show()
#------------------------#

