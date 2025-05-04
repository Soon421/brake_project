import pandas as pd
import matplotlib.pyplot as plt

# Load logs
imu1 = pd.read_csv("imu1_log.csv", names=["timestamp", "accX", "accY", "accZ", "gyroX", "gyroY", "angleX", "angleY", "gyroZ"], header=None)
imu2 = pd.read_csv("imu2_log.csv", names=["timestamp", "accX", "accY", "accZ", "gyroX", "gyroY", "angleX", "angleY", "gyroZ"], header=None)

# Optional: sort by time
imu1 = imu1.sort_values(by="timestamp")
imu2 = imu2.sort_values(by="timestamp")

# === IMU1 Plot ===
plt.figure(figsize=(12, 8))
plt.suptitle("IMU1 Measurements")

plt.subplot(3, 1, 1)
plt.plot(imu1["timestamp"], imu1["angleX"], label="angleX", color="blue")
plt.ylabel("Roll (angleX) [deg]")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(imu1["timestamp"], imu1["angleY"], label="angleY", color="green")
plt.ylabel("Pitch (angleY) [deg]")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(imu1["timestamp"], imu1["gyroZ"], label="gyroZ", color="purple")
plt.ylabel("Yaw rate (gyroZ) [deg/s]")
plt.xlabel("Timestamp [s]")
plt.grid(True)

plt.tight_layout()
plt.show()

# === IMU2 Plot ===
plt.figure(figsize=(12, 8))
plt.suptitle("IMU2 Measurements")

plt.subplot(3, 1, 1)
plt.plot(imu2["timestamp"], imu2["angleX"], label="angleX", color="red")
plt.ylabel("Roll (angleX) [deg]")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(imu2["timestamp"], imu2["angleY"], label="angleY", color="orange")
plt.ylabel("Pitch (angleY) [deg]")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(imu2["timestamp"], imu2["gyroZ"], label="gyroZ", color="brown")
plt.ylabel("Yaw rate (gyroZ) [deg/s]")
plt.xlabel("Timestamp [s]")
plt.grid(True)

plt.tight_layout()
plt.show()

