import scipy.linalg as la

def principal_angles_tensors(VV,WW,n_cluster=5):
    bases_v = la.svd(VV)[0][:,:n_cluster]
    bases_w = la.svd(WW)[0][:,:n_cluster]

    principal_angles = la.subspace_angles(bases_v,bases_w)

    return principal_angles