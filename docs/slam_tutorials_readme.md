# 2D LiDAR SLAM Tutorials

Welcome to the 2D LiDAR SLAM tutorials! This repository serves as a guide and codebase for understanding Simultaneous Localization and Mapping from the ground up.

## Introduction to 2D LiDAR SLAM

### 1. Sensor Data Collection
LiDAR sensors collect data in **polar coordinates**. Each measurement is represented as a distance (radius) from the sensor and an angle. This gives the robot an egocentric view of its immediate surroundings.

### 2. Coordinate Transformation
To make this data useful for a global map, we map these polar points into **Cartesian space** (X, Y) using basic trigonometry:
*   **X-coordinate**: `distance * cos(angle)`
*   **Y-coordinate**: `distance * sin(angle)`

These calculated values are then added to the robot's current estimated position to place the points in the world.

### 3. Occupancy Grid Representation
The **occupancy grid** utilizes a fixed world coordinate system. The origin is typically where the robot first powers on and takes its initial scan. Each cell in this grid represents a specific physical area in the environment and stores a probability value indicating the likelihood of that space being occupied by an obstacle.

### 4. Pose Estimation and Scan Matching
Relying solely on dead reckoning (like an Inertial Measurement Unit, or IMU) leads to rapid positional drift over time due to accumulating tiny measurement errors. 

**Scan matching** mitigates this drift. By aligning new incoming LiDAR scans with the existing occupancy grid map (or the previous scan), the robot can calculate how much it has actually moved. This turns the map into a reference to continuously correct the robot's pose.

---

## Learning Curriculum

1. **Scan-to-Scan Matching Fundamentals:** Aligning two consecutive scans using simple brute-force or correlation methods to understand local relative motion.
2. **Scan-to-Map Integration:** Aligning current scans against an established occupancy grid to correct accumulated dead reckoning drift.
3. **Optimization Techniques:** Introducing non-linear least squares solvers (like Gauss-Newton) to mathematically find the optimal transformation.
4. **Iterative Closest Point (ICP):** Exploring point-to-point and point-to-line ICP algorithms for robust and precise scan alignment.