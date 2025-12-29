def Q9():
 import numpy as np #NumericalPython (gen R.S compute mu and var, create arrays for plotting)
 import matplotlib.pyplot as plt
 from scipy.stats import norm, expon, poisson

 np.random.seed(0)
 n = 10000
 lambda_val = 5

 # Generate data
 uniform_data = np.random.uniform(0, 1, n)
 gaussian_data = np.random.normal(0, 1, n)
 exp_data = np.random.exponential(scale=1.0, size=n)
 poisson_data = np.random.poisson(lambda_val, n)

 fig, axs = plt.subplots(2, 2, figsize=(14, 10))

 # ---------- Uniform ----------
 axs[0, 0].hist(uniform_data, bins=50, density=True, edgecolor='black')
 x = np.linspace(0, 1, 100)
 axs[0, 0].plot(x, np.ones_like(x))
 axs[0, 0].set_title("Uniform (0,1)")
 axs[0, 0].set_xlabel("Value")
 axs[0, 0].set_ylabel("Probability Density")
 axs[0, 0].text(
     0.65, 0.85,
     f"Mean: {np.mean(uniform_data):.2f}\nVar: {np.var(uniform_data):.2f}",
     transform=axs[0, 0].transAxes,
     bbox=dict(facecolor='white', alpha=0.8)
 )

# ---------- Gaussian ----------
 axs[0, 1].hist(gaussian_data, bins=50, density=True, edgecolor='black')
 x = np.linspace(-4, 4, 200)
 axs[0, 1].plot(x, norm.pdf(x, 0, 1))
 axs[0, 1].set_title("Gaussian (0,1)")
 axs[0, 1].set_xlabel("Value")
 axs[0, 1].set_ylabel("Probability Density")
 axs[0, 1].text(
    0.65, 0.85,
    f"Mean: {np.mean(gaussian_data):.2f}\nVar: {np.var(gaussian_data):.2f}",
    transform=axs[0, 1].transAxes,
    bbox=dict(facecolor='white', alpha=0.8)
)

# ---------- Exponential ----------
 axs[1, 0].hist(exp_data, bins=50, density=True, edgecolor='black')
 x = np.linspace(0, 8, 200)
 axs[1, 0].plot(x, expon.pdf(x, scale=1.0))
 axs[1, 0].set_title("Exponential (rate = 1)")
 axs[1, 0].set_xlabel("Value")
 axs[1, 0].set_ylabel("Probability Density")
 axs[1, 0].text(
    0.65, 0.85,
    f"Mean: {np.mean(exp_data):.2f}\nVar: {np.var(exp_data):.2f}",
    transform=axs[1, 0].transAxes,
    bbox=dict(facecolor='white', alpha=0.8)
)

# ---------- Poisson ----------
 values = np.arange(0, np.max(poisson_data) + 1)
 axs[1, 1].hist(poisson_data, bins=values, density=True, edgecolor='black')
 axs[1, 1].plot(values, poisson.pmf(values, lambda_val), marker='o', linestyle='')
 axs[1, 1].set_title("Poisson (λ = 5)")
 axs[1, 1].set_xlabel("Value")
 axs[1, 1].set_ylabel("Probability Mass")
 axs[1, 1].text(
    0.65, 0.85,
    f"Mean: {np.mean(poisson_data):.2f}\nVar: {np.var(poisson_data):.2f}",
    transform=axs[1, 1].transAxes,
    bbox=dict(facecolor='white', alpha=0.8)
)

 plt.suptitle("Visualization of Probability Distribution Samples", fontsize=16)
 plt.tight_layout(rect=[0, 0, 1, 0.96])
 plt.show()
 print("Uniform Distribution: Mean =", np.mean(uniform_data), "Variance =", np.var(uniform_data))
 print("Gaussian Distribution: Mean =", np.mean(gaussian_data), "Variance =", np.var(gaussian_data))
 print("Exponential Distribution: Mean =", np.mean(exp_data), "Variance =", np.var(exp_data))
 print("Poisson Distribution: Mean =", np.mean(poisson_data), "Variance =", np.var(poisson_data))

def Q10():
# Function to estimate mean and sample variance
 def estimate_mean_variance(data):
    n = len(data)  # number of elements in the list
    if n == 0:
        return None, None  # return None if the list is empty
    mean = sum(data) / n  # calculate the mean
    variance = sum((x - mean) ** 2 for x in data) / (n - 1)  # calculate sample variance
    return mean, variance

# --- Get data from the user ---
 user_input = input("Enter values separated by space: ")  # example: 1 2 3 4 5
 data = [float(x) for x in user_input.split()]  # convert input to a list of floats

# --- Calculate mean and variance using the function ---
 mean, variance = estimate_mean_variance(data)

# --- Display the results ---
 print("Data:", data)
 print("Number of elements:", len(data))  # automatically calculated
 print("Mean:", mean)
 print("Variance:", variance)

def Q12():
 import numpy as np
 import matplotlib.pyplot as plt
 from scipy.stats import binom
 # Number of experments
 n = 10
 k = np.arange(0, n + 1)
# Different values of probability p
 p_values = [0.1, 0.4, 0.7]
 # PMF 
 plt.figure()
 colors = ['r', 'g', 'b']  
 for i, p in enumerate(p_values):
    pmf = binom.pmf(k, n, p)
    plt.stem(k, pmf, linefmt=colors[i]+'-', markerfmt=colors[i]+'o', basefmt=' ')

 plt.xlabel('k (number of successes)')
 plt.ylabel('PMF')
 plt.title('Binomial PMF for different values of p')
 plt.legend([f'p={p}' for p in p_values])
 plt.show()
 #CDF
 plt.figure()
 for p in p_values:
    cdf = binom.cdf(k, n, p)
    plt.step(k, cdf, label=f'p = {p}', where='post')

 plt.xlabel('k (number of successes)')
 plt.ylabel('CDF')
 plt.title('Binomial CDF for different values of p')
 plt.legend()
 plt.show()

def Q14():

 import numpy as np
 import matplotlib.pyplot as plt
 from scipy.stats import binom
 # Parameters
 n = 5        # number of experiments
 p = 1/6      # probability of success (getting a 6)
 # Possible values of Z
 Z = np.arange(0, n+1)
 # Probability Mass Function (PMF)
 pmf = binom.pmf(Z, n, p)
 # Cumulative Distribution Function (CDF)
 cdf = binom.cdf(Z, n, p)
 # Plot PMF
 plt.figure()
 plt.bar(Z, pmf, color='skyblue')
 plt.xlabel('Number of 6s (Z)')
 plt.ylabel('Probability')
 plt.title('Probability Mass Function (PMF) of Z')
 plt.show()
 # Plot CDF
 plt.figure()
 plt.step(Z, cdf, where='post', linewidth=2)
 plt.xlabel('Number of 6s (Z)')
 plt.ylabel('Cumulative Probability')
 plt.title('Cumulative Distribution Function (CDF) of Z')
 plt.grid(True)
 plt.show()
def Q16():
 import numpy as np
 import matplotlib.pyplot as plt

 # 1) Generate random data
 np.random.seed(0)  # for reproducibility
 X = np.random.rand(50) * 10   # 50 random values between 0 and 10
 Y = 2 * X + np.random.randn(50) * 5  # approximate linear relation with noise

 # 2) Create scatter plot
 plt.scatter(X, Y, color='blue')
 plt.title('Scatter Plot of X vs Y')
 plt.xlabel('X')
 plt.ylabel('Y')
 plt.grid(True)
 plt.show()

 # 3) Compute correlation coefficient
 corr_matrix = np.corrcoef(X, Y)  # correlation matrix
 corr_XY = corr_matrix[0, 1]      # correlation coefficient between X and Y
 print(f"Correlation coefficient between X and Y: {corr_XY:.2f}")
Q16()