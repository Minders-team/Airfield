from tkinter import *
import turtle
import time
from tkinter import messagebox
import serial
import EV3BT
import RPi.GPIO as GPIO
import dht11
import datetime
import drivers
import subprocess
from create_greenhouse_txt import create_greenhouse_txt
import pygame
import pygame.camera
from pygame.locals import *
#import wmctrl
flag_manual = 0
list_files =subprocess.Popen (["python", "dokimi.py"], stdout=subprocess.DEVNULL)
print("nikame")
time.sleep(5)
'''
list_files2 =subprocess.Popen (["wmctrl", "-r", "cheese", "-e", "0,0,53,635,600"], stdout=subprocess.DEVNULL)
print("nikisame")'''




EV3_1 = serial.Serial('/dev/rfcomm0')
time.sleep(0.1)
EV3_2 = serial.Serial('/dev/rfcomm1')
time.sleep(0.1)
GPIO.setwarnings(True)
GPIO.setwarnings(False)
time.sleep(0.1)
GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

display = drivers.Lcd()

sensor_1 = dht11.DHT11(pin=23)
time.sleep(0.1)
sensor_2 = dht11.DHT11(pin=24)
time.sleep(0.1)

ideal_temperature_1= 17.0
ideal_temperature_2= 22.0

def temperature_inside():

    while True:
        result = sensor_1.read()
        #print("argei")
        if result.is_valid():
            sensor_1_value = result.temperature
            print("Temperature_1: %-3.1f C" % result.temperature)
            break
    time.sleep(0.1)

    return (sensor_1_value)

def temperature_outside():

    while True:
        result = sensor_2.read()
        #print("argei2")
        if result.is_valid():
            sensor_2_value = result.temperature
            print("Temperature_2: %-3.1f C" % result.temperature)
            break
    time.sleep(0.1)
    
    return (sensor_2_value)

counter_potisma = 0
    
def potisma ():
    global counter_potisma
    print(counter_potisma)

    if counter_potisma == 10:

        GPIO.output(20, 0)
        print("relay 1 is on ")

        time.sleep(10)

        GPIO.output(20, 1)
        print("relay 1 is off ")
        time.sleep(5)

        counter_potisma = 0

    else:
        counter_potisma = counter_potisma + 1

        time.sleep(2)
        

flag_temperature=False
flag_turtle_1=False
flag_turtle_2=False
flag_turtle_3=False
flag_turtle_4=False


#Compares temperature_inside, temperature_outside and ideal_temperature
def temperature_actions():
    global t90
    global t91
    global t92
    global t93
    global t94
    global t95
    global t96
    global t200
    global t201
    global t202
    global t203
    global t204
    global flag_temperature
    global flag_turtle_1
    global flag_turtle_2
    global flag_turtle_3
    global flag_turtle_4
    counter = 0
    try:
        lbl300.configure(text="" + str(temperature_inside()))
        lbl300.update()
        time.sleep(0.1)
        
        lbl400.configure(text="" + str(temperature_outside()))
        lbl400.update()
        time.sleep(0.1)
        
        lbl500.configure(text="" + str(humidity_0()))
        lbl500.update()
        time.sleep(0.1)
        
        lbl600.configure(text="" + str(humidity_1()))
        lbl600.update()
        time.sleep(0.1)
        
        lbl700.configure(text="" + str(humidity_2()))
        lbl700.update()
        time.sleep(0.1)
        
        lbl800.configure(text="" + str(humidity_3()))
        lbl800.update()
        time.sleep(0.1)
    except:
        pass
        
    print("flag = ",flag_temperature)  
    if (temperature_inside() > ideal_temperature_1 and temperature_inside() < ideal_temperature_2) :
        
        lbl900.configure(text="Off")
        lbl900.update()
        time.sleep(0.1)
        
        lbl1000.configure(text="Off")
        lbl1000.update()
        time.sleep(0.1)
        
        lbl1100.configure(text="Off")
        lbl1100.update()
        time.sleep(0.1)
        
        if flag_turtle_1==True:
            t90.clear()
            t91.clear()
            t92.clear()
            t93.clear()
            t94.clear()
            t95.clear()
            flag_turtle_1=False
        elif flag_turtle_2==True:
            t200.clear()
            t201.clear()
            t202.clear()
            t203.clear()
            flag_turtle_2=False
        elif flag_turtle_3==True:
            t94.clear()
            t95.clear()
            flag_turtle_3=False
        elif flag_turtle_4==True:
            t204.clear()
            flag_turtle_4=False
        else:
            print("den mpike sthn if")
       
        
        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'logic', 0)
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(0.2)
        flag_temperature=False
    
    
    elif flag_temperature == False and (temperature_inside() > ideal_temperature_2) and (temperature_outside() < temperature_inside()) and (temperature_outside() < ideal_temperature_2):
        lbl900.configure(text="On")
        lbl900.update()
        time.sleep(0.1)
        
        lbl1000.configure(text="On")
        lbl1000.update()
        time.sleep(0.1)
        
        lbl300.configure(text="" + str(temperature_inside()))
        lbl300.update()
        time.sleep(0.1)
        
        lbl400.configure(text="" + str(temperature_outside()))
        lbl400.update()
        time.sleep(0.1)
        print("grillies kai anem")
        t90 = turtle.Turtle()
        t90.color("black")
        t90.shape("arrow")
        t90.speed(20)
        t90.hideturtle()
        t90.penup()
        t90.goto(-220, 102)
        t90.speed(3)
        t90.pendown()
        t90.goto(-240, 90)
        t90.penup()
        t90.goto(-180, 102)
        t90.pendown()
        t90.goto(-160, 90)
        t90.penup()
        t90.goto(-200, 130)
        t90.pendown()
        t90.goto(-200, 150)

        t91 = turtle.Turtle()
        t91.color("black")
        t91.shape("arrow")
        t91.speed(20)
        t91.hideturtle()
        t91.penup()
        t91.goto(-220, -68)
        t91.speed(3)
        t91.pendown()
        t91.goto(-240, -80)
        t91.penup()
        t91.goto(-180, -68)
        t91.pendown()
        t91.goto(-160, -80)
        t91.penup()
        t91.goto(-200, -40)
        t91.pendown()
        t91.goto(-200, -20)

        t92 = turtle.Turtle()
        t92.color("black")
        t92.shape("arrow")
        t92.speed(20)
        t92.hideturtle()
        t92.penup()
        t92.goto(80, 102)
        t92.speed(3)
        t92.pendown()
        t92.goto(60, 90)
        t92.penup()
        t92.goto(120, 102)
        t92.pendown()
        t92.goto(140, 90)
        t92.penup()
        t92.goto(100, 130)
        t92.pendown()
        t92.goto(100, 150)

        t93 = turtle.Turtle()
        t93.color("black")
        t93.shape("arrow")
        t93.speed(20)
        t93.hideturtle()
        t93.penup()
        t93.goto(80, -68)
        t93.speed(3)
        t93.pendown()
        t93.goto(60, -80)
        t93.penup()
        t93.goto(120, -68)
        t93.pendown()
        t93.goto(140, -80)
        t93.penup()
        t93.goto(100, -40)
        t93.pendown()
        t93.goto(100, -20)

        t94 = turtle.Turtle()
        t94.color("black")
        t94.shape("arrow")
        t94.speed(20)
        t94.hideturtle()
        t94.penup()
        t94.goto(-325, 250)
        t94.speed(3)
        t94.pendown()
        t94.goto(-300, 275)
        t94.penup()
        t94.goto(-270, 250)
        t94.pendown()
        t94.goto(-245, 275)
        t94.penup()
        t94.goto(-215, 250)
        t94.pendown()
        t94.goto(-190, 275)
        t94.penup()
        t94.goto(-160, 250)
        t94.pendown()
        t94.goto(-135, 275)
        t94.penup()
        t94.goto(-105, 250)
        t94.pendown()
        t94.goto(-80, 275)
        t94.penup()
        t94.goto(-50, 250)
        t94.pendown()
        t94.goto(-25, 275)
        t94.penup()
        t94.goto(5, 250)
        t94.pendown()
        t94.goto(30, 275)
        t94.penup()
        t94.goto(60, 250)
        t94.pendown()
        t94.goto(85, 275)
        t94.penup()
        t94.goto(115, 250)
        t94.pendown()
        t94.goto(140, 275)
        t94.penup()
        t94.goto(170, 250)
        t94.pendown()
        t94.goto(195, 275)
        t94.penup()
        t94.goto(225, 250)
        t94.pendown()
        t94.goto(250, 275)

        t95 = turtle.Turtle()
        t95.color("black")
        t95.shape("arrow")
        t95.speed(20)
        t95.hideturtle()
        t95.penup()
        t95.goto(-300, -200)
        t95.speed(3)
        t95.pendown()
        t95.goto(-325, -225)
        t95.penup()
        t95.goto(-245, -200)
        t95.pendown()
        t95.goto(-270, -225)
        t95.penup()
        t95.goto(-190, -200)
        t95.pendown()
        t95.goto(-215, -225)
        t95.penup()
        t95.goto(-135, -200)
        t95.pendown()
        t95.goto(-160, -225)
        t95.penup()
        t95.goto(-80, -200)
        t95.pendown()
        t95.goto(-105, -225)
        t95.penup()
        t95.goto(-25, -200)
        t95.pendown()
        t95.goto(-50, -225)
        t95.penup()
        t95.goto(30, -200)
        t95.pendown()
        t95.goto(5, -225)
        t95.penup()
        t95.goto(85, -200)
        t95.pendown()
        t95.goto(60, -225)
        t95.penup()
        t95.goto(140, -200)
        t95.pendown()
        t95.goto(115, -225)
        t95.penup()
        t95.goto(195, -200)
        t95.pendown()
        t95.goto(170, -225)
        t95.penup()
        t95.goto(225, -200)
        t95.pendown()
        t95.goto(200, -225)
        
        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Text, 'option_', 'cooling')
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(0.5)
         

        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'numeric', 0)
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(0.5)
        flag_temperature = True
        flag_turtle_1=True
        print("esteile")
        #anoigoume tis grillies kai bazoume toys anemistires
        
    
    elif flag_temperature == False and (temperature_inside() > ideal_temperature_2) and (temperature_outside() <= temperature_inside()) and (temperature_outside() > ideal_temperature_2):
        lbl900.configure(text="On")
        lbl900.update()
        time.sleep(0.1)
        
        lbl300.configure(text="" + str(temperature_inside()))
        lbl300.update()
        time.sleep(0.1)
        
        lbl400.configure(text="" + str(temperature_outside()))
        lbl400.update()
        time.sleep(0.1)
        print("anem")
        t200 = turtle.Turtle()
        t200.color("black")
        t200.shape("arrow")
        t200.speed(20)
        t200.hideturtle()
        t200.penup()
        t200.goto(-220, 102)
        t200.speed(3)
        t200.pendown()
        t200.goto(-240, 90)
        t200.penup()
        t200.goto(-180, 102)
        t200.pendown()
        t200.goto(-160, 90)
        t200.penup()
        t200.goto(-200, 130)
        t200.pendown()
        t200.goto(-200, 150)

        t201 = turtle.Turtle()
        t201.color("black")
        t201.shape("arrow")
        t201.speed(20)
        t201.hideturtle()
        t201.penup()
        t201.goto(-220, -68)
        t201.speed(3)
        t201.pendown()
        t201.goto(-240, -80)
        t201.penup()
        t201.goto(-180, -68)
        t201.pendown()
        t201.goto(-160, -80)
        t201.penup()
        t201.goto(-200, -40)
        t201.pendown()
        t201.goto(-200, -20)

        t202 = turtle.Turtle()
        t202.color("black")
        t202.shape("arrow")
        t202.speed(20)
        t202.hideturtle()
        t202.penup()
        t202.goto(80, 102)
        t202.speed(3)
        t202.pendown()
        t202.goto(60, 90)
        t202.penup()
        t202.goto(120, 102)
        t202.pendown()
        t202.goto(140, 90)
        t202.penup()
        t202.goto(100, 130)
        t202.pendown()
        t202.goto(100, 150)

        t203 = turtle.Turtle()
        t203.color("black")
        t203.shape("arrow")
        t203.speed(20)
        t203.hideturtle()
        t203.penup()
        t203.goto(80, -68)
        t203.speed(3)
        t203.pendown()
        t203.goto(60, -80)
        t203.penup()
        t203.goto(120, -68)
        t203.pendown()
        t203.goto(140, -80)
        t203.penup()
        t203.goto(100, -40)
        t203.pendown()
        t203.goto(100, -20)
        
        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Text, 'option_', 'cooling')
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(0.5)
         

        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'numeric', 1)
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(0.5)
        flag_temperature = True
        flag_turtle_2=True
        print("esteile")
         
        #psixei xoris grillies
    
    elif flag_temperature == False and (temperature_inside() > ideal_temperature_2) and (temperature_outside() >= temperature_inside()):
        lbl900.configure(text="On")
        lbl900.update()
        time.sleep(0.1)
        
        time.sleep(0.1)
        lbl300.configure(text="" + str(temperature_inside()))
        lbl300.update()
        time.sleep(0.1)
        
        lbl400.configure(text="" + str(temperature_outside()))
        lbl400.update()
        time.sleep(0.1)
        print("anem")
        t200 = turtle.Turtle()
        t200.color("black")
        t200.shape("arrow")
        t200.speed(20)
        t200.hideturtle()
        t200.penup()
        t200.goto(-220, 102)
        t200.speed(3)
        t200.pendown()
        t200.goto(-240, 90)
        t200.penup()
        t200.goto(-180, 102)
        t200.pendown()
        t200.goto(-160, 90)
        t200.penup()
        t200.goto(-200, 130)
        t200.pendown()
        t200.goto(-200, 150)

        t201 = turtle.Turtle()
        t201.color("black")
        t201.shape("arrow")
        t201.speed(20)
        t201.hideturtle()
        t201.penup()
        t201.goto(-220, -68)
        t201.speed(3)
        t201.pendown()
        t201.goto(-240, -80)
        t201.penup()
        t201.goto(-180, -68)
        t201.pendown()
        t201.goto(-160, -80)
        t201.penup()
        t201.goto(-200, -40)
        t201.pendown()
        t201.goto(-200, -20)

        t202 = turtle.Turtle()
        t202.color("black")
        t202.shape("arrow")
        t202.speed(20)
        t202.hideturtle()
        t202.penup()
        t202.goto(80, 102)
        t202.speed(3)
        t202.pendown()
        t202.goto(60, 90)
        t202.penup()
        t202.goto(120, 102)
        t202.pendown()
        t202.goto(140, 90)
        t202.penup()
        t202.goto(100, 130)
        t202.pendown()
        t202.goto(100, 150)

        t203 = turtle.Turtle()
        t203.color("black")
        t203.shape("arrow")
        t203.speed(20)
        t203.hideturtle()
        t203.penup()
        t203.goto(80, -68)
        t203.speed(3)
        t203.pendown()
        t203.goto(60, -80)
        t203.penup()
        t203.goto(120, -68)
        t203.pendown()
        t203.goto(140, -80)
        t203.penup()
        t203.goto(100, -40)
        t203.pendown()
        t203.goto(100, -20)
        
        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Text, 'option_', 'cooling')
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(0.5)
         

        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'numeric', 1)
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(0.5)
        flag_temperature = True
        flag_turtle_2=True
        print("etseile") 
        #psixei
    
    elif flag_temperature == False and  (temperature_inside() < ideal_temperature_1) and (temperature_outside() > temperature_inside()) and (temperature_outside() > ideal_temperature_1):
        lbl1000.configure(text="On")
        lbl1000.update()
        time.sleep(0.1)
        
        
        lbl300.configure(text="" + str(temperature_inside()))
        lbl300.update()
        time.sleep(0.1)
        
        lbl400.configure(text="" + str(temperature_outside()))
        lbl400.update()
        time.sleep(0.1)
        print("grillies")
        t94 = turtle.Turtle()
        t94.color("black")
        t94.shape("arrow")
        t94.speed(20)
        t94.hideturtle()
        t94.penup()
        t94.goto(-325, 250)
        t94.speed(3)
        t94.pendown()
        t94.goto(-300, 275)
        t94.penup()
        t94.goto(-270, 250)
        t94.pendown()
        t94.goto(-245, 275)
        t94.penup()
        t94.goto(-215, 250)
        t94.pendown()
        t94.goto(-190, 275)
        t94.penup()
        t94.goto(-160, 250)
        t94.pendown()
        t94.goto(-135, 275)
        t94.penup()
        t94.goto(-105, 250)
        t94.pendown()
        t94.goto(-80, 275)
        t94.penup()
        t94.goto(-50, 250)
        t94.pendown()
        t94.goto(-25, 275)
        t94.penup()
        t94.goto(5, 250)
        t94.pendown()
        t94.goto(30, 275)
        t94.penup()
        t94.goto(60, 250)
        t94.pendown()
        t94.goto(85, 275)
        t94.penup()
        t94.goto(115, 250)
        t94.pendown()
        t94.goto(140, 275)
        t94.penup()
        t94.goto(170, 250)
        t94.pendown()
        t94.goto(195, 275)
        t94.penup()
        t94.goto(225, 250)
        t94.pendown()
        t94.goto(250, 275)

        t95 = turtle.Turtle()
        t95.color("black")
        t95.shape("arrow")
        t95.speed(20)
        t95.hideturtle()
        t95.penup()
        t95.goto(-300, -200)
        t95.speed(3)
        t95.pendown()
        t95.goto(-325, -225)
        t95.penup()
        t95.goto(-245, -200)
        t95.pendown()
        t95.goto(-270, -225)
        t95.penup()
        t95.goto(-190, -200)
        t95.pendown()
        t95.goto(-215, -225)
        t95.penup()
        t95.goto(-135, -200)
        t95.pendown()
        t95.goto(-160, -225)
        t95.penup()
        t95.goto(-80, -200)
        t95.pendown()
        t95.goto(-105, -225)
        t95.penup()
        t95.goto(-25, -200)
        t95.pendown()
        t95.goto(-50, -225)
        t95.penup()
        t95.goto(30, -200)
        t95.pendown()
        t95.goto(5, -225)
        t95.penup()
        t95.goto(85, -200)
        t95.pendown()
        t95.goto(60, -225)
        t95.penup()
        t95.goto(140, -200)
        t95.pendown()
        t95.goto(115, -225)
        t95.penup()
        t95.goto(195, -200)
        t95.pendown()
        t95.goto(170, -225)
        t95.penup()
        t95.goto(225, -200)
        t95.pendown()
        t95.goto(200, -225)
        
        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Text, 'option_', 'heating')
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(0.5)
         

        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'numeric', 0)
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(0.5)
        flag_temperature = True
        flag_turtle_3=True
        print("esteile")
        #anoigoume grillia
    
    elif flag_temperature == False and  (temperature_inside() < ideal_temperature_1) and (temperature_outside() >= temperature_inside()) and (temperature_outside() < ideal_temperature_1):
        lbl1100.configure(text="On")
        lbl1100.update()
        time.sleep(0.1)
        
        lbl300.configure(text="" + str(temperature_inside()))
        lbl300.update()
        time.sleep(0.1)
        
        lbl400.configure(text="" + str(temperature_outside()))
        lbl400.update()
        time.sleep(0.1)
        
        print("brastir")
        t204 = turtle.Turtle()
        t204.color("black")
        t204.shape("arrow")
        t204.speed(20)
        t204.hideturtle()
        t204.fillcolor("black")
        t204.penup()
        t204.goto(-300, 100)
        t204.begin_fill()
        t204.circle(10)
        t204.end_fill()
        t204.penup()
        t204.goto(-300, -70)
        t204.begin_fill()
        t204.circle(10)
        t204.end_fill()
        
        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Text, 'option_', 'heating')
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(0.5)
        
        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'numeric', 1)
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(0.5)
        
    
        flag_temperature = True
        flag_turtle_4=True
        print("esteile")
        #thermansi
    
    elif flag_temperature == False and  (temperature_inside() < ideal_temperature_1) and (temperature_outside() <= temperature_inside()):
        lbl1100.configure(text="On")
        lbl1100.update()
        time.sleep(0.1)
        
        lbl300.configure(text="" + str(temperature_inside()))
        lbl300.update()
        time.sleep(0.1)
        
        lbl400.configure(text="" + str(temperature_outside()))
        lbl400.update()
        time.sleep(0.1)
        print("brastir")
        t204 = turtle.Turtle()
        t204.color("black")
        t204.shape("arrow")
        t204.speed(20)
        t204.hideturtle()
        t204.fillcolor("black")
        t204.penup()
        t204.goto(-300, 100)
        t204.begin_fill()
        t204.circle(10)
        t204.end_fill()
        t204.penup()
        t204.goto(-300, -70)
        t204.begin_fill()
        t204.circle(10)
        t204.end_fill()
        
        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Text, 'option_', 'heating')
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(0.5)
        
        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'numeric', 1)
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(0.5)
        
        
                
            
        flag_temperature = True
        flag_turtle_4=True          
        print("esteile")
        #thermasni thermokipiou
    else:
        print("eixame na klegame")
        
plant_categ = ''
plant_humidity = 0
current_time = ''
plant_water = False
plant_fertilize = False
location = 0
receive_1 = 1.0
flag_fertilize_1 = True
flag_fertilize_2 = True
flag_fertilize_3 = True
flag_fertilize_4 = True



    
def humidity_0():
    channel = 18
    flag_0 = 0
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.IN) 
    if GPIO.input(channel):
        flag_0 = 1
    else:
        flag_0 = 0
    return flag_0
    

def humidity_1():
    channel = 27
    flag_1 = 0
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.IN)
    if GPIO.input(channel):
        flag_1 = 1
    else:
        flag_1 = 0
    return flag_1
    

def humidity_2():
    channel = 17
    flag_2 = 0
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.IN)
    if GPIO.input(channel):
        flag_2 = 1
    else:
        flag_2 = 0
    return flag_2

def humidity_3():
    channel = 22
    flag_3 = 0
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.IN)
    if GPIO.input(channel):
        flag_3 = 1
    else:
        flag_3 = 0 
    return flag_3

def erpistria():
    global t96
    global t97
    global t98
    global t99
    global t100
    global t101
    global t102
    global t103
    
    
    global flag_fertilize_1
    global flag_fertilize_2
    global flag_fertilize_3
    global flag_fertilize_4
    
    try:
        lbl300.configure(text="" + str(temperature_inside()))
        lbl300.update()
        time.sleep(0.1)
        
        lbl400.configure(text="" + str(temperature_outside()))
        lbl400.update()
        time.sleep(0.1)
        
            
        lbl500.configure(text="" + str(humidity_0()))
        lbl500.update()
        time.sleep(0.1)
        
        lbl600.configure(text="" + str(humidity_1()))
        lbl600.update()
        time.sleep(0.1)
        
        lbl700.configure(text="" + str(humidity_2()))
        lbl700.update()
        time.sleep(0.1)
        
        lbl800.configure(text="" + str(humidity_3()))
        lbl800.update()
        time.sleep(0.1)
    except:
        pass
    print("configure 2")
    print(flag_fertilize_1)
    print(flag_fertilize_2)
    print(flag_fertilize_3)
    print(flag_fertilize_4)
    if humidity_0() == True and flag_fertilize_1==True:
        print("1")
        lbl300.configure(text="" + str(temperature_inside()))
        lbl300.update()
        time.sleep(0.1)
        
        lbl400.configure(text="" + str(temperature_outside()))
        lbl400.update()
        time.sleep(0.1)
                    
        lbl500.configure(text="" + str(humidity_0()))
        lbl500.update()
        time.sleep(0.1)
        
        t102 = turtle.Turtle()
        t102.color("black")
        t102.shape("arrow")
        t102.speed(20)
        t102.hideturtle()
        t102.penup()
        t102.goto(150, 200)
        t102.fillcolor("black")
        t102.begin_fill()
        t102.goto(150, 150)
        t102.goto(200, 150)
        t102.goto(200, 200)
        t102.goto(150, 200)
        t102.end_fill()

        t103 = turtle.Turtle()
        t103.color("black")
        t103.shape("arrow")
        t103.speed(20)
        t103.hideturtle()
        t103.penup()
        t103.goto(150, -150)
        t103.fillcolor("black")
        t103.begin_fill()
        t103.goto(150, -100)
        t103.goto(200, -100)
        t103.goto(200, -150)
        t103.goto(150, -150)
        t103.end_fill()
        
        
    
        try:
            display.lcd_display_string(str("1 needs to be "), 1)
            display.lcd_display_string(str("fertilized"), 2)
        except KeyboardInterrupt:
            print("Cleaning up!")
            display.lcd_clear()
    
        plant_categ  = '0'
        plant_humidity = humidity_0
        plant_fertilize = True
        current_time = datetime.datetime.now() 
        
        s_1 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'number', 0) #lipasma
        EV3_1.write(s_1)
        print(EV3BT.printMessage(s_1))
        time.sleep(0.5)
        
        flag_fertilize_1=False
        flag_fertilize_2=True
        flag_fertilize_3=True
        flag_fertilize_4=True
        
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 666.0:
                    break
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 250.0:
                    break
        t102.clear()        
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 750.0:
                    t103.clear()
                    time.sleep(0.5)
                    try:
                        display.lcd_display_string(str("                "), 1)
                        display.lcd_display_string(str("                "), 2)
                    except KeyboardInterrupt:
                        print("Cleaning up!")
                        display.lcd_clear()
                    lbl300.configure(text="" + str(temperature_inside()))
                    lbl300.update()
                    time.sleep(0.1)
                    
                    lbl400.configure(text="" + str(temperature_outside()))
                    lbl400.update()
                    time.sleep(0.1)
                    
                    lbl500.configure(text="" + str(humidity_0()))
                    lbl500.update()
                    time.sleep(0.1)
                    break
       
       
       
        
 
        
    
    
    
    
    elif humidity_1() == True and flag_fertilize_2==True:
        print("2")
        lbl300.configure(text="" + str(temperature_inside()))
        lbl300.update()
        time.sleep(0.1)
        
        lbl400.configure(text="" + str(temperature_outside()))
        lbl400.update()
        time.sleep(0.1)
        
        lbl600.configure(text="" + str(humidity_1()))
        lbl600.update()
        time.sleep(0.1)
        
        t100 = turtle.Turtle()
        t100.color("black")
        t100.shape("arrow")
        t100.speed(20)
        t100.hideturtle()
        t100.penup()
        t100.speed(3)
        t100.goto(0, 200)
        t100.fillcolor("black")
        t100.begin_fill()
        t100.goto(0, 150)
        t100.goto(50, 150)
        t100.goto(50, 200)
        t100.goto(0, 200)
        t100.end_fill()

        t101 = turtle.Turtle()
        t101.color("black")
        t101.shape("arrow")
        t101.speed(20)
        t101.hideturtle()
        t101.penup()
        t101.goto(0, -150)
        t101.fillcolor("black")
        t101.begin_fill()
        t101.goto(0, -100)
        t101.goto(50, -100)
        t101.goto(50, -150)
        t101.goto(0, -150)
        t101.end_fill()
        
        
        try:
            display.lcd_display_string(str("2 needs to be "), 1)
            display.lcd_display_string(str("fertilized"), 2)
        except KeyboardInterrupt:
            print("Cleaning up!")
            display.lcd_clear()
    
        
        plant_categ  = '1'
        plant_humidity = humidity_1
        plant_fertilize = True
        current_time = datetime.datetime.now()
                        
        s_1 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'number', 1) #lipasma
        EV3_1.write(s_1)
        print(EV3BT.printMessage(s_1))
        time.sleep(0.5)
        
        
        flag_fertilize_1=True
        flag_fertilize_2=False
        flag_fertilize_3=True
        flag_fertilize_4=True
        
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 666.0:
                    break
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 250.0:
                    break
        t100.clear()        
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 750.0:
                    t101.clear()
                    time.sleep(0.5)
                    try:
                        display.lcd_display_string(str("                "), 1)
                        display.lcd_display_string(str("                "), 2)
                    except KeyboardInterrupt:
                        print("Cleaning up!")
                        display.lcd_clear()
                    lbl300.configure(text="" + str(temperature_inside()))
                    lbl300.update()
                    time.sleep(0.1)
                    
                    lbl400.configure(text="" + str(temperature_outside()))
                    lbl400.update()
                    time.sleep(0.1)
                    
                    lbl600.configure(text="" + str(humidity_1()))
                    lbl600.update()
                    time.sleep(0.1)
                    break
        
       
            
    
    
    elif humidity_2() == True and flag_fertilize_3==True:
        print("3")
        lbl300.configure(text="" + str(temperature_inside()))
        lbl300.update()
        time.sleep(0.1)
        
        lbl400.configure(text="" + str(temperature_outside()))
        lbl400.update()
        time.sleep(0.1)
        
        lbl700.configure(text="" + str(humidity_2()))
        lbl700.update()
        time.sleep(0.1)
        
        t98 = turtle.Turtle()
        t98.color("black")
        t98.shape("arrow")
        t98.speed(20)
        t98.hideturtle()
        t98.penup()
        t98.speed(3)
        t98.goto(-150, 200)
        t98.fillcolor("black")
        t98.begin_fill()
        t98.goto(-150, 150)
        t98.goto(-100, 150)
        t98.goto(-100, 200)
        t98.goto(-150, 200)
        t98.end_fill()

        t99 = turtle.Turtle()
        t99.color("black")
        t99.shape("arrow")
        t99.speed(20)
        t99.hideturtle()
        t99.penup()
        t99.goto(-150, -150)
        t99.fillcolor("black")
        t99.begin_fill()
        t99.goto(-150, -100)
        t99.goto(-100, -100)
        t99.goto(-100, -150)
        t99.goto(-150, -150)
        t99.end_fill()

        try:
            display.lcd_display_string(str("3 needs to be "), 1)
            display.lcd_display_string(str("fertilized"), 2)
        except KeyboardInterrupt:
            print("Cleaning up!")
            display.lcd_clear()
    
        plant_categ  = '2'
        plant_humidity = humidity_2
        plant_fertilize = True
        current_time = datetime.datetime.now()
        
        s_1 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'number', 2) #lipasma
        EV3_1.write(s_1)
        print(EV3BT.printMessage(s_1))
        time.sleep(0.5)
        
        flag_fertilize_1=True
        flag_fertilize_2=True
        flag_fertilize_3=False
        flag_fertilize_4=True
        
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 666.0:
                    break
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 250.0:
                    break
        t98.clear()        
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 750.0:
                    t99.clear()
                    time.sleep(0.5)
                    try:
                        display.lcd_display_string(str("                "), 1)
                        display.lcd_display_string(str("                "), 2)
                    except KeyboardInterrupt:
                        print("Cleaning up!")
                        display.lcd_clear()
                    lbl300.configure(text="" + str(temperature_inside()))
                    lbl300.update()
                    time.sleep(0.1)
                    
                    lbl400.configure(text="" + str(temperature_outside()))
                    lbl400.update()
                    time.sleep(0.1)
                    
                    lbl700.configure(text="" + str(humidity_2()))
                    lbl700.update()
                    time.sleep(0.1)
                    break
       
       
       
                    
       

    
        
    
    elif humidity_3() == True and flag_fertilize_4==True:
        print("4")
        lbl300.configure(text="" + str(temperature_inside()))
        lbl300.update()
        time.sleep(0.1)
        
        lbl400.configure(text="" + str(temperature_outside()))
        lbl400.update()
        time.sleep(0.1)
        
        lbl800.configure(text="" + str(humidity_3()))
        lbl800.update()
        time.sleep(0.1)
        
        t96 = turtle.Turtle()
        t96.color("black")
        t96.shape("arrow")
        t96.speed(20)
        t96.hideturtle()
        t96.penup()
        t96.speed(3)
        t96.goto(-300, 200)
        t96.fillcolor("black")
        t96.begin_fill()
        t96.goto(-300, 150)
        t96.goto(-250, 150)
        t96.goto(-250, 200)
        t96.goto(-300, 200)
        t96.end_fill()

        t97 = turtle.Turtle()
        t97.color("black")
        t97.shape("arrow")
        t97.speed(20)
        t97.hideturtle()
        t97.penup()
        t97.goto(-300, -150)
        t97.fillcolor("black")
        t97.begin_fill()
        t97.goto(-300, -100)
        t97.goto(-250, -100)
        t97.goto(-250, -150)
        t97.goto(-300, -150)
        t97.end_fill()
        


        try:
            display.lcd_display_string(str("4 needs to be "), 1)
            display.lcd_display_string(str("fertilized"), 2)
        except KeyboardInterrupt:
            print("Cleaning up!")
            display.lcd_clear()
    
        plant_categ  = '3'
        plant_humidity = humidity_3
        plant_fertilize = True
        current_time = datetime.datetime.now()
        
        s_1 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'number', 3) #lipasma
        EV3_1.write(s_1)
        print(EV3BT.printMessage(s_1))
        time.sleep(0.5)
        
        flag_fertilize_1=True
        flag_fertilize_2=True
        flag_fertilize_3=True
        flag_fertilize_4=False
        
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 666.0:
                    break
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 250.0:
                    break
        t96.clear()        
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 750.0:
                    t97.clear()
                    time.sleep(0.5)
                    try:
                        display.lcd_display_string(str("                "), 1)
                        display.lcd_display_string(str("                "), 2)
                    except KeyboardInterrupt:
                        print("Cleaning up!")
                        display.lcd_clear()
                    lbl300.configure(text="" + str(temperature_inside()))
                    lbl300.update()
                    time.sleep(0.1)
                    
                    lbl400.configure(text="" + str(temperature_outside()))
                    lbl400.update()
                    time.sleep(0.1)
                    
                    lbl800.configure(text="" + str(humidity_3()))
                    lbl800.update()
                    time.sleep(0.1)
                    break
        
        
       
       
        

   



#flag = True
flag_automatic = True

    


window = Tk()
window.geometry("636x463+3+572")
window.title("Menu")

#flag = True

def first_window():
    global t90
    global t91
    global t92
    global t93
    global t94
    global t95
    global t96

    global btn1
    btn1 = Button(window, text="Automatic", fg="black", bg="light blue", width=22, height=2, command = automatic)
    btn1.grid(column=8, row=9, columnspan=10, pady=90, padx=200)

    global btn2
    btn2 = Button(window, text="Manual", fg="black", bg="light blue", width=22, height=2, command = manual)
    btn2.grid(column=8, row=10, columnspan=10, pady=0, padx=200)
    window.update()
    
def automatic():
    global t90
    global t91
    global t92
    global t93
    global t94
    global t95
    global t96
    
    global flag_turtle
    global flag_automatic
    flag_automatic= True

    window.geometry("636x463+3+572")
    window.title("Automatic")

    btn1.destroy()
    btn2.destroy()

    global lbl1
    lbl1 = Label(window, justify='right', text="Automatic Mode", font=('Times', 15, 'bold'))
    lbl1.grid(column=1, row=0)

    global lbl2
    lbl2 = Label(window, justify='right', text="Ideal Temperature:")
    lbl2.grid(column=1, row=1)
    
    global lbl666
    lbl666 = Label(window, justify='left', text="17 - 22 C")
    lbl666.grid(column=2, row=1)

    global lbl10000
    lbl10000 = Label(window, justify='right', text="")
    lbl10000.grid(column=1, row=2)

    global lbl3
    lbl3 = Label(window, justify='right', text="Temperature inside: ")
    lbl3.grid(column=1, row=3)

    global lbl300
    lbl300 = Label(window, justify='right',text=""+ str(temperature_inside()) )
    lbl300.grid(column=2, row=3)


    global lbl4
    lbl4 = Label(window, justify='right', text="Temperature outside:")
    lbl4.grid(column=1, row=4)

    global lbl400
    lbl400 = Label(window, justify='right', text=""+ str(temperature_outside()))
    lbl400.grid(column=2, row=4)

    global lbl10001
    lbl10001 = Label(window, justify='right', text="")
    lbl10001.grid(column=1, row=5)

    global lbl5
    lbl5 = Label(window, justify='left', text="Plant #1 Humidity:")
    lbl5.grid(column=1, row=6)

    global lbl500
    lbl500 = Label(window, justify='right', text=""+ str(humidity_0()))
    lbl500.grid(column=2, row=6)

    global lbl6
    lbl6 = Label(window, justify='left', text="Plant #2 Humidity:")
    lbl6.grid(column=1, row=7)

    global lbl600
    lbl600 = Label(window, justify='right', text=""+ str(humidity_1()))
    lbl600.grid(column=2, row=7)

    global lbl7
    lbl7 = Label(window, justify='left', text="Plant #3 Humidity:")
    lbl7.grid(column=1, row=8)

    global lbl700
    lbl700 = Label(window, justify='right', text=""+ str(humidity_2()))
    lbl700.grid(column=2, row=8)

    global lbl8
    lbl8 = Label(window, justify='left', text="Plant #4 Humidity:")
    lbl8.grid(column=1, row=9)

    global lbl800
    lbl800 = Label(window, justify='right', text=""+ str(humidity_3()))
    lbl800.grid(column=2, row=9)

    global lbl10002
    lbl10002 = Label(window, justify='right', text="")
    lbl10002.grid(column=1, row=16)
    
    
    global lbl9
    lbl9 = Label(window, justify='right', text="Fans:")
    lbl9.grid(column=1, row=12)

    global lbl900
    lbl900 = Label(window, justify='right', text="Off")
    lbl900.grid(column=2, row=12)

    global lbl10
    lbl10 = Label(window, justify='right', text="Windows:")
    lbl10.grid(column=1, row=13)

    global lbl1000
    lbl1000 = Label(window, justify='right', text="Off")
    lbl1000.grid(column=2, row=13)

    global lbl11
    lbl11 = Label(window, justify='right', text="Kettle:")
    lbl11.grid(column=1, row=14)

    global lbl1100
    lbl1100 = Label(window, justify='right', text="Off")
    lbl1100.grid(column=2, row=14)

    
    global btn3
    btn3 = Button(window, text="Back", fg="black", bg="light blue", width=10, height=2, command = back)
    btn3.grid(column=1, row=15)
    
    s_1 = EV3BT.encodeMessage(EV3BT.MessageType.Text, 'A_M_1', 'Automatic') 
    EV3_1.write(s_1)
    print("esteile")
    print(EV3BT.printMessage(s_1))
    time.sleep(0.2)
    
    s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Text, 'A_M_2', 'Automatic') 
    EV3_2.write(s_2)
    print(EV3BT.printMessage(s_2))
    time.sleep(0.2)
    
    tr=turtle.Screen()
    scn = turtle.Screen()
    scn.bgcolor("white")
    turtle.title("AirField Program")
    tr.setup(width=1276,height=982,startx=640,starty=52)
    
    t1 = turtle.Turtle()
    t1.color("black")
    t1.shape("arrow")
    t1.speed(20)
    t1.hideturtle()
    t1.penup()
    t1.goto(-300, 200)
    t1.speed(7)
    t1.pendown()
    t1.goto(-300, 150)
    t1.goto(-250, 150)
    t1.goto(-250, 200)
    t1.goto(-300, 200)
    t1.penup()
    t1.goto(-150, 200)
    t1.pendown()
    t1.goto(-150, 150)
    t1.goto(-100, 150)
    t1.goto(-100, 200)
    t1.goto(-150, 200)
    t1.penup()
    t1.goto(0, 200)
    t1.pendown()
    t1.goto(0, 150)
    t1.goto(50, 150)
    t1.goto(50, 200)
    t1.goto(0, 200)
    t1.penup()
    t1.goto(150, 200)
    t1.pendown()
    t1.goto(150, 150)
    t1.goto(200, 150)
    t1.goto(200, 200)
    t1.goto(150, 200)
    t1.penup()

    t2 = turtle.Turtle()
    t2.color("black")
    t2.shape("arrow")
    t2.speed(20)
    t2.hideturtle()
    t2.penup()
    t2.goto(-300, 0)
    t2.speed(7)
    t2.pendown()
    t2.goto(200, 0)
    t2.goto(200, 50)
    t2.goto(-300, 50)
    t2.goto(-300, 0)
    t2.penup()

    t3 = turtle.Turtle()
    t3.color("black")
    t3.shape("arrow")
    t3.speed(20)
    t3.hideturtle()
    t3.penup()
    t3.goto(-300, -150)
    t3.speed(7)
    t3.pendown()
    t3.goto(-300, -100)
    t3.goto(-250, -100)
    t3.goto(-250, -150)
    t3.goto(-300, -150)
    t3.penup()
    t3.goto(-150, -150)
    t3.pendown()
    t3.goto(-150, -100)
    t3.goto(-100, -100)
    t3.goto(-100, -150)
    t3.goto(-150, -150)
    t3.penup()
    t3.goto(0, -150)
    t3.pendown()
    t3.goto(0, -100)
    t3.goto(50, -100)
    t3.goto(50, -150)
    t3.goto(0, -150)
    t3.penup()
    t3.goto(150, -150)
    t3.pendown()
    t3.goto(150, -100)
    t3.goto(200, -100)
    t3.goto(200, -150)
    t3.goto(150, -150)

    t4 = turtle.Turtle()
    t4.color("black")
    t4.shape("arrow")
    t4.speed(20)
    t4.hideturtle()
    t4.penup()
    t4.goto(-325, 250)
    t4.speed(7)
    t4.pendown()
    t4.goto(225, 250)

    t5 = turtle.Turtle()
    t5.color("black")
    t5.shape("arrow")
    t5.speed(20)
    t5.hideturtle()
    t5.penup()
    t5.goto(-325, -200)
    t5.speed(7)
    t5.pendown()
    t5.goto(225, -200)

    t6 = turtle.Turtle()
    t6.color("black")
    t6.shape("arrow")
    t6.speed(20)
    t6.hideturtle()
    t6.penup()
    t6.goto(-325, -200)
    t6.speed(7)
    t6.pendown()
    t6.goto(-325, 250)

    t7 = turtle.Turtle()
    t7.color("black")
    t7.shape("arrow")
    t7.speed(20)
    t7.hideturtle()
    t7.penup()
    t7.goto(225, -200)
    t7.speed(7)
    t7.pendown()
    t7.goto(225, 250)

    t8 = turtle.Turtle()
    t8.color("black")
    t8.shape("arrow")
    t8.speed(20)
    t8.hideturtle()
    t8.penup()
    t8.goto(-200, 90)
    t8.speed(7)
    t8.pendown()
    t8.circle(20)

    t9 = turtle.Turtle()
    t9.color("black")
    t9.shape("arrow")
    t9.speed(20)
    t9.hideturtle()
    t9.penup()
    t9.goto(-200, -80)
    t9.speed(7)
    t9.pendown()
    t9.circle(20)

    t10 = turtle.Turtle()
    t10.color("black")
    t10.shape("arrow")
    t10.speed(20)
    t10.hideturtle()
    t10.penup()
    t10.goto(100, 90)
    t10.speed(7)
    t10.pendown()
    t10.circle(20)

    t11 = turtle.Turtle()
    t11.color("black")
    t11.shape("arrow")
    t11.speed(20)
    t11.hideturtle()
    t11.penup()
    t11.goto(100, -80)
    t11.speed(7)
    t11.pendown()
    t11.circle(20)

    t12 = turtle.Turtle()
    t12.color("black")
    t12.shape("arrow")
    t12.speed(20)
    t12.hideturtle()
    t12.penup()
    t12.goto(-300, 100)
    t12.speed(10)
    t12.pendown()
    t12.circle(10)

    t13 = turtle.Turtle()
    t13.color("black")
    t13.shape("arrow")
    t13.speed(20)
    t13.hideturtle()
    t13.penup()
    t13.goto(-300, -70)
    t13.speed(10)
    t13.pendown()
    t13.circle(10)
    
    
    
    
   
    while 1:
        if flag_automatic == False:
            break
        else:
            window.update()
            temperature_actions()
            erpistria()
   
            

    
            

def back():
    
    global flag_automatic
    flag_automatic = False
    flag_fertilize_1 = True
    flag_fertilize_2 = True
    flag_fertilize_3 = True
    flag_fertilize_4 = True
    
    s_1 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'interrupt', 2) 
    EV3_1.write(s_1)
    print(EV3BT.printMessage(s_1))
    time.sleep(0.2)
    
    s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'interrupt',2) 
    EV3_2.write(s_2)
    print(EV3BT.printMessage(s_2))
    time.sleep(0.2)
    
    
    
    window.geometry("636x463+3+572")
    window.title("Menu")

    lbl1.destroy()
    lbl2.destroy()
    lbl666.destroy()   
    lbl10000.destroy()
    lbl3.destroy()
    lbl300.destroy()
    lbl4.destroy()
    lbl400.destroy()
    lbl10001.destroy()
    lbl5.destroy()
    lbl500.destroy()
    lbl6.destroy()
    lbl600.destroy()
    lbl7.destroy()
    lbl700.destroy()
    lbl8.destroy()
    lbl800.destroy()
    lbl10002.destroy()
    lbl9.destroy()
    lbl900.destroy()
    lbl10.destroy()
    lbl1000.destroy()
    lbl11.destroy()
    lbl1100.destroy()

    btn3.destroy()
    
    turtle.clearscreen()


    first_window()

def manual():
    global btn1
    global btn2
    
    
    s_1 = EV3BT.encodeMessage(EV3BT.MessageType.Text, 'A_M_1', 'Manual') 
    EV3_1.write(s_1)
    print(EV3BT.printMessage(s_1))
    time.sleep(0.2)
    
    s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Text, 'A_M_2', 'Manual') 
    EV3_2.write(s_2)
    print(EV3BT.printMessage(s_2))
    time.sleep(0.2)
    
    window.geometry("636x463+3+572")
    window.title("Manual")

    btn1.destroy()
    btn2.destroy()

    global lbl12
    lbl12 = Label(window, justify='right', text="Manual Mode", font=('Times', 15, 'bold'))
    lbl12.grid(column=0, row=0, columnspan=10, pady=3)

    global lbl13
    lbl13 = Label(window, justify='right', text="Ideal Temperature (ins): 17 - 22 C")
    lbl13.grid(column=1, row=1, columnspan=10, pady=0, padx=0)

    global lbl10003
    lbl10003 = Label(window, justify='right', text="")
    lbl10003.grid(column=1, row=2)

    global lbl14
    lbl14 = Label(window, justify='right', text="Temperature inside:")
    lbl14.grid(column=1, row=3)

    global lbl15
    lbl15 = Label(window, justify='right', text="Temperature outside:")
    lbl15.grid(column=1, row=4)

    global lbl10004
    lbl10004 = Label(window, justify='right', text="")
    lbl10004.grid(column=1, row=5)

    global lbl16
    lbl16 = Label(window, justify='right', text="Plant #1 Humidity:")
    lbl16.grid(column=1, row=6)

    global lbl17
    lbl17 = Label(window, justify='right', text="Plant #2 Humidity:")
    lbl17.grid(column=1, row=7)

    global lbl18
    lbl18 = Label(window, justify='right', text="Plant #3 Humidity:")
    lbl18.grid(column=1, row=8)

    global lbl19
    lbl19 = Label(window, justify='right', text="Plant #4 Humidity:")
    lbl19.grid(column=1, row=9)

    global txt1
    txt1 = Entry(window, width=10)
    txt1.grid(column=2, row=3)

    global txt2
    txt2 = Entry(window, width=10)
    txt2.grid(column=2, row=4)

    global txt3
    txt3 = Entry(window, width=10)
    txt3.grid(column=2, row=6)

    global txt4
    txt4 = Entry(window, width=10)
    txt4.grid(column=2, row=7)

    global txt5
    txt5 = Entry(window, width=10)
    txt5.grid(column=2, row=8)

    global txt6
    txt6 = Entry(window, width=10)
    txt6.grid(column=2, row=9)

    global btn4
    btn4 = Button(window, text="Clear", fg="black", bg="light blue", width=15, height=2, command = clear)
    btn4.grid(column=1, row=10, columnspan=1, pady=5, padx=2)

    global btn5
    btn5 = Button(window, text="Back", fg="black", bg="light blue", width=15, height=2, command = back2)
    btn5.grid(column=2, row=10, columnspan=1, pady=5, padx=2)

    global btn6
    btn6 = Button(window, text="Submit", fg="black", bg="green", width=32, height=2, command = submit)
    btn6.grid(column=1, row=11, columnspan=2, pady=0, padx=0)

    tr= turtle.Screen()
    scn = turtle.Screen()
    scn.bgcolor("white")
    turtle.title("AirField Program")
    tr.setup(width=1276,height=982,startx=640,starty=52)
   

    t1 = turtle.Turtle()
    t1.color("black")
    t1.shape("arrow")
    t1.speed(20)
    t1.hideturtle()
    t1.penup()
    t1.goto(-300, 200)
    t1.speed(7)
    t1.pendown()
    t1.goto(-300, 150)
    t1.goto(-250, 150)
    t1.goto(-250, 200)
    t1.goto(-300, 200)
    t1.penup()
    t1.goto(-150, 200)
    t1.pendown()
    t1.goto(-150, 150)
    t1.goto(-100, 150)
    t1.goto(-100, 200)
    t1.goto(-150, 200)
    t1.penup()
    t1.goto(0, 200)
    t1.pendown()
    t1.goto(0, 150)
    t1.goto(50, 150)
    t1.goto(50, 200)
    t1.goto(0, 200)
    t1.penup()
    t1.goto(150, 200)
    t1.pendown()
    t1.goto(150, 150)
    t1.goto(200, 150)
    t1.goto(200, 200)
    t1.goto(150, 200)
    t1.penup()

    t2 = turtle.Turtle()
    t2.color("black")
    t2.shape("arrow")
    t2.speed(20)
    t2.hideturtle()
    t2.penup()
    t2.goto(-300, 0)
    t2.speed(7)
    t2.pendown()
    t2.goto(200, 0)
    t2.goto(200, 50)
    t2.goto(-300, 50)
    t2.goto(-300, 0)
    t2.penup()

    t3 = turtle.Turtle()
    t3.color("black")
    t3.shape("arrow")
    t3.speed(20)
    t3.hideturtle()
    t3.penup()
    t3.goto(-300, -150)
    t3.speed(7)
    t3.pendown()
    t3.goto(-300, -100)
    t3.goto(-250, -100)
    t3.goto(-250, -150)
    t3.goto(-300, -150)
    t3.penup()
    t3.goto(-150, -150)
    t3.pendown()
    t3.goto(-150, -100)
    t3.goto(-100, -100)
    t3.goto(-100, -150)
    t3.goto(-150, -150)
    t3.penup()
    t3.goto(0, -150)
    t3.pendown()
    t3.goto(0, -100)
    t3.goto(50, -100)
    t3.goto(50, -150)
    t3.goto(0, -150)
    t3.penup()
    t3.goto(150, -150)
    t3.pendown()
    t3.goto(150, -100)
    t3.goto(200, -100)
    t3.goto(200, -150)
    t3.goto(150, -150)

    t4 = turtle.Turtle()
    t4.color("black")
    t4.shape("arrow")
    t4.speed(20)
    t4.hideturtle()
    t4.penup()
    t4.goto(-325, 250)
    t4.speed(7)
    t4.pendown()
    t4.goto(225, 250)

    t5 = turtle.Turtle()
    t5.color("black")
    t5.shape("arrow")
    t5.speed(20)
    t5.hideturtle()
    t5.penup()
    t5.goto(-325, -200)
    t5.speed(7)
    t5.pendown()
    t5.goto(225, -200)

    t6 = turtle.Turtle()
    t6.color("black")
    t6.shape("arrow")
    t6.speed(20)
    t6.hideturtle()
    t6.penup()
    t6.goto(-325, -200)
    t6.speed(7)
    t6.pendown()
    t6.goto(-325, 250)

    t7 = turtle.Turtle()
    t7.color("black")
    t7.shape("arrow")
    t7.speed(20)
    t7.hideturtle()
    t7.penup()
    t7.goto(225, -200)
    t7.speed(7)
    t7.pendown()
    t7.goto(225, 250)

    t8 = turtle.Turtle()
    t8.color("black")
    t8.shape("arrow")
    t8.speed(20)
    t8.hideturtle()
    t8.penup()
    t8.goto(-200, 90)
    t8.speed(7)
    t8.pendown()
    t8.circle(20)

    t9 = turtle.Turtle()
    t9.color("black")
    t9.shape("arrow")
    t9.speed(20)
    t9.hideturtle()
    t9.penup()
    t9.goto(-200, -80)
    t9.speed(7)
    t9.pendown()
    t9.circle(20)

    t10 = turtle.Turtle()
    t10.color("black")
    t10.shape("arrow")
    t10.speed(20)
    t10.hideturtle()
    t10.penup()
    t10.goto(100, 90)
    t10.speed(7)
    t10.pendown()
    t10.circle(20)

    t11 = turtle.Turtle()
    t11.color("black")
    t11.shape("arrow")
    t11.speed(20)
    t11.hideturtle()
    t11.penup()
    t11.goto(100, -80)
    t11.speed(7)
    t11.pendown()
    t11.circle(20)

    t12 = turtle.Turtle()
    t12.color("black")
    t12.shape("arrow")
    t12.speed(20)
    t12.hideturtle()
    t12.penup()
    t12.goto(-300, 100)
    t12.speed(10)
    t12.pendown()
    t12.circle(10)

    t13 = turtle.Turtle()
    t13.color("black")
    t13.shape("arrow")
    t13.speed(20)
    t13.hideturtle()
    t13.penup()
    t13.goto(-300, -70)
    t13.speed(10)
    t13.pendown()
    t13.circle(10)
    

        
def clear():

    txt1.delete(0, "end")
    txt2.delete(0, "end")
    txt3.delete(0, "end")
    txt4.delete(0, "end")
    txt5.delete(0, "end")
    txt6.delete(0, "end")

def back2():
    
    s_1 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'interrupt', 3) 
    EV3_1.write(s_1)
    print(EV3BT.printMessage(s_1))
    time.sleep(0.2)
    
    s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'interrupt',3) 
    EV3_2.write(s_2)
    print(EV3BT.printMessage(s_2))
    time.sleep(0.2)
    
    window.geometry("636x463+3+572")
    window.title("Menu")

    lbl12.destroy()
    lbl13.destroy()
    lbl10003.destroy()
    lbl14.destroy()
    lbl15.destroy()
    lbl10004.destroy()
    lbl16.destroy()
    lbl17.destroy()
    lbl18.destroy()
    lbl19.destroy()

    txt1.destroy()
    txt2.destroy()
    txt3.destroy()
    txt4.destroy()
    txt5.destroy()
    txt6.destroy()

    btn4.destroy()
    btn5.destroy()
    btn6.destroy()

    turtle.clearscreen()

    first_window()

def submit():

    hum_1 = txt3.get()
    global c
    c = int(hum_1)
    
    hum_2= txt4.get()
    global d
    d = int(hum_2)
    
    hum_3 = txt5.get()
    global e
    e = int(hum_3)
    
    hum_4 = txt6.get()
    global q
    q = int(hum_4)
    
    if ((c != 0) and (c != 1)) or ((d != 0) and (d != 1)) or ((e != 0) and (e != 1)) or ((q != 0) and (q != 1)):
        messagebox.showerror("Invalid Values", "The plant humidities should be 0 or 1!")
    
    
        window.geometry("636x463+3+572")
        window.title("Manual")
        
        clear()
        
    else:

        window.geometry("636x463+3+572")
        window.title("Manual")

        lbl13.destroy()
        lbl10003.destroy()
        lbl14.destroy()
        lbl15.destroy()
        lbl10004.destroy()
        lbl16.destroy()
        lbl17.destroy()
        lbl18.destroy()
        lbl19.destroy()

        btn4.destroy()
        btn5.destroy()
        btn6.destroy()

        global lbl20
        temp_ins = txt1.get()
        global a
        a = int(temp_ins)
        lbl20 = Label(window, justify='right', text="The temperature inside is: " + str(a))
        lbl20.grid(column=1, row=1)

        global lbl21
        temp_out = txt2.get()
        global b
        b = int(temp_out)
        lbl21 = Label(window, justify='right', text="The temperature outside is: " + str(b))
        lbl21.grid(column=1, row=2)

        global lbl22
        lbl22 = Label(window, justify='right', text="The first plant humidity is: " + str(c))
        lbl22.grid(column=1, row=5)

        global lbl23
        lbl23 = Label(window, justify='right', text="The second plant humidity is: " + str(d))
        lbl23.grid(column=1, row=6)

        global lbl24
        lbl24 = Label(window, justify='right', text="The third plant humidity is: " + str(e))
        lbl24.grid(column=1, row=7)

        global lbl25
        lbl25 = Label(window, justify='right', text="The fourth plant humidity is: " + str(q))
        lbl25.grid(column=1, row=8)
        
        

        global btn7
        btn7 = Button(window, text="Back", fg="black", bg="light blue", width=22, height=2, command = back3)
        btn7.grid(column=1, row=9, columnspan=1, pady=5)
        global btn8
        btn8 = Button(window, text="Visualization", fg="black", bg="green", width=22, height=2, command = visualization)
        btn8.grid(column=1, row=10, columnspan=2, pady=0)
        
        txt1.destroy()
        txt2.destroy()
        txt3.destroy()
        txt4.destroy()
        txt5.destroy()
        txt6.destroy()

def back3():
    
    s_1 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'interrupt', 3) 
    EV3_1.write(s_1)
    print(EV3BT.printMessage(s_1))
    time.sleep(0.2)
    
    s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'interrupt',3) 
    EV3_2.write(s_2)
    print(EV3BT.printMessage(s_2))
    time.sleep(0.2)
    
    window.geometry("636x463+3+572")
    window.title("Menu")

    lbl12.destroy()
    lbl20.destroy()
    lbl21.destroy()
    lbl22.destroy()
    lbl23.destroy()
    lbl24.destroy()
    lbl25.destroy()

    btn7.destroy()
    btn8.destroy()

    turtle.clearscreen()

    first_window()

def visualization():

    window.title("Manual")


    flag=0
    global a
    global b

    if (a >= 17) and (a <= 22):

        flag = 5

    elif (a > 22) and (a > b) and (b < 22):

        t90 = turtle.Turtle()
        t90.color("black")
        t90.shape("arrow")
        t90.speed(20)
        t90.hideturtle()
        t90.penup()
        t90.goto(-220, 102)
        t90.speed(3)
        t90.pendown()
        t90.goto(-240, 90)
        t90.penup()
        t90.goto(-180, 102)
        t90.pendown()
        t90.goto(-160, 90)
        t90.penup()
        t90.goto(-200, 130)
        t90.pendown()
        t90.goto(-200, 150)

        t91 = turtle.Turtle()
        t91.color("black")
        t91.shape("arrow")
        t91.speed(20)
        t91.hideturtle()
        t91.penup()
        t91.goto(-220, -68)
        t91.speed(3)
        t91.pendown()
        t91.goto(-240, -80)
        t91.penup()
        t91.goto(-180, -68)
        t91.pendown()
        t91.goto(-160, -80)
        t91.penup()
        t91.goto(-200, -40)
        t91.pendown()
        t91.goto(-200, -20)

        t92 = turtle.Turtle()
        t92.color("black")
        t92.shape("arrow")
        t92.speed(20)
        t92.hideturtle()
        t92.penup()
        t92.goto(80, 102)
        t92.speed(3)
        t92.pendown()
        t92.goto(60, 90)
        t92.penup()
        t92.goto(120, 102)
        t92.pendown()
        t92.goto(140, 90)
        t92.penup()
        t92.goto(100, 130)
        t92.pendown()
        t92.goto(100, 150)

        t93 = turtle.Turtle()
        t93.color("black")
        t93.shape("arrow")
        t93.speed(20)
        t93.hideturtle()
        t93.penup()
        t93.goto(80, -68)
        t93.speed(3)
        t93.pendown()
        t93.goto(60, -80)
        t93.penup()
        t93.goto(120, -68)
        t93.pendown()
        t93.goto(140, -80)
        t93.penup()
        t93.goto(100, -40)
        t93.pendown()
        t93.goto(100, -20)

        t94 = turtle.Turtle()
        t94.color("black")
        t94.shape("arrow")
        t94.speed(20)
        t94.hideturtle()
        t94.penup()
        t94.goto(-325, 250)
        t94.speed(3)
        t94.pendown()
        t94.goto(-300, 275)
        t94.penup()
        t94.goto(-270, 250)
        t94.pendown()
        t94.goto(-245, 275)
        t94.penup()
        t94.goto(-215, 250)
        t94.pendown()
        t94.goto(-190, 275)
        t94.penup()
        t94.goto(-160, 250)
        t94.pendown()
        t94.goto(-135, 275)
        t94.penup()
        t94.goto(-105, 250)
        t94.pendown()
        t94.goto(-80, 275)
        t94.penup()
        t94.goto(-50, 250)
        t94.pendown()
        t94.goto(-25, 275)
        t94.penup()
        t94.goto(5, 250)
        t94.pendown()
        t94.goto(30, 275)
        t94.penup()
        t94.goto(60, 250)
        t94.pendown()
        t94.goto(85, 275)
        t94.penup()
        t94.goto(115, 250)
        t94.pendown()
        t94.goto(140, 275)
        t94.penup()
        t94.goto(170, 250)
        t94.pendown()
        t94.goto(195, 275)
        t94.penup()
        t94.goto(225, 250)
        t94.pendown()
        t94.goto(250, 275)

        t95 = turtle.Turtle()
        t95.color("black")
        t95.shape("arrow")
        t95.speed(20)
        t95.hideturtle()
        t95.penup()
        t95.goto(-300, -200)
        t95.speed(3)
        t95.pendown()
        t95.goto(-325, -225)
        t95.penup()
        t95.goto(-245, -200)
        t95.pendown()
        t95.goto(-270, -225)
        t95.penup()
        t95.goto(-190, -200)
        t95.pendown()
        t95.goto(-215, -225)
        t95.penup()
        t95.goto(-135, -200)
        t95.pendown()
        t95.goto(-160, -225)
        t95.penup()
        t95.goto(-80, -200)
        t95.pendown()
        t95.goto(-105, -225)
        t95.penup()
        t95.goto(-25, -200)
        t95.pendown()
        t95.goto(-50, -225)
        t95.penup()
        t95.goto(30, -200)
        t95.pendown()
        t95.goto(5, -225)
        t95.penup()
        t95.goto(85, -200)
        t95.pendown()
        t95.goto(60, -225)
        t95.penup()
        t95.goto(140, -200)
        t95.pendown()
        t95.goto(115, -225)
        t95.penup()
        t95.goto(195, -200)
        t95.pendown()
        t95.goto(170, -225)
        t95.penup()
        t95.goto(225, -200)
        t95.pendown()
        t95.goto(200, -225)
        
        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Text, 'option_', 'cooling')
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(1)
         

        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'numeric', 0)
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(1)
        

        flag = 1

    elif ((a > 22) and (a >= b) and (b >= 22)) or ((a > 22) and (a <= b)):

        t200 = turtle.Turtle()
        t200.color("black")
        t200.shape("arrow")
        t200.speed(20)
        t200.hideturtle()
        t200.penup()
        t200.goto(-220, 102)
        t200.speed(3)
        t200.pendown()
        t200.goto(-240, 90)
        t200.penup()
        t200.goto(-180, 102)
        t200.pendown()
        t200.goto(-160, 90)
        t200.penup()
        t200.goto(-200, 130)
        t200.pendown()
        t200.goto(-200, 150)

        t201 = turtle.Turtle()
        t201.color("black")
        t201.shape("arrow")
        t201.speed(20)
        t201.hideturtle()
        t201.penup()
        t201.goto(-220, -68)
        t201.speed(3)
        t201.pendown()
        t201.goto(-240, -80)
        t201.penup()
        t201.goto(-180, -68)
        t201.pendown()
        t201.goto(-160, -80)
        t201.penup()
        t201.goto(-200, -40)
        t201.pendown()
        t201.goto(-200, -20)

        t202 = turtle.Turtle()
        t202.color("black")
        t202.shape("arrow")
        t202.speed(20)
        t202.hideturtle()
        t202.penup()
        t202.goto(80, 102)
        t202.speed(3)
        t202.pendown()
        t202.goto(60, 90)
        t202.penup()
        t202.goto(120, 102)
        t202.pendown()
        t202.goto(140, 90)
        t202.penup()
        t202.goto(100, 130)
        t202.pendown()
        t202.goto(100, 150)

        t203 = turtle.Turtle()
        t203.color("black")
        t203.shape("arrow")
        t203.speed(20)
        t203.hideturtle()
        t203.penup()
        t203.goto(80, -68)
        t203.speed(3)
        t203.pendown()
        t203.goto(60, -80)
        t203.penup()
        t203.goto(120, -68)
        t203.pendown()
        t203.goto(140, -80)
        t203.penup()
        t203.goto(100, -40)
        t203.pendown()
        t203.goto(100, -20) 
        
        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Text, 'option_', 'cooling')
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(1)
         

        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'numeric', 1)
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(1)

        flag = 2

    elif (a < 17) and (a < b) and (b > 17):

        t94 = turtle.Turtle()
        t94.color("black")
        t94.shape("arrow")
        t94.speed(20)
        t94.hideturtle()
        t94.penup()
        t94.goto(-325, 250)
        t94.speed(3)
        t94.pendown()
        t94.goto(-300, 275)
        t94.penup()
        t94.goto(-270, 250)
        t94.pendown()
        t94.goto(-245, 275)
        t94.penup()
        t94.goto(-215, 250)
        t94.pendown()
        t94.goto(-190, 275)
        t94.penup()
        t94.goto(-160, 250)
        t94.pendown()
        t94.goto(-135, 275)
        t94.penup()
        t94.goto(-105, 250)
        t94.pendown()
        t94.goto(-80, 275)
        t94.penup()
        t94.goto(-50, 250)
        t94.pendown()
        t94.goto(-25, 275)
        t94.penup()
        t94.goto(5, 250)
        t94.pendown()
        t94.goto(30, 275)
        t94.penup()
        t94.goto(60, 250)
        t94.pendown()
        t94.goto(85, 275)
        t94.penup()
        t94.goto(115, 250)
        t94.pendown()
        t94.goto(140, 275)
        t94.penup()
        t94.goto(170, 250)
        t94.pendown()
        t94.goto(195, 275)
        t94.penup()
        t94.goto(225, 250)
        t94.pendown()
        t94.goto(250, 275)

        t95 = turtle.Turtle()
        t95.color("black")
        t95.shape("arrow")
        t95.speed(20)
        t95.hideturtle()
        t95.penup()
        t95.goto(-300, -200)
        t95.speed(3)
        t95.pendown()
        t95.goto(-325, -225)
        t95.penup()
        t95.goto(-245, -200)
        t95.pendown()
        t95.goto(-270, -225)
        t95.penup()
        t95.goto(-190, -200)
        t95.pendown()
        t95.goto(-215, -225)
        t95.penup()
        t95.goto(-135, -200)
        t95.pendown()
        t95.goto(-160, -225)
        t95.penup()
        t95.goto(-80, -200)
        t95.pendown()
        t95.goto(-105, -225)
        t95.penup()
        t95.goto(-25, -200)
        t95.pendown()
        t95.goto(-50, -225)
        t95.penup()
        t95.goto(30, -200)
        t95.pendown()
        t95.goto(5, -225)
        t95.penup()
        t95.goto(85, -200)
        t95.pendown()
        t95.goto(60, -225)
        t95.penup()
        t95.goto(140, -200)
        t95.pendown()
        t95.goto(115, -225)
        t95.penup()
        t95.goto(195, -200)
        t95.pendown()
        t95.goto(170, -225)
        t95.penup()
        t95.goto(225, -200)
        t95.pendown()
        t95.goto(200, -225)
        
        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Text, 'option_', 'heating')
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(1)
         

        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'numeric', 0)
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(1)

        flag = 3

    elif (a < 17) and (a <= b) and (b <= 17) or ((a < 17) and (a >= b)):

        t204 = turtle.Turtle()
        t204.color("black")
        t204.shape("arrow")
        t204.speed(20)
        t204.hideturtle()
        t204.fillcolor("black")
        t204.penup()
        t204.goto(-300, 100)
        t204.begin_fill()
        t204.circle(10)
        t204.end_fill()
        t204.penup()
        t204.goto(-300, -70)
        t204.begin_fill()
        t204.circle(10)
        t204.end_fill()
        
        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Text, 'option_', 'heating')
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(1)
        
        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'numeric', 1)
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(1)

        flag = 4

        
    if (c == 1):
        
        t102 = turtle.Turtle()
        t102.color("black")
        t102.shape("arrow")
        t102.speed(20)
        t102.hideturtle()
        t102.penup()
        t102.goto(150, 200)
        t102.fillcolor("black")
        t102.begin_fill()
        t102.goto(150, 150)
        t102.goto(200, 150)
        t102.goto(200, 200)
        t102.goto(150, 200)
        t102.end_fill()

        t103 = turtle.Turtle()
        t103.color("black")
        t103.shape("arrow")
        t103.speed(20)
        t103.hideturtle()
        t103.penup()
        t103.goto(150, -150)
        t103.fillcolor("black")
        t103.begin_fill()
        t103.goto(150, -100)
        t103.goto(200, -100)
        t103.goto(200, -150)
        t103.goto(150, -150)
        t103.end_fill()
        
        
    if (d == 1):
        
        t100 = turtle.Turtle()
        t100.color("black")
        t100.shape("arrow")
        t100.speed(20)
        t100.hideturtle()
        t100.penup()
        t100.speed(3)
        t100.goto(0, 200)
        t100.fillcolor("black")
        t100.begin_fill()
        t100.goto(0, 150)
        t100.goto(50, 150)
        t100.goto(50, 200)
        t100.goto(0, 200)
        t100.end_fill()

        t101 = turtle.Turtle()
        t101.color("black")
        t101.shape("arrow")
        t101.speed(20)
        t101.hideturtle()
        t101.penup()
        t101.goto(0, -150)
        t101.fillcolor("black")
        t101.begin_fill()
        t101.goto(0, -100)
        t101.goto(50, -100)
        t101.goto(50, -150)
        t101.goto(0, -150)
        t101.end_fill()
        
    if (e == 1):
        
        t98 = turtle.Turtle()
        t98.color("black")
        t98.shape("arrow")
        t98.speed(20)
        t98.hideturtle()
        t98.penup()
        t98.speed(3)
        t98.goto(-150, 200)
        t98.fillcolor("black")
        t98.begin_fill()
        t98.goto(-150, 150)
        t98.goto(-100, 150)
        t98.goto(-100, 200)
        t98.goto(-150, 200)
        t98.end_fill()

        t99 = turtle.Turtle()
        t99.color("black")
        t99.shape("arrow")
        t99.speed(20)
        t99.hideturtle()
        t99.penup()
        t99.goto(-150, -150)
        t99.fillcolor("black")
        t99.begin_fill()
        t99.goto(-150, -100)
        t99.goto(-100, -100)
        t99.goto(-100, -150)
        t99.goto(-150, -150)
        t99.end_fill()

    if (q == 1):
        
        t96 = turtle.Turtle()
        t96.color("black")
        t96.shape("arrow")
        t96.speed(20)
        t96.hideturtle()
        t96.penup()
        t96.speed(3)
        t96.goto(-300, 200)
        t96.fillcolor("black")
        t96.begin_fill()
        t96.goto(-300, 150)
        t96.goto(-250, 150)
        t96.goto(-250, 200)
        t96.goto(-300, 200)
        t96.end_fill()

        t97 = turtle.Turtle()
        t97.color("black")
        t97.shape("arrow")
        t97.speed(20)
        t97.hideturtle()
        t97.penup()
        t97.goto(-300, -150)
        t97.fillcolor("black")
        t97.begin_fill()
        t97.goto(-300, -100)
        t97.goto(-250, -100)
        t97.goto(-250, -150)
        t97.goto(-300, -150)
        t97.end_fill()

    
    if (flag == 1):

        while (a != 21):
            lbl20.configure(text="The temperature inside is: " + str(a))
            lbl20.update()
            time.sleep(2)
            a = a - 1
        t90.clear()
        t91.clear()
        t92.clear()
        t93.clear()
        t94.clear()
        t95.clear()
        
        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'logic', 0)
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(1)


    if (flag == 2):

        while (a != 21):
            lbl20.configure(text="The temperature inside is: " + str(a))
            lbl20.update()
            time.sleep(2)
            a = a - 1
        t200.clear()
        t201.clear()
        t202.clear()
        t203.clear()
        
        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'logic', 0)
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(1)

    if (flag == 3):

        while (a != 18):
            lbl20.configure(text="The temperature inside is: " + str(a))
            lbl20.update()
            time.sleep(2)
            a = a + 1
        t94.clear()
        t95.clear()
        
        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'logic', 0)
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(1)

    if (flag == 4):

        while (a != 18):
            lbl20.configure(text="The temperature inside is: " + str(a))
            lbl20.update()
            time.sleep(2)
            a = a + 1
        t204.clear()
        
        s_2 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'logic', 0)
        print(EV3BT.printMessage(s_2))
        EV3_2.write(s_2)
        time.sleep(1)
        
    if (c == 1):
        s_1 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'number', 0) #lipasma
        EV3_1.write(s_1)
        print(EV3BT.printMessage(s_1))
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 666.0:
                    break
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 500.0:
                    t102.clear()
                    break
                
        
        
        
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 1000.0:
                    t103.clear()
                    break
        
       
        

    if (d == 1):
        s_1 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'number', 1) #lipasma
        EV3_1.write(s_1)
        print(EV3BT.printMessage(s_1))
        
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 666.0:
                    break
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 500.0:
                    t100.clear()
                    break
                
        
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 1000.0:
                    t101.clear()
                    break
        
      

    if (e == 1):
        s_1 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'number', 2) #lipasma
        EV3_1.write(s_1)
        print(EV3BT.printMessage(s_1))
        
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 666.0:
                    break
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 500.0:
                    t98.clear()
                    break
                
       
        
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 1000.0:
                    t99.clear()
                    break
        
        
        

    if (q == 1):
        s_1 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'number', 3) #lipasma
        EV3_1.write(s_1)
        print(EV3BT.printMessage(s_1))
        
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 666.0:
                    break
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 500.0:
                    t96.clear()
                    break
                
        
        while 1:
    
            n_1 = EV3_1.inWaiting()
            
            if n_1 != 0 :
                
                s_1 = EV3_1.read(n_1)
                mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
                print("Message 1:  ", flag_1)
                if flag_1 == 1000.0:
                    t97.clear()
                    break
        
        
        
    s_1 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'interrupt', 0) #lipasma
    print(EV3BT.printMessage(s_1))
    EV3_1.write(s_1)
    time.sleep(2)

while 1:
    
    n_1 = EV3_1.inWaiting()
    n_2 = EV3_2.inWaiting()
    
    if n_1 != 0 and n_2 != 0:
        
        s_1 = EV3_1.read(n_1)
        mail,flag_1,s_1 = EV3BT.decodeMessage(s_1, EV3BT.MessageType.Numeric)
        print("Message 1:  ", flag_1)

        s_2 = EV3_2.read(n_2)
        mail,flag_2,s_2 = EV3BT.decodeMessage(s_2, EV3BT.MessageType.Numeric)
        print("message 2: ",flag_2)
        time.sleep(5)
        if flag_1 == 1.0 and flag_2 == 5.0:
            break
        


first_window()


        
window.mainloop() 

