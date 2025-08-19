# Valores do desafio (usuário e senha esperados)
usuario_correto = "admin"
senha_correta = "123456"

# Entrada do usuário
usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

# Verificação if-else
if usuario == usuario_correto and senha == senha_correta:
    print("Acesso concedido!")
else:
    print("Nome de usuário ou senha incorretos.")