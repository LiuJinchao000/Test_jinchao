import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from scipy.interpolate import make_interp_spline

filename1 = 'test1020.txt'
filename2 = 'test1020_2_older.txt'
TT0,TT1,Tem1,Tem2,Count,Count1,Count2 = [],[],[],[],[],[],[]
with open(filename1, 'r') as f:
    lines = f.readlines()
    count = 0;
    for line in lines:
        count +=1
        if count%19 ==17:
            valuee = line.split()
            temp1=float(valuee[1][0:5])/1000
            Tem1.append(temp1)
            Count1.append(int(count/19+1))

with open(filename2, 'r') as f:
    lines = f.readlines()
    count2 = 0;
    for line in lines:
        count2 +=1
        if count2%19 ==17:
            valuee2 = line.split()
            temp2=float(valuee2[1][0:5])/1000
            Tem2.append(temp2)
            Count2.append(int(count2/19+1))

print(len(Tem1))
print(len(Tem2))

if len(Count1)>len(Count2):
    TT0 = Tem1[0:len(Tem2)]
    TT1 = Tem2[0:len(Tem2)]
    #TT0 = gaussian_filter1d(TT0, sigma=5)
    #TT1 = gaussian_filter1d(TT1, sigma=5)
    Count = Count2

else:
    TT0 = Tem1[0:len(Tem1)]
    TT1 = Tem2[0:len(Tem1)]
    Count = Count1

plt.plot(Count,TT0,ls = "-",lw = 2,label="$new$")
plt.plot(Count,TT1,ls = "-",lw = 2,label="$older$")

plt.legend()
plt.show()


