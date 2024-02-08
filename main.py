import tkinter, random

dice_dots = [
    '\u2680',
    '\u2681',
    '\u2682',
    '\u2683',
    '\u2684',
    '\u2685'
]

root = tkinter.Tk()
root.geometry('1000x600')
root.title('Max\'s Roll the Dice')

tkinter.Label(root, text="", pady=10).pack()

tkinter.Label(
    root,
    text="Please Roll The Dice!",
    fg = "blue",
    font = "Helvetica 16 bold italic",
    pady=0
).pack()

dice_img_label = tkinter.Label(
    root,
    text=dice_dots[len(dice_dots) - 1],
    font=('times', 250),
)
dice_img_label.pack()

label1 = tkinter.Label(root)
label1.pack(expand=True)

MAX_ROLLS = 25
MS_PER_INTERVAL = 50

img_label = tkinter.Label(
    root,
    fg = "blue",
    font = "Helvetica 16 bold italic"
)
img_label.pack()
label_clear_action = ''

def random_img(counter, final_choice):
    if counter >= MAX_ROLLS:
        dice_img_label.configure(text=dice_dots[final_choice])

        img_label.configure(text=f"You rolled a {final_choice + 1}")
        img_label.pack()
        
        button["state"] = 'normal'
        global label_clear_action
        label_clear_action = img_label.after(10000, lambda: img_label.configure(text=''))
        return

    dice_img_label.configure(text=random.choice(dice_dots))

    root.after(MS_PER_INTERVAL, random_img, counter + 1, final_choice)

def rolling_dice():
    if label_clear_action:
        root.after_cancel(label_clear_action)

    img_label.configure(text='')
    button["state"] = 'disabled'
    counter = 0
    final_choice = random.choice(range(0, len(dice_dots)))
    root.after(MS_PER_INTERVAL, random_img, counter, final_choice)

button = tkinter.Button(
    root,
    text='Roll the Dice',
    fg='blue',
    font=15,
    bg="aqua",
    command=rolling_dice,
    anchor='n'
)
button.pack(expand=True)

root.mainloop()