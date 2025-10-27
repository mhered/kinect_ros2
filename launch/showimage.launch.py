import launch_ros

import launch


def generate_launch_description():
    return launch.LaunchDescription(
        [
            launch_ros.actions.Node(
                package="kinect_ros2",
                executable="kinect_ros2_node",
                namespace="kinect"
            ),
            launch_ros.actions.Node(
                package="image_tools",
                executable="showimage",
                parameters=[{"window_name": "RGB"}],
                remappings=[("image", "kinect/image_raw")],
            ),
            launch_ros.actions.Node(
                package="image_tools",
                executable="showimage",
                parameters=[{"window_name": "Depth"}],
                remappings=[("image", "kinect/depth/image_raw")],
            ),
        ]
    )
