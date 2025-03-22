import tkinter as tk

root = tk.Tk()


root.geometry("300x300")
root.title("My First GUI")

label = tk.Label(root, text="Hello World!", font=("Arial", 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack(padx=20, pady=10)

# myentry = tk.Entry(root)
# myentry.pack()

# button=tk.Button(root, text="Click me", font=("Arial", 12))
# button.pack(padx=10, pady=10)

buttonFrame=tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

btn1=tk.Button(buttonFrame, text="1", font=("Arial", 16))
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn2=tk.Button(buttonFrame, text="2", font=("Arial", 16))
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

btn3=tk.Button(buttonFrame, text="3", font=("Arial", 16))
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

btn4=tk.Button(buttonFrame, text="4", font=("Arial", 16))
btn4.grid(row=1, column=0, sticky=tk.W + tk.E)

btn5=tk.Button(buttonFrame, text="5", font=("Arial", 16))
btn5.grid(row=1, column=1, sticky=tk.W + tk.E)

btn6=tk.Button(buttonFrame, text="6", font=("Arial", 16))
btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

buttonFrame.pack(fill="x")


anotherbtn=tk.Button(root, text="TEST")
anotherbtn.place(x=100, y=100, width=100, height=100)


root.mainloop()