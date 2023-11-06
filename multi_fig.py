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
    #print(filename)


def extract_txt_info(filename,Counts,Temps):
    for file in filename:
        with open(file, 'r') as f:
            lines = f.readlines()
            count = 0
            temp=[]
            counts=[]
            for line in lines:
                count +=1
                if count%19 ==17:
                    valuee = line.split()
                    temp1=float(valuee[1][0:5])/1000
                    temp.append(temp1)
                    counts.append(int(count/19+1))
            Counts.append(counts)
            Temps.append(temp)


def bar_with_date(Temps,filename):
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 显示中文
    mean_temp=[]
    for i in range(len(Temps)):
        mean_temp.append(mean(Temps[i][-10:]))
        print(str(i)+":"+filename[i])
        filename[i]=str(i)
    width = 0.5  # 柱体宽度
    plt.bar(filename, mean_temp, width,label='temp')
    for a,b,i in zip(filename,mean_temp,range(len(filename))): # zip 函数
        plt.text(a,b+0.13,"%.2f"%mean_temp[i],ha='center') # plt.text 函数
       
    plt.xlabel('测试项目编号')
    plt.ylabel('温度/℃')
    plt.title('温度稳态结果')
    plt.legend()
    plt.show()


def process_fig(Temps,filename,Counts):
    Counts_out=[]
    Temps_out=[]
    min_lenvalue=find_min_len_of_sec_dementia(Temps)
    for i in range(len(Temps)):
        Temps_out=Temps[len(Temps)-i-1][0:min_lenvalue]
        Counts_out=Counts[len(Temps)-i-1][0:min_lenvalue]
        plt.plot(Counts_out,Temps_out,ls = "-",lw = 2,label=filename[i])
    plt.legend()
    plt.show()


def run():
    Counts=[]
    Temps=[]
    filename=[]
    find_txt_file_in_now_dir(filename)
    extract_txt_info(filename,Counts,Temps)
    process_fig(Temps,filename,Counts)
    bar_with_date(Temps,filename)

    
if __name__ == '__main__':
    run()
