import sys, re

def time_difference(time1, time2): #returns difference in hours between two times in the form hh:mm
	return int(float(time2.split(":")[0])) - int(float(time1.split(":")[0])) + (int(float(time2.split(":")[1])) - int(float(time1.split(":")[1])))/60

def calculate_rate(invoice_text):
	times = re.findall(r'\d\d:\d\d \d\d:\d\d', file_text)
	total_time = 0
	print(file_text)
	for time_pair in times:
		total_time += time_difference(time_pair.split(" ")[0], time_pair.split(" ")[1])
	total_pay = float(file_text.split("\n")[-2].split('£')[1]);
	return "hours worked: " + str(total_time) + "\n" + "total pay: " + str(total_pay) + "\n" + "hourly rate: " + str(total_pay/total_time)

file = open(str(sys.argv[1])) 
file_text = file.read()
print(calculate_rate(file_text))


	# total_income_line = re.search(r'Total £(\d)*.\d\d', file_text)
	# total_income = float(total_income_line.split('£')[1].
	# print("£" + str(total_income/total_time))

