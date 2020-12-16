import numpy as np

def get_centers(mu=np.zeros(8),std=np.sqrt(5)*np.identity(8),n_cluster=5):
    return  np.random.multivariate_normal(mu,std,size=n_cluster)

def get_data(centers,var=10,n_data=1000):
    X = np.zeros((n_data,centers.shape[1]))
    step = int(n_data/centers.shape[0])
    for i in range(centers.shape[0]):
        n = step*(i+1)
        X[i*step:n] = np.random.multivariate_normal(centers[i],np.sqrt(var)*np.identity(centers.shape[1]),size=step)
    return X