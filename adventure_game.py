from typing import Optional, Tuple, Union
import customtkinter as ctk
# import 


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

class Welcomeframe(ctk.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master,**kwargs)

        # self.welcomingframe = ctk.CTkFrame(master=self,width=200,height=100,corner_radius=10,border_width=2)
        # self.welcomingframe.grid(row=0,column=0,padx=(30,30),pady=(20,20))

        self.welcoming_label = ctk.CTkLabel(master=self,text="HELLO \n------------WELCOME TO WONDERLAND------------\nCHOOSE TO GO LEFT OR RIGHT",text_color="blue",font=("Roboto",17,"bold","italic"))
        self.welcoming_label.grid(padx=(10,10),pady=(10,10))

class Buttonframe(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # self.buttons_frame = ctk.CTkFrame(master=self,corner_radius=10)
        # self.buttons_frame.grid(row=1,column=0,padx=(10,0),pady=(20,0))

        self.leftbutton = ctk.CTkButton(master=self,width=100,corner_radius=10,text="LEFT")
        self.leftbutton.grid(row=1,column=0,padx=(10,10),pady=(20,20))

        self.rightbutton = ctk.CTkButton(master=self,width=100,corner_radius=10,text="RIGHT")
        self.rightbutton.grid(row=1,column=1,padx=(20,10),pady=(20,20))

class Leftbuttonframe(ctk.CTkFrame):           
    def __init__(self, master ,**kwargs):
        super().__init__(master,**kwargs)

        self.faildlabel = ctk.CTkLabel(master=self,text="HERE IS A DANGERZONE \n------------SORRY YOU WERE BITTEN BY A SNAKE------------",font=("Roboto",17,"bold","italic"),text_color="green")
        self.faildlabel.grid(row=0,column=0,padx=(10,10),pady=(20,20))

class Failedframe(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        self.textlabel = ctk.CTkLabel(master=self,text="----------YOU FAILED----------",text_color="red",font=("Roboto",17,"bold","italic"))
        self.textlabel.grid(row=0,column=0,padx=(20,20),pady=(20,10))

        self.playagain_button = ctk.CTkButton(master=self,width=100,text="PLAY AGAIN")
        self.playagain_button.grid(row=2,column=0,padx=(50,0),pady=(0,20))
        
        self.playagain_button = ctk.CTkButton(master=self,width=100,text="QUIT")
        self.playagain_button.grid(row=2,column=1,padx=(0,50),pady=(0,20))

class App(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title("ADVENTURE GAME")
        self.geometry("600x450+250+100")
        self.iconbitmap("ruby.ico")

        
        self.welcoming_frame = Welcomeframe(master=self,height=400, border_width=2)
        self.welcoming_frame.grid(row=0,column=0,padx=(90,0),pady=(50,0),sticky="nswe")

        self.buttonframe = Buttonframe(master=self, border_width=2)
        self.buttonframe.grid(row=1,column=0,padx=(60,0),pady=(80,0))

        self.buttonframe.leftbutton.configure(command=self.left_button)

        self.left_buttonframe = Leftbuttonframe(master=self,border_width=2)

        self.label = Failedframe(master=self,border_width=2)

        self.label.playagain_button.configure(command=self.again_fun)

    
    def left_button(self):
        self.welcoming_frame.grid_remove()
        self.buttonframe.grid_remove()
        
        self.left_buttonframe.grid(row=0,column=0,padx=(50,50),pady=(50,0),sticky="nswe") 
        self.label.grid(row=1,column=0,padx=(80,0),pady=(40,0))
    
    def again_fun(self):
        self.left_buttonframe.grid_remove()
        
if __name__=="__main__":
    window = App()

    window.mainloop()