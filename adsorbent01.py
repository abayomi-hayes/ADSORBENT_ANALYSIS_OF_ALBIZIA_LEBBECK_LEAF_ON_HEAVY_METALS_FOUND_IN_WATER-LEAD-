# -*- coding: utf-8 -*-
"""adsorbent01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18flRr9QeeW2hIXEaRPnG_D6sSCRSCEdV
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""#pH plays a significant role in adsorption processes. The purpose of this study was to find out the suitable pH at which lead (II) adsorption was maximum. The experiment was conducted at initial metal ion concentration 20 mg/L, adsorbent dose 10 g/L, contact time 30 min., and mixing speed 200 rpm. pH 3, 4, 5, 6, 7 were taken into study. The experimental result shows that at pH 4 lead (II) adsorption was 99.1 % followed by 98.57 % in pH 5, 98.96 in pH 6, and 97.8 % in pH 7. The maximum percentage of lead (II)adsorption was found to be 99.33 % in pH 3. (Figure 1, Table 2). So pH 3 was chosen as optimum in the"""

#PH
PH = 3,4,5,6,7
lead_adsorption = 99.33,99.1,98.57,98.96,97.8

plt.figure(figsize=(12,6))
plt.plot(PH, lead_adsorption,"s-b")
plt.xlabel('PH')
plt.ylabel('ADSORPTION EFFICIENCY')
plt.title('EFFECT OF CHANGE IN PH')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

PH = [3, 4, 5, 6, 7]  # pH values
lead_adsorption = [99.33, 99.1, 98.57, 98.96, 97.8]  # lead adsorption efficiency

plt.figure(figsize=(12, 6))
plt.plot(PH, lead_adsorption, "s-b")

# Label each marker point with lead adsorption efficiency
for i in range(len(PH)):
    plt.text(PH[i], lead_adsorption[i], str(lead_adsorption[i]) + "%", ha='center', va='bottom')

plt.xlabel('pH')
plt.ylabel('Lead Adsorption Efficiency')
plt.title('Effect of pH on Lead Adsorption')
plt.grid(True)
plt.show()

"""#In this study, the adsorption of lead (II) with change in initial concentration was studied, initial concentration ranging from 10 mg/L to 50 mg/L was taken for study. The experiment was conducted at pH 5, adsorbent dose 10 g/L, contact time 30 min, and mixing speed 200 rpm. The experimental result shows at 10 mg/L, 20 mg/L, 40 mg/L, 50 mg/L lead (II) removal of 98.93%, 98.67 %, 99.19 %, 99.35 % respectively. Maximum lead (II) removal was foundin 30 mg/L with 99.48 % adsorption (Figure 2, Table 2) so an initial heavy metal concentration of 30 mg/L was chosen as optimum in the experiment for lead (II) removal."""

concentration = 10,20,40,50
adsorbent_efficiency = 98.93,99.47,99.58,99.19

import matplotlib.pyplot as plt
concentration = 10,20,40,50
adsorbent_efficiency = 98.93,99.47,99.58,99.19


plt.figure(figsize=(12, 6))
plt.plot(concentration, adsorbent_efficiency, "o-r")

# Label each marker point with lead adsorption efficiency
for i in range(len(concentration)):
    plt.text(concentration[i], adsorbent_efficiency[i], str(adsorbent_efficiency[i]) + "%", ha='center', va='bottom')

plt.xlabel('concentration')
plt.ylabel('Lead Adsorption Efficiency')
plt.title('Effect of concentration on lead')
plt.grid(True)
plt.show()

"""# Effect of Change in Contact TimeThe purpose of the study was to determine the contact time at which maximum adsorption of metal ions of lead (II) occurs. This study was conducted at pH 5, initial metal concentration 20 mg/L, adsorbent dose 10 g/L, and mixing speed 200 rpm. Contact time of 30 min, 60 min, 90 min, and 120 min was taken for study. The result showed at 60 min, 90 min, and 120 min. Lead (II) removal of 99.45 %, 99.2 %, and 99.16 % respectively. Maximum lead (II) removal was found in 30 min. with more than 99.5 % of adsorption. (Figure 4, Table 2) So contact time of 30 minutes was chosen as"""

contact_TIME = 30,60,90,120
Adsorbent_efficiency_time = 99.5,99.45,99.2,99.16

import matplotlib.pyplot as plt
contact_TIME = 30,60,90,120
Adsorbent_efficiency_time = 99.5,99.45,99.2,99.16




plt.figure(figsize=(12, 6))
plt.plot(contact_TIME, Adsorbent_efficiency_time, "o-r")

# Label each marker point with lead adsorption efficiency
for i in range(len(contact_TIME)):
    plt.text(contact_TIME[i], Adsorbent_efficiency_time[i], str(Adsorbent_efficiency_time[i]) + "%", ha='center', va='bottom')

plt.xlabel('concentration')
plt.ylabel('Lead Adsorption Efficiency')
plt.title('Effect of concentration on lead')
plt.grid(True)
plt.show()

inverse_concentration = 0.41666667,0.12345679,0.068,0.024,0.006,0.002
inverse_adsorption_capacity = 00.197,0.068,0.042,0.025,0.019,0.012

import matplotlib.pyplot as plt
inverse_concentration = 0.41666667,0.12345679,0.068,0.024,0.006,0.002
inverse_adsorption_capacity = 0.197,0.068,0.042,0.025,0.019,0.012





plt.figure(figsize=(12, 6))
plt.plot(inverse_concentration, inverse_adsorption_capacity, "H-r")

# Label each marker point with lead adsorption efficiency
for i in range(len(inverse_concentration)):
    plt.text(inverse_concentration[i], inverse_adsorption_capacity[i], str(inverse_adsorption_capacity[i]) + "%", ha='center', va='bottom')

plt.xlabel('concentration')
plt.ylabel('adsorption capacity')
plt.title('langmuir isotherm')
plt.show()

Time = 0,5,10,15,20,25,30,40,50,60
initial_concentration_at_a_given_time = 0,0.382,-0.91,-1.6,-2.1,-2.7,-2.7,-2.7,-2.7,-2.7

import matplotlib.pyplot as plt
Time = 0,5,10,15,20,25,30,40,50,60
initial_concentration_at_a_given_time = 0,0.382,-0.91,-1.6,-2.1,-2.7,-2.7,-2.7,-2.7,-2.7






plt.figure(figsize=(12, 6))
plt.plot(Time, initial_concentration_at_a_given_time, "h b")

# Label each marker point with lead adsorption efficiency
for i in range(len(Time)):
    plt.text(Time[i], initial_concentration_at_a_given_time[i], str(initial_concentration_at_a_given_time[i]) + "%", ha='center', va='bottom')

plt.xlabel("Time")
plt.ylabel('initial_concentration_at_a_given_time')
plt.title('pseudo first order')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

Time = np.array([0, 5, 10, 15, 20, 25, 30, 40, 50, 60])
initial_concentration_at_a_given_time = np.array([0, 0.382, -0.91, -1.6, -2.1, -2.7, -2.7, -2.7, -2.7, -2.7])

# Perform linear regression
reg = np.polyfit(Time, initial_concentration_at_a_given_time, 1)
m = reg[0]  # Slope
c = reg[1]  # Y-intercept

# Calculate predicted values
initial_concentration_pred = m * Time + c

# Plot the graph with linear regression line
plt.figure(figsize=(12, 6))
plt.plot(Time, initial_concentration_at_a_given_time, "h b", label='Data points')
plt.plot(Time, initial_concentration_pred, 'r-', label='Linear regression line')

# Label each marker point with initial concentration
for i in range(len(Time)):
    plt.text(Time[i], initial_concentration_at_a_given_time[i], str(initial_concentration_at_a_given_time[i]) + "%", ha='center', va='bottom')

plt.xlabel("Time")
plt.ylabel('Initial Concentration')
plt.title('Pseudo First Order')
plt.legend()
plt.show()

