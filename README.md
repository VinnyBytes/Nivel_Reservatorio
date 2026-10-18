# 💧📏 Controle de Níveis de Água

Programa em Python que exibe periodicamente uma situação aleatória para o nível do reservatório.
Cada situação é apresentada no terminal com uma cor correspondente ao nível.

> **Observação:** os níveis são simulados por uma escolha aleatória. O programa não lê dados de sensores nem mede um reservatório real.

## 📋 Níveis exibidos

| Nível | Situação | Cor |
|---:|---|---|
| 1 | Muito Baixo (CRÍTICO) | Vermelha |
| 2 | Baixo | Amarela |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito Alto (ALERTA) | Azul |

## 🛠 Requisitos

- Python 3
- Biblioteca [Colorama](https://pypi.org/project/colorama/)

## 📌 Como executar

No terminal, navegue até a pasta do projeto e execute:

```powershell
py app.py
```

O programa escolhe e exibe um nível imediatamente e, depois, escolhe outro a cada 10 segundos. Como a escolha é aleatória, o mesmo nível pode aparecer em atualizações consecutivas. A cor do texto volta ao estilo padrão após a exibição de cada mensagem.

## 📌 Como encerrar

Pressione **Ctrl+C** no terminal onde o programa está sendo executado. O programa exibirá uma mensagem de encerramento.