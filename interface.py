import customtkinter as ctk

#Janela principal

class KeyNoki(ctk.CTk):

 def __init__(self):

  super().__init__()
  self.geometry("800x500")
  ctk.set_appearance_mode('dark')
  ctk.set_default_color_theme("blue")
  self.configure(fg_color="#21202e")
  
  
  self.titulo = ctk.CTkLabel(self, text="KeyNoki", font=("Helvetica", 26, "bold")).pack(pady=20)
  

app = KeyNoki()
app.mainloop()