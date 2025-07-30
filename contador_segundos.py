import time

def contador_segundos():
    print("=== Contador de Segundos ===")
    
    try:
        # Solicita ao usuário o número de segundos para contar
        segundos = int(input("Digite o número de segundos para contar: "))
        
        if segundos <= 0:
            print("Por favor, digite um número positivo maior que zero.")
            return
        
        print(f"\nIniciando contagem de {segundos} segundos...")
        print("Pressione Ctrl+C para parar a contagem.\n")
        
        # Conta de 1 até o número especificado
        for i in range(1, segundos + 1):
            print(f"Segundo {i}/{segundos}")
            time.sleep(1)  # Pausa por 1 segundo
        
        print(f"\n✅ Contagem concluída! {segundos} segundos contados.")
        
    except ValueError:
        print("❌ Erro: Por favor, digite um número válido.")
    except KeyboardInterrupt:
        print("\n\n⏹️ Contagem interrompida pelo usuário.")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    contador_segundos() 