import random
import time
import colorama
from colorama import Fore, Style

colorama.init()
# Lista contendo as mensagens de status do nível do reservatório
niveis = [
    (1, "Muito Baixo (CRÍTICO)"),
    (2, "Baixo"),
    (3, "Médio"),
    (4, "Alto"),
    (5, "Muito Alto (ALERTA)"),
]

# função para definir a cor do texto com base no nível
def definir_cor(nivel):
    cores = {
        1: Fore.RED,
        2: Fore.YELLOW,
        3: Fore.GREEN,
        4: Fore.CYAN,
        5: Fore.BLUE,
    }
    return cores[nivel]

# Loop principal do programa e saida de dados
try:
    while True:
        print("\n\n" + "=" * 60)
        print("SISTEMA DE MONITORAMENTO DE NÍVEL DO RESERVATÓRIO".center(60))
        print("=" * 60)
# escolhe aleatoriamente um nível de status do reservatório
        numero, descricao = random.choice(niveis)
        cor = definir_cor(numero)
        print(f"Status do nivel do reservatório: {cor}{descricao}{Style.RESET_ALL}")
        time.sleep(10)
# Mensagem de encerramento do monitoramento
        print("\n"*2 + "=" * 60)
        print("Caso deseje encerrar o monitoramento, pressione Ctrl+C.".center(60))
        print("=" * 60)
except KeyboardInterrupt:
    print("\nMonitoramento Encerrado.")
