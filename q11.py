
import matplotlib.pyplot as plt
import scipy.stats as stats

# Parameters
n = 7
p = 1/6
d_values = range(n + 1)

# ---- Example test (BEFORE plots) ----
print("Example numerical results:")
for d in range(3):  # only first few values, very simple
    print(f"P(D = {d}) = {stats.binom.pmf(d, n, p):.3f}")

# ---- PMF & CDF calculations ----
pmf_values = [stats.binom.pmf(d, n, p) for d in d_values]
cdf_values = [stats.binom.cdf(d, n, p) for d in d_values]

# ---- Plot PMF ----
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.stem(d_values, pmf_values, basefmt=" ")
plt.xlabel("Number of 3s (D)")
plt.ylabel("Probability")
plt.title("Binomial PMF (n = 7, p = 1/6)")

# ---- Plot CDF ----
plt.subplot(1, 2, 2)
plt.step(d_values, cdf_values, where='mid')
plt.xlabel("Number of 3s (D)")
plt.ylabel("Cumulative Probability")
plt.title("Binomial CDF (n = 7, p = 1/6)")

plt.tight_layout()
plt.show()