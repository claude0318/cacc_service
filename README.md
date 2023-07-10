# CACC Service 

This ros2 package consists of two ros2 nodes, a dummy OBU node acting as a publisher, and a CACC service node acting as a subscriber and publisher.

The CACC service node subscribes to 'acceleration_topic' to which the OBU publishes, and publishes output to topic topic 'topic'.


# Installation

### 1. Create ros2 workspace

First create your workspace folder with a src folder: 

```
mkdir local_ws
mkdir local_ws/src
```

Install possible dependencies and generate folders inside with (change 'humble' to your ros2 distro):

```
rosdep install -i --from-path src --rosdistro humble -y
```

Clone this repository into local_ws/src so you have to following structure:

local_ws/src/cacc_service/



### 2. Build package

- install dependencies inside root of local_ws/:

```
rosdep install -i --from-path src --rosdistro humble -y
```

- build package with colcon

```
colcon build --packages-select cacc_service
```

### 3. Run nodes 

- in two new terminals, in each   , source inside local_ws/:

```
  source install/setup.bash
```
- run each node in own terminal with

```
ros2 run cacc_service cacc_service   
```

```
ros2 run cacc_service obu_sensor
```


After changing code, run steps 2. and 3. again. If adding dependencies, update your package.xml. Overall workflow can be found here.