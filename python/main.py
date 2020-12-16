#%%
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.stats import moment
from data_creation import get_centers,get_data
from principal_angles import principal_angles_tensors
from tensorize_kronecker import tensorize_kr
from tensorize_moments import tensorize_thirdordermoment
#%%

# Making varying variance (of datasets)
n_cluster = 5

n_runs = 10
list_angles = []
for var in range(0,40):
    pa = []
    for _ in range(n_runs):
        centers  = get_centers(n_cluster=n_cluster)
        centers_w = get_centers(n_cluster=n_cluster)
        V = get_data(centers,n_data=1000,var=var)
        W = get_data(centers,n_data=1000,var=var)
        VV = tensorize_kr(V)
        WW = tensorize_kr(W)
        pa.append(principal_angles_tensors(VV,WW)[0])

    list_angles.append(np.mean(pa))


# %%
plt.plot(list_angles)
plt.xlabel("Variance of datasets")
plt.ylabel("Principal Angles")
plt.show()
# %%
n_cluster = 5

list_angles = []
n_runs = 10
for n_points in np.logspace(1,3,15):
    pa = []
    for _ in range(n_runs):
        centers  = get_centers(n_cluster=n_cluster)
        V = get_data(centers,n_data=int(n_points))
        W = get_data(centers,n_data=int(n_points))
        VV = tensorize_kr(V)
        WW = tensorize_kr(W)
        pa.append(principal_angles_tensors(VV,WW)[0])
    list_angles.append(np.mean(pa))


# %%
plt.plot(list_angles)
plt.xlabel("Number of data points")
plt.ylabel("Principal Angles")
plt.show()
# %%


##### Making cluster centers variance vary


n_cluster = 5

n_runs = 10
list_angles = []
for var in range(0,40):
    pa = []
    for _ in range(n_runs):
        centers  = get_centers(n_cluster=n_cluster,std=np.sqrt(var)*np.identity(8))
        centers_w = get_centers(n_cluster=n_cluster,std=np.sqrt(var)*np.identity(8))
        V = get_data(centers,n_data=1000,var=8)
        W = get_data(centers_w,n_data=1000,var=8)
        VV = tensorize_kr(V)
        WW = tensorize_kr(W)
        pa.append(principal_angles_tensors(VV,WW)[0])

    list_angles.append(np.mean(pa))


# %%
plt.plot(list_angles)
plt.xlabel("Variance")
plt.ylabel("Principal Angles")
plt.show()
# %%

n_runs = 5
dists = []
list_angles= []
for i in np.linspace(0,0.00001,10):
    pa = []
    dist = 0
    for _ in range(n_runs):
        centers  = get_centers()
        centers_w = centers + centers*i
        V = get_data(centers,n_data=1000,var=0)
        W = get_data(centers_w,n_data=1000,var=0)
        # VV = tensorize_kr(V)
        # WW = tensorize_kr(W)
        VV = tensorize_thirdordermoment(V).reshape(V.shape[1],-1)
        WW = tensorize_thirdordermoment(W).reshape(V.shape[1],-1)
        pa.append(principal_angles_tensors(VV,WW)[0])
        
        dist += np.sum((centers-centers_w)**2)
    dists.append(np.mean(dist))
    list_angles.append(np.mean(pa))

plt.plot(dists,list_angles,'o')
plt.xlabel("Distance")
plt.ylabel("Principal Angles")
plt.show()
# %%