import math


def calculate_capacitance(frequency, R1, R2):
    """
    Calculate the capacitance using the given frequency and resistances.
    :param R1: Resistance R1 in ohms
    :param R2: Resistance R2 in ohms
    :param frequency: Measured frequency in Hz
    :return: Capacitance in farads
    """
    C = 1.0 / (frequency * (R1 + 2 * R2) * math.log(2))
    return C


if __name__ == '__main__':
    R1 = 57000.0
    R2 = 500000.0

    f_parasitic = 77500
    f_measured = 1930

    C_parasitic = calculate_capacitance(f_parasitic, R1, R2)
    print(f"Parasitic Capacitance: {C_parasitic * 1e12:.2f} pF")

    C_total = calculate_capacitance(f_measured, R1, R2)
    print(f"Total Capacitance: {C_total * 1e12:.2f} pF")

    C_true = C_total - C_parasitic
    print(f"Actual Capacitance: {C_true * 1e12:.2f} pF")
