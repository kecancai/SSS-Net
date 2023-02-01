# Cifar10

## ========================= 总结 =================================
 1. 尝试过删除.json文件 （几乎没有影响）
 2. 阴影集计算两个用于划分的阈值 p1,p1; avg(p1,p2); max(p1,p2) (几乎没有影响)
 3. 调整batchsize, 64, 128. (为了方便对比原文，128)
 4. 尝试阴影集用概率和用基数计算阈值 （时间消耗大，放弃了）
 5. 高噪声率时，0.8/0.9 提高划分阈值有点用
 6. 低噪声率时，划分阈值影响不大
 7. 增加层数(34)，准确率能有所提高

 层次+伯努力，0.2,0.5效果好。0.8效果不好
 fcm 效果不稳定，数据集比较特殊，距离聚类中心越远，隶属度越小
 出现label sample=0，因为shadow pro = 1-beta

## ======================== 实验结果 ==============================

### ori
|  0.2  |  0.5  |  0.8  |  0.9  | noisy ratio
|  ---  |  ---  |  ---  |  ---  | 
| 96.22 | 94.39 | 92.64 | 74.27 | best acc
| 95.97 | 94.08 | 92.41 | 73.11 | avg acc(last 20 epochs)
|  724  |  506  |  328  |  237  | time(minutes)
|       |       |       |       | AUC(last 20 epochs)
### ori
|  0.2  |  0.5  |  0.8  |  noisy ratio
|  ---  |  ---  |  ---  |   
| 96.16 | 94.59 | 92.43 |  best acc
| 95.95 | 94.25 | 92.16 |  avg acc(last 20 epochs)
|  502  |  350  |  227  |  time(minutes)
|       |       |       |  AUC(last 20 epochs)


### hiera(T_degree) + reselect + shadow（最终结果）
|  0.2  |  0.5  |  0.8  |   noisy ratio
|  ---  |  ---  |  ---  |   
| 97.00 | 95.79 | 92.02 |   best acc 0.2
| 96.61 | 95.60 | 91.69 |   avg acc(last 20 epochs) 0.2
|       |       |       |   time(minutes)
|       |       |       |   AUC(last 20 epochs)

### w/o hiera(T_degree)
|  0.2  |  0.5  |  0.8  |   noisy ratio
|  ---  |  ---  |  ---  |   
| 96.09 | 92.69 | 79.26 |   best acc
| 95.12 | 91.71 | 78.83 |   avg acc(last 20 epochs)
|       |       |       |   time(minutes)
|       |       |       |   AUC(last 20 epochs)

### w/o reselect
|  0.2  |  0.5  |  0.8  |   noisy ratio
|  ---  |  ---  |  ---  |   
| 96.85 | 95.69 | 92.23 |   best acc
| 96.58 | 95.41 | 91.90 |   avg acc(last 20 epochs)
|       |       |       |   time(minutes)
|       |       |       |   AUC(last 20 epochs)

### w/o shadow
|  0.2  |  0.5  |  0.8  |   noisy ratio
|  ---  |  ---  |  ---  |   
| 96.83 | 95.75 | 91.75 |   best acc
| 96.54 | 95.51 | 91.34 |   avg acc(last 20 epochs)
|       |       |       |   time(minutes)
|       |       |       |   AUC(last 20 epochs)

### with minikmeans
|  0.2  |  0.5  |  0.8  | noisy ratio
|  ---  |  ---  |  ---  | 
& 96.66 & 95.26 & 88.60 | best acc
& 96.28 & 95.05 & 86.01 | avg acc(last 20 epochs)

### hiera
|  0.2  |  0.5  |  0.8  | noisy ratio
|  ---  |  ---  |  ---  |  
& 96.75 & 95.51 & 91.44 | best acc
& 96.53 & 95.24 & 90.25 | avg acc(last 20 epochs)


# Cifar100
## ========================= 总结 =================================



## ======================== 实验结果 ==============================

### ori
|  0.2  |  0.5  |  0.8  |  noisy ratio
|  ---  |  ---  |  ---  |   
| 77.13 | 74.82 | 59.24 |  best acc
| 76.74 | 74.47 | 58.86 |  avg acc(last 20 epochs)
|  603  |  429  |  283  |  time(minutes)
|       |       |       |  AUC(last 20 epochs)


### hiera(T_degree) + reselect + shadow（最终结果）
|  0.2  |  0.5  |  0.8  |   noisy ratio
|  ---  |  ---  |  ---  |   
| 81.09 | 77.92 | 61.51 |   best acc 0.1
| 80.31 | 77.10 | 61.12 |   avg acc(last 20 epochs)
|       |       |       |   time(minutes)
|       |       |       |   AUC(last 20 epochs)

### w/o hiera(T_degree)
|  0.2  |  0.5  |  0.8  |   noisy ratio
|  ---  |  ---  |  ---  |   
| 76.81 | 64.75 | 51.16 |   best acc
| 76.46 | 64.28 | 50.78 |   avg acc(last 20 epochs)
|       |       |       |   time(minutes)
|       |       |       |   AUC(last 20 epochs)

### w/o reselect
|  0.2  |  0.5  |  0.8  |   noisy ratio
|  ---  |  ---  |  ---  |   
| 80.84 | 77.31 | 61.17 |   best acc
| 80.03 | 76.64 | 60.70 |   avg acc(last 20 epochs)
|       |       |       |   time(minutes)
|       |       |       |   AUC(last 20 epochs)

### w/o shadow
|  0.2  |  0.5  |  0.8  |   noisy ratio
|  ---  |  ---  |  ---  |   
| 80.86 | 77.37 | 60.10 |   best acc
| 79.99 | 76.57 | 59.41 |   avg acc(last 20 epochs)
|       |       |       |   time(minutes)
|       |       |       |   AUC(last 20 epochs)

### with minikmeans
|  0.2  |  0.5  |  0.8  | noisy ratio
|  ---  |  ---  |  ---  | 
& 80.63 & 76.23 & 55.91 | best acc
& 80.02 & 75.08 & 55.22 | avg acc(last 20 epochs)

### hiera
|  0.2  |  0.5  |  0.8  | noisy ratio
|  ---  |  ---  |  ---  |  
& 80.76 & 76.42 & 59.89 | best acc
& 80.12 & 75.68 & 59.41 | avg acc(last 20 epochs)


### clothing1M  Webvision 
3090
