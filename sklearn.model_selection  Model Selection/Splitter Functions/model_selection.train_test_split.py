"""
sklearn.model_selection.train_test_split(
                                        *arrays,
                                        test_size=None,
                                        train_size=None,
                                        random_state=None,
                                        shuffle=True,
                                        stratify=None)
将数组或矩阵分成随机的训练和测试子集。

快速工具，将输入验证和next(ShuffleSplit().split(X, y))以及对输入数据的应用包装成一个单一的调用，
用于在oneliner中分割（和可选的子抽样）数据。

在User Guide.中阅读更多内容。

Parameters
    *arrays：sequence of indexables with same length / shape[0]
            允许的输入是列表、numpy数组、scipy-稀疏矩阵或pandas dataframes。

    test_size: float or int, default=None
            如果是float，应该在0.0和1.0之间，代表要包含在测试分割中的数据集的比例。
            如果是int，代表测试样本的绝对数量。
            如果是None，该值将被设置为训练规模的补充。
            如果train_size也是None，它将被设置为0.25。

    train_size: float或int, default=None
            如果是float，应该在0.0和1.0之间，代表数据集在训练分割中的比例。
            如果是int，代表训练样本的绝对数量。
            如果是None，该值会自动设置为测试规模的补数。

    random_state: int, RandomState instance or None, default=None
                控制在应用分割之前应用到数据的洗牌。
                传递一个int，以便在多个函数调用中实现可重复的输出。
                参见Glossary.

    shuffle: bool, default=True
            在拆分前是否对数据进行洗牌。
            如果shuffle=False，那么stratify必须为None。

    stratify：array-like, default=None
            如果不是None，数据会以分层的方式进行分割，用这个作为类标签。
            在User Guide.中阅读更多内容。

Returns
    splitting：list, length=2 * len(arrays)
            包含输入的train-test分割的列表。

0.16版新增：如果输入是稀疏的，输出将是scipy.sparse.csr_matrix。
否则，输出类型与输入类型相同。

"""
import numpy as np
from sklearn.model_selection import train_test_split
x, y = np.arange(10).reshape((5,2)), range(5),
print(x)
print(list(y))
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.33,random_state=42)
print(x_train)
print(y_train)
print(x_test)
print(y_test)
print(train_test_split(y, shuffle=False))