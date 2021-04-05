"""
File: weather_master.py
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -100


def main():
	"""
	Compute the highest, lowest and average temperature, and the times of cold days.
	"""
	print('stanCode "Weather Master 4.0"!')
	data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)?'))
	if data == EXIT:
		print('No temperature were entered.')
	else:
		highest = data
		lowest = data
		cold_days = 0
		times = 1
		data_sum = data
		average = data_sum / times
		if data < 16:
			cold_days += 1
		while True:
			data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)?'))
			if data == EXIT:
				break
			if data > highest:
				highest = data
			if data < lowest:
				lowest = data
			if data < 16:
				cold_days += 1
			times += 1
			data_sum = data_sum + data
			average = data_sum / times
		print('Highest Temperature = ' + str(highest))
		print('Lowest Temperature = ' + str(lowest))
		print('Average = ' + str(average))
		print(str(cold_days) + ' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
