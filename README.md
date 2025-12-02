# Simulação de Sistema de Filas (1 Servidor / FCFS)

Aluno: Lucas Abati Zanotto

Projeto da disciplina **Modelagem e Simulação de Sistemas**.  
O objetivo é **simular uma fila com 1 atendente** (ex.: lanchonete) a partir de dados informados pelo usuário e calcular a tabela de funcionamento e as métricas finais.

---

## 🎯 Objetivo

Desenvolver um algoritmo que:
- Recebe como entrada:
  - **Quantidade de clientes (n)**
  - **Intervalos entre chegadas** (lista com *n* valores)
  - **Durações de atendimento** (lista com *n* valores)
- Gera a **tabela do funcionamento do sistema**
- Calcula as métricas:
  - **IC**: intervalo médio entre chegadas
  - **µ**: duração média do atendimento
  - **NF**: tempo médio de espera na fila
  - **TF**: tamanho médio da fila (média no tempo)

---

## 🧠 Modelo do sistema

- **1 servidor (um atendente)**
- Disciplina de fila: **FCFS** (*First Come First Served*)  
  > “quem chega primeiro, é atendido primeiro”
- Um cliente pode:
  - Chegar ao sistema em um tempo calculado a partir dos intervalos
  - Ser atendido (com duração informada)
  - **Esperar na fila** caso o atendente esteja ocupado

---

## ⚙️ Regras / Decisões do algoritmo

### 1) Cálculo do tempo de chegada
As chegadas são obtidas por **soma cumulativa dos intervalos**:

- `chegada(1) = intervalo(1)`
- `chegada(i) = chegada(i-1) + intervalo(i)`

### 2) Início do atendimento (regra principal)
O atendimento inicia quando o cliente chegou e o atendente está livre:

- `inicio(i) = max(chegada(i), fim(i-1))`

### 3) Espera na fila e fim do atendimento
- `espera(i) = inicio(i) - chegada(i)`
- `fim(i) = inicio(i) + duracao(i)`

### 4) Tamanho médio da fila (TF)
TF é uma **média no tempo** do tamanho da fila.
A fila muda apenas em eventos:
- Cliente chega e precisa esperar → **fila +1**
- Cliente inicia atendimento → **fila -1**

Definição:
- **TF = área (fila × tempo) / tempo total**

---

## 📊 Saída (Tabela)

O programa imprime uma tabela com:

- Cliente
- Intervalo
- Chegada
- Duração
- Início
- Fim
- Espera

E no final imprime **IC, µ, NF e TF**.

---

## ▶️ Como executar

### Requisitos
- Python 3.10+ (recomendado)

### Rodar o projeto
```bash
python sistema.py
