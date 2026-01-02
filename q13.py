import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, expon
import math

 # Manual verification examples

print("POISSON DISTRIBUTION - Manual Verification (lambda=2)")
lam = 2
p0 = (lam**0 * math.exp(-lam)) / math.factorial(0)
p1 = (lam**1 * math.exp(-lam)) / math.factorial(1)
p2 = (lam**2 * math.exp(-lam)) / math.factorial(2)
print("P(X=0) =", round(p0,3))
print("P(X=1) =", round(p1,3))
print("P(X=2) =", round(p2,3))

print("\nEXPONENTIAL DISTRIBUTION - Manual Verification (lambda=1)")
lam = 1
F1 = 1 - math.exp(-lam*1)
F2 = 1 - math.exp(-lam*2)
print("F(X≤1) =", round(F1,3))
print("F(X≤2) =", round(F2,3))

# Parameters for plotting

poisson_lambdas = [1, 2, 4]
exp_lambdas = [1, 2, 4]
k = np.arange(0, 15)
x = np.linspace(0, 5, 400)


# Poisson PMF & CDF

plt.figure(figsize=(10,4))

# PMF
plt.subplot(1,2,1)
for lam in poisson_lambdas:
    pmf = poisson.pmf(k, lam)
    plt.plot(k, pmf, marker='o', label=f'lambda={lam}')
plt.title('Poisson PMF')
plt.xlabel('k')
plt.ylabel('P(X=k)')
plt.grid(True)
plt.legend()

# CDF
plt.subplot(1,2,2)
for lam in poisson_lambdas:
    cdf = poisson.cdf(k, lam)
    plt.plot(k, cdf, label=f'lambda={lam}')
plt.title('Poisson CDF')
plt.xlabel('k')
plt.ylabel('P(X≤k)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# Exponential PDF & CDF

plt.figure(figsize=(10,4))

# PDF
plt.subplot(1,2,1)
for lam in exp_lambdas:
    pdf = expon.pdf(x, scale=1/lam)
    plt.plot(x, pdf, label=f'lambda={lam}')
plt.title('Exponential PDF')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

# CDF
plt.subplot(1,2,2)
for lam in exp_lambdas:
    cdf = expon.cdf(x, scale=1/lam)
    plt.plot(x, cdf, label=f'lambda={lam}')
plt.title('Exponential CDF')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()