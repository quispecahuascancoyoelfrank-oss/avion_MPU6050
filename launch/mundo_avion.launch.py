from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable
from launch_ros.actions import Node
import os

def generate_launch_description():
    # Ruta del mundo SDF
    world_path = os.path.join(
        os.getenv('HOME'),
        'avion_ws', 'src', 'avion', 'models', 'mundo_avion.sdf'
    )

    # Ruta del plugin .so
    plugin_path = os.path.join(
        os.getenv('HOME'),
        'avion_ws', 'src', 'avion', 'models'
    )

    return LaunchDescription([
        # Exportar el path del plugin (para Gazebo)
        SetEnvironmentVariable(
            name='IGN_GAZEBO_SYSTEM_PLUGIN_PATH',
            value=plugin_path
        ),

        # Lanzar Gazebo con el mundo del avión
        ExecuteProcess(
            cmd=['ign', 'gazebo', world_path],
            output='screen'
        ),

        # Bridge entre ROS 2 <-> Gazebo
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=['/set_pose_topic@geometry_msgs/msg/Pose@gz.msgs.Pose'],
            output='screen'
        ),
    ])
