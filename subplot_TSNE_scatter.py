# 降维绘制多散点子图

from sklearn import manifold
import matplotlib.pyplot as plt
import numpy as np

path1 = "/home/ckc/workspace/final_results/figure/0.2_feature.txt"
path1_1 = "/home/ckc/workspace/final_results/figure/0.2_label.txt"
path1_2 = "/home/ckc/workspace/final_results/figure/0.2_label_noisy.txt"

path2 = "/home/ckc/workspace/final_results/figure/0.5_feature.txt"
path2_1 = "/home/ckc/workspace/final_results/figure/0.5_label.txt"
path2_2 = "/home/ckc/workspace/final_results/figure/0.5_label_noisy.txt"

path3 = "/home/ckc/workspace/final_results/figure/0.8_feature.txt"
path3_1 = "/home/ckc/workspace/final_results/figure/0.8_label.txt"
path3_2 = "/home/ckc/workspace/final_results/figure/0.8_label_noisy.txt"


def visualize_t_sne(features, labels, cluster_number):

    t_sne = manifold.TSNE(n_components=2, init='pca', random_state=0)
    data = t_sne.fit_transform(features)

    plt.scatter(data[:, 0], data[:, 1], s=2, c=labels, cmap=plt.cm.get_cmap("jet", cluster_number))
    ax = plt.gca() # 设置坐标轴不可见
    # ax.axes.xaxis.set_visible(False)# 坐标轴和标签不可见
    # ax.axes.yaxis.set_visible(False)
    ax.axes.xaxis.set_ticks([]) # 坐标轴不可见,标签可见
    ax.axes.yaxis.set_ticks([])  

if __name__ == "__main__":
    
    fig,axs=plt.subplots(2,3,sharex=True,sharey=False)

    plt.subplot(2,3,1)
    features = np.loadtxt(path1)
    labels = np.loadtxt(path1_1)
    visualize_t_sne(features, labels, cluster_number=10)
    #plt.xlabel("epoch")

    plt.subplot(2,3,2)
    features = np.loadtxt(path2)
    labels = np.loadtxt(path2_1)
    visualize_t_sne(features, labels, cluster_number=10)
 
    plt.subplot(2,3,3)
    features = np.loadtxt(path3)
    labels = np.loadtxt(path3_1)
    visualize_t_sne(features, labels, cluster_number=10)
    #plt.colorbar(ticks=range(10))

    plt.subplot(2,3,4)
    features = np.loadtxt(path1)
    labels = np.loadtxt(path1_2)
    visualize_t_sne(features, labels, cluster_number=10)
    plt.xlabel("$20\% \; label \;noise $")

    plt.subplot(2,3,5)
    features = np.loadtxt(path2)
    labels = np.loadtxt(path2_2)
    visualize_t_sne(features, labels, cluster_number=10)
    plt.xlabel("$50\% \; label \;noise $")

    plt.subplot(2,3,6)
    features = np.loadtxt(path3)
    labels = np.loadtxt(path3_2)
    visualize_t_sne(features, labels, cluster_number=10)
    #plt.colorbar(ticks=range(10))
    plt.xlabel("$80\% \; label \;noise $")

    #前面三个子图的总宽度 为 全部宽度的 0.9；剩下的0.1用来放置colorbar
    fig.subplots_adjust(right=0.9)

    #colorbar 左 下 宽 高 
    l = 0.92
    b = 0.109
    w = 0.015
    h = 1 - 2*b 

    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    plt.colorbar(cax=cbar_ax)

    # plt.colorbar(p1, cax=cbar_ax)
    # plt.colorbar(p2, cax=cbar_ax)
    plt.show()

    fig.savefig('./cifar10_scatter.png', dpi=fig.dpi)





