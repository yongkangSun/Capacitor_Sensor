# 555 Capacitance Measure Circuit



## Original Design

![image-20240709170541374](/Users/johnnnysun/Library/Application Support/typora-user-images/image-20240709170541374.png)



### NE555

#### Truth table

| PIN 2     | PIN 6     | Q        | ^Q   | PIN 3 |
| --------- | --------- | -------- | ---- | ----- |
| > 1/3 VCC | > 2/3 VCC | 0        | 1    | 0     |
| > 1/3 VCC | < 2/3 VCC | Stay     |      |       |
| < 1/3 VCC | < 2/3 VCC | 1        | 0    | 1     |
| < 1/3 VCC | > 2/3 VCC | Unstable |      |       |

#### Pin

* 1 GND: connect to ground line
* 8 VCC: connect to fire line
* 2 TRIG: input 1, compare with 1/3 VCC
* 7 DIS: Connect to GND when output of S-R become 1 (PIN 3 output 0).
* 3 OUT: output
* 6 THR: input 2, compare with 2/3 VCC
* 4 RES: Switch of the S-R latch
* 5 CV: useless, connect to ground through a capacitor



### Formula

C = 1/(f · (R1 + 2R2) · ln(2)) 

* We can enlarge two resistance? Since we neglect the resistence of the electrodes, the larger the resistance is the accurate we get. The trade of is the measuring time which we don't care. The choice in the paper is for real-time case.

* We need to measure and subtract the parasitic capacitance by doing the same experiment on two unconnected conector board.



### Parasitic capacitance

The parasitic capacitance is close to 25.45 pF. Deduct it at each time. 

There are still 1% to 3% of errors. We could eliminate it with a **linear regressor**. 

#### Data Collection

##### With Long Wire

| Capacitor | Frequency  |
| --------- | ---------- |
| 0.0 uF    | 53.95 KHz  |
| 1 pF      | 52.27 Khz  |
| 3.3 pF    | 47.37 Khz  |
| 5 pF      | 44.25 Khz  |
| 10 pF     | 37.71 Khz  |
| 47 pF     | 18.722 Khz |
| 100 pF    | 10.35 Khz  |
| 250 pF    | 4.898 Khz  |
| 470 pF    | 2.878 Khz  |
| 0.001 uF  | 1.3607 KHz |
| 0.0022 uF | 604.1 Hz   |
| 0.0033 uF | 398.7 Hz   |
| 0.0047 uF | 284.9 Hz   |
| 0.01 uF   | 133.7 Hz   |
| 0.022 uF  | 62.6 Hz    |
| 0.033 uF  | 40.92 Hz   |
| 0.047 uF  | 29.86 Hz   |
| 0.068 uF  | 20.85 Hz   |
| 0.1 uF    | 12.8 Hz    |
| 0.15 uF   | 8.93 Hz    |



| Capacitor | Frequency |
| --------- | --------- |
| 0.0 pF    | 52.07 Khz |
| 5 pF      | 42.36 Khz |
| 10 pF     | 36.43 Khz |
| 47 pF     | 18.35 Khz |
| 100 pF    | 10.08 Khz |
| 470pF     | 2.891 Khz |
| 1000 pF   | 1.281 Khz |
| 2200 pF   | 594 Hz    |
| 3300 pF   | 385 Hz    |
| 4700 pF   | 288 Hz    |



##### Without long wire

| Capacitor | Frequency |
| --------- | --------- |
| 0.0 pF    | 51.95 Khz |
| 10 pF     |           |
| 47 pF     |           |
| 100 pF    |           |
| 470pF     |           |
| 1000 pF   |           |
| 2200 pF   |           |
| 3300 pF   |           |
| 4700 pF   |           |
|           |           |
|           |           |
|           |           |
|           |           |
|           |           |
|           |           |
|           |           |
|           |           |
|           |           |

 I think we could only trust 2 digit of the frequency reading. 



## Procedure

#### Useful button

- Auto: on the top of the machine, automatically adjust the range
- Measure: a button below the AUTO, select “measure all” in the list on the right side of the screen. This will provide the measurements of frequencies and everything.



##  MCU

* Read the waveform from the circuit.
* Measure the frequency.
* 