import tkinter
import operator

window = tkinter.Tk()  # beginning of gui loop

window.resizable(False, False)

window.title('PyCalculator')
window.geometry('295x455')

# frame where text would be inputted
textFrame = tkinter.Frame(window, height=50, width=250, borderwidth=5).place(x=23, y=10)

buttonFrames = tkinter.Frame(window)

# Input Button


button = tkinter.Entry(window)
button.pack(pady=30)
input = button.get()

def main():
    global count
    count = 0


    def input_button1():
        global count
        button.insert(count, 1)
        count = count + 1


    def input_button2():
        global count
        button.insert(count, 2)
        count = count + 1


    def input_button3():
        global count
        button.insert(count, 3)
        count = count + 1


    def input_button4():
        global count
        button.insert(count, 4)
        count = count + 1


    def input_button5():
        global count
        button.insert(count, 5)
        count = count + 1


    def input_button6():
        global count
        button.insert(count, 6)
        count = count + 1


    def input_button7():
        global count
        button.insert(count, 7)
        count = count + 1


    def input_button8():
        global count
        button.insert(count, 8)
        count = count + 1


    def input_button9():
        global count
        button.insert(count, 9)
        count = count + 1


    def input_button0():
        global count
        button.insert(count, 0)
        count = count + 1

    global counter_add
    counter_add = 0
    def input_button_add():
        global counter_add
        global count
        button.insert(count, '+')
        count = count + 1
        counter_add+=1

    global counter_sub
    counter_sub = 0
    def input_button_subtract():
        global counter_sub
        global count
        button.insert(count, '-')
        count = count + 1
        counter_sub+=1

    global counter_mul
    counter_mul = 0
    def input_button_multiply():
        global counter_mul
        global count
        button.insert(count, '*')
        count = count + 1
        counter_mul+=1

    global counter_div
    counter_div = 0
    def input_button_divide():
        global counter_div
        global count
        button.insert(count, '/')
        count = count + 1
        counter_div+=1

    global counter_exp
    counter_exp = 0
    def input_button_exp():
        global counter_exp
        global count
        button.insert(count, '^')
        count = count + 1
        counter_exp+=1

    global counter_sqr
    counter_sqr = 0
    def input_button_sqrt():
        global counter_sqr
        global count
        button.insert(count, '√')
        count = count + 1
        counter_sqr+=1

    global total_sum
    global total
    global counter
    def input_buttonClear():
        button.delete("0", "end")
        main()


    global total

    total_sum = ""

    global counter

    counter = 0

    total = 0

    def calculate():
        operator_dict = {"+": operator.add, "-": operator.sub, '*': operator.mul, '/': operator.truediv}
        button.get()
        list = []
        for loopvar in button.get():
            list.append(loopvar)
        for a in list:
            global total
            if a == '1' or a == '2' or a == '3' or a == '4' or a == '5' or a == '6' or a == '7' or a == '8' or a == '9' or a == '0':
                global total_sum
                total_sum += a
            elif a == '+':
                total = float(total_sum)
                total_sum = ""
            elif a == '-':
                global counter
                counter += 1
                total = (-1 * float(total_sum))
                total_sum = ""
            elif a == '*':
                total = 1
                total = float(total_sum)
                total_sum = ""
            elif a == '/':
                total = 1
                total = float(total_sum)
                total_sum = ""
            elif a == '^':
                total = 1
                total = float(total_sum)
                total_sum = ""
            elif a == '√':
                total = 1
                total = float(total_sum)
                total_sum = ""
        if counter_sub == 1:
            answer = (-1*float(total_sum))+ (-1*total)           #Subtraction
        elif counter_add == 1:
            answer = float(total_sum) + total                   #Addition
        elif counter_mul == 1:
            answer = total*float(total_sum)                     #Multiplication
        elif counter_div == 1:
            answer = total/float(total_sum)                     #Division
        elif counter_exp == 1:
            answer = total**(float(total_sum))                  #Exponent
        elif counter_sqr == 1:
            answer = total**(1/2)                             #Square Root
        total_sum = ""
        total = 0
        counter = 0
        answerLabel = tkinter.Label(window, height=1, width=50, text="Answer: " + str(answer)).place(x=-31, y=50)
    # Number Keypad
    button_1 = tkinter.Button(window, text="1", height=4, width=8, command=input_button1).place(x=10, y=300)

    button_2 = tkinter.Button(window, text="2", height=4, width=8, command=input_button2).place(x=80, y=300)

    button_3 = tkinter.Button(window, text="3", height=4, width=8, command=input_button3).place(x=150, y=300)

    button_4 = tkinter.Button(window, text="4", height=4, width=8, command=input_button4).place(x=10, y=225)

    button_5 = tkinter.Button(window, text="5", height=4, width=8, command=input_button5).place(x=80, y=225)

    button_6 = tkinter.Button(window, text="6", height=4, width=8, command=input_button6).place(x=150, y=225)

    button_7 = tkinter.Button(window, text="7", height=4, width=8, command=input_button7).place(x=10, y=150)

    button_8 = tkinter.Button(window, text="8", height=4, width=8, command=input_button8).place(x=80, y=150)

    button_9 = tkinter.Button(window, text="9", height=4, width=8, command=input_button9).place(x=150, y=150)

    button_0 = tkinter.Button(window, text="0", height=4, width=8, command=input_button0).place(x=80, y=375)

    button_period = tkinter.Button(window, text="", height=4, width=8).place(x=150, y=375)

    # Operation buttons

    buttonAdd = tkinter.Button(window, text="+", height=4, width=8, command=input_button_add).place(x=220, y=300)

    buttonSubtract = tkinter.Button(window, text="-", height=4, width=8, command=input_button_subtract).place(x=220, y=225)

    buttonMultiply = tkinter.Button(window, text="*", height=4, width=8, command=input_button_multiply).place(x=220, y=150)

    buttonDivide = tkinter.Button(window, text="/", height=4, width=8, command=input_button_divide).place(x=220, y=75)

    buttonEqual = tkinter.Button(window, text="=", height=4, width=8, command=calculate).place(x=220, y=375)

    buttonClear = tkinter.Button(window, text="Clear", height=4, width=8, command=input_buttonClear).place(x=10, y=375)

    buttonSqrt = tkinter.Button(window, text="√", height=4, width=8, command=input_button_sqrt).place(x=150, y=75)

    buttonExp = tkinter.Button(window, text="^", height=4, width=8, command=input_button_exp).place(x=80, y=75)

    buttonGraph = tkinter.Button(window, text="", height=4, width=8).place(x=10, y=75)

    window.mainloop()  # end of loop
main()
