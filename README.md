# PaperFigureKit  
## plot_correlation_circle_matrix.py
这是一个用于可视化相关系数矩阵的 Python 脚本，使用**圆圈的大小和颜色**同时展示变量之间的相关性（正负号与强弱程度）。适合用于科研绘图、数据探索与展示。
### 功能说明
- 圆圈大小 ∝ 相关系数绝对值（|corr|）  
- 圆圈颜色表示正相关（红）或负相关（蓝）  
- 每个圆圈中央显示数值，主对角线为白字  
- 自动绘制网格线  
- 支持图片保存或直接展示  
### 使用方法
#### 1. 安装依赖
```bash
pip install numpy pandas matplotlib
````
#### 2. 调用示例
```python
import numpy as np
from plot_correlation_circle_matrix import plot_correlation_circle_matrix
# 构造示例数据
np.random.seed(42)
data = np.random.rand(15, 15)
# 绘图并保存
plot_correlation_circle_matrix(data, save_path="15CorrelationCircleMatrix_GridFixed.png")
```

如不设置 `save_path`，将直接弹出图像窗口展示：

```python
plot_correlation_circle_matrix(data)
```

#### 3.函数接口

```python
plot_correlation_circle_matrix(matrix, save_path=None)
```

* `matrix`: 输入数据，`numpy.ndarray` 或 `pandas.DataFrame` 均可
* `save_path`: 图片保存路径（字符串）。如为 `None`，则使用 `plt.show()` 展示图像

