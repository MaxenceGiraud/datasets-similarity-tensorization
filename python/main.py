#%%
import numpy as np
import  scipy.linalg as la
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.stats import moment

#%%
def get_centers(mu=np.zeros(8),std=np.sqrt(5)*np.identity(8),n_cluster=5):
    return  np.random.multivariate_normal(mu,std,size=n_cluster)

def get_data(centers,var=10,n_data=1000):
    X = np.zeros((n_data,centers.shape[1]))
    step = int(n_data/centers.shape[0])
    for i in range(centers.shape[0]):
        n = step*(i+1)
        X[i*step:n] = np.random.multivariate_normal(centers[i],np.sqrt(var)*np.identity(centers.shape[1]),size=step)
    return X

def principal_angles_tensors(VV,WW,n_cluster=5):
    bases_v = la.svd(VV)[0][:,:n_cluster]
    bases_w = la.svd(WW)[0][:,:n_cluster]

    principal_angles = la.subspace_angles(bases_v,bases_w)

    return principal_angles

def tensorize_kr(V):
    VV = la.khatri_rao(V.T,V.T)

    return VV
#%%

def tensorize_thirdordermoment(V):
    
    cov  = np.cov(V.T)
    eig_val,eig_vec = np.linalg.eig(cov)
    u = eig_vec[eig_val.argmin()]

    d = (V.T @ (u.T @ (V-V.mean(axis=0)).T)**2) / V.shape[0]
    D = 0 
    for i in range(V.shape[1]) :
        ei =np.zeros(V.shape[1])
        ei[i] = 1
        D = D + np.outer(np.outer(d,ei),ei) + np.outer(np.outer(ei,d),ei) + np.outer(np.outer(ei,ei),d)
    D = D.reshape(np.repeat(V.shape[1],3))
    moment3 = moment(V,3,axis=0)
    VV = D - moment3

    return VV

# %%

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
        VV = tensorize_kr(V)
        WW = tensorize_kr(W)
        pa.append(principal_angles_tensors(VV,WW)[0])
        
        dist += np.sum((centers-centers_w)**2)
    dists.append(np.mean(dist))
    list_angles.append(np.mean(pa))

plt.plot(dists,list_angles,'o')
plt.xlabel("Distance")
plt.ylabel("Principal Angles")
plt.show()
# %%