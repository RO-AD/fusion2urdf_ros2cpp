# fusion2urdf ROS2_c++ package

Inspired by [syuntoku14/fusion2urdf](https://github.com/syuntoku14/fusion2urdf) and [dheena2k2/fusion2urdf-ros2](https://github.com/dheena2k2/fusion2urdf-ros2), this repertoire is ADDIN, who converts it into a ROS2 c++ package and edited to export description package suited for ROS2 ament_cmake type build. Check out [syuntoku14/fusion2urdf](https://github.com/syuntoku14/fusion2urdf) for converting fusion360 model to robot description package of ROS1.
## Difference
* ROS2 C++ Package
* Color reflection  
![image](https://user-images.githubusercontent.com/68213792/180215132-008cf195-fc48-4943-8203-af7aecdd7c0b.png)

### rviz  
![image](https://user-images.githubusercontent.com/68213792/180215308-a7656d41-46b1-470a-9b25-33fec6f86b2d.png)  
  
If you urdf conversion in xacro, it can be used in unity, omniverse  
### Unity  
![image](https://user-images.githubusercontent.com/68213792/180215772-2f648ed8-a74d-4b7f-9f4b-340f41c546c2.png)
### Omniverse  
![image](https://user-images.githubusercontent.com/68213792/180215935-dc1ff029-65ee-4e18-922e-01d2c5717a6a.png)


## Installation

Run the following command in your shell.

##### Windows (In PowerShell)

```powershell
cd <path to fusion2urdf-ros2cpp>
Copy-Item ".\URDF_Exporter_Ros2cpp\" -Destination "${env:APPDATA}\Autodesk\Autodesk Fusion 360\API\Scripts\" -Recurse
```

##### macOS (In bash or zsh)

```bash
cd <path to fusion2urdf-ros2cpp>
cp -r ./URDF_Exporter_Ros2cpp "$HOME/Library/Application Support/Autodesk/Autodesk Fusion 360/API/Scripts/"
```
## What is this script?
This is a fusion 360 script to export urdf from fusion 360 directly.

This exports:
* .urdf file of your model
* .launch.py files to simulate your robot on gazebo and rviz
* .stl files of your model

#### In your ROS environment

Place the generated _description package directory in your own ROS workspace. "model_ws" is used in this example.
Then, run catkin_make in catkin_ws.

```bash
cd ~/model_ws/
colcon build
```

Now you can see your robot in rviz by using the following command.

Open a new terminal

```bash
cd ~/model_ws/
source install/setup.bash
ros2 launch (whatever your robot_name is)_description display.launch.py
```

<img src="https://github.com/syuntoku14/fusion2urdf/blob/images/rviz_robot.png" alt="rviz" title="rviz" width="300" height="300">

If you want to simulate your robot on gazebo, just run
```bash
ros2 launch (whatever your robot_name is)_description gazebo.launch.py
```

**Enjoy your Fusion 360 and ROS2 life!**
