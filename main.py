import tkinter

#Window
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
#my_label.pack()
my_label.grid(column=0, row=0)
my_label["text"] = "New text"
my_label.config(text="New text2")

#Button
def button_clicked():
    my_label["text"] = input.get()
    print("I got clicked!")

button = tkinter.Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=2)

button2 = tkinter.Button(text="New button", command=button_clicked)
button2.grid(column=2, row=0)

#Entry
input = tkinter.Entry()
input.config(width=10)
#input.pack()
input.grid(column=4, row=3)

window.mainloop()
