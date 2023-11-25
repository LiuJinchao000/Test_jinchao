""" 
used for analsys npu_load file 
 """
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from scipy.interpolate import make_interp_spline
import os
from numpy import mean
import matplotlib.font_manager


def find_txt_file_in_current_dir( filename ):
    for dataname in os.listdir():
        if os.path.splitext(dataname)[1] == '.txt':#目录下包含.txt的文件
            filename.append(dataname) 
    filename.sort() #乱序问题进行解决          
    print(f"文件列表：{filename}")


def bar_with_date(Loads):
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 显示中文
    X,Y=[],[]
    for i in range(0,len(Loads)):
       X.append(str(i)) 
       if i%4 == 3:
        print(f"项目编号{i}:all npus mean load in a period time:{mean(Loads[i]):.2f} %")
       else:
        print(f"项目编号{i}:npu{i} mean load in a period time:{mean(Loads[i]):.2f} %")

    for i in range(len(Loads)):
        Y.append(mean(Loads[i]))
    width = 0.4  # 柱体宽度



    plt.figure(figsize=(8, 6))
    plt.bar(X, Y, width,label='temp')
    for a,b,i in zip(X,Y,range(len(X))): # zip 函数
        plt.text(a,b+0.13,"%.2f"%Y[i],ha='center') # plt.text 函数
    
    plt.xlabel('项目编号')
    plt.ylabel('Npu load/%')
    plt.title('NPU Load')
    #plt.tight_layout()
    plt.savefig(f'./test2.jpg',dpi=300)
    plt.show()



def extract_info(filename,Loads):
    for file in filename:
        with open(file, 'r') as f:
            lines = f.readlines()
            npu1,npu2,npu3,value_means=[],[],[],[]
            for line in lines:
                if "NPU load: " in line:

                    value1 = float(line.split(":")[2].split("%")[0])
                    value2 = float(line.split(":")[3].split("%")[0])
                    value3 = float(line.split(":")[4].split("%")[0])
                    value_mean=(value1+value2+value3)/3
                                     
                    npu1.append(value1)
                    npu2.append(value2)
                    npu3.append(value3)
                    value_means.append(value_mean)
            
            Loads.append(npu1)
            Loads.append(npu2)
            Loads.append(npu3)
            Loads.append(value_means)


def run():
    Loads=[]
    filename=[]
    find_txt_file_in_current_dir( filename )
    extract_info(filename,Loads)
    bar_with_date(Loads)

if __name__ == '__main__':
    run()
