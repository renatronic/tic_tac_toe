from tkinter import *
import tkinter.messagebox

root = Tk()
root.iconbitmap(r'C:/Users/m64/Downloads/python/tic_tac_toe/ttt.ico')
root.title('Tic-tac-toe')
root.resizable(width=False, height=False)

click = True #
count = 0 # it will track the moves number

# text variables are associated with widgets in tkinter, in this case with our buttons
btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()

# setting images
x_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/tic_tac_toe/x.png')
o_img = PhotoImage(file = r'C:/Users/m64/Downloads/python/tic_tac_toe/o.png')

# functions
def play(): # contains the game
    button1 = Button(root, height = 9, width = 19, relief= 'ridge', borderwidth = 0.5, background = '#b3b3ff', textvariable = btn1, command = lambda:press(1, 0, 0))
    button1.grid(row = 0, column = 0)
    button2 = Button(root, height = 9, width = 19, relief= 'ridge', borderwidth = 0.5, background = '#b3b3ff', textvariable = btn2, command = lambda:press(2, 0, 1))
    button2.grid(row = 0, column = 1)
    button3 = Button(root, height = 9, width = 19, relief= 'ridge', borderwidth = 0.5, background = '#b3b3ff', textvariable = btn3, command = lambda:press(3, 0, 2))
    button3.grid(row = 0, column = 2)
    button4 = Button(root, height = 9, width = 19, relief= 'ridge', borderwidth = 0.5, background = '#8080ff', textvariable = btn4, command = lambda:press(4, 1, 0))
    button4.grid(row = 1, column = 0)
    button5 = Button(root, height = 9, width = 19, relief= 'ridge', borderwidth = 0.5, background = '#8080ff', textvariable = btn5, command = lambda:press(5, 1, 1))
    button5.grid(row = 1, column = 1)
    button6 = Button(root, height = 9, width = 19, relief= 'ridge', borderwidth = 0.5, background = '#8080ff', textvariable = btn6, command = lambda:press(6, 1, 2))
    button6.grid(row = 1, column = 2)
    button7 = Button(root, height = 9, width = 19, relief= 'ridge', borderwidth = 0.5, background = '#4d4dff', textvariable = btn7, command = lambda:press(7, 2, 0))
    button7.grid(row = 2, column = 0)
    button8 = Button(root, height = 9, width = 19, relief= 'ridge', borderwidth = 0.5, background = '#4d4dff', textvariable = btn8, command = lambda:press(8, 2, 1))
    button8.grid(row = 2, column = 1)
    button9 = Button(root, height = 9, width = 19, relief= 'ridge', borderwidth = 0.5, background = '#4d4dff', textvariable = btn9, command = lambda:press(9, 2, 2))
    button9.grid(row = 2, column = 2)

play()
def press(num, r, c): # checks wich button we pressed
    pass

def checkWin(): # checks to see who won
    pass

def clear(): # clears the text variables and resets the game
    pass

root.mainloop()