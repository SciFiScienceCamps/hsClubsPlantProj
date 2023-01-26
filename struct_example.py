"""
Machine Construction Example
Author: Samuel Risling
Date: 26/1/23
"""
import tkinter as tk

track = "no bear"

def clear_frames():
    for label in labels:
        label["background"] = "white"
    for button in buttons:
        button.configure(bg = "white")

def wait():
    clear_frames()
    global track
    if(track == "bear seen"):
        track = "eaten"
        lbl_is_eaten.configure(bg="green")
    else:
        track = "no bear"
        btn_see_bear.configure(bg = "Yellow")
        lbl_no_bear.configure(bg="green")

def see_bear():
    global track
    if(track == "no bear"):
        clear_frames()
        track = "bear seen"
        btn_run.configure(bg = "yellow")
        btn_wait.configure(bg = "yellow")
        lbl_is_bear.configure(bg = "green")

def run_away():
    global track
    if(track == "bear seen"):
        clear_frames()
        track = "running"
        btn_run.configure(bg = "yellow")
        btn_stop.configure(bg = "yellow")
        lbl_is_run.configure(bg = "green")

def stop_run():
    global track
    if(track == "running"):
        clear_frames()
        btn_run.configure(bg = "yellow")
        btn_wait.configure(bg = "yellow")
        lbl_no_bear.configure(bg = "green")
        track = "no bear"



states = ["intro","no_bear","is_bear","run","eaten"]
active_state = states[0]

window = tk.Tk()

window.rowconfigure([0,1], minsize=50, weight=1)
window.columnconfigure(0, minsize=50, weight=1)
lbl_title = tk.Label(text = "State Machine GUI Demo")


frm_state_grid = tk.Frame(
    master=window
)
frm_state_grid.grid(row=0, column = 0)

for i in range(3):
    frm_state_grid.columnconfigure(i, weight=4, minsize=75)
    frm_state_grid.rowconfigure(i, weight=4,minsize=50)

frm_intro_state = tk.Frame(
    master = frm_state_grid
)

frm_is_bear = tk.Frame(
    master = frm_state_grid
)

frm_no_bear = tk.Frame(
    master = frm_state_grid
)

frm_is_run = tk.Frame(
    master=frm_state_grid
)

frm_is_eaten = tk.Frame(
    master=frm_state_grid
)

frm_intro_state.grid(row=0,column=0,padx=10,pady=10)
frm_no_bear.grid(row = 1, column = 0,padx = 10, pady = 10)
frm_is_bear.grid(row = 1,column = 1, padx=10, pady=10)
frm_is_run.grid(row=2,column=0,padx=10,pady=10)
frm_is_eaten.grid(row=2,column=1,padx=10,pady=10)

frm_buttons = tk.Frame(
    master=window
)

frm_buttons.grid(row = 1, column = 0)
for i in range(3):
    frm_buttons.columnconfigure(i, weight=1, minsize=75)
    frm_buttons.rowconfigure(i, weight=1,minsize=50)


lbl_intro = tk.Label(
    master = frm_intro_state,
    text = "Startup"
)

lbl_no_bear = tk.Label(
    master = frm_no_bear,
    text = "No bears here"
)

lbl_is_bear = tk.Label(
    master=frm_is_bear,
    text="There is now a bear here"
)

lbl_is_run = tk.Label(
    master=frm_is_run,
    text="I'm running away!"
)

lbl_is_eaten = tk.Label(
    master=frm_is_eaten,
    text="*chomp* *chomp*"
)


lbl_intro.configure(bg = "green")

btn_run = tk.Button(master=frm_buttons,command=run_away,text = "run")
btn_stop = tk.Button(master=frm_buttons,command=stop_run, text = "stop running")
btn_wait = tk.Button(master=frm_buttons,command=wait, text = "wait")
btn_see_bear = tk.Button(master=frm_buttons,command=see_bear, text = "see a bear")

labels = [lbl_intro,lbl_no_bear,lbl_is_bear,lbl_is_run,lbl_is_eaten]
frames = [frm_intro_state,frm_is_bear,frm_is_eaten,frm_no_bear]
buttons = [btn_run,btn_stop,btn_see_bear,btn_wait]

clear_frames()

for i in range(4):
    for j in range(2):
        labels[i+j].grid(row = i + 1, column=j)

for i in range(2):
    for j in range(2):
        buttons[i+j].grid(row = i, column=j/i)



##frm_state_grid.pack()
##frm_buttons.pack()
window.mainloop()