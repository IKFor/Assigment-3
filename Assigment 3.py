import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import csv

class Duck:
    def __init__(self, id, species, category, length_cm, wingspan_cm, body_mass_g):
        self.id = int(id)
        self.species = species
        self.category = category
        self.length_cm = float(length_cm)
        self.wingspan_cm = float(wingspan_cm)
        self.body_mass_g = float(body_mass_g)

def create_plot(x_coords, y_coords, x_label = "x", y_label = "y", data_label = "data"):
    fig, ax = plt.subplots()

    ax.scatter(x_coords, y_coords, label = data_label)
    #ax. (create another graph)

    ax.set_xlabel(x_label, loc = "right", )
    ax.set_ylabel(y_label, loc = "center")
    ax.set_title("Duck graph", pad = 15)
    ax.legend(loc = "lower right")

    plt.show()

with open("duck_data.csv", "r", newline = "") as csv_file:
    csv_reader = csv.reader(csv_file)
    duck_data = [row for row in csv_reader]

duck_data = [Duck(duck_data[i][0], duck_data[i][1], duck_data[i][2],
             duck_data[i][3], duck_data[i][4], duck_data[i][5]) for i in range(1,len(duck_data))]

# x_coords = [i for i in range(len(duck_data))]
# y_coords = [duck.body_mass_g for duck in duck_data]

#length_cm
def plot_by_attribute(attribute):
    if attribute == "length_cm":
        x_coords = [duck.length_cm for duck in duck_data]
    elif attribute == "wingspan_cm":
        x_coords = [duck.wingspan_cm for duck in duck_data]
    elif attribute == "body_mass_g":
        x_coords = [duck.body_mass_g for duck in duck_data]
    else:
        raise NameError("this attribute does not exist")

    y_coords = [(duck.body_mass_g + duck.wingspan_cm) / 2 for duck in duck_data]

    create_plot(x_coords, y_coords, attribute, "Average of other attributes", "duck")
    


window = tk.Tk()
#window.geometry("370x135")
#window.minsize(400, 110)
window.title("Assigment 3")

# frame = tk.Frame(window)
# frame.pack()  

# first_frame = tk.Frame(window)  
# first_frame.pack(side = "left") 

# second_frame = tk.Frame(window)  
# second_frame.pack(side = "left") 

# tk.Grid.rowconfigure(window,0,weight=1)
# tk.Grid.rowconfigure(window,1,weight=1)

# graph_button = tk.Button(window, text="Create a graph", command = lambda: plot_by_attribute("length_cm"))
# graph_button.grid(column=0, row=0, padx=10, sticky=tk.SW, pady=15)
# graph_label = tk.Label(window, text="Display a bar chart of a duck\'s measurements")
# graph_label.grid(column=1, row=0, sticky=tk.SW, pady=15)

# graph_button = tk.Button(window, text="Create a graph", command = lambda: plot_by_attribute("length_cm"))
# graph_button.grid(column=0, row=1, padx=10, sticky=tk.NW, pady=15)
# graph_label = tk.Label(window, text="Display a scatter plot of a attribute measurements")
# graph_label.grid(column=1, row=1, sticky=tk.NW, pady=15)

frame = tk.Frame(window)
frame.pack()  

create_bar_frame = tk.LabelFrame(frame, text='Display a bar chart of a duck\'s measurements')
create_bar_frame.grid(row = 0, column = 0, sticky = "news", padx = 10, pady = 10)

bar_label = tk.Label(create_bar_frame, text="Enter the duck's id")
bar_label.grid(row = 0, column = 0, padx = 5)

id_entry = tk.Entry(create_bar_frame)
id_entry.grid(row = 0, column = 1, padx = 10, pady = 10)

bar_button = tk.Button(create_bar_frame, text="Create a graph", command = lambda: plot_by_attribute("length_cm"))
bar_button.grid(row = 0, column = 2, padx = 5)


create_scatter_frame = tk.LabelFrame(frame, text='Display a scatter plot of attribute measurements')
create_scatter_frame.grid(row = 1, column = 0, sticky = "news", padx = 10, pady = 10)

scatter_label = tk.Label(create_scatter_frame, text="Choose attribute")
scatter_label.grid(row = 0, column = 0, padx = 5)

attribute_combobox = ttk.Combobox(create_scatter_frame, values = ["length_cm", "wingspan_cm", "body_mass_g"])
attribute_combobox.grid(row = 0, column = 1, padx = 10, pady = 10)

scatter_button = tk.Button(create_scatter_frame, text="Create a graph", command = lambda: plot_by_attribute(attribute_combobox.get()))
scatter_button.grid(row = 0, column = 2, padx = 5)

window.mainloop()
