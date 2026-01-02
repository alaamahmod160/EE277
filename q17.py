import numpy as np
import matplotlib.pyplot as plt

# Parameters
np.random.seed(1)
sample_sizes = [10, 20, 30, 40]
num_repeats = 1000
pop_min, pop_max = -40, 40

plt.figure(figsize=(10,12))

for i, n in enumerate(sample_sizes):
    means = [np.mean(np.random.randint(pop_min, pop_max+1, n)) for _ in range(num_repeats)]
    plt.subplot(4,1,i+1)
    plt.hist(means, bins=30, color='lightgreen', edgecolor='black')
    plt.title(f"Sample Means Distribution (n={n})")
    plt.xlabel("Mean")
    plt.ylabel("Frequency")
    plt.grid(True)

plt.tight_layout()
plt.show()