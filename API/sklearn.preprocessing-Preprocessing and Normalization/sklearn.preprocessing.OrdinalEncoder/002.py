from sklearn.preprocessing import OrdinalEncoder
import numpy as np
enc = OrdinalEncoder()

X1 = [['Male', 1], ['Female', 3], ['Female', np.nan]]
print(enc.fit_transform(X1))