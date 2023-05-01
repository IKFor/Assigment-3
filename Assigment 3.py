import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import csv

class Duck:
    def __init__(self, id, species, category, length_cm, wingspan_cm, body_mass_g):
        self.id = int(id)
        self.species = species
        self.category = category
        self.length_cm = float(length_cm)
        self.wingspan_cm = float(wingspan_cm)
        self.body_mass_g = float(body_mass_g)

def create_graph(x_coords, y_coords, g_label = 'data'):
    fig, ax = plt.subplots()

    ax.scatter(x_coords, y_coords, label = g_label)

    ax.set_xlabel("x", loc = "right")
    ax.set_ylabel("y", loc = "top", rotation = "horizontal")
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
x_coords = [duck.length_cm for duck in duck_data]
y_coords = [(duck.body_mass_g + duck.length_cm + duck.wingspan_cm) / 3 for duck in duck_data]
print(x_coords)
print(y_coords)


window = tk.Tk()
window.geometry('370x135')
window.minsize(400, 110)
window.title('Assigment 3')

# frame = tk.Frame(window)
# frame.pack()  

# first_frame = tk.Frame(window)  
# first_frame.pack(side = 'left') 

# second_frame = tk.Frame(window)  
# second_frame.pack(side = 'left') 

tk.Grid.rowconfigure(window,0,weight=1)
tk.Grid.rowconfigure(window,1,weight=1)

graph_button = tk.Button(window, text='Create a graph', command = lambda: create_graph(x_coords, y_coords, 'duck'))
graph_button.grid(column=0, row=0, padx=10, sticky=tk.SW, pady=15)
graph_label = tk.Label(window, text='Display a bar chart of a duck\'s measurements')
graph_label.grid(column=1, row=0, sticky=tk.SW, pady=15)

graph_button = tk.Button(window, text='Create a graph', command = lambda: create_graph(x_coords, y_coords, 'duck'))
graph_button.grid(column=0, row=1, padx=10, sticky=tk.NW, pady=15)
graph_label = tk.Label(window, text='Display a scatter plot of a attribute measurements')
graph_label.grid(column=1, row=1, sticky=tk.NW, pady=15)

window.mainloop()
