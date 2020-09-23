%%Use this script to calculate cortical area (as an average of 20 maps, for
%%each major region of hand - Rows Ordered: D1, D2, D3, D4, D5, P

primate = "macaca"

primate_locations = strcat(primate,'_locations');
primate_regions = strcat('region_prop_',primate);

%load locations
load(primate_locations)

%load region prop
load(primate_regions)

primate_cort_area = zeros(20,6);

for i=1:20
    primate_map_num = strcat(primate,'_map',num2str(i));
    load(primate_map_num)
   [hand_regions,count_size,~] = cortical_area_size(W, locations, 'main', 'py', region_prop);
   count_size = count_size./sum(count_size)*100;
   primate_cort_area(i,1:5) = count_size(1:5);
   primate_cort_area(i,6) = sum(count_size(6:7)) ;
end

for i = 1:6
primate_cort_area(i) = sum(primate_cort_area(:,i))/20
end