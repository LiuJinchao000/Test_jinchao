import matplotlib.pyplot as plt
filename = 'test_qibing1600_open_456.txt'
Tem,Npu,Cpu,Count = [],[],[],[]
with open(filename, 'r') as f:
    lines = f.readlines()
    count = 0;
    for line in lines:
        count +=1
        if count%19 ==17:
            valuee = line.split()
            temp=float(valuee[1][0:5])/1000
            Tem.append(temp)
            Count.append(int(count/19+1))

        if count%19 ==18:
            valuee = line.split()
            npu=float(valuee[1][0:-1])/100000000
            Npu.append(npu)

        if count%19 ==0:
            valuee = line.split()
            cpu=float(valuee[1][0:-1])/100000
            Cpu.append(cpu)
""" print(Count)
print(Tem)
print(Npu)
print(Cpu)
print(len(Count))
print(len(Tem))
print(len(Npu))
print(len(Cpu)) """

plt.plot(Count,Tem,ls = "-",lw = 2,label="$Temperature$")
plt.plot(Count,Npu,c = "r",ls = "-",lw = 2,label="$Npu-frequency$")
plt.plot(Count,Cpu,c = "y",ls = "-",lw = 2,label="$Cpu-frequency$")

plt.legend()
plt.show()
print("end")

