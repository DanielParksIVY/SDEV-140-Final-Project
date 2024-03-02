import tkinter as tk

def open_results_page(selected_options):
    results_window = tk.Toplevel(root)
    results_window.title("Results Page")
    results_window.geometry("400x300")  # Set the size to 400x300 pixels

    # Define the numeric values for each option
    option_values = {
        "Option 1": 5,
        "Option 2": 10,
        "Option 3": 15
    }

    # Calculate the sum of selected values
    total_sum = sum(option_values[option] for option in selected_options)

    result_text = f"Selected Options and Values:\n"
    for option in selected_options:
        result_text += f"- {option} ({option_values[option]})\n"

    result_text += f"\nTotal Sum: {total_sum}"

    tk.Label(results_window, text=result_text).pack()

def open_selection_page():
    selection_window = tk.Toplevel(root)
    selection_window.title("Selection Page")
    selection_window.geometry("500x400")  # Set the size to 500x400 pixels

    selected_options = []

    def submit_selection():
        open_results_page(selected_options)
        selection_window.destroy()

    # Define the numeric values for each option
    option_values = {
        "Option 1": 5,
        "Option 2": 10,
        "Option 3": 15
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

def open_text_entry_page():
    text_entry_window = tk.Toplevel(root)
    text_entry_window.title("Text Entry Page")
    text_entry_window.geometry("500x400")  # Set the size to 500x400 pixels

    with open("text.txt", "w") as file:
        file.write("")

    tk.Label(text_entry_window, text="Welcome to the Text Entry Page").pack()

    # Add text entry widget
    entry_var = tk.StringVar()
    tk.Entry(text_entry_window, textvariable=entry_var).pack()

    # Function to write entered text into a file
    def write_to_file():
        entered_text = entry_var.get()
        with open("text.txt", "a") as file:
            file.write(entered_text + "\n")
        try:
            with open("text.txt", "r") as file:
                content = file.read()
            count = content.lower().count("chocolate")
            tk.Label(text_entry_window, text=f"Number of times 'chocolate' entered: {count}").pack()
        except FileNotFoundError:
            tk.Label(text_entry_window, text="File 'text.txt' not found.").pack()

    # Button to write text to a file
    write_button = tk.Button(text_entry_window, text="Submit", command=write_to_file)
    write_button.pack()

# Create the main window
root = tk.Tk()
root.title("Main Page")
root.geometry("500x400")  # Set the size to 500x400 pixels

# Button to open the Selection Page
selection_button = tk.Button(root, text="Go to Selection Page", command=open_selection_page)
selection_button.pack()

# Button to open the Text Entry Page
text_entry_button = tk.Button(root, text="Go to Text Entry Page", command=open_text_entry_page)
text_entry_button.pack()

# Run the Tkinter event loop
root.mainloop()
