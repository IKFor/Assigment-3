import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv

class Duck:
    def __init__(self, id, species, category, length_cm, wingspan_cm, body_mass_g):
        self.id = int(id)
        self.species = species
        self.category = category
        self.length_cm = float(length_cm)
        self.wingspan_cm = float(wingspan_cm)
        self.body_mass_g = float(body_mass_g)

with open("duck_data.csv", "r", newline = "") as csv_file:
    csv_reader = csv.reader(csv_file)
    duck_data = [row for row in csv_reader]

duck_data = [Duck(duck_data[i][0], duck_data[i][1], duck_data[i][2],
             duck_data[i][3], duck_data[i][4], duck_data[i][5]) for i in range(1,len(duck_data))]


def create_scatter(x_coords, y_coords, x_label = "x", y_label = "y", data_label = "data"):
    fig, ax = plt.subplots()

    ax.scatter(x_coords, y_coords, label = data_label)

    ax.set_xlabel(x_label, loc = "right", )
    ax.set_ylabel(y_label, loc = "center")
    ax.set_title("Duck graph", pad = 15)
    ax.legend(loc = "lower right")

    plt.show()

def plot_by_attribute(attribute):
    if attribute == "length_cm":
        x_coords = [duck.length_cm for duck in duck_data]
    elif attribute == "wingspan_cm":
        x_coords = [duck.wingspan_cm for duck in duck_data]
    elif attribute == "body_mass_g":
        x_coords = [duck.body_mass_g for duck in duck_data]
    else:
        messagebox.showerror("Programm Error", "This attribute does not exist")
        return

    y_coords = [(duck.body_mass_g + duck.wingspan_cm) / 2 for duck in duck_data]

    create_scatter(x_coords, y_coords, attribute, "Average of other attributes", "duck")

def bar_chart_by_id(id):
    duck = try_find_duck_by_id(id)

    if not duck: #is it good?
        messagebox.showerror("Programm Error", "Duck with this id does not exist")
        return

    attributes = [duck.length_cm, duck.wingspan_cm, duck.body_mass_g]
    attribute_names = ["length_cm", "wingspan_cm", "body_mass_g"]

    fig, ax = plt.subplots()

    ax.bar(attribute_names, attributes, width = 0.4)

    ax.set_ylabel("Measurement", loc = "center")
    ax.set_title(f"Attributes for Duck {id}: {duck.species}", pad = 15)

    plt.show()

def try_find_duck_by_id(id):
    try:
        id = int(id)
    except ValueError:
        messagebox.showerror("Programm Error", "Please input correct id")
        return None
    
    for duck in duck_data:
        if duck.id == id:
            return duck #is it a good function?
    return None

window = tk.Tk()
window.geometry("400x160")
window.minsize(395, 155)
window.maxsize(600, 300)
window.title("Assigment 3")

frame = tk.Frame(window)
frame.pack()  

#creating frame for bar chart
create_bar_frame = tk.LabelFrame(frame, text = "Display a bar chart of a duck's measurements")
create_bar_frame.grid(row = 0, column = 0, sticky = "news", padx = 10, pady = 10)

bar_label = tk.Label(create_bar_frame, text="Enter the duck's id")
bar_label.grid(row = 0, column = 0, padx = 5)

id_entry = tk.Entry(create_bar_frame)
id_entry.grid(row = 0, column = 1, padx = 10, pady = 10)

bar_button = tk.Button(create_bar_frame, text = "Create a graph", command = lambda: bar_chart_by_id(id_entry.get()))
bar_button.grid(row = 0, column = 2, padx = 5)

#creating frame for scatter
create_scatter_frame = tk.LabelFrame(frame, text = "Display a scatter plot of attribute measurements")
create_scatter_frame.grid(row = 1, column = 0, sticky = "news", padx = 10, pady = 10)

scatter_label = tk.Label(create_scatter_frame, text="Choose attribute")
scatter_label.grid(row = 0, column = 0, padx = 5)

attribute_combobox = ttk.Combobox(create_scatter_frame, values = ["length_cm", "wingspan_cm", "body_mass_g"])
attribute_combobox.grid(row = 0, column = 1, padx = 10, pady = 10)

scatter_button = tk.Button(create_scatter_frame, text="Create a graph", command = lambda: plot_by_attribute(attribute_combobox.get()))
scatter_button.grid(row = 0, column = 2, padx = 5)

window.mainloop()

#does close button work as an exit?