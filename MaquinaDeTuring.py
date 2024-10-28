import json

def carregar_especificacoes(json_file):
    with open(json_file, 'r') as file:
        especificacoes = json.load(file)
    return especificacoes

def carregar_entrada(entrada_file):
    with open(entrada_file, 'r') as file:
        return list(file.read().strip())

def executar_maquina(especificacoes, fita):
    estado_atual = especificacoes["initial"]
    posicao_cabecote = 0
    branco = especificacoes["white"]
    estados_finais = set(especificacoes["final"])
    transicoes = especificacoes["transitions"]

    while estado_atual not in estados_finais:
        simbolo_atual = fita[posicao_cabecote] if posicao_cabecote < len(fita) else branco

        transicao = next((t for t in transicoes if t["from"] == estado_atual and t["read"] == simbolo_atual), None)

        if transicao is None:
            print("0")  
            return fita

        fita[posicao_cabecote] = transicao["write"]
        estado_atual = transicao["to"]
        posicao_cabecote += 1 if transicao["dir"] == "R" else -1

        if posicao_cabecote < 0:
            fita.insert(0, branco)
            posicao_cabecote = 0
        elif posicao_cabecote >= len(fita):
            fita.append(branco)

    print("1")  
    return fita

def salvar_saida(fita, output_file):
    with open(output_file, 'w') as file:
        file.write("".join(fita))

json_file = "duplo_bal.json"
entrada_file = "entrada1.txt"
output_file = "saida.txt"

especificacoes = carregar_especificacoes(json_file)
fita = carregar_entrada(entrada_file)
fita_resultante = executar_maquina(especificacoes, fita)
salvar_saida(fita_resultante, output_file)
