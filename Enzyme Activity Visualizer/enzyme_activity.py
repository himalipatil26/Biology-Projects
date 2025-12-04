import numpy as np
import matplotlib.pyplot as plt

# --- Enzyme activity model functions ---

def enzyme_activity_temp(temp, optimum=37, width=10):
    """Returns relative enzyme activity vs temperature."""
    return np.exp(-((temp - optimum) ** 2) / (2 * width ** 2))


def enzyme_activity_pH(ph, optimum=7, width=1.5):
    """Returns relative enzyme activity vs pH."""
    return np.exp(-((ph - optimum) ** 2) / (2 * width ** 2))


# --- Temperature Curve ---

temp = np.linspace(0, 80, 400)
activity_temp = enzyme_activity_temp(temp)

plt.figure(figsize=(7, 4))
plt.plot(temp, activity_temp)
plt.title("Enzyme Activity vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Relative Activity")
plt.grid(True)
plt.show()

# --- pH Curve ---

ph = np.linspace(0, 14, 400)
activity_ph = enzyme_activity_pH(ph)

plt.figure(figsize=(7, 4))
plt.plot(ph, activity_ph)
plt.title("Enzyme Activity vs pH")
plt.xlabel("pH Level")
plt.ylabel("Relative Activity")
plt.grid(True)
plt.show()

# --- Combined Curve ---

combined_activity = enzyme_activity_temp(temp[:, None]) * enzyme_activity_pH(ph[None, :])
plt.figure(figsize=(8, 6))
plt.imshow(combined_activity, extent=[0, 14, 0, 80], origin='lower', aspect='auto', cmap='viridis')
plt.colorbar(label='Relative Activity')
plt.title("Enzyme Activity vs Temperature and pH")
plt.xlabel("pH Level")
plt.ylabel("Temperature (°C)")
plt.show()

# --- 3D Surface Plot ---

from mpl_toolkits.mplot3d import Axes3D
temp_grid, ph_grid = np.meshgrid(temp, ph)
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')      
ax.plot_surface(temp_grid, ph_grid, combined_activity.T, cmap='viridis')
ax.set_title("3D Surface Plot of Enzyme Activity")
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("pH Level")
ax.set_zlabel("Relative Activity")
plt.show()

# --- Contour Plot ---

plt.figure(figsize=(8, 6))
contour = plt.contourf(ph, temp, combined_activity, levels=50, cmap='viridis')
plt.colorbar(label='Relative Activity')
plt.title("Contour Plot of Enzyme Activity")
plt.xlabel("pH Level")
plt.ylabel("Temperature (°C)")
plt.show()

# --- Heatmap ---

plt.figure(figsize=(8, 6))  
plt.imshow(combined_activity, extent=[0, 14, 0, 80], origin='lower', aspect='auto', cmap='viridis')
plt.colorbar(label='Relative Activity')     
plt.title("Heatmap of Enzyme Activity")
plt.xlabel("pH Level")
plt.ylabel("Temperature (°C)")
plt.show()





