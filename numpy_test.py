import open3d as o3d
import numpy as np
print("Modules loaded successfully")
np.set_printoptions(threshold = np.inf) # displaying the whole array in numpy



pcd = o3d.io.read_point_cloud("fragment.ply")
pcl_points = np.asarray(pcd.points) # creating a numpy array out of the point clouds