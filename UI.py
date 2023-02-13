import tkinter as tk

root = tk.Tk()
root.geometry("800x450")

Stats = tk.Label(root, text="Stats", bg="blue")
Stats.place(x=0, y=0, width=200, height=400)
Title = tk.Label(root, text="Title", bg="green")
Title.place(x=200, y=0, width=600, height=100)
Graph = tk.Label(root, text="Range", bg="yellow")
Graph.place(x=200, y=100, width=600, height=50)
Range = tk.Label(root, text="Graph", bg="pink")
Range.place(x=200, y=150, width=600, height=250)
Dock = tk.Label(root, text="Dock", bg="red")
Dock.place(x=0, y=400, width=800, height=50)



root.mainloop()