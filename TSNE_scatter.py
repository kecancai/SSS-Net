# 降维绘制散点图

from sklearn import manifold
import matplotlib.pyplot as plt
import numpy as np


def visualize_t_sne(features, labels, cluster_number, title):
    """
    features: np.ndarray
    labels: np.ndarray
    cluster_number: for example, 10
    title: figure name, for example, 'cifar10_t_sne.png'
    """
    # features = features.numpy()
    # labels = labels.numpy()
    # labels = labels.astype(int)

    t_sne = manifold.TSNE(n_components=2, init='pca', random_state=0)  # random_state: random seed, setting for reproducibility
    data = t_sne.fit_transform(features)

    fig = plt.figure()
    plt.scatter(data[:, 0], data[:, 1], s=2, c=labels, cmap=plt.cm.get_cmap("jet", cluster_number))
    plt.colorbar(ticks=range(cluster_number))
    ax = plt.gca() # 设置坐标轴不可见
    ax.axes.xaxis.set_visible(False)# 坐标轴和标签不可见
    ax.axes.yaxis.set_visible(False)
    # ax.axes.xaxis.set_ticks([]) # 坐标轴不可见,标签可见
    # ax.axes.yaxis.set_ticks([])    

    fig.savefig(title, dpi=fig.dpi)


if __name__ == "__main__":
    features = np.loadtxt("/home/ckc/workspace/final_results/figure/0.8_feature.txt")
    labels = np.loadtxt("/home/ckc/workspace/final_results/figure/0.8_label.txt")
    print(features.shape)
    print(labels.shape)
    visualize_t_sne(features, labels, cluster_number=10, title="./cifar10_test_t_sne_0.8.png")


