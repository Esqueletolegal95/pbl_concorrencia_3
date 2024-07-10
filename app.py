import time

def contador_indefinido():
    segundo = 0
    while True:
        print(f"Segundos: {segundo}")
        time.sleep(1)
        segundo += 1

# Exemplo de uso
contador_indefinido()
