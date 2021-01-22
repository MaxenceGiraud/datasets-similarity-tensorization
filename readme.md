# Datasets similarity via Tensorization

In this work we implements algorithms based on the preprint "Determining whether two datasets cluster similarly without determining the clusters" by Van Eeghem et al.

This work was an initial part of a research project by [Maxence Giraud](https://github.com/MaxenceGiraud) on "highest order clustering" supervized by [Remy Boyer](https://pro.univ-lille.fr/remy-boyer/). 

## Usage 

```python3
import dataset_similarity_tensor as dst

# Load 2 datasets V,W

## 1. Using kronecker product
VV = dst.tensorize_kr(V) 
WW = dst.tensorize_kr(W)

## 2. Using Third Order moment
VV = dst.tensorize_thirdordermoment(V).reshape(V.shape[1],-1) # We reshape because the principal angle are computed on an unfolded tensor (which becomes a matrix)
WW = dst.tensorize_thirdordermoment(W).reshape(W.shape[1],-1)

## Compute principal angle 
angle = dst.principal_angles_tensors(VV,WW)
```

The algorithms computing the principal angle thus resulting in an output between 0 and π/2, the closest this number is to 0 the more similar are the 2 datasets.