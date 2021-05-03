import serial 

ser = serial.Serial('COM3', 9600)

def compute():

    response = ser.read()

    if response[0] == 'x':
        distance_1 = ''

        for char in range(1, len(response)):
            distance_1 += str(response[char]) 
            
        f_distance_1 = int(distance_1) 

    else:
        distance_2 = '' 

        for char in range(1, len(response)): 
            distance_1 += str(response[char])  

        f_distance_2 = int(distance_2)

    if f_distance_1 > f_distance_2: 
        ser.write('a'.encode())
        
    else:
        ser.write('b'.encode())

      

            
