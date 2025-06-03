# physicalai_teleop

A ROS2 package for teleoperating CRANE+ V2 robot.

## Features
- Keyboard teleoperation in joint space

## Installation
1. Setup Environment

Follow https://github.com/AI-Robot-Book-Humble/docker-ros2-desktop-ai-robot-book-humble to setup the Docker environment
Launch CRANE+ V2 manipulator in Gazebo by running
```bash
ros2 launch crane_plus_gazebo crane_plus_with_table.launch.py
```

2. Clone this repository into your ROS2 workspace:

```bash
cd ~/pai_ws/src
git clone https://github.com/matsuolab/physicalai_teleop.git
```

3. Install dependencies

```bash
cd ~/pai_ws
rosdep install --from-paths src --ignore-src -r -y
```

4. Build the package:

```bash
colcon build --symlink-install --packages-select physicalai_teleop
```

5. Source your workspace:

```bash
source install/setup.bash
```

## Usage
```bash
ros2 run physicalai_teleop teleop_keyboard
```

### Key Mappings

| Key | Function |
|-----|----------|
| Q/E | Select joint (1-4) |
| W/S | Increase/Decrease selected joint angle |
| R/F | Increase/Decrease all joint angles (coarse adjustment) |
| O | Open gripper |
| C | Close gripper |
| X | Reset robot to vertical (all-zero) position |
| ESC | Quit |

The joints are:
- Joint 1: Base rotation
- Joint 2: Shoulder
- Joint 3: Elbow
- Joint 4: Wrist