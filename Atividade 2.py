# Definindo um produto com um dicionário (chave: valor)
produto = {
"nome": "Teclado Mecânico",
"preco": 250.00,
"estoque": 3
}
# Simulando uma lista de vários produtos no servidor
catalogo = [
{"nome": "Mouse Gamer", "preco": 120.0, "estoque": 8},
{"nome": "Monitor 144Hz", "preco": 1200.0, "estoque": 6}
]

print("--- Alerta de Estoque Baixo ---")
# Percorrendo a lista de dicionários
for item in catalogo:
# Regra de negócio: se o estoque for menor que 5, avisar o administrador

 if item["estoque"] < 5:
   print(f"ATENÇÃO: O item {item['nome']} tem apenasn{item['estoque']} unidades!")

 else:
   print("")
