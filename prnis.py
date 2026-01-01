import tkinter
from tkinter import messagebox

USERS= {
    "admin":"admin",
    "user1":"12345",
}



window = tkinter.Tk()
window.title("login form")
window.geometry('800x450')
window.configure(bg="#6D8196")

# Create a frame to hold all widgets
frame = tkinter.Frame(window, bg="#6D8196")
frame.grid(row=0, column=0, sticky="nsew")

# Configure window grid weights to center the frame
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Configure frame grid weights to center widgets
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=0)
frame.grid_rowconfigure(2, weight=0)
frame.grid_rowconfigure(3, weight=0)
frame.grid_rowconfigure(4, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)

login_label = tkinter.Label(frame, text="SPQR", bg="#6D8196", fg="#ffffff", font=("cinzel", 30,))
username_label = tkinter.Label(frame, text="username", bg="#6D8196", fg="#ffffff", font=("arial", 10))
username_entry = tkinter.Entry(frame, width=35, font=("arial", 11), fg="#474747")
username_entry.insert(0, "username")
def user_in(e):
    if username_entry.get() == "username":
        username_entry.delete(0, tkinter.END)
        username_entry.config(fg="#000000")

def user_out(e):
    if username_entry.get() == "":
        username_entry.insert(0, "username")
        username_entry.config(fg="#474747")

username_entry.bind("<FocusIn>", user_in)
username_entry.bind("<FocusOut>", user_out)


password_entry = tkinter.Entry(frame, fg="#8e9ead", width=35, font=("arial", 11))
password_entry.insert(0, "password")
def pw_in(e):
    if password_entry.get() == "password":
        password_entry.delete(0, tkinter.END)
        password_entry.config(fg="#8e9ead", show="*")

def pw_out(e):
    if password_entry.get() == "":
        password_entry.insert(0, "password")
        password_entry.config(fg="#474747", show="")

password_entry.bind("<FocusIn>", pw_in)
password_entry.bind("<FocusOut>", pw_out)

# Login action: read entries, treat placeholders as empty, and show a messagebox
def login(self):
    print("login button clicked")
    self.username = username_entry.get().strip()
    self.password = password_entry.get().strip()

    if self.username == "" or self.username.lower() == "username":
        self.username = ""
    if self.password == "" or self.password.lower() == "password":
        self.password = ""
    if not self.username or not self.password:
             messagebox.showwarning("Login Failed", "Please enter both username and password." )
    return

    if username not in USERS or USERS[username] != password:
             messagebox.showerror("access denied", "invalid login credentials.") 
    return
    
notice = (
"System use notification \n\n"
 " users of this system are adviced they are accessing a restricted infomation system"
        "governed by applicable angency policies. unauthorized use of this system is prohibited and may be subject to criminal and civil penalties."
        "unauthorized users will be subject to monitoring, recording, and auditing."
        "all activities on this system are monitored and recorded. "
        "by continuing to use this system, you acknowledge awareness of and consent to these terms and conditions of use."




    )
show_notice(username, notice)
# If we reach here, login is successful

def show_notice(username, notice_text):
    dlg = tkinter.Toplevel(window)
    dlg.title("System Use Notification")
    dlg.transient(window)
    dlg.grab_set()
    dlg.resizable(False, False)

    # extra shit. probs gotta del
    label = tkinter.Label(dlg, text=notice_text, wraplength=500)
    label.pack(padx=20, pady=20)

    # use standard window decorations (default title bar)

    text_frame = tkinter.Frame(dlg)
    text_frame.pack(padx=10, pady=10, fill="both", expand=True)
    scrollbar = tkinter.Scrollbar(text_frame)
    scrollbar.pack(side="right", fill="y")
    txt = tkinter.Text(text_frame, wrap="word", width=60, height=10, yscrollcommand=scrollbar.set)
    txt.insert("1.0", notice_text)
    txt.config(state="disabled")
    txt.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=txt.yview)

    btn_frame = tkinter.Frame(dlg)
    btn_frame.pack(pady=(0,10))

    def accept():
        messagebox.showinfo("Login", f"Logged in as: {username}")
        dlg.destroy()

    def decline():
        dlg.destroy()
        window.destroy()

    accept_btn = tkinter.Button(btn_frame, text="Accept and continue", command=accept, width=17, bg="#4F5AFF", fg="#ffffff")
    decline_btn = tkinter.Button(btn_frame, text="Decline and Exit", command=decline, width=17, bg="#4f5aff", fg="#ffffff")
    accept_btn.pack(side="left", padx=5)
    decline_btn.pack(side="left", padx=5)

    # Ensure sizes/positions are up-to-date
    window.update_idletasks()
    dlg.update_idletasks()

    # Determine dialog size (use requested sizes as fallback)
    dlg_w = dlg.winfo_width()
    dlg_h = dlg.winfo_height()
    if dlg_w <= 1:
        dlg_w = dlg.winfo_reqwidth()
    if dlg_h <= 1:
        dlg_h = dlg.winfo_reqheight()

    # Determine main window position/size (ensure mapped)
    win_x = window.winfo_rootx()
    win_y = window.winfo_rooty()
    win_w = window.winfo_width()
    win_h = window.winfo_height()
    if win_w <= 1 or win_h <= 1:
        window.update()
        win_x = window.winfo_rootx()
        win_y = window.winfo_rooty()
        win_w = window.winfo_width() or window.winfo_reqwidth()
        win_h = window.winfo_height() or window.winfo_reqheight()

    # If main window position/size still looks invalid, fallback to screen center
    if win_w <= 1 or win_h <= 1:
        screen_w = window.winfo_screenwidth()
        screen_h = window.winfo_screenheight()
        x = max(0, (screen_w - dlg_w) // 2)
        y = max(0, (screen_h - dlg_h) // 2)
    else:
        x = win_x + max(0, (win_w - dlg_w) // 2)
        y = win_y + max(0, (win_h - dlg_h) // 2)

    dlg.geometry(f"+{x}+{y}")
    dlg.lift()
    dlg.attributes("-topmost", True)
    dlg.attributes("-topmost", False)
    dlg.wait_window()

login_button = tkinter.Button(frame, text="login", bg="#818181", fg="#d6d6d6", font=("google sans", 10), width=12, padx=3, pady=2, command=login, cursor="hand2")

login_label.grid(row=1, column=0, columnspan=3, sticky="news")
username_label.grid(row=2, column=1)
username_entry.grid(row=2, column=1, ipady=2, ipadx=5, pady=10)
password_entry.grid(row=3, column=1, ipady=2, ipadx=5, pady=10)
login_button.grid(row=4, column=0, columnspan=3, ipady=0, ipadx=5, pady=0)



window.mainloop()
