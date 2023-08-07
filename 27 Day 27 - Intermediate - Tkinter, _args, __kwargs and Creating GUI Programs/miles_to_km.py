import tkinter

# 0. create window
# 1. text entry for miles
# 2. label - Miles
# 3. label - is equal to
# 4. label - ##
# 5. label - Km
# 6. button - calculate

# 0. create window
window = tkinter.Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=200)
window.config(pady=20, padx=20)

# 1. text entry for miles
user_input = tkinter.Entry(width=15, justify='center', font=("Courier", 10, 'bold'))
user_input.grid(column=1, row=0)

# 2. label - Miles
miles = tkinter.Label(text='Miles', font=("Courier", 10, 'bold'))
miles.grid(column=2, row=0)

# 3. label - is equal to
equals = tkinter.Label(text='is equal to', font=("Courier", 10, 'bold'))
equals.grid(column=0, row=1)

# 4. label - ##
converted_num = tkinter.Label(text=" ", font=("Courier", 10, 'bold'))
converted_num.grid(column=1, row=1)

# 5. label - Km
km = tkinter.Label(text='Km', font=("Courier", 10, 'bold'))
km.grid(column=2, row=1)

# 6. button - calculate


def button_click():
    kms = 1.609344 * float(user_input.get())
    converted_num.config(text=f"{kms}")


button = tkinter.Button(text='Convert', font=("Courier", 10, 'bold'), command=button_click)
button.grid(column=1, row=2)

window.mainloop()

