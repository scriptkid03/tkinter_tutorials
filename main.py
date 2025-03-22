import tkinter as tk
from tkinter import messagebox

class MyGUI:
  def __init__(self):
    # Create the main window
    self.root = tk.Tk()

    # Create the menubar
    self.menubar = tk.Menu(self.root)

    # Create File menu with close options
    self.filemenu = tk.Menu(self.menubar, tearoff=0)
    self.filemenu.add_command(label="Close", command=self.on_closing)
    self.filemenu.add_separator()
    self.filemenu.add_command(label="Close without question", command=exit)

    # Create Action menu with message and clear options
    self.actionmenu = tk.Menu(self.menubar, tearoff=0)
    self.actionmenu.add_command(label="Show Message", command=self.show_message)
    self.actionmenu.add_separator()
    self.actionmenu.add_command(label="Clear", command=self.clearbtn)

    # Add the File and Action menus to the menubar
    self.menubar.add_cascade(label="File", menu=self.filemenu)
    self.menubar.add_cascade(label="Action", menu=self.actionmenu)

    # Configure the root window to use the menubar
    self.root.config(menu=self.menubar)

    # Create and place the title label
    self.label = tk.Label(self.root, text="Your Message", font=("Arial", 16))
    self.label.pack(padx=10, pady=10)

    # Create and place the text input area
    self.textbox = tk.Text(self.root, height=5, font=("Arial", 14))
    self.textbox.bind("<KeyPress>", self.shortcut)  # Bind keyboard events
    self.textbox.pack(padx=10, pady=10)

    # Create a variable to store checkbox state
    self.check_state = tk.IntVar()

    # Create and place the checkbox to toggle message box display
    self.check = tk.Checkbutton(self.root, text="Show Message Box", font=("Arial", 14),variable=self.check_state)
    self.check.pack(padx=10, pady=10)
    
    # Create and place the button to show the message
    self.button = tk.Button(self.root, text="Show Message", font=("Aria;", 14), command=self.show_message)
    self.button.pack(padx=10, pady=10)

    # Create and place the button to clear the text input
    self.clearbtn = tk.Button(self.root, text="Clear", font=("Arial", 14), command=self.clearbtn)
    self.clearbtn.pack(padx=10, pady=10)

    # Set up protocol for window closing
    self.root.protocol("WM_DELETE_WINDOW", self.on_closing)\
    



    # Start the main event loop
    self.root.mainloop()


    
  # Display the message either in console or message box based on checkbox state
  def show_message(self):
    # print(self.check_state.get()) # Print the checkbox state
    
    # If checkbox is unchecked, print message to console
    if self.check_state.get() == 0:
      print(self.textbox.get('1.0', tk.END))
    
    # If checkbox is checked, show message in a popup box
    else:
      messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

  # Ctrl+Return triggers the show_message function
  def shortcut(self, event):
    if event.state == 4 and event.keysym == 'Return':
      self.show_message()

  # Handle keyboard shortcuts - find the key combination (key symbol and state) 
    # print(event.keysym)
    # print(event.state)

  # Handle window close event with a confirmation dialog
  def on_closing(self):
    if messagebox.askyesno(title="Quit", message="Do you want to quit?"):
      self.root.destroy()
  
  # Clear all text from the textbox
  def clearbtn(self):
    self.textbox.delete('1.0', tk.END)

MyGUI()