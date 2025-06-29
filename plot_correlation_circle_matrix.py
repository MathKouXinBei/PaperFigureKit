import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 20


def plot_correlation_circle_matrix(matrix, save_path=None):
    if isinstance(matrix, np.ndarray):
        matrix = pd.DataFrame(matrix)

    matrix.index = [i + 1 for i in range(matrix.shape[0])]
    matrix.columns = [i + 1 for i in range(matrix.shape[1])]

    corr = matrix.corr()
    size = corr.shape[0]

    fig, ax = plt.subplots(figsize=(min(1.6 * size, 16), min(1.2 * size, 12)))
    ax.set_aspect('equal')

    cmap = plt.get_cmap('coolwarm')

    for i in range(size):
        for j in range(size):
            value = corr.iloc[i, j]
            radius = np.abs(value) * 0.45
            color = cmap((value + 1) / 2)
            circle = plt.Circle((j + 1, size - i), radius, color=color)
            ax.add_patch(circle)
            text_color = 'white' if i == j else 'black'
            ax.text(j + 1, size - i, f"{value:.2f}", ha='center', va='center', color=text_color)

    # 设置主刻度
    ax.set_xticks(np.arange(1, size + 1))
    ax.set_yticks(np.arange(1, size + 1))
    ax.set_xticklabels(corr.columns)
    ax.set_yticklabels(reversed(corr.index))
    ax.tick_params(length=0)

    # 设置边界范围
    ax.set_xlim(0.5, size + 0.5)
    ax.set_ylim(0.5, size + 0.5)
    # ax.invert_yaxis()

    # ✅ 添加边界网格线：正方形格子
    for i in range(size + 1):
        ax.axhline(i + 0.5, color='lightgray', linewidth=0.8)
        ax.axvline(i + 0.5, color='lightgray', linewidth=0.8)

    # 色条
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=-1, vmax=1))
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, shrink=1, pad=0.02, ticks=[-1, -0.5, 0, 0.5, 1])
    cbar.ax.tick_params()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()

# 测试数据
np.random.seed(42)
random_data = np.random.rand(15, 15)
# random_data = np.random.rand(5, 5)
plot_correlation_circle_matrix(random_data, save_path="15CorrelationCircleMatrix_GridFixed.png")
