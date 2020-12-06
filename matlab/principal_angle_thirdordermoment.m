function out = principal_angle_thirdordermoment(V,W)
    moment_v = moment(V,3);
    moment_w = moment(W,3);
     
    % TODO compute D matrix
    Dv = 0;
    Dw = 0;
    
    VV = moment_v-DV; % TODO
    WW = moment_w-DW; % TODO
    
    % 1) check  III.2, using ref 20
    % 2) Number of cluster  is already known
    % 3) SVD
    [uv,sv,vv] = svd(VV);
    bases_v   = uv(:,1:n_center);
    [uw,sw,vw] = svd(WW);
    bases_w   = uw(:,1:n_center);
    
    %4) Compute Principal angle
    out = subspace(bases_v,bases_w);
end