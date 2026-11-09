import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.datasets import make_classification
from sklearn.impute import Simpieimputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import train_test_split
def create_pipeline():
  #Define which features are numeric vs categorical
    numeric_features=['age','income']
    categorical_features=['city','occupation']
  
