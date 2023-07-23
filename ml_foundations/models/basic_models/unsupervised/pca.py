import numpy as np 

class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.components = None 
        self.mean = None 
    
    def fit(self, X, y):
        self.mean = np.mean(X, axis=0)
        X = X = self.mean
    
    def transform(self):
        pass 

if __name__ == "__main__":
    from sklearn import datasets 

    data = datasets.load_iris()
    X = data.data
    y = data.target 
