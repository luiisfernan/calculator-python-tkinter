from tkinter import *
import parser


root = Tk()
root.title('Calculator')

display = Entry(root)
display.grid(row=1, columnspan=8, sticky=W+E)






i = 0

def numbers(n):
    global i
    display.insert(i, n)
    i+=1 

def operation(operator):
    global i
    operator_length = len(operator)
    display.insert(i, operator)
    i+=operator_length

def clear():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if (display_state):
        display_new_state = display_state[:-1]
        clear()
        display.insert(0, display_new_state)
    else:
        clear()
        display.insert(0, 'Error')

def calculate():
    display_state = display.get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        clear()
        display.insert(0, result)
    except:
        clear()
        display.insert(0, 'Error')

#Numeric Buttons
Button(root, text="1", command=lambda:numbers(1)).grid(row=4, column=0, sticky=W+E)
Button(root, text="2", command=lambda:numbers(2)).grid(row=4, column=1, sticky=W+E)
Button(root, text="3", command=lambda:numbers(3)).grid(row=4, column=2, sticky=W+E)

Button(root, text="4", command=lambda:numbers(4)).grid(row=5, column=0, sticky=W+E)
Button(root, text="5", command=lambda:numbers(5)).grid(row=5, column=1, sticky=W+E)
Button(root, text="6", command=lambda:numbers(6)).grid(row=5, column=2, sticky=W+E)

Button(root, text="7", command=lambda:numbers(7)).grid(row=6, column=0, sticky=W+E)
Button(root, text="8", command=lambda:numbers(8)).grid(row=6, column=1, sticky=W+E)
Button(root, text="9", command=lambda:numbers(9)).grid(row=6, column=2, sticky=W+E)





#Buttons Extra
Button(root, text="C", command=lambda: clear()).grid(row=3, column=0, sticky=W+E)
Button(root, text="/", command=lambda:operation("/")).grid(row=3, column=3, sticky=W+E)
Button(root, text="^2", command=lambda:operation("**2")).grid(row=3, column=4, sticky=W+E)
Button(root, text="ᐊ", command=lambda: undo()).grid(row=3, column=1, sticky=W+E, columnspan=2)

Button(root, text="0", command=lambda:numbers(0)).grid(row=7, column=0, sticky=W+E, columnspan=2)
Button(root, text=".", command=lambda:operation(".")).grid(row=7, column=2, sticky=W+E)

Button(root, text="+", command=lambda:operation("+")).grid(row=6, column=3, sticky=W+E)
Button(root, text="-", command=lambda:operation("-")).grid(row=5, column=3, sticky=W+E)
Button(root, text="*", command=lambda:operation("*")).grid(row=4, column=3, sticky=W+E)




Button(root, text="exp", command=lambda:operation("**")).grid(row=4, column=4, sticky=W+E)

Button(root, text="(", command=lambda:operation("(")).grid(row=5, column=4, sticky=W+E)
Button(root, text=")", command=lambda:operation(")")).grid(row=6, column=4, sticky=W+E)
Button(root, text="=", command=lambda: calculate()).grid(row=7, column=3, sticky=W+E, columnspan=2)

root.mainloop()