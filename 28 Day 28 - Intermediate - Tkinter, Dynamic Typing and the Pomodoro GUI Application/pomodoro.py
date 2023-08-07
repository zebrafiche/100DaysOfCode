from tkinter import *
import math

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Timer Mechanism
# 25 5 25 5 25 5 25 20
reps = 0
check_mark = ''
timer = None

# Timer reset


def reset_timer():
    screen.after_cancel(timer)
    # change timer text
    canvas.itemconfig(timer_text, text=f'00:00')
    # change label to 'timer'
    label.config(text="Timer", fg='black')
    # reset checkmarks
    global check_mark
    check_mark = ''
    check_label.config(text=f'{check_mark}')
    # once you hit reset and start again the reps will be 2 and it will start from a break, fix that
    global reps
    reps = 0

def start_timer():
    global reps
    global check_mark
    if reps == 0 or reps == 2 or reps == 4 or reps == 6:
        count_down(10)
        # I also want the title to say work
        label.config(text="WORK", fg=RED)
    # I also want a check mark to be generated once a work session is complete
    # this check mark should be generated after every work session is complete and a break session begins
    # so when reps == 1, 3, 5, 7
    elif reps == 1 or reps == 3 or reps == 5:
        count_down(5)
        # I also want the title to say break
        label.config(text="BREAK", fg=YELLOW)
        check_mark = check_mark + '🗸'
        check_label.config(text=f'{check_mark}')
    elif reps == 7:
        count_down(20)
        # I also want the title to say break
        label.config(text="BREAK", fg='black')
        check_mark = check_mark + '🗸'
        check_label.config(text=f'{check_mark}')
    reps += 1


# Countdown Mechanism


def count_down(sec):
    timer_min = math.floor(sec / 60)
    timer_sec = sec % 60
    # if timer_sec == 0:
    #     timer_sec = '00'
    if timer_min < 10:
        timer_min = f'{0}{math.floor(sec / 60)}'
    if timer_sec < 10:
        timer_sec = f'{0}{sec % 60}'
    canvas.itemconfig(timer_text, text=f'{timer_min}:{timer_sec}')
    if sec > 0:
        global timer
        timer = screen.after(1000, count_down, sec - 1)
    # if you want to continue the timer once it completes a work cycle
    # else:
    #     start_timer()


# UI Setup

# Screen
screen = Tk()
screen.title('Pomodoro')
screen.config(bg=GREEN)

# 1. Put a timer label at the top, fg to change text color, bg to change the label background color
label = Label(text="Timer", fg='black', bg=GREEN, font=('Courier', 50, 'bold'))
label.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=690, height=362, bg=GREEN, highlightthickness=0)
tomato_png = PhotoImage(file="tomato-removebg-preview.png")
canvas.create_image(345, 181, image=tomato_png)
timer_text = canvas.create_text(345, 190, text="00:00", fill='white', font=('Courier', 35, 'bold'))
canvas.grid(column=1, row=1, padx=100, pady=50)

# 2. Put a start button, place it at the lower left side of the tomato
start_button = Button(text='Start', bg=GREEN, highlightthickness=0, font=('Courier', 20, 'bold'))
start_button.config(command=start_timer)
start_button.grid(column=0, row=2)


# 3. Put a reset button, place it at the lower right side of the tomato
reset_button = Button(text='Reset', bg=GREEN, highlightthickness=0, font=('Courier', 20, 'bold'))
reset_button.config(command=reset_timer)
reset_button.grid(column=2, row=2)

# 4. Put a checkmark below the tomato
check_label = Label(text="", fg='black', bg=GREEN, font=('Courier', 40, 'bold'))
check_label.grid(column=1, row=2)

screen.mainloop()
