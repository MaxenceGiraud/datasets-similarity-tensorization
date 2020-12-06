function out = principal_angle_kronecker(V,W)
    n_center = 5;
    % tensorization
    % A kronecker product
    VV = kr(V,V);
    WW = kr(W,W);

    % 1) check  III.2, using ref 20
    % 2) Number of cluster  is already known
    % 3) SVD
    [uv,sv,vv] = svd(VV);
    bases_v   = uv(:,1:n_center);
    [uw,sw,vw] = svd(WW);
    bases_w   = uw(:,1:n_center);
    
    %disp(subspace(bases_v,bases_w));
    %disp(subspace(bases_v.',bases_w.'));
    
    %4) Compute Principal angle
    out = subspace(bases_v,bases_w);
end