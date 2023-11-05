""" 
used for muilt file to detect temp
 """
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from scipy.interpolate import make_interp_spline
import os


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
    print(filename)


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


def run():
    aa =[1,2,3]
    aa =1
    Counts=[]
    Counts_out=[]
    Temps=[]
    Temps_out=[]
    filename=[]
    find_txt_file_in_now_dir(filename)
    extract_txt_info(filename,Counts,Temps)
    min_lenvalue=find_min_len_of_sec_dementia(Temps)


    for i in range(len(Temps)):
        Temps_out=Temps[len(Temps)-i-1][0:min_lenvalue]
        Counts_out=Counts[len(Temps)-i-1][0:min_lenvalue]
        plt.plot(Counts_out,Temps_out,ls = "-",lw = 2,label=filename[i])
    plt.legend()
    plt.show()

if __name__ == '__main__':
    run()