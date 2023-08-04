import tkinter as tk

def show_small_window():
    # Create the main window
    window = tk.Tk()
    window.title("Small Window")
    
    # Set the window size
    window_width = 500
    window_height = 500
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # Create a label inside the window
    label = tk.Label(window, text="Hello, this is a small window!", padx=10, pady=10)
    label.pack()
    
    # Create a button inside the window
    button = tk.Button(window, text="Click Me!", command=open_another_window)
    button.pack()
    
    # Run the main event loop
    window.mainloop()
def on_button_click():
    print("Button clicked!")
def open_another_window():
    # Create a new window
    another_window = tk.Toplevel()
    another_window.title("Another Window")
    
    # Set the window size
    window_width = 300
    window_height = 200
    screen_width = another_window.winfo_screenwidth()
    screen_height = another_window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    another_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # Create a label inside the new window
    label = tk.Label(another_window, text="Nam",)
    label.grid(padx=100, pady=5)  

    # Create an Entry widget inside the new window and position it using grid()
    Name = tk.Entry(another_window)
    Name.grid( padx=100, pady=10)


    # Create a button inside the window
    button = tk.Button(another_window, text="add", command=on_button_click)
    button.grid( pady=15, padx=100)

    

if __name__ == "__main__":
    show_small_window()


