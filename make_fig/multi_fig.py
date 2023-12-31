""" 
used for muilt file to temperature fig
 """
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from scipy.interpolate import make_interp_spline
import os
from numpy import mean


def find_min_len_of_sec_dementia( Temps ):
    lens_temp=[]
    for i in range(len(Temps)):
        lens_temp.append(len(Temps[len(Temps)-i-1]))
    min_lenvalue = min(lens_temp) # 求列表最小值
    max_lenvalue = max(lens_temp) # 求列表最大值
    return min_lenvalue


def find_txt_file_in_now_dir( filename ):
    datanames = os.listdir()
    for dataname in datanames:
        if os.path.splitext(dataname)[1] == '.txt':#目录下包含.txt的文件
            filename.append(dataname) 
    filename.sort() #乱序问题进行解决          
    #print(filename)

def extract_info(filename,Temps):
    for file in filename:
        with open(file, 'r') as f:
            lines = f.readlines()
            temp=[]
            for line in lines:
                if "温度" in line:
                    valuee = line.split()
                    temp1=float(valuee[1][0:5])/1000
                    temp.append(temp1)
            Temps.append(temp)

def bar_with_date(Temps,filename):
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 显示中文
    mean_temp=[]
    print("---------------")
    for i in range(len(Temps)):
        if len(Temps[i])<10:
            mean_temp.append(Temps[i][-1])
        else:
            mean_temp.append(mean(Temps[i][-15:]))
        print("item"+str(i)+":"+filename[i])
        filename[i]=str(i)
        #print((mean_temp[i]))

    print("---------------")
    width = 0.5  # 柱体宽度
    plt.bar(filename, mean_temp, width,label='temp')
    for a,b,i in zip(filename,mean_temp,range(len(filename))): # zip 函数
        plt.text(a,b+0.13,"%.2f"%mean_temp[i],ha='center') # plt.text 函数
       
    plt.xlabel('测试项目编号')
    plt.ylabel('温度/℃')
    plt.title('温度稳态结果')
    #plt.legend()
    plt.show()


def process_fig(Temps,filename):
    min_lenvalue=find_min_len_of_sec_dementia(Temps)
    Counts_out=[x for x in range(min_lenvalue)]
    for i in range(len(Temps)):
        Temps_out=Temps[len(Temps)-i-1][0:min_lenvalue]
        plt.plot(Counts_out,Temps_out,ls = "-",lw = 2,label=filename[i])
    plt.legend()
    plt.show()

def run():
    Temps=[]
    filename=[]
    find_txt_file_in_now_dir(filename)
    extract_info(filename,Temps)
    #process_fig(Temps,filename)
    bar_with_date(Temps,filename)

    
if __name__ == '__main__':
    run()
