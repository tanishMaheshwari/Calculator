import tkinter as tk
from tkinter.constants import DISABLED, END, FLAT, GROOVE, RIDGE, SUNKEN
from typing import Collection

x = 200
y = 450

Theme = '1'

xXy = str(x) + 'x' + str(y)
root = tk.Tk()
root.title('Simple Calculator')


exp = ''

topFrame = tk.Frame(root)

# Top Frame Items
displayEntryText = tk.StringVar()
displayEntry = tk.Entry(topFrame, width=12, font=('arial', 20), fg='black', textvariable=displayEntryText, relief=RIDGE)

def keyPressed(event):
    if event.keysym == 'Return':
        ans()


displayEntry.bind('<Key>', keyPressed)
displayEntry.focus()

displayEntryText.set(exp)


calcLabel = tk.Label(topFrame, text='Calculator', font=('orbitron', 16, 'bold'))
label1 = tk.Label(topFrame, text='(you can also type directly)', font=('orbitron', 9))


# Bottom Frame

bottomFrame = tk.Frame(root)


# Operations

def clearText():
    global exp
    exp = ''
    displayEntryText.set(exp)
    print('clear')
def delText():
    global exp
    exp = exp[0:-1]
    displayEntryText.set(exp)
    print('del')
def addPlus():
    global exp
    if exp == '':
        print('Bruh')
    elif exp[-1] not in ['+', '-', '*', '/', '(', '.']:
        exp += '+'
        displayEntryText.set(exp)
        displayEntry.icursor(len(exp));displayEntry.xview(END)
        print("+")
    else:
        print("Nope")
def addMinus():
    global exp
    if exp == '':
        exp = '-'
        displayEntryText.set(exp)
        displayEntry.icursor(len(exp));displayEntry.xview(END)
    elif exp[-1] not in ['+', '*', '/', '.']:
        exp += '-'
        displayEntryText.set(exp)
        displayEntry.icursor(len(exp));displayEntry.xview(END)
        print("-")
    else:
        print("Nope")
def addMul():
    global exp
    if exp == '':
        print('Bruh')
    elif exp[-1] not in ['+', '-', '*', '/', '(', '.']:
        exp += '*'
        displayEntryText.set(exp)
        displayEntry.icursor(len(exp));displayEntry.xview(END)
        print("*")
    else:
        print("Nope")
def addDiv():
    global exp
    if exp == '':
        print('Bruh')
    elif exp[-1] not in ['+', '-', '*', '/', '(', '.']:
        exp += '/'
        displayEntryText.set(exp)
        displayEntry.icursor(len(exp));displayEntry.xview(END)
        print("/")
    else:
        print("Nope")
def addOb():
    global exp
    if exp == '':
        exp += '('
        displayEntryText.set(exp)
        displayEntry.icursor(len(exp));displayEntry.xview(END)
        print('(')
    elif exp[-1] not in ['.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        exp += '('
        displayEntryText.set(exp)
        displayEntry.icursor(len(exp));displayEntry.xview(END)
        print('(')
def addCb():
    global exp
    if exp[-1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ')']:
        exp += ')'
        displayEntryText.set(exp)
        displayEntry.icursor(len(exp));displayEntry.xview(END)
        print(')')
def addDot():
    global exp
    if exp == '':
        print('Bruh')
    elif exp[-1] not in ['+', '-', '*', '/', '(', ')']:
        exp += '.'
        
        displayEntryText.set(exp)
        displayEntry.icursor(len(exp));displayEntry.xview(END)
        print("+")
    else:
        print("Nope")

# Numbers

def add(x):
    global exp
    exp += str(x)
    displayEntryText.set(exp)
    displayEntry.icursor(len(exp));displayEntry.xview(END)
    print(str(x))

# ========
def ans():
    global exp
    print(displayEntry.get())
    try:
        exp = displayEntry.get()
        exp = str(eval(exp))
        displayEntryText.set(exp)
        displayEntry.icursor(len(exp));displayEntry.xview(END)
    except:
        if displayEntry.get() == 'Error':
            exp = ''
            displayEntryText.set('Bruh...Error')
            displayEntry.icursor(len(exp));displayEntry.xview(END)
        elif displayEntry.get() == 'Bruh...Error':
            exp = ''
            displayEntryText.set('Error')
            displayEntry.icursor(len(exp));displayEntry.xview(END)
        elif displayEntry.get() == 'Help':
            exp = 'Nope'
            displayEntryText.set('Nope')
            displayEntry.icursor(len(exp));displayEntry.xview(END)
        elif exp == '':
            exp = ''
            displayEntryText.set(exp)
            displayEntry.icursor(len(exp));displayEntry.xview(END)
        else:
            exp=''
            displayEntryText.set('Error')
            displayEntry.icursor(len(exp));displayEntry.xview(END)
    
    print('display answer')

def getExp():
    global exp
    exp = displayEntry.get()
    displayEntryText.set(exp)
    print("Get Eqn from Display")


# Row 0

clearButton = tk.Button(bottomFrame, text='  Clear  ', command=clearText, relief=FLAT)
delButton = tk.Button(bottomFrame, text='←', command=delText, relief=FLAT)


# Row 1
obButton = tk.Button(bottomFrame, text='(', command=addOb, relief=FLAT)
cbButton = tk.Button(bottomFrame, text=')', command=addCb, relief=FLAT)
mulButton = tk.Button(bottomFrame, text='* ', command=addMul, relief=FLAT)
divButton = tk.Button(bottomFrame, text='/ ', command=addDiv, relief=FLAT)

# Row 2
Button1 = tk.Button(bottomFrame, text='1', command=lambda:add(1), relief=FLAT)
Button2 = tk.Button(bottomFrame, text='2', command=lambda:add(2), relief=FLAT)
Button3 = tk.Button(bottomFrame, text='3', command=lambda:add(3), relief=FLAT)
addButton = tk.Button(bottomFrame, text='+', command=addPlus, relief=FLAT)

# Row 3
Button4 = tk.Button(bottomFrame, text='4', command=lambda:add(4), relief=FLAT)
Button5 = tk.Button(bottomFrame, text='5', command=lambda:add(5), relief=FLAT)
Button6 = tk.Button(bottomFrame, text='6', command=lambda:add(6), relief=FLAT)
subButton = tk.Button(bottomFrame, text='- ', command=addMinus, relief=FLAT)

# Row 4
Button7 = tk.Button(bottomFrame, text='7', command=lambda:add(7), relief=FLAT)
Button8 = tk.Button(bottomFrame, text='8', command=lambda:add(8), relief=FLAT)
Button9 = tk.Button(bottomFrame, text='9', command=lambda:add(9), relief=FLAT)

# Row 5
Button0 = tk.Button(bottomFrame, text='    0  ', command=lambda:add(0), relief=FLAT)
ButtonDot = tk.Button(bottomFrame, text='. ', command=addDot, relief=FLAT)

# Non 4 + 5
ansButton = tk.Button(bottomFrame, text='\n=\n', command=ans, relief=FLAT)

# Row 6
themeLabel = tk.Label(bottomFrame, text='Theme: ')


def themeClick():
    global Theme
    if Theme == '1':
        Theme = '2'
        themeButton.config(text='Dark', fg='white', bg='black')
        themeApply()
    else:
        Theme = '1'
        themeButton.config(text='Light', fg='black', bg='white')
        themeApply()

themeButton = tk.Button(bottomFrame, text='', relief=GROOVE, command=themeClick, width=13)
if Theme == '1':
    themeButton.config(text='Light')
else:
    themeButton.config(text='Dark')

# Apply Theme
def themeApply():
    if Theme == '2':
        displayEntry.config(fg='white', bg='black')
        calcLabel.config(bg='black', fg='gold')
        label1.config(bg='black', fg='gold')
        clearButton.config(fg='white', bg='black')
        delButton.config(fg='white', bg='black')
        obButton.config(fg='white', bg='black')
        cbButton.config(fg='white', bg='black')
        mulButton.config(fg='white', bg='black')
        divButton.config(fg='white', bg='black')
        Button1.config(fg='white', bg='black')
        Button2.config(fg='white', bg='black')
        Button3.config(fg='white', bg='black')
        addButton.config(fg='white', bg='black')
        Button4.config(fg='white', bg='black')
        Button5.config(fg='white', bg='black')
        Button6.config(fg='white', bg='black')
        subButton.config(fg='white', bg='black')
        Button7.config(fg='white', bg='black')
        Button8.config(fg='white', bg='black')
        Button9.config(fg='white', bg='black')
        Button0.config(fg='white', bg='black')
        ButtonDot.config(fg='white', bg='black')
        ansButton.config(fg='white', bg='black')
        topFrame.config(bg='black')
        bottomFrame.config(bg='black')
        root.config(bg='black')
        themeLabel.config(fg='white', bg='black')
        themeButton.config(fg='white', bg='black')
    else:
        displayEntry.config(bg='white', fg='black')
        calcLabel.config(bg='white', fg='black')
        label1.config(bg='white', fg='black')
        clearButton.config(bg='white', fg='black')
        delButton.config(bg='white', fg='black')
        obButton.config(bg='white', fg='black')
        cbButton.config(bg='white', fg='black')
        mulButton.config(bg='white', fg='black')
        divButton.config(bg='white', fg='black')
        Button1.config(bg='white', fg='black')
        Button2.config(bg='white', fg='black')
        Button3.config(bg='white', fg='black')
        addButton.config(bg='white', fg='black')
        Button4.config(bg='white', fg='black')
        Button5.config(bg='white', fg='black')
        Button6.config(bg='white', fg='black')
        subButton.config(bg='white', fg='black')
        Button7.config(bg='white', fg='black')
        Button8.config(bg='white', fg='black')
        Button9.config(bg='white', fg='black')
        Button0.config(bg='white', fg='black')
        ButtonDot.config(bg='white', fg='black')
        ansButton.config(bg='white', fg='black')
        topFrame.config(bg='white')
        bottomFrame.config(bg='white')
        root.config(bg='white')
        themeLabel.config(bg='white', fg='black')
        themeButton.config(bg='white', fg='black')

themeApply()


# Putting the Widgets in the window
# Top Frame
topFrame.pack(side='top')
calcLabel.pack()
label1.pack()


displayEntry.pack(ipadx=2)

# Bottom Frame
bottomFrame.pack()

clearButton.grid(row=0, column=0, columnspan=3, ipadx=46, ipady=10)
delButton.grid(row=0, column=3, ipadx=14, ipady=10)

obButton.grid(row=1, column=0, ipadx=16, ipady=10)
cbButton.grid(row=1, column=1, ipadx=16, ipady=10)
mulButton.grid(row=1, column=2, ipadx=14, ipady=10)
divButton.grid(row=1, column=3, ipadx=15, ipady=10)

Button1.grid(row=2, column=0, ipadx=15, ipady=10)
Button2.grid(row=2, column=1, ipadx=15, ipady=10)
Button3.grid(row=2, column=2, ipadx=15, ipady=10)
addButton.grid(row=2, column=3, ipadx=15, ipady=10)

Button4.grid(row=3, column=0, ipadx=15, ipady=10)
Button5.grid(row=3, column=1, ipadx=15, ipady=10)
Button6.grid(row=3, column=2, ipadx=15, ipady=10)
subButton.grid(row=3, column=3, ipadx=15, ipady=10)

Button7.grid(row=4, column=0, ipadx=15, ipady=10)
Button8.grid(row=4, column=1, ipadx=15, ipady=10)
Button9.grid(row=4, column=2, ipadx=15, ipady=10)

ansButton.grid(row=4, rowspan=2, column=3, ipadx=15, ipady=20)
Button0.grid(row=5, column=0, columnspan=2, ipadx=30, ipady=11)
ButtonDot.grid(row=5, column=2, ipadx=15, ipady=11)

themeLabel.grid(row=6, column=0, columnspan=2)
themeButton.grid(row=6, column=2, columnspan=2)


root.mainloop()