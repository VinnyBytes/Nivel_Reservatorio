import random
import time
import colorama
from colorama import Fore, Style

colorama.init()
# Lista com os níveis e as mensagens de status do reservatório.
niveis = [
    (1, "Muito Baixo (CRÍTICO)"),
    (2, "Baixo"),
    (3, "Médio"),
    (4, "Alto"),
    (5, "Muito Alto (ALERTA)"),
]

# Define a cor do texto com base no nível.
def definir_cor(nivel: int) -> str:
    cores = {
        1: Fore.RED,
        2: Fore.YELLOW,
        3: Fore.GREEN,
        4: Fore.CYAN,
        5: Fore.BLUE,
    }
    return cores[nivel]

print("=" * 60)
print("SISTEMA DE MONITORAMENTO DE NÍVEL DO RESERVATÓRIO".center(60))
print("=" * 60)
print("Para encerrar o monitoramento, pressione Ctrl+C.")

try:
    while True:
        # Escolhe aleatoriamente um nível de status do reservatório.
        numero, descricao = random.choice(niveis)
        cor = definir_cor(numero)
        print(f"Status do nível do reservatório: {cor}{descricao}{Style.RESET_ALL}")
        time.sleep(10)
except KeyboardInterrupt:
    print("\nMonitoramento encerrado.")
