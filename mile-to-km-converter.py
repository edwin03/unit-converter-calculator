import tkinter

# Calculate function
def calculate():
    miles1 = miles.get()
    km = float(miles1) * 1.609
    lable4.config(text=f"{km}")

# Creating window
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Is equal to lable
lable = tkinter.Label(text="is equal to")
lable.grid(column=0, row=1)

# Input field
miles = tkinter.Entry(width=7)
miles.grid(column=1, row=0)

# Convert button
bttn = tkinter.Button(text="Calculate", command=calculate)
bttn.grid(column=1, row=3)

# Additional lablels
lable2 = tkinter.Label(text="Miles")
lable2.grid(column=2, row=0)

lable3 = tkinter.Label(text="Km")
lable3.grid(column=2, row=1)

lable4 = tkinter.Label(text=0)
lable4.grid(column=1, row=1)

# Keep the window presistent
window.mainloop()