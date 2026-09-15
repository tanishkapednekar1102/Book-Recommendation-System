from tkinter import *
from tkinter import messagebox
import requests
from PIL import ImageTk, Image
from io import BytesIO
import urllib.parse
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # set cwd to script dir

class Request:
    def __init__(self, method, args):
        self.args = args
        self.method = method

inc = 0
poster_cache = {}    # prevent image garbage collection

def fetch_information(title, poster_url, date, rating):
    """
    Updates a single book slot (title, poster, date, rating)
    """
    global inc
    inc += 1

    # ---- Title ----
    text[f'a{inc}'].config(text=title)

    # ---- Date ----
    text2[f'a{inc}{inc}'].config(text=str(date))

    # ---- Rating ----
    text3[f'a{inc}{inc}{inc}'].config(text=str(rating))

    # ---- Poster ----
    if poster_url != "N/A":
        try:
            response = requests.get(poster_url)
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            img = img.resize((120, 170))
            img_tk = ImageTk.PhotoImage(img)

            # cache so Python does NOT delete the image
            poster_cache[f"p{inc}"] = img_tk
            image[f"b{inc}"].config(image=img_tk)

        except Exception:
            image[f"b{inc}"].config(text="No Image")
    else:
        image[f"b{inc}"].config(text="No Image")


def search():
    """
    Fetch books from Google Books API
    """
    global inc
    inc = 0

    # Reset slots
    for i in range(1, 6):
        text[f'a{i}'].config(text="Book Title")
        image[f'b{i}'].config(image='', text='')
        text2[f'a{i}{i}'].config(text="date" if check_var.get() else "")
        text3[f'a{i}{i}{i}'].config(text="rating" if check_var2.get() else "")
    
    # Hide detail frames during reset
    frame11.place_forget()
    frame22.place_forget()
    frame33.place_forget()
    frame44.place_forget()
    frame55.place_forget()

    request = Request('GET', {'search': Search.get()})

    if request.method == 'GET':
        query = urllib.parse.quote(request.args.get('search', ''))
        url = f"https://openlibrary.org/search.json?q={query}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            for item in data.get("docs", [])[:5]:  # Limit to 5 books
                title = item.get("title", "N/A")
                date = item.get("first_publish_year", "N/A")
                rating = item.get("ratings_average", "N/A")
                poster = f"https://covers.openlibrary.org/b/id/{item.get('cover_i')}-M.jpg" if item.get('cover_i') else "N/A"

                fetch_information(title, poster, date, rating)

            # Update detail frames based on current checkbox states
            toggle_details()

        else:
            messagebox.showinfo("info", "Failed to fetch data from Open Library API")


def show_menu(event):
    menu.post(event.x_root, event.y_root)


def toggle_details():
    """Toggle detail frames based on checkbox states"""
    if check_var.get() or check_var2.get():
        frame11.place(x=75, y=540)
        frame22.place(x=275, y=540)
        frame33.place(x=475, y=540)
        frame44.place(x=675, y=540)
        frame55.place(x=875, y=540)
    else:
        frame11.place_forget()
        frame22.place_forget()
        frame33.place_forget()
        frame44.place_forget()
        frame55.place_forget()

    for i in range(1, 6):
        if check_var.get():
            text2[f'a{i}{i}'].place(x=10, y=6)
        else:
            text2[f'a{i}{i}'].place_forget()

        if check_var2.get():
            text3[f'a{i}{i}{i}'].place(x=10, y=32)
        else:
            text3[f'a{i}{i}{i}'].place_forget()


# -------------------- UI START --------------------
root = Tk()
root.title("Book Recommendation System")
window_width = 1100
window_height = 820
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_x = max((screen_width - window_width) // 2, 0)
position_y = max((screen_height - window_height) // 2, 0)
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
root.update_idletasks()
root.config(bg="#111119")
root.resizable(False, False)

#ICON
icon = PhotoImage(file="Images/icon.png")
root.iconphoto(False, icon)

# BACKGROUND
heading_image = PhotoImage(file="Images/background.png")
Label(root, image=heading_image, bg="#111119").place(x=-2, y=-2)

# LOGO
logo_image = PhotoImage(file="Images/logo.png")
Label(root, image=logo_image, bg="#0099ff").place(x=300, y=80)

# HEADING
Label(root, text="BOOK RECOMMENDATION",font=("Lato", 30, "bold"), fg="white", bg="#0099ff").place(x=410, y=90)

# SEARCH BOX
search_box = PhotoImage(file="Images/Rectangle 2.png")
Label(root, image=search_box, bg="#0099ff").place(x=300, y=155)

Search = StringVar()
Entry(root, textvariable=Search, width=20,
      font=("Lato", 25), bg="white", fg="black", bd=0).place(x=415, y=172)

# SEARCH BTN
recommend_button_image = PhotoImage(file="Images/Search.png")
Button(root, image=recommend_button_image, bg="#0099ff", bd=0,
       activebackground="#252532", cursor="hand2",
       command=search).place(x=860, y=169)

# SETTINGS
Setting_image = PhotoImage(file="Images/setting.png")
setting = Button(root, image=Setting_image, bd=0, cursor="hand2",
                 activebackground="#0099ff", bg="#0099ff")
setting.place(x=1050, y=175)
setting.bind('<Button-1>', show_menu)

# MENU
menu = Menu(root, tearoff=0)
check_var = BooleanVar(value=True)
menu.add_checkbutton(label="Publish Date", variable=check_var, command=toggle_details)
check_var2 = BooleanVar(value=True)
menu.add_checkbutton(label="Rating", variable=check_var2, command=toggle_details)

# LOGOUT BTN
logout_img = PhotoImage(file="Images/logout.png")
Button(root, image=logout_img, bg="#0099ff", cursor="hand2",
       command=lambda: root.destroy()).place(x=1030, y=20)

# -------------------- BOOK FRAMES --------------------
frame1 = Frame(root, width=150, height=210, bg="white")
frame2 = Frame(root, width=150, height=210, bg="white")
frame3 = Frame(root, width=150, height=210, bg="white")
frame4 = Frame(root, width=150, height=210, bg="white")
frame5 = Frame(root, width=150, height=210, bg="white")

frame1.place(x=75, y=280)
frame2.place(x=275, y=280)
frame3.place(x=475, y=280)
frame4.place(x=675, y=280)
frame5.place(x=875, y=280)

# TITLE LABELS
text = {
    f'a{i}': Label(
        [frame1, frame2, frame3, frame4, frame5][i-1],
        font=("arial", 10), fg="green"
    )
    for i in range(1, 6)
}
for i in range(1, 6):
    text[f'a{i}'].place(x=10, y=4)

# IMAGES
image = {
    f'b{i}': Label([frame1, frame2, frame3, frame4, frame5][i-1])
    for i in range(1, 6)
}
for i in range(1, 6):
    image[f'b{i}'].place(x=3, y=30)

# -------------------- DATE & RATING FRAMES --------------------
frame11 = Frame(root, width=150, height=60, bg="white")
frame22 = Frame(root, width=150, height=60, bg="white")
frame33 = Frame(root, width=150, height=60, bg="white")
frame44 = Frame(root, width=150, height=60, bg="white")
frame55 = Frame(root, width=150, height=60, bg="white")

# DATE LABELS
text2 = {
    f'a{i}{i}': Label(
        [frame11, frame22, frame33, frame44, frame55][i-1],
        text="date", font=("arial", 10, "bold"), fg="red", bg="#e6e6e6", anchor="w"
    )
    for i in range(1, 6)
}
for i in range(1, 6):
    text2[f'a{i}{i}'].place(x=10, y=6)

# RATING LABELS
text3 = {
    f'a{i}{i}{i}': Label(
        [frame11, frame22, frame33, frame44, frame55][i-1],
        text="rating", font=("arial", 10, "bold"), fg="black", bg="#e6e6e6", anchor="w"
    )
    for i in range(1, 6)
}
for i in range(1, 6):
    text3[f'a{i}{i}{i}'].place(x=10, y=32)

# SHOW DETAIL FRAMES BY DEFAULT
toggle_details()

# -------------------- START APP --------------------
root.mainloop()
