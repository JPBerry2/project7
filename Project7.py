import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# --- PART 1: Lorenz System (Butterfly Effect) ---
# Parameters sigma, rho, and beta represent physical properties of the system [cite: 8]
def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return x_dot, y_dot, z_dot


def run_simulation(r_val):
    dt = 0.01
    num_steps = 10000

    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)

    # Initial values [cite: 6]
    xs[0], ys[0], zs[0] = (0., 1., 1.05)

    # Calculation loop using Euler Method to solve the ODEs [cite: 7]
    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], r=r_val)
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)

    # --- Step 1: 3D Phase Space ---
    print(f"\nDisplaying 3D Plot for r={r_val}...")
    fig_3d = plt.figure(figsize=(8, 6))
    ax = fig_3d.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs, lw=0.7, color='purple')
    ax.set_title(f"3D Lorenz Attractor (rho = {r_val})")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    plt.show()

    # --- Step 2: X Time-Series ---
    print("Displaying X time-series...")
    plt.figure(figsize=(10, 4))
    plt.plot(xs, color='r', lw=0.8)
    plt.title(f"X-Coordinate vs Time (rho = {r_val})")
    plt.ylabel("X")
    plt.xlabel("Steps")
    plt.grid(True, alpha=0.3)
    plt.show()

    # --- Step 3: Y Time-Series ---
    print("Displaying Y time-series...")
    plt.figure(figsize=(10, 4))
    plt.plot(ys, color='g', lw=0.8)
    plt.title(f"Y-Coordinate vs Time (rho = {r_val})")
    plt.ylabel("Y")
    plt.xlabel("Steps")
    plt.grid(True, alpha=0.3)
    plt.show()

    # --- Step 4: Z Time-Series ---
    print("Displaying Z time-series...")
    plt.figure(figsize=(10, 4))
    plt.plot(zs, color='b', lw=0.8)
    plt.title(f"Z-Coordinate vs Time (rho = {r_val})")
    plt.ylabel("Z")
    plt.xlabel("Steps")
    plt.grid(True, alpha=0.3)
    plt.show()


# --- PART 2: Queueing Theory (M/M/1 Analysis) ---
def run_queueing_analysis():
    print("\n" + "=" * 50)
    print("STARTING PART 2: M/M/1 QUEUEING ANALYSIS")
    print("=" * 50)

    # Gateway Measurements [cite: 11]
    lam_orig = 125.0  # Mean arrival rate (pps)
    mu_orig = 1 / 0.002  # Service rate (500 pps, derived from 2ms service time)

    # Mathematical analysis for gateway [cite: 12]
    rho_val = lam_orig / mu_orig
    K = 12
    # Probability of overflow for an M/M/1/K system [cite: 12]
    p_loss = (rho_val ** K * (1 - rho_val)) / (1 - rho_val ** (K + 1))

    print(f"Original Arrival Rate (lambda): {lam_orig} pps")
    print(f"Original Service Rate (mu): {mu_orig} pps")
    print(f"Utilization (rho): {rho_val}")
    print(f"Probability of overflow with 12 buffers: {p_loss:.10f}")

    # Scaling Factor Analysis (k) [cite: 14]
    k_vals = np.linspace(1, 10, 100)

    # Formulas for scaled system metrics [cite: 16, 17, 18, 19]
    util = (k_vals * lam_orig) / (k_vals * mu_orig)  # Utilization remains constant
    thr = k_vals * lam_orig  # Throughput grows linearly
    en = util / (1 - util)  # Mean number remains constant
    et = 1 / (k_vals * (mu_orig - lam_orig))  # Mean time decreases inversely

    # Sequential Visualizations for Part 2 [cite: 20]

    # Plot A: Utilization
    print("\nDisplaying Plot A: Utilization...")
    plt.figure(figsize=(8, 5))
    plt.plot(k_vals, util, color='r', lw=2)
    plt.axhline(y=rho_val, color='gray', linestyle='--')
    plt.title("a. Utilization (rho): UNCHANGED")
    plt.xlabel("Scaling Factor (k)")
    plt.ylabel("Utilization")
    plt.grid(True, alpha=0.3)
    plt.show()

    # Plot B: Throughput
    print("Displaying Plot B: Throughput...")
    plt.figure(figsize=(8, 5))
    plt.plot(k_vals, thr, color='g', lw=2)
    plt.title("b. Throughput (X): Linear Growth")
    plt.xlabel("Scaling Factor (k)")
    plt.ylabel("Throughput (pps)")
    plt.grid(True, alpha=0.3)
    plt.show()

    # Plot C: Mean Number
    print("Displaying Plot C: Mean Number in System...")
    plt.figure(figsize=(8, 5))
    plt.plot(k_vals, en, color='b', lw=2)
    plt.axhline(y=rho_val / (1 - rho_val), color='gray', linestyle='--')
    plt.title("c. Mean Number (E[N]): UNCHANGED")
    plt.xlabel("Scaling Factor (k)")
    plt.ylabel("E[N]")
    plt.grid(True, alpha=0.3)
    plt.show()

    # Plot D: Mean Time
    print("Displaying Plot D: Mean Time in System...")
    plt.figure(figsize=(8, 5))
    plt.plot(k_vals, et, color='brown', lw=2)
    plt.title("d. Mean Time (E[T]): Decreases (Inverse 1/k)")
    plt.xlabel("Scaling Factor (k)")
    plt.ylabel("E[T] (seconds)")
    plt.grid(True, alpha=0.3)
    plt.show()


# --- MAIN LOOP ---
if __name__ == "__main__":
    print("CST-305: Project 7 – Code Errors and the Butterfly Effect [cite: 1]")
    print("Part 1: Lorenz System Visualization [cite: 3]")
    print("Close each plot window to proceed to the next visualization.")

    while True:
        choice = input("\nEnter rho (r) value for Lorenz (or 'n' to move to Part 2): ").strip().lower()
        if choice == 'n':
            break
        try:
            run_simulation(float(choice))
        except ValueError:
            print("Please enter a valid numeric value for rho.")

    # Execute Part 2 after user exits Part 1 loop
    run_queueing_analysis()
    print("\nFinal simulation complete. Ready for documentation[cite: 43].")