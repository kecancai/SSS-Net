#生成不同比例的噪声标签

import random

r=0.8
len =10000
f = open('/home/ckc/workspace/final_results/figure/0.8_label.txt','r',encoding='utf-8')

label = []
lines = f.readlines() 
for line in lines:
    label.append(line)

idx = list(range(len))
random.shuffle(idx)
num_noise = int(r*len)            
noise_idx = idx[:num_noise]
#print(noise_idx)
with open('/home/ckc/workspace/final_results/figure/0.8_label_noisy.txt', 'w') as file:  # 提取偶数列数据文件
    for i in range(len):
        if i in noise_idx:
            label[i] = str(random.randint(0,9))
            file.write(label[i]+'\n')
        else:
            file.write(str(label[i]))