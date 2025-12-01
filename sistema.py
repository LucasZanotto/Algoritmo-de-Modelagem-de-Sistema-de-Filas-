# Unoesc Videira - Modelagem e Simulação de Sistemas
# Professora: Tatiele Bolson Moro
# Atividade: Modelagem de Sistema de Filas 
# Aluno: Lucas Abati Zanotto

from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Linha:
    cliente: int
    intervalo: float
    chegada: float
    duracao: float
    inicio: float
    fim: float
    espera: float

def ler_lista(n: int, msg: str) -> List[float]:
    raw = input(msg).strip().replace(",", " ")
    parts = [p for p in raw.split() if p]
    if len(parts) != n:
        raise ValueError(f"Esperado {n} valores, mas veio {len(parts)}.")
    return [float(x) for x in parts]

def simular(intervalos: List[float], duracoes: List[float]) -> List[Linha]:
    n = len(intervalos)

    chegadas: List[float] = []
    t = 0.0
    for inter in intervalos:
        t += inter
        chegadas.append(t)

    linhas: List[Linha] = []
    fim_anterior = 0.0

    for i in range(n):
        chegada = chegadas[i]
        inicio = max(chegada, fim_anterior)
        espera = inicio - chegada
        fim = inicio + duracoes[i]

        linhas.append(Linha(
            cliente=i + 1,
            intervalo=intervalos[i],
            chegada=chegada,
            duracao=duracoes[i],
            inicio=inicio,
            fim=fim,
            espera=espera
        ))
        fim_anterior = fim

    return linhas

def tamanho_medio_fila_TF(linhas: List[Linha]) -> float:
    eventos: List[Tuple[float, int]] = []
    for l in linhas:
        if l.espera > 0:
            eventos.append((l.chegada, +1))
            eventos.append((l.inicio, -1))

    if not linhas:
        return 0.0

    t0 = linhas[0].chegada
    t_end = linhas[-1].fim
    total = t_end - t0
    if total <= 0:
        return 0.0

    eventos.sort(key=lambda x: x[0])

    q = 0
    area = 0.0
    last = t0
    i = 0
    while i < len(eventos):
        t = eventos[i][0]
        area += q * (t - last)
        last = t
        while i < len(eventos) and eventos[i][0] == t:
            q += eventos[i][1]
            i += 1

    area += q * (t_end - last)
    return area / total

def imprimir_tabela(linhas: List[Linha]) -> None:
    print("\nCliente | Intervalo | Duração | Chegada | Início | Fim | Espera")
    print("-" * 70)
    for l in linhas:
        print(f"{l.cliente:>7} | {l.intervalo:>9.2f} | {l.duracao:>6.2f} | {l.chegada:>6.2f} | "
              f"{l.inicio:>5.2f} | {l.fim:>4.2f} | {l.espera:>6.2f}")

def main():
    print("=== Simulação de fila (1 servidor / FCFS) ===")

    n = int(input("Quantidade de clientes: ").strip())
    intervalos = ler_lista(n, f"Digite {n} intervalos entre chegadas: ")
    duracoes  = ler_lista(n, f"Digite {n} durações de atendimento: ")

    if n <= 0:
        print("Quantidade de clientes precisa ser maior que 0.")
        return

    linhas = simular(intervalos, duracoes)

    IC = sum(intervalos) / n
    mu = sum(duracoes) / n
    NF = sum(l.espera for l in linhas) / n
    TF = tamanho_medio_fila_TF(linhas)

    imprimir_tabela(linhas)

    print("\n=== Resultados ===")
    print(f"a) IC (intervalo médio entre chegadas): {IC:.4f}")
    print(f"b) µ  (duração média do atendimento):  {mu:.4f}")
    print(f"d) TF (tamanho médio da fila):         {TF:.4f}")
    print(f"e) NF (tempo médio de espera na fila): {NF:.4f}")

if __name__ == "__main__":
    main()
