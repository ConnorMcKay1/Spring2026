import numpy as np
import matplotlib.pyplot as plt

    # mu (mean) and little-sigma (variance)
mu0, sigma0 = 1, 0.5
mu1, sigma1 = 3, 0.8

    # x range
x = np.arange(0, 10, 0.1)

    # Gaussian PDF function
def gaussian(x, mu, sigma):
    return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-((x - mu)**2) / (2 * sigma**2))

    # densities
f0 = gaussian(x, mu0, sigma0)
f1 = gaussian(x, mu1, sigma1)

    # posterior P(Y=1 | X=x)
posterior = f1 / (f0 + f1)

    # ploting both
plt.figure(figsize=(10,6))

    # Gaussian densities
plt.plot(x, f0, label="f0(x): N(1, 0.5^2)", color='blue')
plt.plot(x, f1, label="f1(x): N(3, 0.8^2)", color='red')

    # posterior (scaled visually if needed)
plt.plot(x, posterior, label="P(Y=1 | X=x)", color='green', linestyle='--')


plt.title("Gaussian Densities and Posterior Probability")
plt.xlabel("x")
plt.ylabel("Value")
plt.legend()
plt.grid(True)

plt.show()