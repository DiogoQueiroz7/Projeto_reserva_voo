from controller import FlightOperator
import time 

def main():
    '''
    função principal que inicia todo o programa
    '''
    operator = FlightOperator("IFMS AirLines Group ")
    print(f"--- Bem-vindo ao Sistema da {operator.name} ---")

    while True:
        print("\nOpções do Sistema:")
        print("1. Listar Todos Os Voos Programados")
        print("2. Ver Passageiros De Um Voo")
        print("3. Ver Tripulação De Um Voo")
        print("4. Ver Dados Do Avião De Um Voo ")
        print("5. Consultar Clientes Por Reserva")
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

        elif choice == '5':
            flight_code = input("Digite o código do voo da reserva: ").upper()
            flight = operator.find_flight(flight_code)
            
            if not flight:
                print("Voo não encontrado.")
                continue
            locator_code = input("Digite o CÓDIGO da reserva: ")
            found_customer = None
            for reservation in flight.reservation.values():
                if reservation.locator.lower() == locator_code.lower():
                    found_customer = reservation.customer
                    break
            if found_customer:
                print("\n--- Dados do Cliente da Reserva ---")
                print(f"Nome: {found_customer.name}")
                print(f"CPF: {found_customer.show_cpf}")
                print(f"E-mail: {found_customer.email}")
            else:
                print("Reserva não encontrada neste voo.")

        elif choice == '0':
            print('Saindo do Sitema, aguarde...')
            time.sleep(3)
            print("Obrigado por escolher o IFMS AirLines Group!")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()