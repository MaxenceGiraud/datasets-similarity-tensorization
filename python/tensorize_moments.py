import numpy as np
from scipy.stats import moment

def tensorize_thirdordermoment(V):
    Vmu = V - V.mean(axis=0)
    cov  = (Vmu.T @Vmu )/V.shape[0]
    eig_val,eig_vec = np.linalg.eig(cov)
    u = eig_vec[:,eig_val.argmin()]

    d = (V.T @ (u.T @ (V-V.mean(axis=0)).T)**2) / V.shape[0]
    D = 0 
    for i in range(V.shape[1]) :
        ei =np.zeros(V.shape[1])
        ei[i] = 1
        D = D + np.outer(np.outer(d,ei),ei) + np.outer(np.outer(ei,d),ei) + np.outer(np.outer(ei,ei),d)
    D = D.reshape(V.shape[1],V.shape[1],V.shape[1])
    moment3 = moment(V,3,axis=0)
    VV = D - moment3

    return VV