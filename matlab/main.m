clear;

%%
% Making varying the variance
% list_pa = 0;
% for var = 0:40
%     centers_v = get_centers(5,8,var);
%     centers_w = get_centers(5,8,var);
%     V = get_data(centers_v,5,1000);
%     W = get_data(centers_w,5,1000);
%     principal_angle = principal_angle_kronecker(V,W);
%     list_pa(end+1)= principal_angle;    
% end
% 
% plot(list_pa(:,2:end));



%% 
npoints = 1000;
list_pa = 0;
dist = 0;
for d = 0:100
    disp(d);
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