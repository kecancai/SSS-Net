# 打印每个文件最后100个epoch中最高的准确率

import numpy as np
file_path= '/home/ckc/workspace/final_results/cifar100/cluster/checkpoint_hiera_select/cifar100_0.8_acc.txt'
with open(file_path) as file:
    lines = file.readlines()
    list=[]
    for i in range(50,300):
        list.append(lines[i][-6:-1])
    m = max(list)
    print(m)

# 打印每个文件收敛时20个epoch中平均准确率
    
from numpy import *
import statistics

file_path= '/home/ckc/workspace/final_results/cifar100/cluster/checkpoint_hiera_select/cifar100_0.2_acc.txt'
with open(file_path) as file:
    lines = file.readlines()
    list=[]
    for i in range(279,300):
        list.append(lines[i][-6:-1])
    prob =[float(x) for x in list]
    avg = statistics.mean(prob)
    print("%.2f"%avg)
      
