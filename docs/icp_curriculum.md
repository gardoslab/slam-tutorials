# 2D LiDAR SLAM Curriculum: From Basics to ICP

This curriculum is designed to take you from the fundamental concepts of handling LiDAR data to implementing advanced scan matching algorithms like Iterative Closest Point (ICP).

## Module 1: Foundations of LiDAR and Data Representation

**Goal:** Understand the shape of the data and how to manipulate it in 2D space.

* **1.1 Polar to Cartesian Math:** Converting raw `(distance, angle)` LiDAR readings into `(x, y)` points.
  * 📓 **Notebook:** `1a_polar_to_cartesian.ipynb` (Interactive plots showing raw LiDAR rays converting to points)
* **1.2 Synthetic Data Generation:** Creating controlled environments (walls, corners, boxes) in Python to test algorithms without real-world sensor noise.
* **1.3 Introduction to Transforms:** Mathematically translating and rotating arrays of 2D points using transformation matrices (Homogeneous coordinates).
  * 📓 **Notebook:** `1b_matrix_transforms.ipynb` (Visualizing translation and rotation of synthetic shapes)
* **1.4 The Occupancy Grid:** Building a simple 2D grid in Python (e.g., using a NumPy array) and mapping Cartesian points into grid cells.
  * 💻 **Script:** `1c_basic_occupancy_grid.py` (Creating a discrete grid and filling cells based on our synthetic data)

## Module 2: Basic Scan Matching (The Brute-Force Approach)

**Goal:** Understand the core concept of alignment by minimizing an error function.

* **2.1 Translation-Only Brute Force:** Searching a grid of possible X/Y movements to find the lowest error between two scans.
  * 💻 **Script:** `01_synthetic_scan_matching.py` *(Already completed!)*
* **2.2 Adding Rotation:** Expanding the search grid to include heading/yaw ($\theta$). Understanding how the "curse of dimensionality" makes brute force computationally expensive as you add rotation.
  * 💻 **Script:** `2a_brute_force_with_rotation.py` (Expanding our first script to search 3 degrees of freedom)
* **2.3 Defining the Cost Function:** Formalizing the Sum of Squared Errors (SSE) or Mean Squared Error (MSE) to quantify "how well do these two scans align?"
  * 📓 **Notebook:** `2b_cost_function_surface.ipynb` (Plotting a 3D surface of the error space to visually see the "bowl" we want to minimize)

## Module 3: Introduction to Optimization

**Goal:** Learn how to find the best alignment mathematically without checking every single possibility.

* **3.1 The Limits of Brute Force:** Discussing processing time and real-time requirements for robotics.
* **3.2 Gradient Descent Basics:** A conceptual overview of "walking down the hill" to find the minimum error.
  * 📓 **Notebook:** `3a_gradient_descent_toy.ipynb` (A simple 1D/2D optimization problem to understand learning rates and convergence)
* **3.3 Non-Linear Least Squares:** Introduction to the Gauss-Newton algorithm.
* **3.4 Optimization for Scan Matching:** Applying Gauss-Newton to iteratively adjust the transformation `(dx, dy, dtheta)` to minimize the distance between a scan and a map.
  * 💻 **Script:** `3b_gauss_newton_alignment.py` (Replacing brute-force with mathematical optimization)

## Module 4: Iterative Closest Point (ICP) - Point-to-Point

**Goal:** Implement the standard ICP algorithm to align two unknown point clouds.

* **4.1 The Correspondence Problem:** How do we know which point in Scan A matches which point in Scan B?
* **4.2 Nearest Neighbor Search:** Using KD-Trees to efficiently find the closest points between two scans.
  * 📓 **Notebook:** `4a_nearest_neighbors_kdtree.ipynb` (Experimenting with `scipy.spatial.KDTree` and visualizing matched pairs)
* **4.3 Singular Value Decomposition (SVD):** The magic math! Using SVD to calculate the optimal rotation and translation matrix in a single closed-form step *once correspondences are known*.
  * 💻 **Script:** `4b_svd_solver.py` (Given two *perfectly matched* point clouds, find the transform)
* **4.4 The ICP Loop:** Combining correspondence and SVD to iterate until convergence.
  * 💻 **Script:** `4c_vanilla_icp.py` (The complete point-to-point ICP algorithm)

## Module 5: Advanced ICP - Point-to-Line

**Goal:** Solve common failure cases in standard ICP, such as sliding along featureless corridors.

* **5.1 The "Corridor Problem":** Why point-to-point ICP fails when looking at a flat wall (it can slide the scan sideways without changing the error).
  * 📓 **Notebook:** `5a_the_corridor_problem.ipynb` (Demonstrating the failure of standard ICP on a featureless hallway)
* **5.2 Estimating Surface Normals:** Calculating the perpendicular direction (normal) of the walls in the reference scan or map.
* **5.3 Point-to-Line Metric:** Changing the error function to measure the distance from a point to the *surface plane* of the target, rather than a specific target point.
* **5.4 Solving Point-to-Line ICP:** Implementing the optimization loop for the new error metric.
  * 💻 **Script:** `5b_point_to_line_icp.py` (Implementing normal estimation and the upgraded ICP algorithm)

## Module 6: Putting it into
**Goal:** Integrate the scan matcher into a continuous mapping loop.
*   **6.1 Scan-to-Map Matching:** Instead of matching Scan $t$ to Scan $t-1$, match Scan $t$ against the global Occupancy Grid to eliminate cumulative drift.
*   **6.2 Probabilistic Map Updating:** Using Bayes' theorem or log-odds to update the occupancy probabilities of grid cells as new, aligned scans come in.
*   **6.3 Drift and Loop Closure:** A conceptual overview of why drift still happens eventually, and how recognizing a previously visited place (loop closure) pulls the whole map back into alignment using graph optimization.