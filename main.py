from controller import FlightOperator

def main():
    operator = FlightOperator("I")
    print(f"--- Bem-vindo ao Sistema do {operator.name} ---")

    while True:
        print("\nOpções do Sistema:")
        print("1. Listar todos os voos programados")
        print("2. Ver passageiros de um voo")
        print("3. Ver tripulação de um voo")
        print("0. Sair")
        
        choice = input("Digite sua escolha: ")

        if choice == '1':
            print("\n--- Voos Programados ---")
            if not operator.flights:
                print("Nenhum voo programado.")
            else:
                for flight in operator.flights.values():
                    print(f"  Voo {flight.code}: {flight.origin} -> {flight.destination} | {len(flight.reservation)} passageiros")

        elif choice == '2':
            code = input("Digite o código do voo: ").upper()
            flight = operator.find_flight(code)
            if flight:
                flight.show_passengers(10)
            else:
                print("Voo não encontrado.")

        elif choice == '3':
            code = input("Digite o código do voo: ").upper()
            flight = operator.find_flight(code)
            if flight:
                flight.show_crew()
            else:
                print("Voo não encontrado.")

        elif choice == '0':
            print("Obrigado por usar o sistema!")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()