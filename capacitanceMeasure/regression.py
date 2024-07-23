import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def linear_fit(x, a, b):
    return a * x + b


small_capacitance_values = [1e-12, 3.3e-12, 5e-12]
proper_capacitance_values = [0, 1e-11, 4.7e-11, 1e-10, 2.5e-10, 4.7e-10, 1e-9, 2.2e-9, 3.3e-9, 4.7e-9]  # F
large_capacitance_values = [1e-8, 2.2e-8, 3.3e-8, 4.7e-8, 6.8e-8, 1e-7, 1.5e-7]

small_frequency_values = [52.27e3, 47.37e3, 44.25e3]
proper_frequency_values = [53.95e3, 37.71e3, 18.722e3, 10.35e3, 4.898e3, 2.878e3, 1.3607e3, 604.1, 398.7, 284.9]  # Hz
large_frequency_values = [133.7, 62.6, 40.92, 29.86, 20.85, 12.8, 8.93]

inverse_frequency_values = [1/f for f in proper_frequency_values]


popt, pcov = curve_fit(linear_fit, inverse_frequency_values, proper_capacitance_values)
a_opt, b_opt = popt

print(f"Parameter: a = {a_opt}, b = {b_opt}")


x_fit = np.logspace(np.log10(min(inverse_frequency_values)), np.log10(max(inverse_frequency_values)), 10000)
y_fit = linear_fit(x_fit, a_opt, b_opt)

plt.scatter(proper_capacitance_values, inverse_frequency_values, label='Measured Data')
plt.plot(y_fit, x_fit, color='red', label='Fitted Line')
plt.xscale('log')
plt.yscale('log')
plt.ylabel('1 / Frequency (1/Hz)')
plt.xlabel('Capacitance (F)')
plt.title('1/Frequency vs Capacitance with Fitted Line')
plt.legend()
plt.show()
