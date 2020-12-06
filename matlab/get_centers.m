function out  = get_centers(n_centers,center_dim,var)
    % default values
   if nargin < 3
    var =   5;
    if nargin < 2
      center_dim=8;
      if nargin < 1 
        n_centers=5;
      end
    end
   end
   
   cov_matrix = sqrt(var)*eye(center_dim);
   mean_cluster_centers  =  zeros(center_dim,1);
   out = mvnrnd(mean_cluster_centers,cov_matrix,n_centers);
   
end