from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import Binarizer

print(make_pipeline(Binarizer(), MultinomialNB()))