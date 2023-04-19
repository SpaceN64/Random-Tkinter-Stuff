# Imports
import customtkinter, random

# Create score_x & classify
score_x = 1

# Create Window
window = customtkinter.CTk()
window.title("Click Game")
window.geometry("500x390")
window.resizable(False, False) 

# ------ Creation of Clicks, Multipliyer ------- #
# Create Label + Score
score = 0
score_multi_number = 1

# Create Click Number
oi = customtkinter.CTkLabel(window, 
                            text=score,
                            padx=0,
                            pady=0)
oi.place(x=48,y=-5, anchor="nw")

# Create Click Label
bruv = customtkinter.CTkLabel(window, 
                              text="Clicks:",
                              padx=0,
                              pady=0)
bruv.place(x=5,y=-5, anchor="nw")

# Score Updater
def update_score():
    score=1
    oi.configure(text=score)

# Score Multiplier
score_multi = customtkinter.CTkLabel(window,
                                     text="Score Multi:")
score_multi.place(x=400,y=-5, anchor="nw")

fortnite = str(score_multi_number) + "x"

scorio = customtkinter.CTkLabel(window,
                                text=fortnite,
                                padx=0,
                                pady=0)
scorio.place(x=478,y=-5)

# Create var Argument
var = customtkinter.IntVar()

# ---------- Main'ish Code ---------- #
# Create Button
button = customtkinter.CTkButton(window, text="Click Me", command=lambda:var.set(1))
button.place(x=180,y=180)

button.wait_variable(var)

update_score()

# Move Button Randomly
x = random.randint(5,355)
y = random.randint(20,355)
button.place(x=x,y=y)
var.set(0)

# Info Number
number_info = 0

# ---------- Main Code ---------- #
def main():
    while True:
        # Global Variables
        global score
        global score_x
        global score_multi_number
        global number_info

        # Update Score
        score=score+score_x
        oi.configure(text=score)

        # Multiplier Updater + Upgrader
        if score == 10:
            score_x = score_x + 1
            score_multi_number = score_multi_number + 1
            scorio.configure(text=(str(score_multi_number) + "x"))
        elif score == 50:
            score_x = score_x + 1
            score_multi_number = score_multi_number + 1
            scorio.configure(text=(str(score_multi_number) + "x"))
        elif score == 74:
            score_x = score_x + 1
            score_multi_number = score_multi_number + 1
            scorio.configure(text=(str(score_multi_number) + "x"))
        elif score == 102:
            score_x = score_x + 1
            score_multi_number = score_multi_number + 1
            scorio.configure(text=(str(score_multi_number) + "x"))
        elif score == 202:
            score_x = score_x + 1
            score_multi_number = score_multi_number + 1
            scorio.configure(text=(str(score_multi_number) + "x"))
        elif score == 304:
            score_x = score_x + 1
            score_multi_number = score_multi_number + 1
            scorio.configure(text=(str(score_multi_number) + "x"))

        # Prints Button Position + More
        number_info = number_info + 1
        print("------------------------------")
        print('Info #' + str(number_info) + ':')
        print("")
        print("Button Position: X=" + str(button.winfo_x()) + " Y=" + str(button.winfo_y()))
        print("Score: " + str(score) + " Score Multiplier: " + str(score_multi_number) + "x")

        # Wait for press
        button.wait_variable(var)
        
        # Move Button
        x = random.randint(5,355)
        y = random.randint(20,355)
        button.place(x=x,y=y)
        var.set(0)

# Start Main Code
main()

# Window Refresh
window.mainloop()
