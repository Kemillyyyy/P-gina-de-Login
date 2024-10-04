import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")

def clique():
    print("Fazer login")

texto = customtkinter.CTkLabel(janela, text="Fazer login")
texto.pack(padx=10, pady= 10)

email = customtkinter.CTkEntry(janela, placeholder_text="Email")
email.pack (padx= 10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*")
senha.pack (padx= 10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar de login")
checkbox.pack (padx=10, pady= 10)

botao = customtkinter.CTkButton (janela, text="Entrar", command=clique)
botao.pack (padx=10, pady=10)

janela.mainloop()