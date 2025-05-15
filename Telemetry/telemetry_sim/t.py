import serial

running = True

#transfer of 9600 bits per second and timeout added to wait for data to collect 
#before printing
ser = serial.Serial('COM3',baudrate = 9600, timeout = 1)
while running:
    a_data = ser.readline()

    #append into a list

    #change bytes to string text format:utf-8
    anew_data = a_data.decode('utf-8')

    #list
    #timestamp = []
    #oilPres = []
    #coolant = []

    for chara in anew_data:
    	if chara == ',':
    		ts,op,coo = anew_data.split(",")
    		# for placing into a list
    		#timestamp.append(ts)
    		#oilPres.append(op)
    		#coolant.append(coo)
    		
    		#block only for testing
    		#print(timestamp)
    		#print(oilPres)
    		#print(coolant)


    		#print(timestamp)
    		#print(oilPres)
    		#print(coolant)

    		f = open("timestamp.txt","a")
    		f.write(ts)
    		f = open("oilPressure.txt","a")
    		f.write(op)
    		f = open("coolant.txt","a")
    		f.write(coo)




    #print(timestamp)

    #sensor_data = []
    #sensor_data.append(anew_data)
    #print (sensor_data)

    #print(anew_data)

    #print("\n")



#plan
#append to list or text
#with keeping in mind to separate data