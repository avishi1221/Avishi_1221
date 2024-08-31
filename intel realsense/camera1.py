import pyrealsense2 as rs
import numpy as np
import open3d as o3d
import cv2

# Configure and start the RealSense camera
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipeline.start(config)

# Function to convert depth image to point cloud
def depth_to_point_cloud(depth_image, intrinsics):
    height, width = depth_image.shape
    u, v = np.meshgrid(np.arange(width), np.arange(height))
    z = depth_image.astype(float) / 1000.0  # Convert depth from mm to meters
    x = (u - intrinsics[0]) * z / intrinsics[2]
    y = (v - intrinsics[1]) * z / intrinsics[2]
    points = np.stack([x, y, z], axis=-1).reshape(-1, 3)
    return o3d.geometry.PointCloud(o3d.utility.Vector3dVector(points))

try:
    while True:
        # Wait for a frame and get the depth and color frames
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        if not depth_frame or not color_frame:
            continue

        # Convert depth frame to numpy array
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Convert depth image to point cloud
        intrinsics = [320, 240, 1]  # Assuming a basic camera model for simplicity
        point_cloud = depth_to_point_cloud(depth_image, intrinsics)

        # Visualize the point cloud
        o3d.visualization.draw_geometries([point_cloud], window_name="Point Cloud")

        # Optionally display the color image
        cv2.imshow('Color Image', color_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    pipeline.stop()
    cv2.destroyAllWindows()
