from canvas import *
from helpers import *


def render_entry():
    reg_button = Button(
        root,
        text="Register",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=20,
        height=3,
        command=register
    )
    log_button = Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=20,
        height=3,
        command=login
    )

    frame.create_window(350, 260, window=reg_button)
    frame.create_window(350, 320, window=log_button)


def register():
    clean_screen()
    frame.create_text(80, 50, text="First name:")
    frame.create_text(80, 100, text="Last name:")
    frame.create_text(80, 150, text="Username:")
    frame.create_text(80, 200, text="Password:")

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    reg_button = Button(
        root,
        text="Register",
        bg="blue",
        fg="white",
        bd=2,
        width=20,
        height=1,
        command=register
    )

    frame.create_window(200, 250, window=reg_button)


def login():
    clean_screen()
    frame.create_text(80, 100, text="Username:")
    frame.create_text(80, 150, text="Password:")

    frame.create_window(200, 100, window=username_box)
    frame.create_window(200, 150, window=password_box)

    log_button = Button(
        root,
        text="Login",
        bg="blue",  # background
        fg="white",  # foreground
        bd=2,
        width=20,
        height=1,
        command=login
    )

    frame.create_window(200, 200, window=log_button)


first_name_box = Entry(root, width=20, font="Arial 10", bd=2)
last_name_box = Entry(root, width=20, font="Arial 10", bd=2)
username_box = Entry(root, width=20, font="Arial 10", bd=2)
password_box = Entry(root, width=20, font="Arial 10", bd=2)
