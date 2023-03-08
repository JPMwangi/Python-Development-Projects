from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(my_timer)
    timer_label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
    canvas.itemconfig(timer_text, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
    check_marks.config(fg=GREEN, bg=YELLOW, highlightthickness=0)
    global reps
    reps = 0
# ----------------------------(step 3) TIMER MECHANISM ------------------------------- # 
def start_timer():
    """ This function calls the timer function so that it can start its count down """
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text='Work', fg=GREEN)
        

# ----------------------------(step2) COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    """This is the count down mechanism.
    Args:
        count ([int]): [time in seconds]
    """
    
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec =  count % 60
    if count_sec == 0:
        count_sec = '00'
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark, font=(FONT_NAME, 30, 'normal'))

    
# ----------------------------(step1) UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW) 


# timer label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
timer_label.grid(row=0, column=1)

tomato_image = PhotoImage(file="pomodoro-start/tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 132, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)


# start button
start_button = Button(text='Start', font=(FONT_NAME, 10, 'normal'),  highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

# reset button
reset_button = Button(text='Reset', font=(FONT_NAME, 10, 'normal'),  highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# tick label
# check_marks
check_marks = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
check_marks.grid(row=3, column=1)

window.mainloop()