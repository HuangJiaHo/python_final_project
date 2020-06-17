#---------import---------#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#------------------------#


#--------Variable--------#

#------------------------#


#------Setting_font------#
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
#------------------------#


#------Read_csv_file-----#
data = pd.read_csv('C:\\Users\\IRVING\\Desktop\\python_final_project\\data\\考試人數.txt')
Original_data = pd.DataFrame(data)
#------------------------#

            
#------num_of_people-----#
num_of_people = Original_data.copy()
num_of_people = num_of_people.iloc[0:]
num_of_people = num_of_people.set_index(num_of_people["年度"])
num_of_people = num_of_people.drop(["年度"], axis=1)

'''
#------Save_to_csv-------#
Senior_high_compare.to_csv('C:\\Users\\IRVING\\Desktop\\python_final_project\\15歲以上教育程度\\15歲以上教育程度_process_csv\\升高中與高職的比例變化\\Senior_high_compare.csv')
#------------------------#
'''
print(num_of_people)
#------Show_all_img------# 
num_of_people.plot(fontsize=15, lw=7)
plt.xticks(np.arange(2001, 2020, step = 1))
plt.title("國中生參加考試人數變化 2001年 ~ 2019年", fontsize=50)
plt.legend(loc='upper left', fontsize=15)
plt.xlabel('年度', fontsize=25)
plt.ylabel('人數', fontsize=25)
plt.show()
#------------------------#
