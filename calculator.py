import math
import tkinter

def show_number(num):
    msg = textbox.get()
    textbox.delete(0, tkinter.END)
    msg += str(num)
    textbox.insert(0, msg)


def set_operator(op):
    global number1
    number1 = float(textbox.get())
    textbox.delete(0, tkinter.END)
    global operator
    operator = op

def sqrt():
    global one_num
    one_num = float(textbox.get())
    result = math.sqrt(one_num)
    textbox.insert(0, result)
    
def fac():
    one_num = int(textbox.get())
    result = math.factorial(one_num)
    textbox.insert(0, result)        

def show_result():
    number2 = int(textbox.get())
    textbox.delete(0, tkinter.END)
    match operator:
        case "+":
            result = number1+number2
            strResult = str(result)
            with open('memory.txt','a') as file:
                file.write(f" {number1} + {number2} = {strResult}\n")
            textbox.insert(0, result)
        case "-":
            result = number1-number2
            strResult = str(result)
            with open('memory.txt','a') as file:
                file.write(f" {number1} - {number2} = {strResult}\n")
            textbox.insert(0, result)
        case "*":
            result = number1*number2
            strResult = str(result)
            with open('memory.txt','a') as file:
                file.write(f" {number1} * {number2} = {strResult}\n")
            textbox.insert(0, result)
        case "/":
            try:
                result = number1/number2
                strResult = str(result)
                with open('memory.txt','a') as file:
                     file.write(f" {number1} / {number2} = {strResult}\n")
            except:
                window2 = tkinter.Tk()
                window2.title("Error Message")
                window2.geometry("300x100")
                window2["bg"] = "#000000"
                label1 = tkinter.Label(window2,text='you cant divide a number to zero', font=(16),fg='#ffffff',bg="#000000")
                label1.grid(row="0", column="0")
                button1 = tkinter.Button(window2,text='Close calculator',bg="white",fg="red", command= window1.destroy)
                button1.grid(row="1", column="0",padx=10,pady=10)
                window2.mainloop()

        case "**":
            result = math.pow(number1,number2)
            strResult = str(result)
            with open('memory.txt','a') as file:
                file.write(f"{number1} ** {number2} = {strResult}\n")
            textbox.insert(0, result)
    
    
def go_history():
    with open('memory.txt','r') as file:
        print("\n\n\n")
        print(file.read())

def clear_message():
    textbox.delete(0, tkinter.END)
    number1=0
    number2=0


window1 = tkinter.Tk()
window1.title("Calculator")
window1.geometry("330x450")
window1["bg"] = "#eeeeee"

textbox = tkinter.Entry(window1, width="28", bg="#f9f9f9", bd="1",font=(17))

btn0 = tkinter.Button(window1, text="0", padx=20,
                      pady=10, bg="white", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=lambda: show_number(0))
btn1 = tkinter.Button(window1, text="1", padx=20,
                      pady=10, bg="white", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=lambda: show_number(1))
btn2 = tkinter.Button(window1, text="2", padx=20,
                      pady=10, bg="white", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=lambda: show_number(2))
btn3 = tkinter.Button(window1, text="3", padx=20,
                      pady=10, bg="white", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=lambda: show_number(3))
btn4 = tkinter.Button(window1, text="4", padx=20,
                      pady=10, bg="white", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=lambda: show_number(4))
btn5 = tkinter.Button(window1, text="5", padx=20,
                      pady=10, bg="white", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=lambda: show_number(5))
btn6 = tkinter.Button(window1, text="6", padx=20,
                      pady=10, bg="white", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=lambda: show_number(6))
btn7 = tkinter.Button(window1, text="7", padx=20,
                      pady=10, bg="white", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=lambda: show_number(7))
btn8 = tkinter.Button(window1, text="8", padx=20,
                      pady=10, bg="white", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=lambda: show_number(8))
btn9 = tkinter.Button(window1, text="9", padx=20,
                      pady=10, bg="white", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=lambda: show_number(9))
btn_add = tkinter.Button(window1, text="+", padx=18,
                         pady=10, bg="#f3f3f3", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=lambda: set_operator("+"))
btn_subtraction = tkinter.Button(window1, text="-", padx=20,
                                 pady=10, bg="#f3f3f3", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=lambda: set_operator("-"))
btn_multiply = tkinter.Button(window1, text="*", padx=20,
                              pady=10, bg="#f3f3f3", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=lambda: set_operator("*"))
btn_divide = tkinter.Button(window1, text="/", padx=21,
                            pady=10, bg="#f3f3f3", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=lambda: set_operator("/"))
btn_equal = tkinter.Button(window1, text="=", padx=19,
                           pady=10, bg="#f3f3f3", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=show_result)
btn_clear = tkinter.Button(window1, text="Clear", padx=1.5,
                           pady=10, bg="#f3f3f3", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=clear_message)
btn_power = tkinter.Button(window1, text="pow", padx=12,
                           pady=10, bg="#f3f3f3", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=lambda: set_operator("**"))
btn_sqrt = tkinter.Button(window1, text="sqr", padx=12,
                           pady=10, bg="#f3f3f3", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=lambda: sqrt())
btn_fac = tkinter.Button(window1, text="fac", padx=12,
                           pady=10, bg="#f3f3f3", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=lambda: fac())
btn_history = tkinter.Button(window1, text="his", padx=12,
                           pady=10, bg="#f3f3f3", fg="#000000", activebackground="gray", activeforeground="black", bd="4",font=(12), command=lambda: go_history())

textbox.grid(row="0", column="0", columnspan="4",ipady=20, pady=15,padx=4)
btn0.grid(row="4", column="0",padx=5,pady=4)
btn1.grid(row="3", column="0",padx=5,pady=4)
btn2.grid(row="3", column="1",padx=5,pady=4)
btn3.grid(row="3", column="2",padx=5,pady=4)
btn4.grid(row="2", column="0",padx=5,pady=4)
btn5.grid(row="2", column="1",padx=5,pady=4)
btn6.grid(row="2", column="2",padx=5,pady=4)
btn7.grid(row="1", column="0",padx=5,pady=4)
btn8.grid(row="1", column="1",padx=5,pady=4)
btn9.grid(row="1", column="2",padx=5,pady=4)
btn_add.grid(row="1", column="3",padx=5,pady=4)
btn_subtraction.grid(row="2", column="3",padx=5,pady=4)
btn_multiply.grid(row="3", column="3",padx=5,pady=4)
btn_divide.grid(row="4", column="3",padx=5,pady=4)
btn_equal.grid(row="4", column="2",padx=5,pady=4)
btn_clear.grid(row="4", column="1",padx=5,pady=4)
btn_power.grid(row="5", column="0",padx=5,pady=4)
btn_sqrt.grid(row="5", column="1",padx=5,pady=4)
btn_fac.grid(row="5", column="2",padx=5,pady=4)
btn_history.grid(row="5", column="3",padx=5,pady=4)

window1.mainloop()
