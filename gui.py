#import
import threading
from tkinter import *
#vars
calc_operator = ""
root = Tk()
root.title("Calc")
root.geometry("550x450")
text_input = StringVar()
#entry and defs
def button_equal():
    global calc_operator
    temp_op = str(eval(calc_operator))
    text_input.set(temp_op)
    calc_operator = temp_op

def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

entry1 = Entry(bg='black', textvariable=text_input, fg='white')
#buttons
btn0 = Button(root, text = '1', command = lambda: button_click('1'))
btn1 = Button(root, text = '2', command = lambda: button_click('2'))
btn2 = Button(root, text = '3', command = lambda: button_click('3'))
btn3 = Button(root, text = '4', command = lambda: button_click('4'))
btn4 = Button(root, text = '5', command = lambda: button_click('5'))
btn5 = Button(root, text = '6', command = lambda: button_click('6'))
btn6 = Button(root, text = '7', command = lambda: button_click('7'))
btn7 = Button(root, text = '8', command = lambda: button_click('8'))
btn8 = Button(root, text = '9', command = lambda: button_click('9'))
btn9 = Button(root, text = '0', command = lambda: button_click('0'))
btn10 = Button(root, text = 'add', command = lambda: button_click('+'))
btn11 = Button(root, text = 'subtract', command= lambda: button_click('-'))
btn12 = Button(root, text = 'multiply', command = lambda: button_click('*'))
btn13 = Button(root, text = 'divide', command = lambda: button_click('/'))
btn15 = Button(root, text = 'equal', command=lambda: button_equal())
btn16 = Button(root, text = 'clear', command=lambda:  button_clear_all())
#pack
entry1.grid(row=1, column=4)
btn0.grid(row = 1, column = 1)
btn1.grid(row = 1, sticky = W, column = 2)
btn2.grid(row = 1, sticky = W, column = 3)
btn3.grid(row = 2, column = 1)
btn4.grid(row = 2, sticky = W, column = 2)
btn5.grid(row = 2, sticky = W, column = 3)
btn6.grid(row = 3, column = 1)
btn7.grid(row = 3, sticky = W, column = 2)
btn8.grid(row = 3, sticky = W, column = 3)
btn9.grid(row = 4, column = 1)
btn10.grid(row = 4, sticky = W, column = 2)
btn11.grid(row = 4, sticky = W, column = 3)
btn12.grid(row = 5, column = 1)
btn13.grid(row = 5, sticky = W, column = 2)
btn15.grid(row = 6, column = 1)
btn16.grid(row = 7, column = 1)



#end
root.mainloop()