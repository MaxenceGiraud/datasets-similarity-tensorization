clear;

%{
% Making varying the variance
list_pa = 0;
for var = 0:40
    centers_v = get_centers(5,8,var);
    centers_w = get_centers(5,8,var);
    V = get_data(centers_v,5,1000);
    W = get_data(centers_w,5,1000);
    principal_angle = principal_angle_kronecker(V,W);
    list_pa(end+1)= principal_angle;    
end

plot(list_pa(:,2:end));
%}
%% 
npoints = 1000;
list_pa = 0;
dist = 0;
for d = 0:100
    centers = get_centers();
    centers_w = centers + centers*d/10;
    dist(end+1) = norm(centers-centers_w);
    V = get_data(centers,5,round(npoints));
    W = get_data(centers_w,5,round(npoints));
    principal_angle = principal_angle_kronecker(V,W);
    list_pa(end+1)= principal_angle;    
end

dist = dist(:,2:end);
dist = dist(:);
pa = list_pa(:,2:end);
pa = pa(:);

reg = dist\pa;
s = size(dist);
x = linspace(0, max(dist), s(1));
r = x*reg;
scatter(dist,pa);
hold on;
plot(x,r);
ylabel("Principal Angle");
xlabel("distance between cluster centers");


%% Making varying the number of points

% list_pa = 0;
% for npoints = logspace(1,3,3)
%     disp(round(npoints))
%     centers = get_centers();
%     %centers_w = get_centers();
%     V = get_data(centers,5,round(npoints));
%     W = get_data(centers,5,round(npoints));
%     principal_angle = principal_angle_kronecker(V,W);
%     list_pa(end+1)= principal_angle;    
% end
% 
% plot(logspace(1,3,3),list_pa(:,2:end));
% ylabel("Principal Angle");
% xlabel("Number of points in the dataset");


% Making  varying the variance of the datasets
% list_pa = 0;
% n_runs = 2;
% for var = 0:40
%     disp(var);
%     principal_angle = 0;
%     for n = 1:n_runs
%         centers = get_centers();
%         %centers_w = get_centers();
%         V = get_data(centers,var,1000);
%         W = get_data(centers,var,1000);
%         principal_angle = principal_angle + principal_angle_kronecker(V,W);
%             
%     end
%     principal_angle = principal_angle/ n_runs;
%     list_pa(end+1)= principal_angle;
% end
% 
% plot(0:40,list_pa(:,2:end));
% ylabel("Principal Angle");
% xlabel("Variance of the datasets");


% % Making varying the variance of the clusters centers
% list_pa = 0;
% n_runs = 2;
% for var = 0:40
%     disp(var);
%     principal_angle = 0;
%     for n = 1:n_runs
%         centers = get_centers(5,8,var);
%         centers_w = get_centers(5,8,var);
%         V = get_data(centers,8,1000);
%         W = get_data(centers_w,8,1000);
%         principal_angle = principal_angle + principal_angle_kronecker(V,W);
%             
%     end
%     principal_angle = principal_angle/ n_runs;
%     list_pa(end+1)= principal_angle;
% end
% 
% plot(0:40,list_pa(:,2:end));
% ylabel("Principal Angle");
% xlabel("Variance of the cluster centers");


%% Makying varying the Ratio largest to smallest cluster
% list_pa = 0;
% n_runs = 2;
% for var = 0:40
%     disp(var);
%     principal_angle = 0;
%     for n = 1:n_runs
%         centers = get_centers();
%         %centers_w = get_centers(5,8,var);
%         V = get_data(centers,8,1000);
%         W = get_data(centers_w,8,1000);
%         principal_angle = principal_angle + principal_angle_kronecker(V,W);
%             
%     end
%     principal_angle = principal_angle/ n_runs;
%     list_pa(end+1)= principal_angle;
% end
% 
% plot(0:40,list_pa(:,2:end));
% ylabel("Principal Angle");
% xlabel("Variance of the cluster centers");



% rapprocher centroid petit a petit
% calcul moment ordre 3 modele

%%

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
%%
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

function X = kr(U,varargin)
    %KR Khatri-Rao product.
    %   kr(A,B) returns the Khatri-Rao product of two matrices A and B, of 
    %   dimensions I-by-K and J-by-K respectively. The result is an I*J-by-K
    %   matrix formed by the matching columnwise Kronecker products, i.e.
    %   the k-th column of the Khatri-Rao product is defined as
    %   kron(A(:,k),B(:,k)).
    %
    %   kr(A,B,C,...) and kr({A B C ...}) compute a string of Khatri-Rao 
    %   products A o B o C o ..., where o denotes the Khatri-Rao product.
    %
    %   See also kron.

    %   Version: 21/10/10
    %   Authors: Laurent Sorber (Laurent.Sorber@cs.kuleuven.be)

    if ~iscell(U), U = [U varargin]; end
    K = size(U{1},2);
    if any(cellfun('size',U,2)-K)
        error('kr:ColumnMismatch', ...
              'Input matrices must have the same number of columns.');
    end
    J = size(U{end},1);
    X = reshape(U{end},[J 1 K]);
    for n = length(U)-1:-1:1
        I = size(U{n},1);
        A = reshape(U{n},[1 I K]);
        X = reshape(bsxfun(@times,A,X),[I*J 1 K]);
        J = I*J;
    end
    X = reshape(X,[size(X,1) K]);
end


