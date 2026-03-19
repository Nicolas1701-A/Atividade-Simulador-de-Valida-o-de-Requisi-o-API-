# Definindo as variáveis que simulam os dados recebidos pelo servidor
senha_cadastrada = "admin123"
token_valido = True
# Entrada do usuário (simulando uma tentativa de acesso)
tentativa_senha = input("Digite a senha para acessar o sistema: ")

# Verificação de segurança
# O operador 'and' garante que ambas as condições sejam verdadeiras
if tentativa_senha == senha_cadastrada and token_valido:
    status_code = 200 # Sucesso (Padrão HTTP)
    mensagem = "Acesso concedido. Bem-vindo ao servidor!"
else:
status_code = 401 # Não autorizado
mensagem = "Erro: Senha incorreta ou token expirado."

# Exibindo a resposta final do processamento
print(f"Status: {status_code}")
print(f"Resposta do Servidor: {mensagem}")
