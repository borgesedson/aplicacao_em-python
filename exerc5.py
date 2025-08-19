# Lista de hotéis disponíveis
hoteis = ["Casabranca", "Nove de Julho", "Agatha Pension", "Seu Conforto"]

# Título do programa
print("=== Sistema de Consulta de Hotéis ===\n")

for hotel in hoteis:
    print(f"🏨 {hotel}")

# Interação com o usuário
print("\nDeseja buscar um hotel específico?")
busca = input("Digite o nome do hotel: ")

# Verificando se o hotel está na lista
for hotel in hoteis:
    if busca.lower() == hotel.lower():
        print(f"\n✅ Hotel '{hotel}' está disponível!")
        encontrado = True
        break

else: 
    print(f"\n❌ Hotel '{busca}' não foi encontrado.")
