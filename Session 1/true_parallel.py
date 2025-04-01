import multiprocessing
import time
import random
from functools import partial


def monte_carlo_pi(points):
    """Estimate Pi using Monte Carlo method - CPU intensive and parallelizable"""
    inside_circle = 0
    random.seed()  # Ensure different random sequences in each process

    for _ in range(points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        # Check if point lies inside unit circle
        if x * x + y * y <= 1:
            inside_circle += 1

    return inside_circle


def run_simulation(total_points, num_processes):
    points_per_process = total_points // num_processes
    start_time = time.time()

    with multiprocessing.Pool(processes=num_processes) as pool:
        # Distribute work across processes
        results = pool.map(monte_carlo_pi, [points_per_process] * num_processes)

    total_inside = sum(results)
    pi_estimate = 4 * total_inside / total_points
    duration = time.time() - start_time
    return pi_estimate, duration


def single_process(total_points):
    start_time = time.time()
    inside = monte_carlo_pi(total_points)
    pi_estimate = 4 * inside / total_points
    duration = time.time() - start_time
    return pi_estimate, duration


if __name__ == "__main__":
    # Total points to simulate - large number for CPU intensity
    TOTAL_POINTS = 10_000_000

    # Single process baseline
    pi_single, time_single = single_process(TOTAL_POINTS)
    print(f"Single process: Pi ≈ {pi_single:.6f}, Time: {time_single:.2f} seconds")

    # Test with different numbers of processes
    cpu_counts = [1, 2, 4, 8, 16, 32, 64]  # Adjust based on your CPU cores
    for cores in cpu_counts:
        pi_multi, time_multi = run_simulation(TOTAL_POINTS, cores)
        speedup = time_single / time_multi
        print(
            f"Processes: {cores:2d}, Pi ≈ {pi_multi:.6f}, "
            f"Time: {time_multi:.2f} seconds, Speedup: {speedup:.2f}x"
        )

    # Print actual Pi for reference
    import math

    print(f"Actual Pi: {math.pi:.6f}")
