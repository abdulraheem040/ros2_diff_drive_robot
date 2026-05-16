from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

import os

def generate_launch_description():

    urdf_path = os.path.expanduser(
        '~/urdf_robot_ws/src/my_robot_description/urdf/my_robot.urdf'
    )

    return LaunchDescription([

        # Start Gazebo
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),

        # Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            arguments=[urdf_path],
            output='screen'
        ),

        # Spawn Robot in Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'my_robot',
                '-file', urdf_path
            ],
            output='screen'
        )
    ])