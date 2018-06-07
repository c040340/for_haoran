import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x = np.array(range(1, 45))
y = np.array([
    -0.0523,
    0.0060,
    0.0019,
    0.0147,
    0.0634,
    0.0259,
    0.0223,
    0.1035,
    0.0596,
    0.0781,
    0.1738,
    0.1085,
    0.0803,
    0.0959,
    0.1397,
    0.2501,
    0.3063,
    0.2296,
    0.2771,
    0.3379,
    0.4691,
    0.5034,
    0.5579,
    0.6377,
    0.5851,
    0.5181,
    0.6079,
    0.5699,
    0.5084,
    0.5474,
    0.4801,
    0.3721,
    0.3032,
    0.2584,
    0.1613,
    0.0636,
    0.0196,
    0.0208,
    0.0358,
    0.0159,
    0.0395,
    0.0348,
    0.0257,
    0.0041
])


def fit_func(t, alpha1, alpha2, alpha3, delta1, delta2, beta1, beta2):
    return alpha1 + (alpha2 / (1 + np.exp(-delta1 * (t - beta1)))) + (alpha3 / (1 + np.exp(-delta2 * (t - beta2))))


params = curve_fit(fit_func, x, y, method='trf', maxfev=100000000)
[alpha1, alpha2, alpha3, delta1, delta2, beta1, beta2] = params[0]


X = x
Y = fit_func(X, alpha1, alpha2, alpha3, delta1, delta2, beta1, beta2)
plt.plot(x, y, 'co')
plt.plot(X, Y)
plt.show()

pass