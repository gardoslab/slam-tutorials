import numpy as np
import matplotlib.pyplot as plt

def generate_synthetic_wall(num_points=50, length=10.0):
    """Generates a synthetic LiDAR scan of a flat wall 5 meters ahead."""
    # X coordinates spread across the wall
    x = np.linspace(-length/2, length/2, num_points)
    # Y coordinates are a constant 5 meters away
    y = np.ones(num_points) * 5.0 
    return np.vstack((x, y)).T

def apply_movement(scan, dx, dy):
    """Simulates robot movement by shifting the scan."""
    # If the robot moves forward (+dy) and right (+dx), 
    # the wall appears to move backward (-dy) and left (-dx) relative to the robot.
    moved_scan = np.copy(scan)
    moved_scan[:, 0] -= dx
    moved_scan[:, 1] -= dy
    return moved_scan

def brute_force_scan_match(scan1, scan2, search_range=1.0, step=0.1):
    """
    A simple brute-force search to find the translation (dx, dy)
    that best aligns scan2 onto scan1.
    """
    best_dx, best_dy = 0.0, 0.0
    min_error = float('inf')

    # Create a grid of possible movements to test
    translations = np.arange(-search_range, search_range + step, step)

    for dx in translations:
        for dy in translations:
            # Shift scan2 by the test translation
            test_scan = np.copy(scan2)
            test_scan[:, 0] += dx
            test_scan[:, 1] += dy

            # Calculate error (sum of squared distances between corresponding points)
            # Note: In real life, points don't map 1:1 perfectly, so you'd use a 
            # Nearest Neighbor search here. For this perfectly synthetic data, 
            # direct array subtraction works perfectly.
            error = np.sum((scan1 - test_scan)**2)

            # Keep track of the translation that yields the lowest error
            if error < min_error:
                min_error = error
                best_dx = dx
                best_dy = dy

    return best_dx, best_dy

if __name__ == "__main__":
    print("Generating synthetic data...")
    
    # 1. Generate base scan (Time = 0)
    scan_t0 = generate_synthetic_wall()

    # 2. Simulate robot movement 
    # Let's say the robot moved 0.6m to the right and 0.3m forward
    true_dx = 0.6
    true_dy = 0.3
    scan_t1 = apply_movement(scan_t0, true_dx, true_dy)

    print(f"True Robot Movement: dx={true_dx:.2f}, dy={true_dy:.2f}")
    print("Running brute-force scan matching...")

    # 3. Perform scan matching to estimate movement
    estimated_dx, estimated_dy = brute_force_scan_match(scan_t0, scan_t1)

    print(f"Estimated Movement:  dx={estimated_dx:.2f}, dy={estimated_dy:.2f}")

    # 4. Visualize the results
    plt.figure(figsize=(10, 6))
    
    # Plot original scan
    plt.scatter(scan_t0[:, 0], scan_t0[:, 1], c='blue', label='Scan t0 (Reference)', alpha=0.6)
    
    # Plot new scan (unaligned)
    plt.scatter(scan_t1[:, 0], scan_t1[:, 1], c='red', label='Scan t1 (Uncorrected)', alpha=0.6)
    
    # Plot corrected scan using our estimated movement
    corrected_scan = np.copy(scan_t1)
    corrected_scan[:, 0] += estimated_dx
    corrected_scan[:, 1] += estimated_dy
    plt.scatter(corrected_scan[:, 0], corrected_scan[:, 1], c='green', marker='x', label='Scan t1 (Corrected/Matched)', alpha=0.8)

    plt.title("Synthetic Scan Matching - Brute Force Translation")
    plt.xlabel("X (meters)")
    plt.ylabel("Y (meters)")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

    