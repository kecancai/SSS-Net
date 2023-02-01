import matplotlib.pyplot as plt
import os
import numpy as np
plt.figure()

# 路径
path2_1 = '/home/ckc/workspace/final_results/cifar100/cluster/0.2/hiera_0.2_acc.txt'
path2_2 = '/home/ckc/workspace/final_results/cifar100/cluster/0.2/kmeans_0.2_acc.txt'
path2_3 = '/home/ckc/workspace/final_results/cifar100/cluster/0.2/mini_0.2_acc.txt'
path2_4 = '/home/ckc/workspace/final_results/cifar100/cluster/0.2/no_0.2_acc.txt'
 
path5_1 = '/home/ckc/workspace/final_results/cifar100/cluster/0.5/hiera_0.5_acc.txt'
path5_2 = '/home/ckc/workspace/final_results/cifar100/cluster/0.5/kmeans_0.5_acc.txt'
path5_3 = '/home/ckc/workspace/final_results/cifar100/cluster/0.5/mini_0.5_acc.txt'
path5_4 = '/home/ckc/workspace/final_results/cifar100/cluster/0.5/no_0.5_acc.txt'

path8_1 = '/home/ckc/workspace/final_results/cifar100/cluster/0.8/hiera_0.8_acc.txt'
path8_2 = '/home/ckc/workspace/final_results/cifar100/cluster/0.8/kmeans_0.8_acc.txt'
path8_3 = '/home/ckc/workspace/final_results/cifar100/cluster/0.8/mini_0.8_acc.txt'
path8_4 = '/home/ckc/workspace/final_results/cifar100/cluster/0.8/no_0.8_acc.txt'

x = np.arange(0,300)
def loadData(file):
    y = [] # y轴
    with open(file, 'r') as f:
        lines = f.readlines()  #读取所有行
        for line in lines:
            y.append(float(line))
    return y
 
#画图
if __name__ == '__main__':

    plt.subplot(1,3,1)
    y = loadData(path2_1)
    plt.plot(x, y, color='r', alpha=0.6, label='$hiera \; cluster$')
    #plt.legend()
    y = loadData(path2_2)
    plt.plot(x, y, color='g', alpha=0.6, label='$kmeans \; cluster$')
    #plt.legend()
    y = loadData(path2_3)
    plt.plot(x, y, color='y', alpha=0.6, label='$mini \; cluster$')
    #plt.legend() 
    y = loadData(path2_4)
    plt.plot(x, y, color='b', alpha=0.6, label='$no \; cluster$')
    plt.legend()
    plt.title("noisy ratio:0.2")
    plt.xlabel("epoch")
    plt.ylabel("accuracy")


    plt.subplot(1,3,2)
    y = loadData(path5_1)
    plt.plot(x, y, color='r', alpha=0.6, label='$hiera \; cluster$')
    #plt.legend()
    y = loadData(path5_2)
    plt.plot(x, y, color='g', alpha=0.6, label='$kmeans \; cluster$')
    #plt.legend()
    y = loadData(path5_3)
    plt.plot(x, y, color='y', alpha=0.6, label='$mini \; cluster$')
    #plt.legend() 
    y = loadData(path5_4)
    plt.plot(x, y, color='b', alpha=0.6, label='$no \; cluster$')
    plt.legend()
    plt.title("noisy ratio:0.5")
    plt.xlabel("epoch")
    plt.ylabel("accuracy")

    plt.subplot(1,3,3)
    y = loadData(path8_1)
    plt.plot(x, y, color='r', alpha=0.6, label='$hiera \; cluster$')
    #plt.legend()
    y = loadData(path8_2)
    plt.plot(x, y, color='g', alpha=0.6, label='$kmeans \; cluster$')
    #plt.legend()
    y = loadData(path8_3)
    plt.plot(x, y, color='y', alpha=0.6, label='$mini \; cluster$')
    #plt.legend() 
    y = loadData(path8_4)
    plt.plot(x, y, color='b', alpha=0.6, label='$no \; cluster$')
    plt.legend()
    plt.title("noisy ratio:0.8")
    plt.xlabel("epoch")
    plt.ylabel("accuracy")

    # color 'm', 'c'
    plt.suptitle("cifar100")  
    plt.tight_layout()
    plt.subplots_adjust(left=0.1, wspace=0.2, hspace=0)

    plt.show()
  