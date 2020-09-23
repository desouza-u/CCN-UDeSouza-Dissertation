function [ distance_rtl, distance_fingertip ] = cortical_distances(primate)
%calculates rtl & fingertip centroid distance

rtl_coords = strcat(primate,'_coords_rtl');
fingertip_coords = strcat(primate,'_coords_fingertip');

%load centroid data
rtl_coords = load(rtl_coords)
fingertip_coords = load(fingertip_coords)

%convert to double
rtl_coords = struct2array(rtl_coords);
fingertip_coords = struct2array(fingertip_coords);

%calculate distances
distance_rtl = pdist(rtl_coords);
distance_fingertip = pdist(fingertip_coords);

end

