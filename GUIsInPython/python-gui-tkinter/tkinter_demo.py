from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox



#function to handle login

def handle_login():
    email = email_input.get()
    password = password_input.get()
    print(email, password)

    if email=='visyuvi@gmail.com' and password=='1234':
        messagebox.showinfo('Yay!', 'Login successful')
    else:
        messagebox.showerror('Error!', 'Login Failed!')


root = Tk()

root.title('Login Form')

# root.iconbitmap("favicon.ico")

# root.minsize(400,400)
root.geometry('350x500')
root.configure(background='blue')

img = Image.open('wallpapers/flipkart-logo.png')

resized_img = img.resize((100, 100))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root, image=img)
img_label.pack(pady=(10, 10))

text_label = Label(root, text='Flipkart', fg='white', bg='blue')
text_label.pack()
text_label.config(font=('verdana', 24))

# email input
email_label = Label(root, text="Enter email", fg='white', bg='blue')
email_label.pack(pady=(20, 5))
email_label.config(font=('verdana', 12))

email_input = Entry(root, width=40)
email_input.pack(ipady=6, pady=(1, 15))

# password input

password_label = Label(root, text="Enter password", fg='white', bg='blue')
password_label.pack(pady=(1, 5))
password_label.config(font=('verdana', 12))

password_input = Entry(root, width=40)
password_input.pack(ipady=6, pady=(1, 15))

#Login button

login_btn = Button(root,text='Login Here', bg='white',fg='black',command=handle_login)
login_btn.config(font=('verdana', 12))

login_btn.pack(pady=(10,20))




root.mainloop()
