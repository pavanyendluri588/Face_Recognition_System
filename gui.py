import tkinter as tk
import db_code
class window:
    def __init__(self):
        self.root = tk.Tk()
        self.screem_width=int(self.root.winfo_screenwidth())
        self.screem_height=int(self.root.winfo_screenheight())
        self.root.geometry(f'{self.screem_width-40}x{self.screem_height-40}+0+0')
        self.root.resizable(True,True)
        self.root.title("Face Recognization System")
        
        self.login_frame= tk.Frame(self.root,width=self.screem_width,height=self.screem_height)
        self.login_frame.place(x=0,y=0)
        self.Face_Recognization_System_label = tk.Label(self.login_frame,text="Face Recognization System",font=('calibre',70,''),fg="green")
        self.Face_Recognization_System_label.place(x=220,y=170)
        self.user_name_var= tk.StringVar()
        self.password_var = tk.StringVar()
        self.user_name_var.set("")
        self.password_var.set("")

        self.login_frame_login_name_label= tk.Label(self.login_frame,text="USERNAME",font=("calibre",15))
        self.login_frame_login_name_label.place(x=570,y=400)
        self.login_frame_login_name_entry=tk.Entry(self.login_frame,textvariable=self.user_name_var,font=("calibre",15,""))
        self.login_frame_login_name_entry.place(x=720,y=400)
        self.login_frame_password_label=tk.Label(self.login_frame,text="PASSWORD",font=("calibre",15,""))
        self.login_frame_password_label.place(x=570,y=450)
        self.login_frame_password_entry=tk.Entry(self.login_frame,textvariable=self.password_var,font=("calibre",15,""),show="*")
        self.login_frame_password_entry.place(x=720,y=450)
        self.login_frame_submit_button=tk.Button(self.login_frame,text="SUBMIT",font=("calibre",15),command=self.login_frame_submit)
        self.login_frame_submit_button.place(x=620,y=500)
        self.login_frame_reset_button=tk.Button(self.login_frame,text="RESET",font=("calibre",15))
        self.login_frame_reset_button.place(x=790,y=500)

        self.root.mainloop()
    def login_frame_submit(self):
        if db_code.login_check1(self.user_name_var.get(),self.password_var.get()):
            self.login_frame.place_forget()
            self.main_page()

    def login_frame_reset(self):
        self.password_var.set("")
        self.user_name_var.set("")
        
    def main_page(self):
        self.main_page_frame= tk.Frame(self.root,width=self.screem_width,height=self.screem_height)
        self.main_page_frame.place(x=0,y=0)
        self.main_page_logout_button= tk.Button(self.main_page_frame,text="LOOUT",bg="red",command=self.main_page_logout_button_function)
        self.main_page_logout_button.place(x=1460,y=0)
    def main_page_logout_button_function(self):
        self.login_frame_reset()
        self.main_page_frame.place_forget()
        self.login_frame.place(x=0,y=0)

    

        



if __name__  == "__main__":
    obj = window()