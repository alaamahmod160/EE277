import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

sample_sizes = [10, 20, 30, 40]  # different sample sizes
num_repeats = 1000               # number of repeated samples

distributions = {
    "Uniform(0,10)": lambda n: np.random.uniform(0,10,n),
    "Exponential(1)": lambda n: np.random.exponential(1,n),
    "Poisson(5)": lambda n: np.random.poisson(5,n)
}

plt.figure(figsize=(12,10))

for i, (name, dist) in enumerate(distributions.items()):
    for j, n in enumerate(sample_sizes):
        means = [np.mean(dist(n)) for _ in range(num_repeats)]
        plt.subplot(len(distributions), len(sample_sizes), i*len(sample_sizes)+j+1)
        plt.hist(means, bins=30, color='lightblue', edgecolor='black')
        plt.title(f"{name}, n={n}")
        plt.xticks([])
        plt.yticks([])

plt.tight_layout()
plt.show()
