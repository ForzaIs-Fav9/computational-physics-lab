import numpy as np
import matplotlib.pyplot as plt


def simulate_projectile(
    initial_speed=20.0,
    launch_angle_deg=45.0,
    gravity=9.81,
    dt=0.01
):
    """
    Simulates projectile motion using Euler integration.

    Parameters:
        initial_speed (float): Initial launch speed (m/s)
        launch_angle_deg (float): Launch angle (degrees)
        gravity (float): Acceleration due to gravity (m/s^2)
        dt (float): Time step (seconds)

    Returns:
        x_positions (list), y_positions (list)
    """

    angle_rad = np.radians(launch_angle_deg)

    vx = initial_speed * np.cos(angle_rad)
    vy = initial_speed * np.sin(angle_rad)

    x = 0.0
    y = 0.0

    x_positions = []
    y_positions = []

    while y >= 0:
        x_positions.append(x)
        y_positions.append(y)

        # Update position
        x += vx * dt
        y += vy * dt

        # Update velocity
        vy -= gravity * dt

    return x_positions, y_positions


def plot_trajectory(x, y):
    plt.figure()
    plt.plot(x, y)
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Vertical Height (m)")
    plt.title("Projectile Motion (Gravity Only)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    x_vals, y_vals = simulate_projectile(
        initial_speed=25,
        launch_angle_deg=50
    )

    plot_trajectory(x_vals, y_vals)
