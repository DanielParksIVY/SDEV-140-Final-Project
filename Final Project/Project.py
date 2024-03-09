import tkinter as tk
from tkinter import Frame
from PIL import ImageTk,Image

def exit_program():
    root.destroy()

def display_image(image_path):
    global image_label  # Declare image_label as a global variable
    image = Image.open(image_path)
    image = ImageTk.PhotoImage(image)
    image_label = tk.Label(results_window, image=image)
    image_label.image = image
    image_label.pack()

def Selection_results(selected_options):
    global results_window  # Declare results_window as a global variable
    results_window = tk.Toplevel()
    results_window.title("Results Page")
    results_window.geometry("1000x500")

    # Define the numeric values for each option
    option_values = {
        "Fruits/Vegetables": -8,
        "Protien": -4,
        "Added Salt": 5,
        "Sugary": 10,
        "Fatty": 15,
    }
    # Calculate the sum of selected values
    total_sum = sum(option_values[option] for option in selected_options)

    if total_sum <= -12:
        result_text = "Nice and Healthy"
    elif total_sum <= -1:
        result_text = "Perfectly fine to eat"
    elif total_sum == 0:
        result_text = "You gotta enter SOMEthing."
    elif total_sum <= 5:
        result_text = "A little never hurt anyone, right?"
    elif total_sum <= 10:
        result_text = "Just this one time. No more after."
    elif total_sum <= 15:
        result_text = "Just this one time. No more after."
    elif total_sum <= 20:
        result_text = "I'd watch it if I were you. It's not good to eat stuff like this regularly."
    elif total_sum <= 29:
        result_text = "You really should NOT eat that."
    elif total_sum == 30:
        result_text = ""
        display_image("max.jpg")

    tk.Label(results_window, text=result_text).pack()

    # Exit button to close the program
    exit_button = tk.Button(results_window, text="Exit", command=exit_program)
    exit_button.pack()

def open_selection_page():
    selection_window = tk.Toplevel()
    selection_window.title("Selection Page")
    selection_window.geometry("1000x500")
    tk.Label(selection_window, text="Select optins to describe what you are about to eat:").pack()

    selected_options = []

    def submit_selection():
        Selection_results(selected_options)
        selection_window.destroy()

    # Define the numeric values for each option
    option_values = {
        "Fruits/Vegetables": -8,
        "Protien": -4,
        "Added Salt": 5,
        "Sugary": 10,
        "Fatty": 15,
    }

    # Add selectable options using Checkbuttons
    option_vars = {option: tk.BooleanVar() for option in option_values}

    for option, var in option_vars.items():
        tk.Checkbutton(selection_window, text=option, variable=var).pack()

    # Function to update the selected options list
    def update_selection():
        selected_options.clear()
        for option, var in option_vars.items():
            if var.get():
                selected_options.append(option)

    # Button to submit selections
    submit_button = tk.Button(selection_window, text="Submit", command=submit_selection)
    submit_button.pack()

    # Update the selection list when the submit button is clicked
    submit_button.config(command=lambda: [update_selection(), submit_selection()])

def Text_Results(count_value):
    global results_window  # Declare results_window as a global variable
    results_window = tk.Toplevel()
    results_window.title("Results Page")
    results_window.geometry("1000x500")
    if count_value <= 0:
        text = ""
        display_image("Good.jpg")
    elif count_value <= 1:
        text = "You're fine."
    elif count_value <= 2:
        text = "Go a head."
    elif count_value <= 3:
        text = "Maybe you shouldn't."
    elif count_value <= 4:
        text = "I wouldn't if I were you."
    elif count_value <= 5:
        text = "You really should NOT eat that."
    elif count_value <= 6:
        text = "ABSOULUTELY NOT!"
    else:
        text = "Do you have a death wish?"
            
    tk.Label(results_window, text=text).pack()

    exit_button = tk.Button(results_window, text="Exit", command=exit_program)
    exit_button.pack()

def open_text_entry_page():
    text_entry_window = tk.Toplevel()
    text_entry_window.title("Text Entry Page")
    text_entry_window.geometry("1000x500")

    with open("text.txt", "w") as file:
        file.write("")

    tk.Label(text_entry_window, text="Describe what you are about to eat:").pack()

    # Add text entry widget with increased height
    entry_var = tk.StringVar()
    entry = tk.Text(text_entry_window, height=10, width=50)  # Adjust height and width as needed
    entry.pack()

    # Counter variable
    count = tk.IntVar()

    # Function to write entered text into a file
    def write_to_file():
        entered_text = entry.get("1.0", "end-1c")  # Retrieve text from the Text widget
        with open("text.txt", "a") as file:
            file.write(entered_text + "\n")
        try:
            with open("text.txt", "r") as file:
                content = file.read()
            substrings = ["candy", "soda", "chips", "donuts", "ice cream", "cookies", "cake", "pizza", "burgers", "fries", "hot dogs", "nachos", "fried chicken", "milkshakes", "sugary cereals", "chocolate bars", "pastries", "deep-fried Twinkies", "macaroni and cheese", "mozzarella sticks", "bacon-wrapped anything", "onion rings", "loaded nachos", "energy drinks", "sugary cocktails", "fried Oreos", "creamy dips", "processed cheese", "cotton candy", "greasy", "sugary", "fried", "processed", "fatty" ,"high-calorie", "artificial", "trans-fat", "over-processed", "salty", "deep-fried", "empty-calorie", "high-sodium", "refined", "additive-laden", "excessive-carb", "preservative-heavy", "sugary", "high-fat", "syrupy", "trans-fatty", "ultra-processed", "saturated", "empty-nutrient", "sweetened", "overindulgent", "high-cholesterol"]
            count_value = sum(content.lower().count(substring) for substring in substrings)
            count.set(count_value)
            # Use the count value to determine which phrase to print
            Text_Results(count_value)
            text_entry_window.destroy()
        except FileNotFoundError:
            tk.Label(text_entry_window, text="File 'text.txt' not found.").pack()

    # Button to write text to a file
    write_button = tk.Button(text_entry_window, text="Submit", command=write_to_file)
    write_button.pack()

def main_window():
    # Create the main window
    global root
    root = tk.Tk()
    root.title("Main Page")
    root.geometry("1000x500")

    # Button to open the Selection Page
    selection_button = tk.Button(root, text="Go to Selection Page", command=open_selection_page)
    selection_button.pack()

    # Button to open the Text Entry Page
    text_entry_button = tk.Button(root, text="Go to Text Entry Page", command=open_text_entry_page)
    text_entry_button.pack()

    # Run the Tkinter event loop
    root.mainloop()

main_window()
