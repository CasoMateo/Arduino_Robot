from abc import ABC, abstractmethod
import serial

ser = serial.Serial('COM3', 9600)


class Motor:

    def __init__(GND, VCC): 
        self.GND = GND 
        self.VCC = VCC

    @abstractmethod
    def send_parameter(parameter):
        pass 
    
        
class MotorDC(Motor):

    def __init__(GND, VCC): 
        super().__init(GND, VCC)

    def send_parameter(character):

        ser.write(character.encode())
        print(f"sent: {character}")
    
class Servomotor(Motor):

    def __init__(GND, VCC, PWM_pin):
        super().__init__(GND, VCC) 
        PWM_pin = PWM_pin

    def send_parameter(character):

        ser.write(character.encode())
        print(f"sent: {character}")
            
class Sensor:

    def __init__(voltage_capacity, GND, VCC, trigger_pin, echo_pin, max_distance):
        self.voltage_capacity = voltage_capacity 
        self.GND = GND 
        self.VCC = VCC 
        self.trigger_pin = trigger_pin 
        self.echo_pin = echo_pin 
        self.max_distance = max_distance

   
    def send_instructions():

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
            


      

            