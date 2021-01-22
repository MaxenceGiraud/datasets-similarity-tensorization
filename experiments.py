# %%
import numpy as np
import matplotlib.pyplot as plt
from data import get_centers,get_data
from dataset_similarity_tensor import principal_angles_tensors,tensorize_kr,tensorize_thirdordermoment

# %% [markdown]
# ## Tensorization using Kronecker product 
# %% [markdown]
# ### Making the variance (of datasets) vary

# %%
n_cluster = 5

n_runs = 10
list_angles = []
list_angles_median = []
for var in range(0,40):
    print(var)
    pa = []
    for _ in range(n_runs):
        centers  = get_centers(n_cluster=n_cluster)
        V = get_data(centers,n_data=5000,var=var)
        W = get_data(centers,n_data=5000,var=var)
        VV = tensorize_kr(V)
        WW = tensorize_kr(W)
        pa.append(principal_angles_tensors(VV,WW)[0])

    list_angles.append(np.mean(pa))
    list_angles_median.append(np.median(pa))


# %%
plt.plot(list_angles,label='mean')
plt.plot(list_angles_median,label='median')
plt.xlabel("Variance of datasets")
plt.ylabel("Principal Angles")
plt.legend()
plt.show()

# %% [markdown]
# ### Making distance between centroids vary

# %%
n_runs = 30
dists = []
list_angles= []
list_angles_median = []

for i in np.linspace(0,1,10):
    print(i)
    pa = []
    dist = 0
    for _ in range(n_runs):
        centers  = get_centers()
        centers_w = centers + centers*i
        V = get_data(centers,n_data=5000,var=2)
        W = get_data(centers_w,n_data=5000,var=2)   
        VV = tensorize_kr(V)
        WW = tensorize_kr(W)
        pa.append(principal_angles_tensors(VV,WW)[0])
        
        dist += np.sqrt(np.sum((centers-centers_w)**2))
    dists.append(np.mean(dist))
    list_angles.append(np.mean(pa))
    list_angles_median.append(np.median(pa))


# %%
plt.plot(dists,list_angles,label='mean')
plt.plot(dists,list_angles_median,label='median')
plt.xlabel("Distance")
plt.ylabel("Principal Angles")
plt.legend()
plt.show()


# %% [markdown]
# ## Tensorization via Third order moment

# %%
n_cluster = 5

n_runs = 30
list_angles = []
list_angles_median = []
for var in range(0,40):
    print(var)
    pa = []
    for _ in range(n_runs):
        centers  = get_centers(n_cluster=n_cluster)
        # centers_w = get_centers(n_cluster=n_cluster)
        V = get_data(centers,n_data=10000,var=var)
        W = get_data(centers,n_data=10000,var=var)
        VV = tensorize_thirdordermoment(V).reshape(V.shape[1],-1)
        WW = tensorize_thirdordermoment(W).reshape(V.shape[1],-1)
        pa.append(principal_angles_tensors(VV.T,WW.T)[0])

    list_angles.append(np.mean(pa))
    list_angles_median.append(np.median(pa))


# %%
plt.plot(list_angles,label='mean')
plt.plot(list_angles_median,label='median')
plt.xlabel("Variance of datasets")
plt.ylabel("Principal Angles")
plt.legend()
plt.show()


# %%



# %%
n_runs = 10
dists = []
list_angles= []
list_angles_median = []

for i in np.linspace(0,10,11):
    print(i)
    pa = []
    dist = 0
    for _ in range(n_runs):
        centers  = get_centers()
        centers_w = centers + centers*i
        V = get_data(centers,n_data=100000,var=2)
        W = get_data(centers_w,n_data=100000,var=2)   
        VV = tensorize_thirdordermoment(V).reshape(V.shape[1],-1)
        WW = tensorize_thirdordermoment(W).reshape(V.shape[1],-1)
        pa.append(principal_angles_tensors(VV.T,WW.T)[0])
        
        dist += np.sqrt(np.sum((centers-centers_w)**2))
    dists.append(np.mean(dist))
    list_angles.append(np.mean(pa))
    list_angles_median.append(np.median(pa))


# %%
plt.plot(dists,list_angles,label='mean')
plt.plot(dists,list_angles_median,label='median')
plt.xlabel("Distance")
plt.ylabel("Principal Angles")
plt.legend()
plt.show()
# %%