function out  = get_data(centers,var,n_data)
    % Default values
   if nargin < 3
    n_data = 1000;
    if nargin < 2
      var =8;
    end
   end
   data_dim = size(centers);
   n_per_cluster = n_data/data_dim(1);
   
   X = [];
   for i = 1:data_dim(1)
       cov = sqrt(var)*eye(data_dim(2));
       data_i = mvnrnd(centers(i,:),cov,n_per_cluster);
       X = vertcat(X,data_i);
   end

   out = X.';

end