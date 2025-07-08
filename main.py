from controller import FlightOperator
import time 

def main():
    operator = FlightOperator("IFMS AirLines Group ")
    print(f"--- Bem-vindo ao Sistema da {operator.name} ---")

    while True:
        print("\nOpções do Sistema:")
        print("1. Listar todos os voos programados")
        print("2. Ver passageiros de um voo")
        print("3. Ver tripulação de um voo")
        print("4. Ver dados do avião de um voo ")
        print("0. Sair")
        
        choice = input("Digite sua escolha: ")

        if choice == '1':
            print("\n--- Voos Programados No Sistema ---")
            print('Loading...')
            time.sleep(1.5)
            if not operator.flights:
                print("Nenhum voo programado.")
            else:
                for flight in operator.flights.values():
                    departure_str = flight.departure_time.strftime("%d/%m/%Y às %H:%M")
                    print(f"  Voo {flight.code}: {flight.origin} -> {flight.destination} | Partida: {departure_str} | {len(flight.reservation)} passageiros")

        elif choice == '2':
            code = input("Digite o código do voo: ").upper()
            flight = operator.find_flight(code)
            if flight:
                print('Listando passageiros')
                print('Loading...')
                time.sleep(1.5)
                flight.show_passengers(10)
            else:
                print("Voo não encontrado.")

        elif choice == '3':
            code = input("Digite o código do voo: ").upper()
            flight = operator.find_flight(code)
            if flight:
                print('Listando a Tripulção do voo')
                print('Loading...')
                time.sleep(1.5)
                flight.show_crew()
            else:
                print("Voo não encontrado.")

        elif choice == '4':
            code = input("Digite o código do voo para ver sua aeronave: ").upper()
            flight = operator.find_flight(code)
            if flight:
                print(f"\n--- Dados do Avião do Voo {flight.code} ---")
                print('Loading...')
                time.sleep(1)
                print(f"  {flight.airplane}") 
            else:
                print("Voo não encontrado.")

        elif choice == '0':
            print('Saindo do Sitema, aguarde...')
            time.sleep(3)
            print("Obrigado por escolher o IFMS AirLines Group!")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()