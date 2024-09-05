import math
import matplotlib.pyplot as plt


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

    f_parasitic1 = 77500
    f_parasitic = 29100
    f_measured = [[0 ,1.78],
                    [5	,1.64],
                    [10	,1.54],
                    [15	,1.44],
                    [20	,1.36],
                    [25	,1.28],
                    [30	,1.20],
                    [35	,1.15],
                    [40	,1.09],
                    [45	,1.03]]

    total_capacitance = []

    # C_parasitic = calculate_capacitance(f_parasitic, R1, R2)
    #
    # for i in range(10):
    #     C_total = calculate_capacitance(f_measured[i][1] * 1000, R1, R2)
    #     C_true = (C_total - C_parasitic) * 1e12
    #     total_capacitance.append(C_true)
    #
    # x_ticks = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
    # plt.figure()
    # plt.plot(x_ticks, total_capacitance, marker='o')
    # plt.title('Capacitance with stretching')
    # plt.xlabel('Stretch distance')
    # plt.ylabel('Capacitance')
    # plt.show()

    C_parasitic1 = calculate_capacitance(f_parasitic1, R1, R2)
    print(f"Parasitic Capacitance: {C_parasitic1 * 1e12:.2f} pF")

    C_parasitic = calculate_capacitance(f_parasitic, R1, R2)
    print(f"Parasitic Capacitance: {C_parasitic * 1e12:.2f} pF")

    #
    # C_total = calculate_capacitance(f_measured, R1, R2)
    # print(f"Total Capacitance: {C_total * 1e12:.2f} pF")

    # C_true = C_total - C_parasitic
    # print(f"Actual Capacitance: {C_true * 1e12:.2f} pF")
