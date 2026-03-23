import json 
import customtkinter as ctk
from gerenciador_de_senhas import  dados, senha_mestre, f, salvar_dados, autenticar
import hashlib 
#JANELA -------------------------------------------------------------------------------------------------------------------------------

def validar_login():

 global senha_mestre 
  
 senha = entrada_senha.get()
 if not senha:
      print("Digite algo!")
      return 
   
 if senha_mestre is None:
     print("Criando sua primeira senha...")
     
     novo_hash = hashlib.sha256(senha.encode()).hexdigest()
     senha_mestre = novo_hash
     salvar_dados()
     
     print ('Senha cadastrada com sucesso!')
   
 else:
    hash_digitado = hashlib.sha256(senha.encode()).hexdigest()

    if hash_digitado == senha_mestre:
      entrada_senha.configure(border_color="Green")
      print("Acesso permitido!")

    else:
      entrada_senha.configure(border_color="red")
      print("Senha incorreta, tente novamente!")


janela = ctk.CTk()
janela.title('KeyNoki')

ctk.set_appearance_mode('black')
ctk.set_default_color_theme('blue')
janela.geometry('800x600')

#titulo e login
titulo_app = ctk.CTkLabel(janela, text='\nKeyNoki', font=('helvetica', 26, 'bold'))
titulo_app.pack(pady=15)


login_usuario = ctk.CTkLabel(janela, text='Login', font=('helvetica', 20, 'bold'))
login_usuario.pack(pady=(75, 10))

#caixa de texto senha
entrada_senha = ctk.CTkEntry(janela, width=220, height= 40, placeholder_text='Digite sua senha')
entrada_senha.pack(pady=(15, 15))

#botão
botal_logar = ctk.CTkButton(janela, text='Iniciar sessão', command=validar_login,)
botal_logar.pack(pady=20)


janela.mainloop()
