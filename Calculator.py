import tkinter
from tkinter import RIGHT, END, DISABLED, NORMAL

# Define the window
root = tkinter.Tk()
root.title("Calculator")
root.geometry("300x350")
root.resizable(0, 0)
root.configure(bg="light blue")

# Define the colors and fonts
display_color = "#EDEFE0"
button_font = ("Arial", 18)
display_font = ("Arial", 30)

# Define the functions
def submit_number(number):
    """Add a number or decimal to the display"""
    # Insert the number or decimal at the end of the display
    display.insert(END, number)
    # If decimal was pressed, disable the decimal button
    if "." in display.get():
        decimal_button.config(state=DISABLED)


def operate(operator):
    """Store the first number of the operation and the operation to be used"""
    global first_number
    global operation
    # Get the operator pressed and the current value of the display
    operation = operator
    first_number = display.get()
    # Delete the first value from the display
    display.delete(0, END)
    # Disable all operator buttons until clear or equal is pressed
    add_button.config(state=DISABLED)
    subtract_button.config(state=DISABLED)
    multiply_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)
    exponent_button.config(state=DISABLED)
    square_button.config(state=DISABLED)
    inverse_button.config(state=DISABLED)
    # Return the decimal button to normal
    decimal_button.config(state=NORMAL)


def equal():
    """Run the stored operation for two numbers"""
    global value
    # Do the math
    if operation == "add":
        value = float(first_number) + float(display.get())
    elif operation == "subtract":
        value = float(first_number) - float(display.get())
    elif operation == "multiply":
        value = float(first_number) * float(display.get())
    elif operation == "divide":
        if display.get() == "0":
            value = "ERROR"
        else:
            value = float(first_number) / float(display.get())
    elif operation == "exponent":
        value = float(first_number) ** float(display.get())
    # Change the result to an int if the result is an integer
    int_check()
    # Remove the current value of the display and replace it with the answer
    display.delete(0, END)
    display.insert(0, value)
    # Return the buttons to their normal state
    enable_buttons()
    # If there is a decimal in the answer, disable the decimal button
    decimal_check()


def enable_buttons():
    """Enable all disabled buttons on the calculator"""
    decimal_button.config(state=NORMAL)
    add_button.config(state=NORMAL)
    subtract_button.config(state=NORMAL)
    multiply_button.config(state=NORMAL)
    divide_button.config(state=NORMAL)
    exponent_button.config(state=NORMAL)
    square_button.config(state=NORMAL)
    inverse_button.config(state=NORMAL)


def clear():
    """Clear the display"""
    display.delete(0, END)
    # Return the buttons to normal
    enable_buttons()


def inverse():
    """Find the inverse of a number"""
    global value
    # Do not allow for 1/0
    if display.get() == "0":
        value = "ERROR"
    else:
        value = 1/float(display.get())
    # Change the result to an int if the result is an integer
    int_check()
    # Remove the current value of the display and replace it with the answer
    display.delete(0, END)
    display.insert(0, value)
    # If there is a decimal in the answer, disable the decimal button
    decimal_check()


def square():
    """Find the square of a number"""
    global value
    value = float(display.get()) ** 2
    # Change the result to an int if the result is an integer
    int_check()
    # Remove the current value of the display and replace it with the answer
    display.delete(0, END)
    display.insert(0, value)
    # If there is a decimal in the answer, disable the decimal button
    decimal_check()


def negate():
    """Negate a number"""
    global value
    value = float(display.get()) * -1
    # Change the result to an int if the result is an integer
    int_check()
    # Remove the current value of the display and replace it with the answer
    display.delete(0, END)
    display.insert(0, value)
    # If there is a decimal in the answer, disable the decimal button
    decimal_check()


def int_check():
    """Remove the decimal in the answer if we don't need it"""
    global value
    # Check whether the value has a zero at the end
    if str(value)[-1] == "0":
        # Change the answer to an int if it does, leave it alone if it doesn't
        value = int(value)


def decimal_check():
    """Disable decimal button if there is a decimal in the answer"""
    # Check if there is a decimal in the answer
    if "." in display.get():
        # If there is, disable the decimal button
        decimal_button.config(state=DISABLED)


def delete():
    """Delete the last character in the display"""
    # Check if the display is empty
    if display.get() == "":
        # If it is, stop the function from going further
        return
    # Check if the last character is a decimal
    elif display.get()[-1] == ".":
        # If it is, reset it to normal
        decimal_button.config(state=NORMAL)
    # Get rid of the last character
    text = display.get()[:-1]
    display.delete(0, END)
    display.insert(0, text)


# Define the layout and frames
# Frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root)
display_frame.pack(padx=2, pady=(5, 20))
button_frame.pack(padx=2, pady=5)

# Display frame layout
display = tkinter.Entry(display_frame, width=50, font=display_font, bg=display_color, borderwidth=5, justify=RIGHT)
display.pack(padx=5, pady=5)

# Button frame layout
clear_button = tkinter.Button(button_frame, text="Clear", font=button_font, command=clear)
delete_button = tkinter.Button(button_frame, text="Delete", font=button_font, command=delete)

inverse_button = tkinter.Button(button_frame, text="1/x", font=button_font, command=inverse)
square_button = tkinter.Button(button_frame, text="x^2", font=button_font, command=square)
exponent_button = tkinter.Button(button_frame, text="x^n", font=button_font, command=lambda: operate("exponent"))
divide_button = tkinter.Button(button_frame, text=" / ", font=button_font, command=lambda: operate("divide"))
multiply_button = tkinter.Button(button_frame, text="*", font=button_font, command=lambda: operate("multiply"))
subtract_button = tkinter.Button(button_frame, text="-", font=button_font, command=lambda: operate("subtract"))
add_button = tkinter.Button(button_frame, text="+", font=button_font, command=lambda: operate("add"))
equal_button = tkinter.Button(button_frame, text="=", font=button_font, command=equal)
decimal_button = tkinter.Button(button_frame, text=".", font=button_font, command=lambda: submit_number("."))
negate_button = tkinter.Button(button_frame, text="+/-", font=button_font, command=negate)

nine_button = tkinter.Button(button_frame, text="9", font=button_font, command=lambda: submit_number("9"))
eight_button = tkinter.Button(button_frame, text="8", font=button_font, command=lambda: submit_number("8"))
seven_button = tkinter.Button(button_frame, text="7", font=button_font, command=lambda: submit_number("7"))
six_button = tkinter.Button(button_frame, text="6", font=button_font, command=lambda: submit_number("6"))
five_button = tkinter.Button(button_frame, text="5", font=button_font, command=lambda: submit_number("5"))
four_button = tkinter.Button(button_frame, text="4", font=button_font, command=lambda: submit_number("4"))
three_button = tkinter.Button(button_frame, text="3", font=button_font, command=lambda: submit_number("3"))
two_button = tkinter.Button(button_frame, text="2", font=button_font, command=lambda: submit_number("2"))
one_button = tkinter.Button(button_frame, text="1", font=button_font, command=lambda: submit_number("1"))
zero_button = tkinter.Button(button_frame, text="0", font=button_font, command=lambda: submit_number("0"))

# Putting first row in window
clear_button.grid(row=0, column=0, pady=1, columnspan=2, sticky="WE")
delete_button.grid(row=0, column=2, pady=1, columnspan=2, sticky="WE")
# Putting second row in window
inverse_button.grid(row=1, column=0, pady=1, sticky="WE")
square_button.grid(row=1, column=1, pady=1, sticky="WE")
exponent_button.grid(row=1, column=2, pady=1, sticky="WE")
divide_button.grid(row=1, column=3, pady=1, sticky="WE")
# Putting third row in window (Adding padding to create the size of the columns)
seven_button.grid(row=2, column=0, pady=1, ipadx=20, sticky="WE")
eight_button.grid(row=2, column=1, pady=1, ipadx=20, sticky="WE")
nine_button.grid(row=2, column=2, pady=1, ipadx=20, sticky="WE")
multiply_button.grid(row=2, column=3, pady=1, ipadx=20, sticky="WE")
# Putting fourth row in window
four_button.grid(row=3, column=0, pady=1, sticky="WE")
five_button.grid(row=3, column=1, pady=1, sticky="WE")
six_button.grid(row=3, column=2, pady=1, sticky="WE")
subtract_button.grid(row=3, column=3, pady=1, sticky="WE")
# Putting fifth row in window
one_button.grid(row=4, column=0, pady=1, sticky="WE")
two_button.grid(row=4, column=1, pady=1, sticky="WE")
three_button.grid(row=4, column=2, pady=1, sticky="WE")
add_button.grid(row=4, column=3, pady=1, sticky="WE")
# Putting sixth row in window
negate_button.grid(row=5, column=0, pady=1, sticky="WE")
zero_button.grid(row=5, column=1, pady=1, sticky="WE")
decimal_button.grid(row=5, column=2, pady=1, sticky="WE")
equal_button.grid(row=5, column=3, pady=1, sticky="WE")

# Running mainloop
root.mainloop()
