import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("heart_rate.csv")

# Separate resting and active rates
resting = df[df['activity'] == 'rest']['heart_rate']
active = df[df['activity'] != 'rest']['heart_rate']

print("---- HEART RATE SUMMARY ----")
print(f"Resting Heart Rate: Mean={resting.mean():.2f}, Min={resting.min()}, Max={resting.max()}")
print(f"Active Heart Rate:  Mean={active.mean():.2f}, Min={active.min()}, Max={active.max()}")

# Plot
plt.figure(figsize=(7,5))
plt.plot(df['heart_rate'], marker='o')
plt.title("Heart Rate Over Time")
plt.xlabel("Time Index")
plt.ylabel("Heart Rate (bpm)")
plt.grid(True)
plt.show()

# Plot Resting vs Active comparison
plt.figure(figsize=(7,5))
plt.bar(["Resting", "Active"],
        [resting.mean(), active.mean()])
plt.title("Average Resting vs Active Heart Rate")
plt.ylabel("Heart Rate (bpm)")
plt.show()

# Save summary to file
with open("heart_rate_summary.txt", "w") as f:
    f.write("---- HEART RATE SUMMARY ----\n")
    f.write(f"Resting Heart Rate: Mean={resting.mean():.2f}, Min={resting.min()}, Max={resting.max()}\n")
    f.write(f"Active Heart Rate:  Mean={active.mean():.2f}, Min={active.min()}, Max={active.max()}\n")                  



