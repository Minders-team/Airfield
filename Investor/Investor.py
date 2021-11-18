from tkinter import *
from tkinter import messagebox

import math
import time
import datetime


global air_turbines
global greenhouses
global city







def budget_algo(budget, city ):

    if city == 'Athens':
        greece = [1, 0, 0, 0, 0, 80]
    elif city == 'Thesalonniki':
        greece = [0, 1, 0, 0, 0, 60]
    elif city == 'Volos':
        greece = [0, 0, 1, 0, 0, 65]
    elif city == 'Korinthos':
        greece = [0, 0, 0, 1, 0, 55]
    elif city == 'Kriti':
        greece = [0, 0, 0, 0, 1, 60]

    at_ind_cost = 325
    gh_acre_ren_year = 20
    at_ind_ren_year = 20
    gh_acre_profits_year = 40
    at_ind_profits_year = 75

    times = budget / at_ind_cost
    decimal, whole = math.modf(times)
    times = times - decimal
    times_int = int(times)

    gh_cost = 65

    #air_turbines    greenhouse    profits
    comparison_profits = [0, 0, 0]
    profits_final = [0, 0, 0]

    #air_turbines    greenhouse    depreciation
    comparison_depreciation = [0, 0, 0]
    depreciation_final = [0, 0, 9999]

    #air_turbines    greenhouse    profits    depreciation
    comparison_profits_depreciation = [0, 0, 0, 0]
    i = 1
    for at_amm in range(times_int):
        at_amm = at_amm + 1

        gh_amm = (budget - at_ind_cost*i) / gh_cost

        decimal, whole = math.modf(gh_amm)
        gh_amm = gh_amm - decimal

        # Construction Cost
        if gh_amm > 0:
            total_at_con_cost = at_ind_cost * at_amm
            total_gh_con_cost = greece[5] * gh_amm
            total_con_cost = total_at_con_cost + total_gh_con_cost

        if gh_amm < 0:
            total_at_con_cost = at_ind_cost * at_amm + greece[5] // 3 * at_amm
            total_gh_con_cost = greece[5] * gh_amm
            total_con_cost = total_at_con_cost + total_gh_con_cost

        # Renovation Cost
        total_at_ren_cost = at_ind_ren_year * at_amm
        total_gh_ren_cost = gh_acre_ren_year * gh_amm
        total_ren_cost = total_at_ren_cost + total_gh_ren_cost
        print(total_ren_cost)

        # Yearly Profit
        total_at_year_profits = at_ind_profits_year * at_amm
        total_gh_year_profits = gh_acre_profits_year * gh_amm
        yearly_profit = total_at_year_profits + total_gh_year_profits - total_ren_cost

        # Depreciation
        d_years = (total_at_con_cost + total_gh_con_cost) / yearly_profit

        comparison_profits = [at_amm, round(gh_amm, 0), round(yearly_profit, 0)]

        comparison_depreciation = [at_amm, round(gh_amm, 0), round(d_years, 2)]

        if comparison_profits[2] > profits_final[2]:
            x = round(comparison_profits[0])
            y = round(comparison_profits[1])
            o = round(comparison_profits[2])
            profits_final = [x, y, o]

        if comparison_depreciation[2] < depreciation_final[2]:
            x = round(comparison_depreciation[0], 1)
            y = round(comparison_depreciation[1], 1)
            o = round(comparison_depreciation[2], 1)
            depreciation_final = [x, y, o]

        i = i + 1

    nt_s = budget//at_ind_cost
    total_at_con_cost = at_ind_cost * at_amm + greece[5]//3 * at_amm

    total_at_ren_cost = at_ind_ren_year * at_amm

    total_at_year_profits = at_ind_profits_year * at_amm - total_at_ren_cost

    d_years = total_at_con_cost / yearly_profit

    not_suggested_profits = [nt_s, 0, total_at_year_profits]
    not_suggested_depriciation = [nt_s, 0, round(d_years, 1)]

    turbine = 0
    in_budget = budget

    if profits_final[0] == 1:
        greenhouse = 0

        while True:
            budget = budget - at_ind_cost
            turbine = turbine + 1
            for i in range (1,12,1):
                if budget > 0:
                    budget = budget - greece[5]
                    greenhouse = greenhouse + 1
            if budget < 0:
                greenhouse = greenhouse - 1
                break

        profits_final[0] = turbine
        profits_final[1] = greenhouse
        depreciation_final[0] = turbine
        depreciation_final[1] = greenhouse

        # Construction Cost
        if greenhouse > 0:
            total_at_con_cost = at_ind_cost * turbine
            total_gh_con_cost = greece[5] * greenhouse
            total_con_cost = total_at_con_cost + total_gh_con_cost
        if greenhouse == 0:
            total_at_con_cost = at_ind_cost * turbine + greece[5] // 3 * turbine
            total_gh_con_cost = greece[5] * greenhouse
            total_con_cost = total_at_con_cost + total_gh_con_cost

        # Renovation Cost
        total_at_ren_cost = at_ind_ren_year * turbine
        total_gh_ren_cost = gh_acre_ren_year * greenhouse
        total_ren_cost = total_at_ren_cost + total_gh_ren_cost

        # Yearly Profit
        total_at_year_profits = at_ind_profits_year * turbine
        total_gh_year_profits = gh_acre_profits_year * greenhouse
        yearly_profit = total_at_year_profits + total_gh_year_profits - total_at_ren_cost - total_gh_ren_cost

        # Depreciation
        d_years = (total_at_con_cost + total_gh_con_cost) / yearly_profit

        remaining = in_budget - total_con_cost

        profits_final = [turbine,greenhouse,yearly_profit]
        depreciation_final = [turbine,greenhouse,round(d_years,1)]


        # --------------------- #

        substruct = remaining/gh_cost
        decimal, whole = math.modf(substruct)
        substruct = round(substruct - decimal)*-1


        # Construction Cost
        if greenhouse > 0:
            total_at_con_cost = at_ind_cost * (turbine)
            total_gh_con_cost = greece[5] * (greenhouse-substruct)
            total_con_cost = total_at_con_cost + total_gh_con_cost
        if greenhouse == 0:
            total_at_con_cost = at_ind_cost * (turbine) + greece[5] // 3 * (turbine)
            total_gh_con_cost = greece[5] * (greenhouse-substruct)
            total_con_cost = total_at_con_cost + total_gh_con_cost

        if turbine>2:
            # Renovation Cost
            total_at_ren_cost = at_ind_ren_year * (turbine)
            total_gh_ren_cost = gh_acre_ren_year * (greenhouse-substruct)
            total_ren_cost = total_at_ren_cost + total_gh_ren_cost

            # Yearly Profit
            total_at_year_profits = at_ind_profits_year * (turbine)
            total_gh_year_profits = gh_acre_profits_year * (greenhouse-substruct)
            yearly_profit = total_at_year_profits + total_gh_year_profits - total_at_ren_cost - total_gh_ren_cost

            # Depreciation
            d_years = (total_at_con_cost + total_gh_con_cost) / yearly_profit

            option_2_price = yearly_profit
            option_2_depreciation = round(d_years,1)

            flag = True

            return profits_final, depreciation_final, not_suggested_profits, not_suggested_depriciation, remaining, flag, option_2_price, option_2_depreciation, substruct
        else:
            flag = False
            return profits_final, depreciation_final, not_suggested_profits, not_suggested_depriciation, remaining, flag,1,1,substruct



def month_cal(month):
    
    if month == 1:
        month_str = 'January'
    elif month == 2:
        month_str = 'February'
    elif month == 3:
        month_str = 'March'
    elif month == 4:
        month_str = 'April'
    elif month == 5:
        month_str = 'May'
    elif month == 6:
        month_str = 'June'
    elif month == 7:
        month_str = 'July'
    elif month == 8:
        month_str = 'August'
    elif month == 9:
        month_str = 'September'
    elif month == 10:
        month_str = 'October'
    elif month == 11:
        month_str = 'November'
    elif month == 12:
        month_str = 'December'
    elif month == 13:
        month_str = 'December'
        

    return month_str


def setup_algo(city, gh_amm, at_amm):
    greece = [0, 0, 0, 0, 0, 0]

    at_ind_cost = 325
    gh_acre_ren_year = 20
    at_ind_ren_year = 20
    gh_acre_profits_year = 40
    at_ind_profits_year = 75

    if city == 'Athens':
        greece = [1, 0, 0, 0, 0, 80]
    elif city == 'Thesalonniki':
        greece = [0, 1, 0, 0, 0, 60]
    elif city == 'Volos':
        greece = [0, 0, 1, 0, 0, 65]
    elif city == 'Korinthos':
        greece = [0, 0, 0, 1, 0, 55]
    elif city == 'Kriti':
        greece = [0, 0, 0, 0, 1, 60]

    # Construction Cost
    if gh_amm > 0:
        total_at_con_cost = at_ind_cost * at_amm
        total_gh_con_cost = greece[5] * gh_amm
        total_con_cost = total_at_con_cost + total_gh_con_cost
    if gh_amm == 0:
        total_at_con_cost = at_ind_cost * at_amm + greece[5]//3 * at_amm
        total_gh_con_cost = greece[5] * gh_amm
        total_con_cost = total_at_con_cost + total_gh_con_cost


    # Renovation Cost
    total_at_ren_cost = at_ind_ren_year * at_amm
    total_gh_ren_cost = gh_acre_ren_year * gh_amm
    total_ren_cost = total_at_ren_cost + total_gh_ren_cost

    # Yearly Profit
    total_at_year_profits = at_ind_profits_year * at_amm
    total_gh_year_profits = gh_acre_profits_year * gh_amm
    yearly_profit = total_at_year_profits + total_gh_year_profits - total_at_ren_cost - total_gh_ren_cost

    # Depreciation
    d_years = (total_at_con_cost + total_gh_con_cost) // yearly_profit
    depreciation_months = ((total_at_con_cost + total_gh_con_cost) / yearly_profit - d_years) * 1.2
    rounded_depreciation_months = round(depreciation_months, 1)
    decimal, whole = math.modf(rounded_depreciation_months)
    d_months = str(int(rounded_depreciation_months + 1 - decimal))

    year = datetime.date.today().year + d_years
    month_num = datetime.date.today().month + int(d_months)

    d_date = month_cal(month_num) + ' of ' + str(year)

    acre_price = greece[5]


    return yearly_profit, d_years, d_months, d_date, total_con_cost, total_ren_cost, acre_price


greece = [0, 0, 0, 0, 0, 0]

window = Tk()
window.geometry("350x400")
window.title("Investor")


logo1 = PhotoImage(file="Greece Map.png")
logo1= logo1.subsample(3)



    

def first_window():

    global btn1
    btn1 = Button(window, text="Budget", fg="black", bg="light blue", width=22, height=2, command = budget)
    btn1.grid(column=1, row=9, columnspan=1, pady=50, padx=50)

    global btn2
    btn2 = Button(window, text="Set up", fg="black", bg="light blue", width=22, height=2, command = set_up)
    btn2.grid(column=1, row=10, columnspan=1, pady=0, padx=1)



def budget():

    window.geometry("350x400")
    window.title("Budget")

    btn1.destroy()
    btn2.destroy()

    global lbl1
    lbl1 = Label(window, justify='right', text="Budget", font=('family', 13, 'bold'))
    lbl1.grid(column=1, row=1)

    global lbl2
    lbl2 = Label(window, justify='right', text="Money to invest (K $): ", font=('family', 11))
    lbl2.grid(column=1, row=2, pady=10, padx=0)

    global txt1
    txt1 = Entry(window, width=7)
    txt1.grid(column=2, row=2)

    global btn3
    btn3 = Button(window, text="Submit", fg="black", bg="light blue", width=15, height=2, command = submit_athens)
    btn3.grid(column=1, row=3, columnspan=2, pady=5, padx=8)

    global btn4
    btn4 = Button(window, text="Back to Menu", fg="black", bg="light green", width=15, height=2, command = back_tomenu_1)
    btn4.grid(column=1, row=4, columnspan=2, pady=5, padx=8)

def back_tomenu_1():

    window.geometry("350x400")
    window.title("Investor")

    lbl1.destroy()
    lbl2.destroy()

    txt1.destroy()

    btn3.destroy()
    btn4.destroy()

    first_window()






def submit_athens():

    window.title("Athens")

    lbl2.destroy()

    a = txt1.get()
    global input_budget
    input_budget = int(a)

    if input_budget < 390:

        window.geometry("350x400")
        window.title("Investor")

        lbl1.destroy()
        lbl2.destroy()

        txt1.destroy()

        btn3.destroy()
        btn4.destroy()

        first_window()

        messagebox.showerror("Invalid values", "The budget should be more than 390K $")



    else:
        txt1.destroy()

        btn3.destroy()
        btn4.destroy()

        suggestions = budget_algo(input_budget, 'Athens')

        lbl1.configure(text = "Athens: 80K $ / acre ")

        global flag


        if suggestions[4] < 0:

            window.geometry("660x480")



            global lbl3
            lbl3 = Label(window, justify='right', text="Option 1: Fastest Payback and Greater Profits (Suggested)", font=('family', 11))
            lbl3.grid(column=1, row=2)

            global lbl4
            lbl4 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 11))
            lbl4.grid(column=1, row=3)

            global lbl5
            lbl5 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]), font=('family', 11))
            lbl5.grid(column=1, row=4)

            global lbl6
            lbl6 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[0][2]) + "K $", font=('family', 11))
            lbl6.grid(column=1, row=5)

            global lbl7
            lbl7 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 11))
            lbl7.grid(column=1, row=6)

            global lbl200
            lbl200 = Label(window, justify='right', text="Money to Add: " + str(suggestions[4]*-1) + "K $", font=('family', 11))
            lbl200.grid(column=1, row=7)

            global lbl201
            lbl201 = Label(window, justify='right', text="Option 2: Fastest Payback and Greater Profits", font=('family', 11))
            lbl201.grid(column=1, row=8)

            global lbl202
            lbl202 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 11))
            lbl202.grid(column=1, row=9)

            global lbl203
            lbl203 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]-suggestions[8]), font=('family', 11))
            lbl203.grid(column=1, row=10)

            global lbl204
            lbl204 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[6]) + "K $", font=('family', 11))
            lbl204.grid(column=1, row=11)

            global lbl205
            lbl205 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 11))
            lbl205.grid(column=1, row=12)



            global lbl8
            lbl8 = Label(window, justify='right', text="\nOption 3: 100% Investment On Airborne Air-Turbine(s)", font=('family', 11))
            lbl8.grid(column=1, row=14)

            global lbl9
            lbl9 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[2][0]), font=('family', 11))
            lbl9.grid(column=1, row=15)

            global lbl10
            lbl10 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[2][2]) + "K $", font=('family', 11))
            lbl10.grid(column=1, row=16)

            global lbl11
            lbl11 = Label(window, justify='right', text="Payback in: " + str(suggestions[3][2]) + " Years", font=('family', 11))
            lbl11.grid(column=1, row=17)

            global btn5
            btn5 = Button(window, text="Back to Menu", fg="black", bg="light green", width=10, height=2, command = back_tomenu_2)
            btn5.grid(column=0, row=18)

            global btn6
            btn6 = Button(window, text="Next City", fg="black", bg="light green", width=10, height=2, command =  next_city_thessaloniki)
            btn6.grid(column=3, row=18, columnspan=1, pady=5)

            flag = 1

        if suggestions[4] > 0:

            window.geometry("620x350")

            global lbl207
            lbl207 = Label(window, justify='right', text="Option 1: Fastest PaybackGreater Profits (Suggested)", font=('family', 11))
            lbl207.grid(column=1, row=2)

            global lbl208
            lbl208 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 11))
            lbl208.grid(column=1, row=3)

            global lbl209
            lbl209 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]), font=('family', 11))
            lbl209.grid(column=1, row=4)

            global lbl210
            lbl210 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[0][2]) + "K $", font=('family', 11))
            lbl210.grid(column=1, row=5)

            global lbl211
            lbl211 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 11))
            lbl211.grid(column=1, row=6)

            global lbl500
            lbl500 = Label(window, justify='right', text="Remaining Money: " + str(suggestions[4]) + "K $", font=('family', 11))
            lbl500.grid(column=1, row=12)

            global lbl212
            lbl212 = Label(window, justify='right', text="\nOption 2: 100% Investment On Airborne Air-Turbine(s)", font=('family', 11))
            lbl212.grid(column=1, row=14)

            global lbl213
            lbl213 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[2][0]), font=('family', 11))
            lbl213.grid(column=1, row=15)

            global lbl214
            lbl214 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[2][2]) + "K $", font=('family', 11))
            lbl214.grid(column=1, row=16)

            global lbl215
            lbl215 = Label(window, justify='right', text="Payback in: " + str(suggestions[3][2]) + " Years", font=('family', 11))
            lbl215.grid(column=1, row=17)

            global btn200
            btn200 = Button(window, text="Back to Menu", fg="black", bg="light green", width=10, height=2, command = back_tomenu_2)
            btn200.grid(column=0, row=18)

            global btn201
            btn201 = Button(window, text="Next City", fg="black", bg="light green", width=10, height=2, command =  next_city_thessaloniki)
            btn201.grid(column=3, row=18, columnspan=1, pady=5)

            flag = 2

def back_tomenu_2():

    window.geometry("350x400")
    window.title("Investor")

    lbl1.destroy()

    if flag == 1:
        lbl3.destroy()
        lbl4.destroy()
        lbl5.destroy()
        lbl6.destroy()
        lbl7.destroy()
        lbl8.destroy()
        lbl9.destroy()
        lbl10.destroy()
        lbl11.destroy()
        lbl200.destroy()
        lbl201.destroy()
        lbl202.destroy()
        lbl203.destroy()
        lbl204.destroy()
        lbl205.destroy()

        btn5.destroy()
        btn6.destroy()



    if flag == 2:
        lbl207.destroy()
        lbl208.destroy()
        lbl209.destroy()
        lbl210.destroy()
        lbl211.destroy()
        lbl500.destroy()
        lbl212.destroy()
        lbl213.destroy()
        lbl214.destroy()
        lbl215.destroy()

        btn200.destroy()
        btn201.destroy()

    first_window()



def next_city_thessaloniki():

    window.title("Thessaloniki")

    global flag




    if flag == 1:
        lbl3.destroy()
        lbl4.destroy()
        lbl5.destroy()
        lbl6.destroy()
        lbl7.destroy()
        lbl8.destroy()
        lbl9.destroy()
        lbl10.destroy()
        lbl11.destroy()
        lbl200.destroy()
        lbl201.destroy()
        lbl202.destroy()
        lbl203.destroy()
        lbl204.destroy()
        lbl205.destroy()

        btn5.destroy()
        btn6.destroy()

    if flag == 2:
        lbl207.destroy()
        lbl208.destroy()
        lbl209.destroy()
        lbl210.destroy()
        lbl211.destroy()
        lbl500.destroy()
        lbl212.destroy()
        lbl213.destroy()
        lbl214.destroy()
        lbl215.destroy()

        btn200.destroy()
        btn201.destroy()


    suggestions = budget_algo(input_budget, 'Thesalonniki')

    lbl1.configure(text = "Thessaloniki: 60K $ / acre ")



    if suggestions[4] < 0:

        window.geometry("660x480")

        global lbl12
        lbl12 = Label(window, justify='right', text="Option 1: Fastest Payback and Greater Profits (Suggested)", font=('family', 11))
        lbl12.grid(column=1, row=2)

        global lbl13
        lbl13 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 11))
        lbl13.grid(column=1, row=3)

        global lbl14
        lbl14 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]), font=('family', 11))
        lbl14.grid(column=1, row=4)

        global lbl15
        lbl15 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[0][2]) + "K $", font=('family', 11))
        lbl15.grid(column=1, row=5)

        global lbl16
        lbl16 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 11))
        lbl16.grid(column=1, row=6)

        global lbl216
        lbl216 = Label(window, justify='right', text="Money to Add: " + str(suggestions[4]*-1) + "K $", font=('family', 11))
        lbl216.grid(column=1, row=7)

        global lbl217
        lbl217 = Label(window, justify='right', text="Option 2: Fastest Payback and Greater Profits", font=('family', 11))
        lbl217.grid(column=1, row=8)

        global lbl218
        lbl218 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 11))
        lbl218.grid(column=1, row=9)

        global lbl219
        lbl219 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]-suggestions[8]), font=('family', 11))
        lbl219.grid(column=1, row=10)

        global lbl220
        lbl220 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[6]) + "K $", font=('family', 11))
        lbl220.grid(column=1, row=11)

        global lbl221
        lbl221 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 11))
        lbl221.grid(column=1, row=12)



        global lbl17
        lbl17 = Label(window, justify='right', text="\nOption 3: 100% Investment On Airborne Air-Turbine(s)", font=('family', 11))
        lbl17.grid(column=1, row=14)

        global lbl18
        lbl18 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[2][0]), font=('family', 10))
        lbl18.grid(column=1, row=15)

        global lbl19
        lbl19 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[2][2]) + "K $", font=('family', 10))
        lbl19.grid(column=1, row=16)

        global lbl20
        lbl20 = Label(window, justify='right', text="Payback in: " + str(suggestions[3][2]) + " Years", font=('family', 10))
        lbl20.grid(column=1, row=17)

        global btn7
        btn7 = Button(window, text="Previous City", fg="black", bg="light green", width=10, height=2, command = previous_to_athens)
        btn7.grid(column=0, row=18)

        global btn8
        btn8 = Button(window, text="Next City", fg="black", bg="light green", width=10, height=2, command = next_city_volos)
        btn8.grid(column=3, row=18, columnspan=1, pady=5)

        flag = 3

    if suggestions[4] > 0:


        window.geometry("650x350")

        global lbl222
        lbl222 = Label(window, justify='right', text="Option 1: Fastest Payback and Greater Profits (Suggested)", font=('family', 11))
        lbl222.grid(column=1, row=2)

        global lbl223
        lbl223 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 10))
        lbl223.grid(column=1, row=3)

        global lbl224
        lbl224 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]), font=('family', 10))
        lbl224.grid(column=1, row=4)

        global lbl225
        lbl225 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[0][2]) + "K $", font=('family', 10))
        lbl225.grid(column=1, row=5)

        global lbl226
        lbl226 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 10))
        lbl226.grid(column=1, row=6)

        global lbl501
        lbl501 = Label(window, justify='right', text="Remaining Money: " + str(suggestions[4]) + "K $", font=('family', 10))
        lbl501.grid(column=1, row=12)


        global lbl227
        lbl227 = Label(window, justify='right', text="\nOption 2: 100% Investment On Airborne Air-Turbine(s)", font=('family', 11))
        lbl227.grid(column=1, row=13)

        global lbl228
        lbl228 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[2][0]), font=('family', 10))
        lbl228.grid(column=1, row=14)

        global lbl229
        lbl229 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[2][2]) + "K $", font=('family', 10))
        lbl229.grid(column=1, row=15)

        global lbl230
        lbl230 = Label(window, justify='right', text="Payback in: " + str(suggestions[3][2]) + " Years", font=('family', 10))
        lbl230.grid(column=1, row=16)

        global btn202
        btn202 = Button(window, text="Previous City", fg="black", bg="light green", width=10, height=2, command = previous_to_athens)
        btn202.grid(column=0, row=17)

        global btn203
        btn203 = Button(window, text="Next City", fg="black", bg="light green", width=10, height=2, command = next_city_volos)
        btn203.grid(column=3, row=17, columnspan=1, pady=5)

        flag = 4

def previous_to_athens():

    window.title("Athens")
    global flag

    if flag == 3:
        lbl12.destroy()
        lbl13.destroy()
        lbl14.destroy()
        lbl15.destroy()
        lbl16.destroy()
        lbl17.destroy()
        lbl18.destroy()
        lbl19.destroy()
        lbl20.destroy()
        lbl216.destroy()
        lbl217.destroy()
        lbl218.destroy()
        lbl219.destroy()
        lbl220.destroy()
        lbl221.destroy()

        btn7.destroy()
        btn8.destroy()

        suggestions = budget_algo(input_budget, 'Athens')

        lbl1.configure(text = "Athens: 80K $ / acre ")

        if suggestions[4] < 0:

            window.geometry("660x480")



            global lbl3
            lbl3 = Label(window, justify='right', text="Option 1: Fastest Payback and Greater Profits (Suggested)", font=('family', 11))
            lbl3.grid(column=1, row=2)

            global lbl4
            lbl4 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 10))
            lbl4.grid(column=1, row=3)

            global lbl5
            lbl5 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]), font=('family', 10))
            lbl5.grid(column=1, row=4)

            global lbl6
            lbl6 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[0][2]) + "K $", font=('family', 10))
            lbl6.grid(column=1, row=5)

            global lbl7
            lbl7 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 10))
            lbl7.grid(column=1, row=6)

            global lbl200
            lbl200 = Label(window, justify='right', text="Money to Add: " + str(suggestions[4]*-1) + "K $", font=('family', 10))
            lbl200.grid(column=1, row=7)

            global lbl201
            lbl201 = Label(window, justify='right', text="Option 2: Fastest Payback and Greater Profits", font=('family', 11))
            lbl201.grid(column=1, row=8)

            global lbl202
            lbl202 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 10))
            lbl202.grid(column=1, row=9)

            global lbl203
            lbl203 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]-suggestions[8]), font=('family', 10))
            lbl203.grid(column=1, row=10)

            global lbl204
            lbl204 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[6]) + "K $", font=('family', 10))
            lbl204.grid(column=1, row=11)

            global lbl205
            lbl205 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 10))
            lbl205.grid(column=1, row=12)


            global lbl8
            lbl8 = Label(window, justify='right', text="\nOption 3: 100% Investment On Airborne Air-Turbine(s)", font=('family', 11))
            lbl8.grid(column=1, row=14)

            global lbl9
            lbl9 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[2][0]), font=('family', 10))
            lbl9.grid(column=1, row=15)

            global lbl10
            lbl10 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[2][2]) + "K $", font=('family', 10))
            lbl10.grid(column=1, row=16)

            global lbl11
            lbl11 = Label(window, justify='right', text="Payback in: " + str(suggestions[3][2]) + " Years", font=('family', 10))
            lbl11.grid(column=1, row=17)

            global btn5
            btn5 = Button(window, text="Back to Menu", fg="black", bg="light green", width=10, height=2, command = back_tomenu_2)
            btn5.grid(column=0, row=18)

            global btn6
            btn6 = Button(window, text="Next City", fg="black", bg="light green", width=10, height=2, command =  next_city_thessaloniki)
            btn6.grid(column=3, row=18, columnspan=1, pady=5)

            flag = 1


        if suggestions[4] > 0:

            window.geometry("650x350")

            global lbl207
            lbl207 = Label(window, justify='right', text="Option 1: Fastest Payback and Greater Profits (Suggested)", font=('family', 11))
            lbl207.grid(column=1, row=2)

            global lbl208
            lbl208 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 10))
            lbl208.grid(column=1, row=3)

            global lbl209
            lbl209 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]), font=('family', 10))
            lbl209.grid(column=1, row=4)

            global lbl210
            lbl210 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[0][2]) + "K $", font=('family', 10))
            lbl210.grid(column=1, row=5)

            global lbl211
            lbl211 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 10))
            lbl211.grid(column=1, row=6)

            global lbl500
            lbl500 = Label(window, justify='right', text="Remaining Money: " + str(suggestions[4]) + "K $", font=('family', 10))
            lbl500.grid(column=1, row=12)

            global lbl212
            lbl212 = Label(window, justify='right', text="\nOption 2: 100% Investment On Airborne Air-Turbine(s)", font=('family', 11))
            lbl212.grid(column=1, row=14)

            global lbl213
            lbl213 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[2][0]), font=('family', 10))
            lbl213.grid(column=1, row=15)

            global lbl214
            lbl214 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[2][2]) + "K $", font=('family', 10))
            lbl214.grid(column=1, row=16)

            global lbl215
            lbl215 = Label(window, justify='right', text="Payback in: " + str(suggestions[3][2]) + " Years", font=('family', 10))
            lbl215.grid(column=1, row=17)

            global btn200
            btn200 = Button(window, text="Back to Menu", fg="black", bg="light green", width=10, height=2, command = back_tomenu_2)
            btn200.grid(column=0, row=18)

            global btn201
            btn201 = Button(window, text="Next City", fg="black", bg="light green", width=10, height=2, command =  next_city_thessaloniki)
            btn201.grid(column=3, row=18, columnspan=1, pady=5)

            flag = 2

    if flag == 4:
        lbl222.destroy()
        lbl223.destroy()
        lbl224.destroy()
        lbl225.destroy()
        lbl226.destroy()
        lbl501.destroy()
        lbl227.destroy()
        lbl228.destroy()
        lbl229.destroy()
        lbl230.destroy()

        btn202.destroy()
        btn203.destroy()

        suggestions = budget_algo(input_budget, 'Athens')

        lbl1.configure(text = "Athens: 80K $ / acre ")

        if suggestions[4] < 0:

            window.geometry("660x480")


            lbl3 = Label(window, justify='right', text="Option 1: Fastest Payback and Greater Profits (Suggested)", font=('family', 11))
            lbl3.grid(column=1, row=2)

            lbl4 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 10))
            lbl4.grid(column=1, row=3)

            lbl5 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]), font=('family', 10))
            lbl5.grid(column=1, row=4)

            lbl6 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[0][2]) + "K $", font=('family', 10))
            lbl6.grid(column=1, row=5)

            lbl7 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 10))
            lbl7.grid(column=1, row=6)

            lbl200 = Label(window, justify='right', text="Money to Add: " + str(suggestions[4]*-1) + "K $", font=('family', 10))
            lbl200.grid(column=1, row=7)

            lbl201 = Label(window, justify='right', text="Option 2: Fastest Payback and Greater Profits", font=('family', 11))
            lbl201.grid(column=1, row=8)

            lbl202 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 10))
            lbl202.grid(column=1, row=9)

            lbl203 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]-suggestions[8]), font=('family', 10))
            lbl203.grid(column=1, row=10)

            lbl204 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[6]) + "K $", font=('family', 10))
            lbl204.grid(column=1, row=11)

            lbl205 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 10))
            lbl205.grid(column=1, row=12)



            lbl8 = Label(window, justify='right', text="\nOption 3: 100% Investment On Airborne Air-Turbine(s)", font=('family', 11))
            lbl8.grid(column=1, row=14)

            lbl9 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[2][0]), font=('family', 10))
            lbl9.grid(column=1, row=15)

            lbl10 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[2][2]) + "K $", font=('family', 10))
            lbl10.grid(column=1, row=16)

            lbl11 = Label(window, justify='right', text="Payback in: " + str(suggestions[3][2]) + " Years", font=('family', 10))
            lbl11.grid(column=1, row=17)

            btn5 = Button(window, text="Back to Menu", fg="black", bg="light green", width=10, height=2, command = back_tomenu_2)
            btn5.grid(column=0, row=18)

            btn6 = Button(window, text="Next City", fg="black", bg="light green", width=10, height=2, command =  next_city_thessaloniki)
            btn6.grid(column=3, row=18, columnspan=1, pady=5)

            flag = 1


        if suggestions[4] > 0:

            window.geometry("650x350")

            lbl207 = Label(window, justify='right', text="Option 1: Fastest Payback and Greater Profits (Suggested)", font=('family', 11))
            lbl207.grid(column=1, row=2)

            lbl208 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 10))
            lbl208.grid(column=1, row=3)

            lbl209 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]), font=('family', 10))
            lbl209.grid(column=1, row=4)

            lbl210 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[0][2]) + "K $", font=('family', 10))
            lbl210.grid(column=1, row=5)

            lbl211 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 10))
            lbl211.grid(column=1, row=6)

            lbl500 = Label(window, justify='right', text="Remaining Money: " + str(suggestions[4]) + "K $", font=('family', 10))
            lbl500.grid(column=1, row=12)

            lbl212 = Label(window, justify='right', text="\nOption 2: 100% Investment On Airborne Air-Turbine(s)", font=('family', 11))
            lbl212.grid(column=1, row=14)

            lbl213 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[2][0]), font=('family', 10))
            lbl213.grid(column=1, row=15)

            lbl214 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[2][2]) + "K $", font=('family', 10))
            lbl214.grid(column=1, row=16)

            lbl215 = Label(window, justify='right', text="Payback in: " + str(suggestions[3][2]) + " Years", font=('family', 10))
            lbl215.grid(column=1, row=17)

            btn200 = Button(window, text="Back to Menu", fg="black", bg="light green", width=10, height=2, command = back_tomenu_2)
            btn200.grid(column=0, row=18)

            btn201 = Button(window, text="Next City", fg="black", bg="light green", width=10, height=2, command =  next_city_thessaloniki)
            btn201.grid(column=3, row=18, columnspan=1, pady=5)

            flag = 2




def next_city_volos():

    global flag

    window.title("Volos")

    if flag == 3:
        lbl12.destroy()
        lbl13.destroy()
        lbl14.destroy()
        lbl15.destroy()
        lbl16.destroy()
        lbl17.destroy()
        lbl18.destroy()
        lbl19.destroy()
        lbl20.destroy()
        lbl216.destroy()
        lbl217.destroy()
        lbl218.destroy()
        lbl219.destroy()
        lbl220.destroy()
        lbl221.destroy()


        btn7.destroy()
        btn8.destroy()

    if flag == 4:
        lbl222.destroy()
        lbl223.destroy()
        lbl224.destroy()
        lbl225.destroy()
        lbl226.destroy()
        lbl501.destroy()
        lbl227.destroy()
        lbl228.destroy()
        lbl229.destroy()
        lbl230.destroy()

        btn202.destroy()
        btn203.destroy()


    suggestions = budget_algo(input_budget, 'Volos')

    lbl1.configure(text = "Volos: 65K $ / acre ")

    if suggestions[4] < 0:

        window.geometry("660x480")

        global lbl700
        lbl700 = Label(window, justify='right', text="Option 1: Fastest Payback and Greater Profits (Suggested)", font=('family', 11))
        lbl700.grid(column=1, row=2)

        global lbl701
        lbl701 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 10))
        lbl701.grid(column=1, row=3)

        global lbl702
        lbl702 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]), font=('family', 10))
        lbl702.grid(column=1, row=4)

        global lbl703
        lbl703 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[0][2]) + "K $", font=('family', 10))
        lbl703.grid(column=1, row=5)

        global lbl704
        lbl704 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 10))
        lbl704.grid(column=1, row=6)

        global lbl705
        lbl705 = Label(window, justify='right', text="Money to Add: " + str(suggestions[4]*-1) + "K $", font=('family', 10))
        lbl705.grid(column=1, row=7)

        global lbl706
        lbl706 = Label(window, justify='right', text="Option 2: Fastest Payback and Greater Profits", font=('family', 11))
        lbl706.grid(column=1, row=8)

        global lbl707
        lbl707 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 10))
        lbl707.grid(column=1, row=9)

        global lbl708
        lbl708 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]-suggestions[8]), font=('family', 10))
        lbl708.grid(column=1, row=10)

        global lbl709
        lbl709 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[6]) + "K $", font=('family', 10))
        lbl709.grid(column=1, row=11)

        global lbl710
        lbl710 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 10))
        lbl710.grid(column=1, row=12)



        global lbl711
        lbl711 = Label(window, justify='right', text="\nOption 3: 100% Investment On Airborne Air-Turbine(s)", font=('family', 11))
        lbl711.grid(column=1, row=14)

        global lbl712
        lbl712 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[2][0]), font=('family', 10))
        lbl712.grid(column=1, row=15)

        global lbl713
        lbl713 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[2][2]) + "K $", font=('family', 10))
        lbl713.grid(column=1, row=16)

        global lbl714
        lbl714 = Label(window, justify='right', text="Payback in: " + str(suggestions[3][2]) + " Years", font=('family', 10))
        lbl714.grid(column=1, row=17)

        global btn700
        btn700 = Button(window, text="Previous City", fg="black", bg="light green", width=10, height=2, command = previous_to_thessaloniki)
        btn700.grid(column=0, row=18)

        global btn701
        btn701 = Button(window, text="Next City", fg="black", bg="light green", width=10, height=2, command = next_city_korinthos)
        btn701.grid(column=3, row=18, columnspan=1, pady=5)

        flag = 5

    if suggestions[4] > 0:


        window.geometry("650x350")

        global lbl21
        lbl21 = Label(window, justify='right', text="Option 1: Fastest Payback and Greater Profits (Suggested)", font=('family', 11))
        lbl21.grid(column=1, row=2)

        global lbl22
        lbl22 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 10))
        lbl22.grid(column=1, row=3)

        global lbl23
        lbl23 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]), font=('family', 10))
        lbl23.grid(column=1, row=4)

        global lbl24
        lbl24 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[0][2]) + "K $", font=('family', 10))
        lbl24.grid(column=1, row=5)

        global lbl25
        lbl25 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 10))
        lbl25.grid(column=1, row=6)

        global lbl502
        lbl502 = Label(window, justify='right', text="Remaining Money: " + str(suggestions[4]) + "K $", font=('family', 10))
        lbl502.grid(column=1, row=7)

        global lbl26
        lbl26 = Label(window, justify='right', text="\nOption 2: 100% Investment On Airborne Air-Turbine(s)", font=('family', 11))
        lbl26.grid(column=1, row=8)

        global lbl27
        lbl27 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[2][0]), font=('family', 10))
        lbl27.grid(column=1, row=9)

        global lbl28
        lbl28 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[2][2]) + "K $", font=('family', 10))
        lbl28.grid(column=1, row=10)

        global lbl29
        lbl29 = Label(window, justify='right', text="Payback in: " + str(suggestions[3][2]) + " Years", font=('family', 10))
        lbl29.grid(column=1, row=11)

        global btn9
        btn9 = Button(window, text="Previous City", fg="black", bg="light green", width=10, height=2, command = previous_to_thessaloniki)
        btn9.grid(column=0, row=12)

        global btn10
        btn10 = Button(window, text="Next City", fg="black", bg="light green", width=10, height=2, command = next_city_korinthos)
        btn10.grid(column=3, row=12, columnspan=1, pady=5)


        flag = 6



def previous_to_thessaloniki():

    window.title("Thessaloniki")

    if flag == 5:

        lbl700.destroy()
        lbl701.destroy()
        lbl702.destroy()
        lbl703.destroy()
        lbl704.destroy()
        lbl705.destroy()
        lbl706.destroy()
        lbl707.destroy()
        lbl708.destroy()
        lbl709.destroy()
        lbl710.destroy()
        lbl711.destroy()
        lbl712.destroy()
        lbl713.destroy()
        lbl714.destroy()

        btn700.destroy()
        btn701.destroy()

    if flag == 6:

        lbl21.destroy()
        lbl22.destroy()
        lbl23.destroy()
        lbl24.destroy()
        lbl25.destroy()
        lbl26.destroy()
        lbl27.destroy()
        lbl28.destroy()
        lbl29.destroy()
        lbl502.destroy()


        btn9.destroy()
        btn10.destroy()


    next_city_thessaloniki()

def next_city_korinthos():

    window.title("Korinthos")

    global flag

    if flag == 5:

        lbl700.destroy()
        lbl701.destroy()
        lbl702.destroy()
        lbl703.destroy()
        lbl704.destroy()
        lbl705.destroy()
        lbl706.destroy()
        lbl707.destroy()
        lbl708.destroy()
        lbl709.destroy()
        lbl710.destroy()
        lbl711.destroy()
        lbl712.destroy()
        lbl713.destroy()
        lbl714.destroy()

        btn700.destroy()
        btn701.destroy()

    if flag == 6:

        lbl21.destroy()
        lbl22.destroy()
        lbl23.destroy()
        lbl24.destroy()
        lbl25.destroy()
        lbl26.destroy()
        lbl27.destroy()
        lbl28.destroy()
        lbl29.destroy()
        lbl502.destroy()


        btn9.destroy()
        btn10.destroy()


    suggestions = budget_algo(input_budget, 'Korinthos')

    lbl1.configure(text = "Korinthos: 55K $ / acre ")

    if suggestions[4] < 0:

        window.geometry("660x480")


        global lbl715
        lbl715 = Label(window, justify='right', text="Option 1: Fastest Payback and Greater Profits (Suggested)", font=('family', 11))
        lbl715.grid(column=1, row=2)

        global lbl716
        lbl716 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 10))
        lbl716.grid(column=1, row=3)

        global lbl717
        lbl717 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]), font=('family', 10))
        lbl717.grid(column=1, row=4)

        global lbl718
        lbl718 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[0][2]) + "K $", font=('family', 10))
        lbl718.grid(column=1, row=5)

        global lbl719
        lbl719 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 10))
        lbl719.grid(column=1, row=6)

        global lbl720
        lbl720 = Label(window, justify='right', text="Money to Add: " + str(suggestions[4]*-1) + "K $", font=('family', 10))
        lbl720.grid(column=1, row=7)

        global lbl721
        lbl721 = Label(window, justify='right', text="Option 2: Fastest Payback and Greater Profits", font=('family', 11))
        lbl721.grid(column=1, row=8)

        global lbl722
        lbl722 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 10))
        lbl722.grid(column=1, row=9)

        global lbl723
        lbl723 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]-suggestions[8]), font=('family', 10))
        lbl723.grid(column=1, row=10)

        global lbl724
        lbl724 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[6]) + "K $", font=('family', 10))
        lbl724.grid(column=1, row=11)

        global lbl725
        lbl725 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 10))
        lbl725.grid(column=1, row=12)

        global lbl726
        lbl726 = Label(window, justify='right', text="\nOption 3: 100% Investment On Airborne Air-Turbine(s)", font=('family', 11))
        lbl726.grid(column=1, row=14)

        global lbl727
        lbl727 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[2][0]), font=('family', 10))
        lbl727.grid(column=1, row=15)

        global lbl728
        lbl728 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[2][2]) + "K $", font=('family', 10))
        lbl728.grid(column=1, row=16)

        global lbl729
        lbl729 = Label(window, justify='right', text="Payback in: " + str(suggestions[3][2]) + " Years", font=('family', 10))
        lbl729.grid(column=1, row=17)

        global btn702
        btn702 = Button(window, text="Previous City", fg="black", bg="light green", width=10, height=2, command = previous_to_volos)
        btn702.grid(column=0, row=18)

        global btn703
        btn703 = Button(window, text="Next City", fg="black", bg="light green", width=10, height=2, command = next_city_crete)
        btn703.grid(column=3, row=18, columnspan=1, pady=5)

        flag = 7


    if suggestions[4] > 0:

        window.geometry("650x350")

        global lbl30
        lbl30 = Label(window, justify='right', text="Option 1: Fastest Payback and Greater Profits (Suggested)", font=('family', 11))
        lbl30.grid(column=1, row=2)

        global lbl31
        lbl31 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 10))
        lbl31.grid(column=1, row=3)

        global lbl32
        lbl32 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]), font=('family', 10))
        lbl32.grid(column=1, row=4)

        global lbl33
        lbl33 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[0][2]) + "K", font=('family', 10))
        lbl33.grid(column=1, row=5)

        global lbl34
        lbl34 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 10))
        lbl34.grid(column=1, row=6)

        global lbl503
        lbl503 = Label(window, justify='right', text="Remaining Money: " + str(suggestions[4]) + "K $", font=('family', 10))
        lbl503.grid(column=1, row=7)

        global lbl35
        lbl35 = Label(window, justify='right', text="\nOption 2: 100% Investment On Airborne Air-Turbine(s)", font=('family', 11))
        lbl35.grid(column=1, row=8)

        global lbl36
        lbl36 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[2][0]), font=('family', 10))
        lbl36.grid(column=1, row=9)

        global lbl37
        lbl37 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[2][2]) + "K", font=('family', 10))
        lbl37.grid(column=1, row=10)

        global lbl38
        lbl38 = Label(window, justify='right', text="Payback in: " + str(suggestions[3][2]) + " Years", font=('family', 10))
        lbl38.grid(column=1, row=11)

        global btn11
        btn11 = Button(window, text="Previous City", fg="black", bg="light green", width=10, height=2, command = previous_to_volos)
        btn11.grid(column=0, row=12)

        global btn12
        btn12 = Button(window, text="Next City", fg="black", bg="light green", width=10, height=2, command = next_city_crete)
        btn12.grid(column=3, row=12, columnspan=1, pady=5)

        flag = 8


def previous_to_volos():

    window.title("Volos")

    if flag == 7:

        lbl715.destroy()
        lbl716.destroy()
        lbl717.destroy()
        lbl718.destroy()
        lbl719.destroy()
        lbl720.destroy()
        lbl721.destroy()
        lbl722.destroy()
        lbl723.destroy()
        lbl724.destroy()
        lbl725.destroy()
        lbl726.destroy()
        lbl727.destroy()
        lbl728.destroy()
        lbl729.destroy()

        btn702.destroy()
        btn703.destroy()

    if flag == 8:

        lbl30.destroy()
        lbl31.destroy()
        lbl32.destroy()
        lbl33.destroy()
        lbl34.destroy()
        lbl503.destroy()
        lbl35.destroy()
        lbl36.destroy()
        lbl37.destroy()
        lbl38.destroy()

        btn11.destroy()
        btn12.destroy()

    next_city_volos()

def next_city_crete():

    window.title("Crete")

    global flag


    if flag == 7:

        lbl715.destroy()
        lbl716.destroy()
        lbl717.destroy()
        lbl718.destroy()
        lbl719.destroy()
        lbl720.destroy()
        lbl721.destroy()
        lbl722.destroy()
        lbl723.destroy()
        lbl724.destroy()
        lbl725.destroy()
        lbl726.destroy()
        lbl727.destroy()
        lbl728.destroy()
        lbl729.destroy()

        btn702.destroy()
        btn703.destroy()

    if flag == 8:

        lbl30.destroy()
        lbl31.destroy()
        lbl32.destroy()
        lbl33.destroy()
        lbl34.destroy()
        lbl503.destroy()
        lbl35.destroy()
        lbl36.destroy()
        lbl37.destroy()
        lbl38.destroy()

        btn11.destroy()
        btn12.destroy()


    suggestions = budget_algo(input_budget, 'Kriti')

    lbl1.configure(text = "Crete: 60K $ / acre ")

    if suggestions[4] < 0:

        window.geometry("660x480")


        global lbl730
        lbl730 = Label(window, justify='right', text="Option 1: Fastest Payback and Greater Profits (Suggested)", font=('family', 11))
        lbl730.grid(column=1, row=2)

        global lbl731
        lbl731 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 10))
        lbl731.grid(column=1, row=3)

        global lbl732
        lbl732 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]), font=('family', 10))
        lbl732.grid(column=1, row=4)

        global lbl733
        lbl733 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[0][2]) + "K $", font=('family', 10))
        lbl733.grid(column=1, row=5)

        global lbl734
        lbl734 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 10))
        lbl734.grid(column=1, row=6)

        global lbl735
        lbl735 = Label(window, justify='right', text="Money to Add: " + str(suggestions[4]*-1) + "K $", font=('family', 10))
        lbl735.grid(column=1, row=7)

        global lbl736
        lbl736 = Label(window, justify='right', text="Option 2: Fastest Payback and Greater Profits", font=('family', 11))
        lbl736.grid(column=1, row=8)

        global lbl737
        lbl737 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 10))
        lbl737.grid(column=1, row=9)

        global lbl738
        lbl738 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]-suggestions[8]), font=('family', 10))
        lbl738.grid(column=1, row=10)

        global lbl739
        lbl739 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[6]) + "K $", font=('family', 10))
        lbl739.grid(column=1, row=11)

        global lbl740
        lbl740 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 10))
        lbl740.grid(column=1, row=12)

        global lbl741
        lbl741 = Label(window, justify='right', text="\nOption 3: 100% Investment On Airborne Air-Turbine(s)", font=('family', 11))
        lbl741.grid(column=1, row=14)

        global lbl742
        lbl742 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[2][0]), font=('family', 10))
        lbl742.grid(column=1, row=15)

        global lbl743
        lbl743 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[2][2]) + "K $", font=('family', 10))
        lbl743.grid(column=1, row=16)

        global lbl744
        lbl744 = Label(window, justify='right', text="Payback in: " + str(suggestions[3][2]) + " Years", font=('family', 10))
        lbl744.grid(column=1, row=17)

        global btn704
        btn704 = Button(window, text="Previous City", fg="black", bg="light green", width=10, height=2, command = previous_to_korinthos)
        btn704.grid(column=0, row=18)

        global btn705
        btn705 = Button(window, text="Back to Menu", fg="black", bg="light green", width=10, height=2, command = back_tomenu_6)
        btn705.grid(column=3, row=18, columnspan=1, pady=5)

        flag = 9


    if suggestions[4] > 0:


        window.geometry("650x350")

        global lbl39
        lbl39 = Label(window, justify='right', text="Option 1: Fastest Payback and Greater Profits (Suggested)", font=('family', 11))
        lbl39.grid(column=1, row=2)

        global lbl40
        lbl40 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[0][0]), font=('family', 10))
        lbl40.grid(column=1, row=3)

        global lbl41
        lbl41 = Label(window, justify='right', text="Acre(s) of Greenhouse: " + str(suggestions[0][1]), font=('family', 10))
        lbl41.grid(column=1, row=4)

        global lbl42
        lbl42 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[0][2]) + "K", font=('family', 10))
        lbl42.grid(column=1, row=5)

        global lbl43
        lbl43 = Label(window, justify='right', text="Payback in: " + str(suggestions[1][2]) + " Years", font=('family', 10))
        lbl43.grid(column=1, row=6)

        global lbl504
        lbl504 = Label(window, justify='right', text="Remaining Money: " + str(suggestions[4]) + "K $", font=('family', 10))
        lbl504.grid(column=1, row=8)

        global lbl44
        lbl44 = Label(window, justify='right', text="\nOption 2: 100% Investment On Airborne Air-Turbine(s)", font=('family', 11))
        lbl44.grid(column=1, row=9)

        global lbl45
        lbl45 = Label(window, justify='right', text="Airborne Air-Turbine(s): " + str(suggestions[2][0]), font=('family', 10))
        lbl45.grid(column=1, row=10)

        global lbl46
        lbl46 = Label(window, justify='right', text="\nAnnually Profits: " + str(suggestions[2][2]) + "K", font=('family', 10))
        lbl46.grid(column=1, row=11)

        global lbl47
        lbl47 = Label(window, justify='right', text="Payback in: " + str(suggestions[3][2]) + " Years", font=('family', 10))
        lbl47.grid(column=1, row=12)

        global btn13
        btn13 = Button(window, text="Previous City", fg="black", bg="light green", width=10, height=2, command = previous_to_korinthos)
        btn13.grid(column=0, row=13)

        global btn14
        btn14 = Button(window, text="Back to Menu", fg="black", bg="light green", width=10, height=2, command = back_tomenu_6)
        btn14.grid(column=3, row=13, columnspan=1, pady=5)

        flag = 10




def previous_to_korinthos():

    window.title("Korinthos")

    if flag == 9:

        lbl730.destroy()
        lbl731.destroy()
        lbl732.destroy()
        lbl733.destroy()
        lbl734.destroy()
        lbl735.destroy()
        lbl736.destroy()
        lbl737.destroy()
        lbl738.destroy()
        lbl739.destroy()
        lbl740.destroy()
        lbl741.destroy()
        lbl742.destroy()
        lbl743.destroy()
        lbl744.destroy()

        btn704.destroy()
        btn705.destroy()

    if flag == 10:

        lbl39.destroy()
        lbl40.destroy()
        lbl41.destroy()
        lbl42.destroy()
        lbl43.destroy()
        lbl504.destroy()
        lbl44.destroy()
        lbl45.destroy()
        lbl46.destroy()
        lbl47.destroy()

        btn13.destroy()
        btn14.destroy()

    next_city_korinthos()

def back_tomenu_6():

    window.geometry("350x400")
    window.title("Investor")

    lbl1.destroy()

    if flag == 9:

        lbl730.destroy()
        lbl731.destroy()
        lbl732.destroy()
        lbl733.destroy()
        lbl734.destroy()
        lbl735.destroy()
        lbl736.destroy()
        lbl737.destroy()
        lbl738.destroy()
        lbl739.destroy()
        lbl740.destroy()
        lbl741.destroy()
        lbl742.destroy()
        lbl743.destroy()
        lbl744.destroy()

        btn704.destroy()
        btn705.destroy()

    if flag == 10:

        lbl39.destroy()
        lbl40.destroy()
        lbl41.destroy()
        lbl42.destroy()
        lbl43.destroy()
        lbl504.destroy()
        lbl44.destroy()
        lbl45.destroy()
        lbl46.destroy()
        lbl47.destroy()

        btn13.destroy()
        btn14.destroy()



    first_window()







def set_up():

    global lbl100
    lbl100 = Label(window, justify='right', text="Location / Country", font=('family', 13, 'bold'))
    lbl100.grid(column=1, row=1,columnspan = 20, pady=10, padx=0)

    window.geometry("350x400")
    window.title("Location / Country")

    btn1.destroy()
    btn2.destroy()

    global btn100
    btn100 = Button(window, text="Greece", fg="black", bg="light blue", width=10, height=2, command = greece)
    btn100.grid(column=1, row=3, columnspan=1, pady=5, padx=2)

    global btn101
    btn101 = Button(window, text="Back to Menu", fg="black", bg="light green", width=10, height=2, command = back_tomenu_3)
    btn101.grid(column=1, row=4, columnspan=2, pady=5, padx=2)


def back_tomenu_3():

    window.geometry("350x400")
    window.title("Investor")

    lbl100.destroy()

    btn100.destroy()
    btn101.destroy()

    first_window()


def back_tomenu_4():

    window.geometry("350x400")
    window.title("Investor")

    lbl101.destroy()

    btn102.destroy()
    btn103.destroy()
    btn104.destroy()
    btn105.destroy()
    btn106.destroy()
    btn107.destroy()

    first_window()


def greece():

    window.geometry("500x500")
    window.title("Greece Map")
    
    lbl100.destroy()

    btn100.destroy()
    btn101.destroy()

    global lbl101
    lbl101 = Label(window, justify='right', text="", image = logo1)
    lbl101.grid( columnspan = 15, rowspan = 30)

    global btn102
    btn102 = Button(window, text="Athens", fg="black", bg="light blue", width=5, height=1,  font=('Times', 8), command = athens)
    btn102.grid(column=3, row=16)

    global btn103
    btn103 = Button(window, text="Thessal.", fg="black", bg="light blue", width=5, height=1, font=('Times', 8), command = thessaloniki)
    btn103.grid(column=2, row=5)

    global btn104
    btn104 = Button(window, text="Volos", fg="black", bg="light blue", width=5, height=1, font=('Times', 8), command = volos)
    btn104.grid(column=2, row=10)

    global btn105
    btn105 = Button(window, text="Crete", fg="black", bg="light blue", width=5, height=1, font=('Times', 8), command = crete)
    btn105.grid(column=3, row=27)

    global btn106
    btn106 = Button(window, text="Korinthos", fg="black", bg="light blue", width=7, height=1, font=('Times', 7), command = korinthos)
    btn106.grid(column=2, row=16)

    global btn107
    btn107 = Button(window, text="Back to Menu", fg="black", bg="light green", width=10, height=2, command = back_tomenu_4)
    btn107.grid(column=1, row=31)


def athens():

    window.geometry("500x320")
    window.title("Athens")




    lbl101.destroy()

    btn102.destroy()
    btn103.destroy()
    btn104.destroy()
    btn105.destroy()
    btn106.destroy()
    btn107.destroy()

    global city
    city = 'Athens'
    acre_price = setup_algo(city,5,5)

    global lbl102
    lbl102 = Label(window, justify='right', text="Athens: 80K $ / acre", font=('family', 13))
    lbl102.grid(column=1, row=1)

    global lbl103
    lbl103 = Label(window, justify='right', text="Airborne air turbine(s):", font=('family', 10))
    lbl103.grid(column=1, row=2)

    global lbl104
    lbl104 = Label(window, justify='right', text="Greenhouse(s) / acre:", font=('family', 10))
    lbl104.grid(column=1, row=3)

    global txt100
    txt100 = Entry(window, width=7)
    txt100.grid(column=2, row=2)

    global txt101
    txt101 = Entry(window, width=7)
    txt101.grid(column=2, row=3)

    global btn108
    btn108 = Button(window, text="Submit", fg="black", bg="light blue", width=12, height=2, command = results)
    btn108.grid(column=1, row=4, columnspan = 2, pady = 5)

    global btn109
    btn109 = Button(window, text="Back to Map", fg="black", bg="light green", width=12, height=2, command = back_to_map)
    btn109.grid(column=1, row=5, columnspan = 2, pady = 5)

    global lbl105
    lbl105 = Label(window, justify='right', text="• Individual price of airborne air turbine: 325K $", font=('family', 10))
    lbl105.grid(column=1, row=7)

    global lbl106
    lbl106 = Label(window, justify='right', text="• Annually renovation cost per acre of greenhouse: 20K $", font=('family', 10))
    lbl106.grid(column=1, row=8)

    global lbl107
    lbl107 = Label(window, justify='right', text="• Annually renovation cost per acre of airborne air turbine: 20K $", font=('family', 10))
    lbl107.grid(column=1, row=9)

    global lbl108
    lbl108 = Label(window, justify='right', text="• Annually profits per acre of greenhouse: 40K $", font=('family', 10))
    lbl108.grid(column=1, row=10)

    global lbl109
    lbl109 = Label(window, justify='right', text="• Annually profits per airborne air turbine: 75K $", font=('family', 10))
    lbl109.grid(column=1, row=11)

    global lbl110
    lbl110 = Label(window, justify='right', text="• Individual price per acre of greenhouse: " + str(acre_price[6]) + "K $", font=('family', 10))
    lbl110.grid(column=1, row=6)

    return city


def thessaloniki():

    window.geometry("500x320")
    window.title("Thessaloniki")


    lbl101.destroy()

    btn102.destroy()
    btn103.destroy()
    btn104.destroy()
    btn105.destroy()
    btn106.destroy()
    btn107.destroy()

    global city
    city = 'Thesalonniki'
    acre_price = setup_algo(city,5,5)


    global lbl102
    lbl102 = Label(window, justify='right', text="Thessaloniki: 60K $ / acre", font=('family', 13))
    lbl102.grid(column=1, row=1)

    global lbl103
    lbl103 = Label(window, justify='right', text="Airborne air turbine(s):", font=('family', 10))
    lbl103.grid(column=1, row=2)

    global lbl104
    lbl104 = Label(window, justify='right', text="Greenhouse(s) / acre:", font=('family', 10))
    lbl104.grid(column=1, row=3)

    global txt100
    txt100 = Entry(window, width=7)
    txt100.grid(column=2, row=2)

    global txt101
    txt101 = Entry(window, width=7)
    txt101.grid(column=2, row=3)

    global btn108
    btn108 = Button(window, text="Submit", fg="black", bg="light blue", width=12, height=2, command = results)
    btn108.grid(column=1, row=4, columnspan = 2, pady = 5)

    global btn109
    btn109 = Button(window, text="Back to Map", fg="black", bg="light green", width=12, height=2, command = back_to_map)
    btn109.grid(column=1, row=5, columnspan = 2, pady = 5)

    global lbl105
    lbl105 = Label(window, justify='right', text="• Individual price of airborne air turbine: 325K $", font=('family', 10))
    lbl105.grid(column=1, row=7)

    global lbl106
    lbl106 = Label(window, justify='right', text="• Annually renovation cost per acre of greenhouse: 20K $", font=('family', 10))
    lbl106.grid(column=1, row=8)

    global lbl107
    lbl107 = Label(window, justify='right', text="• Annually renovation cost per acre of airborne air turbine: 20K $", font=('family', 10))
    lbl107.grid(column=1, row=9)

    global lbl108
    lbl108 = Label(window, justify='right', text="• Annually profits per acre of greenhouse: 40K $", font=('family', 10))
    lbl108.grid(column=1, row=10)

    global lbl109
    lbl109 = Label(window, justify='right', text="• Annually profits per airborne air turbine: 75K $", font=('family', 10))
    lbl109.grid(column=1, row=11)

    global lbl110
    lbl110 = Label(window, justify='right', text="• Individual price per acre of greenhouse: " + str(acre_price[6]) + "K $", font=('family', 10))
    lbl110.grid(column=1, row=6)


    return city


def volos():

    window.geometry("500x320")
    window.title("Volos")

    lbl101.destroy()

    btn102.destroy()
    btn103.destroy()
    btn104.destroy()
    btn105.destroy()
    btn106.destroy()
    btn107.destroy()

    global city
    city = 'Volos'
    acre_price = setup_algo(city,5,5)


    global lbl102
    lbl102 = Label(window, justify='right', text="Volos: 65K $ / acre", font=('family', 13))
    lbl102.grid(column=1, row=1)

    global lbl103
    lbl103 = Label(window, justify='right', text="Airborne air turbine(s):", font=('family', 10))
    lbl103.grid(column=1, row=2)

    global lbl104
    lbl104 = Label(window, justify='right', text="Greenhouse(s) / acre:", font=('family', 10))
    lbl104.grid(column=1, row=3)

    global txt100
    txt100 = Entry(window, width=7)
    txt100.grid(column=2, row=2)

    global txt101
    txt101 = Entry(window, width=7)
    txt101.grid(column=2, row=3)

    global btn108
    btn108 = Button(window, text="Submit", fg="black", bg="light blue", width=12, height=2, command = results)
    btn108.grid(column=1, row=4, columnspan = 2, pady = 5)

    global btn109
    btn109 = Button(window, text="Back to Map", fg="black", bg="light green", width=12, height=2, command = back_to_map)
    btn109.grid(column=1, row=5, columnspan = 2, pady = 5)

    global lbl105
    lbl105 = Label(window, justify='right', text="• Individual price of airborne air turbine: 325K $", font=('family', 10))
    lbl105.grid(column=1, row=7)

    global lbl106
    lbl106 = Label(window, justify='right', text="• Annually renovation cost per acre of greenhouse: 20K $", font=('family', 10))
    lbl106.grid(column=1, row=8)

    global lbl107
    lbl107 = Label(window, justify='right', text="• Annually renovation cost per acre of airborne air turbine: 20K $", font=('family', 10))
    lbl107.grid(column=1, row=9)

    global lbl108
    lbl108 = Label(window, justify='right', text="• Annually profits per acre of greenhouse: 40K $", font=('family', 10))
    lbl108.grid(column=1, row=10)

    global lbl109
    lbl109 = Label(window, justify='right', text="• Annually profits per airborne air turbine: 75K $", font=('family', 10))
    lbl109.grid(column=1, row=11)

    global lbl110
    lbl110 = Label(window, justify='right', text="• Individual price per acre of greenhouse: " + str(acre_price[6]) + "K $", font=('family', 10))
    lbl110.grid(column=1, row=6)


    return city


def korinthos():

    window.geometry("500x320")
    window.title("Korinthos")


    lbl101.destroy()

    btn102.destroy()
    btn103.destroy()
    btn104.destroy()
    btn105.destroy()
    btn106.destroy()
    btn107.destroy()

    global city
    city = 'Korinthos'
    acre_price = setup_algo(city,5,5)


    global lbl102
    lbl102 = Label(window, justify='right', text="Korinthos: 55K $ / acre", font=('family', 13))
    lbl102.grid(column=1, row=1)

    global lbl103
    lbl103 = Label(window, justify='right', text="Airborne air turbine(s):", font=('family', 10))
    lbl103.grid(column=1, row=2)

    global lbl104
    lbl104 = Label(window, justify='right', text="Greenhouse(s) / acre:", font=('family', 10))
    lbl104.grid(column=1, row=3)

    global txt100
    txt100 = Entry(window, width=7)
    txt100.grid(column=2, row=2)

    global txt101
    txt101 = Entry(window, width=7)
    txt101.grid(column=2, row=3)

    global btn108
    btn108 = Button(window, text="Submit", fg="black", bg="light blue", width=12, height=2, command = results)
    btn108.grid(column=1, row=4, columnspan = 2, pady = 5)

    global btn109
    btn109 = Button(window, text="Back to Map", fg="black", bg="light green", width=12, height=2, command = back_to_map)
    btn109.grid(column=1, row=5, columnspan = 2, pady = 5)

    global lbl105
    lbl105 = Label(window, justify='right', text="• Individual price of airborne air turbine: 325K $", font=('family', 10))
    lbl105.grid(column=1, row=7)

    global lbl106
    lbl106 = Label(window, justify='right', text="• Annually renovation cost per acre of greenhouse: 20K $", font=('family', 10))
    lbl106.grid(column=1, row=8)

    global lbl107
    lbl107 = Label(window, justify='right', text="• Annually renovation cost per acre of airborne air turbine: 20K $", font=('family', 10))
    lbl107.grid(column=1, row=9)

    global lbl108
    lbl108 = Label(window, justify='right', text="• Annually profits per acre of greenhouse: 40K $", font=('family', 10))
    lbl108.grid(column=1, row=10)

    global lbl109
    lbl109 = Label(window, justify='right', text="• Annually profits per airborne air turbine: 75K $", font=('family', 10))
    lbl109.grid(column=1, row=11)

    global lbl110
    lbl110 = Label(window, justify='right', text="• Individual price per acre of greenhouse: " + str(acre_price[6]) + "K $", font=('family', 10))
    lbl110.grid(column=1, row=6)


    return city


def crete():

    window.geometry("500x320")
    window.title("Crete")

    lbl101.destroy()

    btn102.destroy()
    btn103.destroy()
    btn104.destroy()
    btn105.destroy()
    btn106.destroy()
    btn107.destroy()

    global city
    city = 'Kriti'
    acre_price = setup_algo(city,5,5)


    global lbl102
    lbl102 = Label(window, justify='right', text="Crete: 60K $ / acre", font=('family', 13))
    lbl102.grid(column=1, row=1)

    global lbl103
    lbl103 = Label(window, justify='right', text="Airborne air turbine(s):", font=('family', 10))
    lbl103.grid(column=1, row=2)

    global lbl104
    lbl104 = Label(window, justify='right', text="Greenhouse(s) / acre:", font=('family', 10))
    lbl104.grid(column=1, row=3)

    global txt100
    txt100 = Entry(window, width=7)
    txt100.grid(column=2, row=2)

    global txt101
    txt101 = Entry(window, width=7)
    txt101.grid(column=2, row=3)

    global btn108
    btn108 = Button(window, text="Submit", fg="black", bg="light blue", width=12, height=2, command = results)
    btn108.grid(column=1, row=4, columnspan = 2, pady = 5)

    global btn109
    btn109 = Button(window, text="Back to Map", fg="black", bg="light green", width=12, height=2, command = back_to_map)
    btn109.grid(column=1, row=5, columnspan = 2, pady = 5)

    global lbl105
    lbl105 = Label(window, justify='right', text="• Individual price of airborne air turbine: 325K $", font=('family', 10))
    lbl105.grid(column=1, row=7)

    global lbl106
    lbl106 = Label(window, justify='right', text="• Annually renovation cost per acre of greenhouse: 20K $", font=('family', 10))
    lbl106.grid(column=1, row=8)

    global lbl107
    lbl107 = Label(window, justify='right', text="• Annually renovation cost per acre of airborne air turbine: 20K $", font=('family', 10))
    lbl107.grid(column=1, row=9)

    global lbl108
    lbl108 = Label(window, justify='right', text="• Annually profits per acre of greenhouse: 40K $", font=('family', 10))
    lbl108.grid(column=1, row=10)

    global lbl109
    lbl109 = Label(window, justify='right', text="• Annually profits per airborne air turbine: 75K $", font=('family', 10))
    lbl109.grid(column=1, row=11)

    global lbl110
    lbl110 = Label(window, justify='right', text="• Individual price per acre of greenhouse: " + str(acre_price[6]) + "K $", font=('family', 10))
    lbl110.grid(column=1, row=6)

    return city


def back_to_map():

    window.geometry("500x500")
    window.title("Greece Map")

    lbl102.destroy()
    lbl103.destroy()
    lbl104.destroy()
    lbl105.destroy()
    lbl106.destroy()
    lbl107.destroy()
    lbl108.destroy()
    lbl109.destroy()
    lbl110.destroy()

    txt100.destroy()
    txt101.destroy()

    btn108.destroy()
    btn109.destroy()

    greece()


def results():

    window.geometry("230x165")
    window.title("Results")

    lbl103.destroy()
    lbl104.destroy()
    lbl105.destroy()
    lbl106.destroy()
    lbl107.destroy()
    lbl108.destroy()
    lbl109.destroy()
    lbl110.destroy()



    btn108.destroy()
    btn109.destroy()

    b = txt100.get()
    global air_turbines
    air_turbines = int(b)

    c = txt101.get()
    global greenhouses
    greenhouses = int(c)

    txt100.destroy()
    txt101.destroy()

    if greenhouses / air_turbines > 12:

        window.geometry("500x500")
        window.title("Greece Map")

        lbl102.destroy()
        lbl103.destroy()
        lbl104.destroy()
        lbl105.destroy()
        lbl106.destroy()
        lbl107.destroy()
        lbl108.destroy()
        lbl109.destroy()
        lbl110.destroy()

        txt100.destroy()
        txt101.destroy()

        btn108.destroy()
        btn109.destroy()

        greece()

        messagebox.showerror("Invalid values", "1 Airborne Air Turbine cannot supply more than 12 Greenhouses ")




    else:
        values = setup_algo(city, greenhouses, air_turbines)

        global lbl111
        lbl111= Label(window, justify='right', text="Annually Profits: " + str(values[0]) + "K $", font=('family', 10))
        lbl111.grid(column=1, row=2)

        global lbl112
        lbl112 = Label(window, justify='right', text="Payback Date: " + str(values[3]), font=('family', 10))
        lbl112.grid(column=1, row=3)

        global lbl113
        lbl113= Label(window, justify='right', text="Total Construction Cost: " + str(values[4]) + "K $", font=('family', 10))
        lbl113.grid(column=1, row=4)

        global lbl114
        lbl114 = Label(window, justify='right', text="Annually Renovation Cost: " + str(values[5]) + "K $", font=('family', 10))
        lbl114.grid(column=1, row=5)

        global btn110
        btn110 = Button(window, text="Back to Menu", fg="black", bg="light green", width=12, height=2, command = back_tomenu_5)
        btn110.grid(column=1, row=6, columnspan = 2)


def back_tomenu_5():

    window.geometry("350x400")
    window.title("Investor")

    lbl102.destroy()

    lbl111.destroy()
    lbl112.destroy()
    lbl113.destroy()
    lbl114.destroy()


    btn110.destroy()

    first_window()


first_window()
window.mainloop()


