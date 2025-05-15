import serial
import csv
import datetime

running = True
errorcount = 0
datecounter = 0

#transfer of 9600 bits per second and timeout added to wait for data to collect 
#before printing
ser = serial.Serial('COM3',baudrate = 9600, timeout = 1)

while running:

	a_data = ser.readline()
	#change bytes to string text format:utf-8
	anew_data = a_data.decode('utf-8')
	#remove any spaces,newlines and other radnom characters
	anew_data = anew_data.strip()
	#split the string into three and store 
	#each data into its dedicated variable
	plotdata = anew_data.split(',')

	#testing
	print(plotdata)
	print(len(plotdata))

	if len(plotdata) != 3:
		errorcount += 1
	else:

		#append to csv files with dates for each run
		data = open('timestamp.csv', 'a')
		adata = csv.writer(data)
		adata.writerow(str(plotdata[0]))

		if datecounter == 0:
			adata.writerow(str(datetime.datetime.now()))

		data = open('oilPressure.csv', 'a')
		adata = csv.writer(data)
		adata.writerow(str(plotdata[1]))

		if datecounter == 0:
			adata.writerow(str(datetime.datetime.now()))
			
		data = open('coolant.csv', 'a')
		adata = csv.writer(data)
		adata.writerow(str(plotdata[2]))

		if datecounter == 0:
			adata.writerow(str(datetime.datetime.now()))
			

		datecounter = 1
		data.close()