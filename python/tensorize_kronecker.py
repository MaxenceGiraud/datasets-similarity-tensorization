import scipy.linalg as la

def tensorize_kr(V):
    VV = la.khatri_rao(V.T,V.T)

    return VV