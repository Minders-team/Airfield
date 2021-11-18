from tkinter import*
import requests
from bs4 import BeautifulSoup
from itertools import islice
import time
from timeit import default_timer as timer
import serial
import EV3BT
import drivers
import dht11
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
channel = 1
adc.start_adc(channel, gain=GAIN)
value = adc.get_last_result()
value_shown = '{:.3f}'.format((value/30600.0)*4.0)
#print('Channel 0:', '{:.3f}'.format((value/30600.0)*4.0))
volt_flag = False


EV3_4 = serial.Serial('/dev/rfcomm0')
time.sleep(0.1)

def convert_html_to_txt(url, txt_name):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    file = open(txt_name, 'w')
    file.write(soup.prettify())
    file.close()


def get_line(first, last, ):
    with open('html.txt') as lines:
        for line in islice(lines, first, last):
            word = line
            return word

def height_calculator(wind):
    if (wind >= 1) and (wind <= 5):
        height = 500
        ground = False
    elif (wind >= 6) and (wind <= 10):
        height = 450
        ground = False
    elif (wind >= 11) and (wind <= 15):
        height = 400
        ground = False
    elif (wind >= 16) and (wind <= 20):
        height = 300
        ground = False
    elif (wind >= 21) and (wind <= 25):
        height = 250
        ground = False
    elif (wind >= 26) and (wind <= 30):
        height = 220
        ground = False
    elif (wind >= 31) and (wind <= 35):
        height = 200
        ground = False
    elif (wind >= 36) and (wind <= 40):
        height = 100
        ground = False
    elif (wind >= 41) and (wind <= 45):
        height = 30
        ground = False
    else:
        height = 0
        ground = True

    return height, ground


def get_number_from_wind_speed(speed):
    counter = 0
    i = 0
    for x in speed:
        if i == 0:
            first_digit = x
        if i == 1:
            try:
                second_digit = x
                int(second_digit)
                test_flag = True
            except:
                test_flag = False

        i = i + 1
        counter = counter + 1

    converted_first_digit = int(first_digit)
    if test_flag is True:
        converted_second_digit = int(second_digit)

    if counter == 6:
        final_speed = converted_first_digit
    elif counter == 7:
        final_speed = converted_first_digit * 10 + converted_second_digit

    return final_speed

def weather_cond(weather_condition):
    if weather_condition == "RAIN":
        flag_weather = True
    if weather_condition == "ΒΡΟΧΗ":
        flag_weather = True
    elif weather_condition == "HEAVY RAIN":
        flag_weather = True
    elif weather_condition == "SNOW":
        flag_weather = True
    elif weather_condition == "SNOWSTORM":
        flag_weather = True
    elif weather_condition == "rain":
        flag_weather = True
    elif weather_condition == "heavy rain":
        flag_weather = True
    elif weather_condition == "snow":
        flag_weather = True
    elif weather_condition == "snowstorm":
        flag_weather = True
    elif weather_condition == "Rain":
        flag_weather = True
    elif weather_condition == "RAIN":
        flag_weather = True
    elif weather_condition == "Heavy rain":
        flag_weather = True
    elif weather_condition == "Snow":
        flag_weather = True
    elif weather_condition == "Snowstorm":
        flag_weather = True
    elif weather_condition == "Heavy Rain":
        flag_weather = True
    else:
        flag_weather = False

    return flag_weather


def search_line(word, txt):
    search = word
    file_read = open(txt, "r")
    flag = 0
    index = 0

    for line in file_read:
        index = index + 1

        if search in line:
            flag = 1
            break

    file_read.close()

    return index


def wind_direction(direction_code):
    
    if direction_code == 'N':
        final_direction = 0
    elif direction_code == "ND":
        final_direction = 45
    elif direction_code == "D":
        final_direction = 90
    elif direction_code == "BD":
        final_direction = 135
    elif direction_code == "B":
        final_direction = 180
    elif direction_code == "BA":
        final_direction = 225
    elif direction_code == "A":
        final_direction = 270
    elif direction_code == "NA":
        final_direction = 325
        
    elif direction_code == 'Ν':
        final_direction = 0
    elif direction_code == "ΝΔ":
        final_direction = 45
    elif direction_code == "Δ":
        final_direction = 90
    elif direction_code == "ΒΔ":
        final_direction = 135
    elif direction_code == "Β":
        final_direction = 180
    elif direction_code == "ΒΑ":
        final_direction = 225
    elif direction_code == "Α":
        final_direction = 270
    elif direction_code == "ΝΑ":
        final_direction = 325
        
    else:
        final_direction = 270
        
        
    return final_direction

            
window = Tk()
window.geometry("242x250")
window.title("Menu")
flag = True

def first_window():
    global volt_flag
    volt_flag = False

    global btn1
    btn1 = Button(window, text = "Automatic", fg = "black", bg = "light green", width = 15, height = 2, command = automatic)
    btn1.grid(column = 0, row = 1, columnspan = 5, pady = 10)

    global btn2
    btn2 = Button(window, text = "Manual", fg = "black", bg = "light green", width = 15, height = 2, command = manual)
    btn2.grid(column = 0, row = 2, columnspan = 5, pady = 10)
    
    global lbl10
    lbl10 = Label(window, justify = 'right', text = "Voltage: ", font = ('family','12'))
    lbl10.grid(column = 0, row = 3)

    global lbl100
    lbl100 = Label(window,justify = 'right', text = "", font = ('family','12'))
    lbl100.grid(column = 1, row = 3)
    
    
    while True:
    
        if volt_flag == True:
            break
        else:
            value = adc.get_last_result()
            value_shown = '{:.1f}'.format((value/30600.0)*4.0)
            if float(value_shown) > 3.9:
                lbl100.configure(text="" + str(value_shown))
                lbl100.update()
                time.sleep(0.1)
            else:
                lbl100.configure(text="" + str(0))
                lbl100.update()
                time.sleep(0.1)
            
            '''
            else:
                zero = 0
                lbl100.configure(text="" + "zero")
                lbl100.update()
                time.sleep(1)
            '''
                
                            
            
    

def automatic():
    window.geometry("325x250")
    window.title("Auto")

    btn1.destroy()
    btn2.destroy()
    
    lbl10.destroy()
    lbl100.destroy()
    
    global value_shown
    global volt_flag
    volt_flag = True
    
    global lbl5
    lbl5 = Label(window,justify = 'right', text = "Automatic", font = ('family', 15, 'bold'))
    lbl5.grid(column = 0, row = 0, columnspan = 2, padx = 5, pady = 5)

    global lbl6
    lbl6 = Label(window,justify = 'right', text = "Weather: ", font = ('family','12'))
    lbl6.grid(column = 0, row = 2)

    global lbl61
    lbl61 = Label(window,justify = 'right', text = "", font = ('family','12'))
    lbl61.grid(column = 1, row = 2)

    global lbl7
    lbl7 = Label(window, justify = 'right', text = "Wind Speed: ", font = ('family','12'))
    lbl7.grid(column = 0, row = 3)

    global lbl71
    lbl71 = Label(window,justify = 'right', text = "", font = ('family','12'))
    lbl71.grid(column = 1, row = 3)

    global lbl8
    lbl8 = Label(window, justify = 'right', text = "Height: ", font = ('family','12'))
    lbl8.grid(column = 0, row = 4)

    global lbl81
    lbl81 = Label(window,justify = 'right', text = "", font = ('family','12'))
    lbl81.grid(column = 1, row = 4)
    
    global lbl9
    lbl9 = Label(window, justify = 'right', text = "Wind Direction: ", font = ('family','12'))
    lbl9.grid(column = 0, row = 5)

    global lbl91
    lbl91 = Label(window,justify = 'right', text = "", font = ('family','12'))
    lbl91.grid(column = 1, row = 5)
    


    global btn8
    btn8 = Button(window, text = "Back to Menu", fg = "black", bg = "light green", width = 15, height = 2, command = back2)
    btn8.grid(column = 0, row = 7, columnspan= 2, pady= 0, padx = 0)
    

    


    if flag is True:

        convert_html_to_txt('https://www.meteo.gr/cf.cfm?city_id=231', 'html.txt')

        wind_line = search_line("km", "html.txt")
        weather_line = search_line("phenomeno", "html.txt")
        direction_line = search_line("graphics/forecasticons/3/WindDirection", "html.txt")

        weather = get_line(weather_line, weather_line + 1)
        wind_speed = get_line(wind_line, wind_line + 1)
        direction = get_line(direction_line - 1, direction_line)

        strip_weather = weather.strip()
        strip_wind_speed = wind_speed.strip()
        strip_direction = direction.strip()

        final_wind_speed = get_number_from_wind_speed(strip_wind_speed)

        weather_flag = weather_cond(strip_weather)
        final_height = height_calculator(final_wind_speed)
        
        if len(strip_direction) == 110:
            direction = strip_direction[86]
        elif len(strip_direction) == 111:
            direction = strip_direction[86] + strip_direction[87]
            
        
        if strip_weather == "ΚΑΘΑΡΟΣ":  
            strip_weather = "CLEAR"
            
        elif strip_weather == "ΠΕΡΙΟΡΙΣΜΕΝΗ ΟΡΑΤΟΤΗΤΑ":
            strip_weather = "POOR VISIBILITY (FOG)"
            
        elif strip_weather == "ΛΙΓΑ ΣΥΝΝΕΦΑ":
            strip_weather = "SLIGHTLY CLOUDY"
            
        elif strip_weather == "ΑΡΑΙΗ ΣΥΝΝΕΦΙΑ":
            strip_weather = "SLIGHTLY CLOUDY"
            
        elif strip_weather == "ΑΡΚΕΤΑ ΣΥΝΝΕΦΑ":
            strip_weather = "VERY CLOUDY"
            
        elif strip_weather == "ΒΡΟΧΗ":
            strip_weather = "RAIN"
            
        elif strip_weather == "ΑΣΘΕΝΗΣ ΒΡΟΧΗ":
            strip_weather = "WEAK RAIN"
            
        elif strip_weather == "ΣΥΝΝΕΦΙΑΣΜΕΝΟΣ":
            strip_weather = "CLOUDY"            


        wind_degrees = wind_direction(direction)
        
        if weather_flag is False:
            

            lbl61.configure(text="" + strip_weather)
            lbl61.update()
            time.sleep(0.1)

            lbl71.configure(text="" + str(final_wind_speed) + " km/h")
            lbl71.update()
            time.sleep(0.1)

            lbl81.configure(text="" + str((final_height[0])) + " m")
            lbl81.update()
            time.sleep(0.1)
            
            lbl91.configure(text="" + str(wind_degrees) + " °")
            lbl91.update()
            time.sleep(0.1)
            
            s_4 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'Numeric', final_height[0])
            print(EV3BT.printMessage(s_4))
            EV3_4.write(s_4)
            time.sleep(1)
            
        elif weather_flag is True:
            lbl61.configure(text="" + strip_weather)
            lbl61.update()
            time.sleep(0.1)

            lbl71.configure(text="" + str(final_wind_speed) + " km/h")
            lbl71.update()
            time.sleep(0.1)
            
            zero = 0

            lbl81.configure(text="" + str(zero) + " m")
            lbl81.update()
            time.sleep(0.1)
            
            lbl91.configure(text="" + str(wind_degrees) + " °")
            lbl91.update()
            time.sleep(0.1)
            
            s_4 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'Numeric', 0)
            print(EV3BT.printMessage(s_4))
            EV3_4.write(s_4)
            time.sleep(1)
        



def manual():
    window.geometry("325x250")
    window.title("Manual")
    global volt_flag
    volt_flag = True

    lbl10.destroy()
    lbl100.destroy()

    btn1.destroy()
    btn2.destroy()

    global lbl2
    lbl2 = Label(window,justify = 'right', text = "Manual", font = ('Times', 15, 'bold'))
    lbl2.grid(column = 0, row = 0, columnspan = 2, padx = 5, pady = 5)

    global lbl3
    lbl3 = Label(window,justify = 'right', text = "Weather: ", font = ('family','12'))
    lbl3.grid(column = 0, row = 2, pady = 5)

    global lbl4
    lbl4 = Label(window, justify = 'right', text = "Wind Speed: ", font = ('family','12'))
    lbl4.grid(column = 0, row = 3)

    global txt1
    txt1 = Entry(window, width = 7)
    txt1.grid(column = 1, row = 2)

    global txt2
    txt2 = Entry(window, width = 7)
    txt2.grid(column = 1, row = 3)
    

    global btn5
    btn5 = Button(window, text = "Clear", fg = "black", bg="light blue", width = 13, height = 2, command = clear)
    btn5.grid(column = 0, row = 5, columnspan = 1, pady = 8, padx = 2)
    global btn6
    btn6 = Button(window, text = "Back to Menu", fg = "black", bg = "light blue", width = 14, height = 2, command = back)
    btn6.grid(column = 1, row = 5, columnspan = 1, pady = 0, padx = 2)
    global btn7
    btn7 = Button(window, text = "Submit", fg = "black", bg = "light green", width = 29, height = 2, command = submit)
    btn7.grid(column = 0, row = 6, columnspan= 2, pady= 0, padx = 0)


def clear():
    txt1.delete(0, "end")
    txt2.delete(0, "end")


def back():
    window.geometry("242x250")
    window.title("Menu")
    

    lbl2.destroy()
    lbl3.destroy()
    lbl4.destroy()
    txt1.destroy()
    txt2.destroy()
    btn5.destroy()
    btn6.destroy()
    btn7.destroy()

    first_window()
    global volt_flag
    '''
    while True:
        if volt_flag == True:
            break
        else:
            value = adc.get_last_result()
            value_shown = '{:.3f}'.format((value/30600.0)*4.0)
            lbl100.configure(text="" + str(value_shown))
            lbl100.update()
            time.sleep(0.1)
            '''

def back2():
    window.geometry("242x250")
    window.title("Menu")

    lbl5.destroy()
    lbl6.destroy()
    lbl61.destroy()
    lbl7.destroy()
    lbl71.destroy()
    lbl8.destroy()
    lbl81.destroy()
    lbl9.destroy()
    lbl91.destroy()

    btn8.destroy()

    first_window()
    global volt_flag
    '''
    while True:
        if volt_flag == True:
            break
        else:
            value = adc.get_last_result()
            value_shown = '{:.3f}'.format((value/30600.0)*4.0)
            lbl100.configure(text="" + str(value_shown))
            lbl100.update()
            time.sleep(0.1)
            '''

def submit():
    window.geometry("242x250")
    window.title("Manual")

    lbl3.destroy()
    lbl4.destroy()
    btn5.destroy()
    btn6.destroy()
    btn7.destroy()

    global lbl20

    weather = txt1.get()

    global manual_weather
    manual_weather = str(weather)
    lbl20 = Label(window, justify='right', text="The weather is: " + manual_weather , font = ('family','12'))
    lbl20.grid(column=0, row=1)

    #send message to ev3

    global lbl21
    wind_speed = txt2.get()
    global manual_wind_speed
    manual_wind_speed = int(wind_speed)
    lbl21 = Label(window, justify='right', text="The wind speed is: " + str(manual_wind_speed) + " km / h",  font = ('family','12'))
    lbl21.grid(column=0, row=2)

    #send message to ev3

    global lbl22
    global manual_height
    manual_height = height_calculator(manual_wind_speed)
    flag_weather = weather_cond(manual_weather)
    print(flag_weather)
    
    if flag_weather is True:
        lbl22 = Label(window, justify = 'right', text = "Height: 0 m" )
        lbl22.grid(column = 0, row = 3)
        manual_height = 0
        
        
        s_4 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'Numeric', 0)
        print(EV3BT.printMessage(s_4))
        EV3_4.write(s_4)
        time.sleep(1)


    elif flag_weather is False:
        lbl22 = Label(window, justify = 'right', text = "Height: " +  str(manual_height[0]) + " m", font = ('family','12'))
        lbl22.grid(column = 0, row = 3)
        
        time.sleep(0.1)
        
        
        s_4 = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'Numeric', manual_height[0])
        print(EV3BT.printMessage(s_4))
        EV3_4.write(s_4)
        time.sleep(1)
    

    #send message to ev3

    txt1.destroy()
    txt2.destroy()

    global btn10
    btn10 = Button(window, text = "Back to Menu", fg = "black", bg = "light blue", width = 20, height = 2, command = back3)
    btn10.grid(column = 0, row = 5, pady = 0, padx = 0)



def back3():
    window.geometry("242x250")
    window.title("Menu")
    

    lbl2.destroy()
    lbl20.destroy()
    lbl21.destroy()
    lbl22.destroy()
    btn10.destroy()

    first_window()
    global volt_flag
    '''
    while True:
        if volt_flag == True:
            break
        else:
            value = adc.get_last_result()
            value_shown = '{:.3f}'.format((value/30600.0)*4.0)
            lbl100.configure(text="" + str(value_shown))
            lbl100.update()
            time.sleep(0.1)
            '''





first_window()


window.mainloop()








