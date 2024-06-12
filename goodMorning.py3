#!/usr/bin/python3
import numpy as np
import datetime
from time import sleep

# Facts about you!
name = "Brantley"
birth = np.datetime64("1998-01-21", "D")
death = np.datetime64('2072-12-18') #Estimated death date
male = True #Used to decide which death probability tables to consult

if male:
	yearly_death_probabilities_by_age = [
	    0.005860, 0.000420, 0.000272, 0.000225, 0.000184,
	    0.000157, 0.000140, 0.000128, 0.000122, 0.000123,
	    0.000129, 0.000138, 0.000164, 0.000220, 0.000310,
	    0.000446, 0.000637, 0.000868, 0.001100, 0.001270,
	    0.001373, 0.001488, 0.001605, 0.001714, 0.001835,
	    0.001963, 0.002082, 0.002202, 0.002330, 0.002457,
	    0.002574, 0.002683, 0.002787, 0.002881, 0.002974,
	    0.003074, 0.003175, 0.003295, 0.003444, 0.003608,
	    0.003780, 0.003958, 0.004144, 0.004337, 0.004540,
	    0.004774, 0.005064, 0.005399, 0.005796, 0.006214,
	    0.006671, 0.007167, 0.007736, 0.008351, 0.009035,
	    0.009770, 0.010567, 0.011398, 0.012291, 0.013224,
	    0.014267, 0.015353, 0.016484, 0.017617, 0.018759,
	    0.019914, 0.021104, 0.022423, 0.023847, 0.025357,
	    0.027050, 0.028970, 0.031188, 0.033754, 0.036747,
	    0.040563, 0.044308, 0.048498, 0.053229, 0.058778,
	    0.064617, 0.070947, 0.077834, 0.085686, 0.094809,
	    0.105090, 0.116592, 0.129306, 0.142732, 0.157638,
	    0.174458, 0.193027, 0.212930, 0.232657, 0.251826,
	    0.270943, 0.289756, 0.307998, 0.325393, 0.341662,
	    0.358746, 0.376683, 0.395517, 0.415293, 0.436058,
	    0.457860, 0.480753, 0.504791, 0.530031, 0.556532,
	    0.584359, 0.613577, 0.644256, 0.676468, 0.710292,
	    0.745806, 0.783097, 0.822251, 0.863364, 0.906532,
	] #Pulled from https://www.ssa.gov/oact/STATS/table4c6.html, table 2021(2024 TR)
else:
	yearly_death_probabilities_by_age = [
		0.005063, 0.000393, 0.000223, 0.000177, 0.000144,
		0.000122, 0.000109, 0.000102, 0.000098, 0.000097,
		0.000103, 0.000113, 0.000131, 0.000157, 0.000190,
		0.000233, 0.000291, 0.000355, 0.000418, 0.000461,
		0.000507, 0.000556, 0.000610, 0.000666, 0.000722,
		0.000775, 0.000831, 0.000889, 0.000952, 0.001025,
		0.001104, 0.001192, 0.001289, 0.001383, 0.001465,
		0.001544, 0.001626, 0.001719, 0.001824, 0.001940,
		0.002066, 0.002202, 0.002351, 0.002482, 0.002622,
		0.002789, 0.002994, 0.003219, 0.003467, 0.003729,
		0.004011, 0.004306, 0.004634, 0.004981, 0.005370,
		0.005831, 0.006326, 0.006837, 0.007399, 0.008033,
		0.008687, 0.009411, 0.010139, 0.010849, 0.011550,
		0.012216, 0.012952, 0.013844, 0.014863, 0.016028,
		0.017329, 0.018859, 0.020609, 0.022620, 0.024958,
		0.027906, 0.030925, 0.034140, 0.037620, 0.041725,
		0.046324, 0.051334, 0.056911, 0.063279, 0.070704,
		0.079184, 0.088697, 0.099240, 0.110480, 0.123078,
		0.137152, 0.152605, 0.169494, 0.187623, 0.206647,
		0.225890, 0.245054, 0.263815, 0.281828, 0.298738,
		0.316662, 0.335662, 0.355802, 0.377150, 0.399779,
		0.423766, 0.449192, 0.476143, 0.504712, 0.534994,
		0.567094, 0.601120, 0.637187, 0.675418, 0.710292,
		0.745806, 0.783097, 0.822251, 0.863364, 0.906532,
	] #Pulled from https://www.ssa.gov/oact/STATS/table4c6.html, table 2021(2024 TR)

line_delay=2 #Time delay between printing lines (in seconds)

now_raw = datetime.datetime.now()
now = np.datetime64(now_raw, "D")
now_year = np.datetime64(now_raw, "Y")
birth_year = np.datetime64(birth, "Y")
diff = int((now - birth) / np.timedelta64(1, "D"))
age = int((now_year - birth_year) / np.timedelta64(1, "Y"))
time_left = int((death - now) / np.timedelta64(1, "D"))
percent_done = 100. * diff / (diff + time_left)
percent_today_death = yearly_death_probabilities_by_age[age]/365 * 100.
print("")
sleep(line_delay)
print(f"Good morning {name}.")
sleep(line_delay)
print(f"You are {age} years old.")
sleep(line_delay)
print(f"You have been alive for {diff} days.")
sleep(line_delay)
print(f"You are projected to live for another {time_left} days,")
sleep(line_delay)
print(f"dying on {death}.")
sleep(line_delay)
print("")
print("%.3f%%: " % percent_done, end="")
for i in range(50):
	sleep(0.05)
	if 2 * i <= percent_done:
		print('|', end="", flush=True)
	else:
		print('-', end="", flush=True)
sleep(line_delay)
print('\n')
print("Your probability of dying today is approximately %.7f%%." % (percent_today_death))
sleep(line_delay)
input("\nPress enter to continue...")