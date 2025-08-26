usuarios = ["admin", "ana", "joana", "marcos"]


print("=== Usuários cadastrados ===")
for usuario in usuarios:
    print(f"Login: {usuario}")


print("\n=== IDs de Sessão ===")
# 2. Relatório de IDs de sessão (de 1001 até 1004)
for id_sessao in range(1001, 1005):  # vai até 1004
    print(f"ID de sessão: {id_sessao}")


print("\n=== Verificação de senha padrão ===")


senha = "123456"
for caractere in senha:
    print(f"Verificando caractere: {caractere}")
