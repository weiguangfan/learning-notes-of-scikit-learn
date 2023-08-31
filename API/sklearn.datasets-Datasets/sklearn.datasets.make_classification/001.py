from sklearn.datasets import make_classification
X,y = make_classification(random_state=42)
print(type(X))
print(X.shape)
print(type(y))
print(y.shape)