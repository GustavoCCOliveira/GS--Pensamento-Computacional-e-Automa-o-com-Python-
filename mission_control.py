# ============================================================
# MISSION CONTROL AI
# Global Solution 2026.1
# Pensamento Computacional e Automação com Python
# ============================================================

# -----------------------------
# Dados da missão
# -----------------------------

nome_missao = "ALADA test Alpha"
nome_equipe = "Equipe EDEN"

dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

# Acumuladores de risco por área
risco_areas = [0, 0, 0, 0, 0]


# ============================================================
# FUNÇÕES DE ANÁLISE
# ============================================================

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura abaixo do ideal"
    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"
    elif valor < 60:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif valor < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif valor < 90:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif valor < 70:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


# ============================================================
# CLASSIFICAÇÃO DOS CICLOS
# ============================================================

def classificar_ciclo(risco):
    if risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


# ============================================================
# RECOMENDAÇÕES
# ============================================================

def gerar_recomendacao(risco):
    if risco <= 2:
        return "Manter operação normal e continuar monitoramento."

    elif risco <= 5:
        return "Monitorar sistemas em atenção e preparar plano de contingência."

    else:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."


# ============================================================
# TENDÊNCIA DA MISSÃO
# ============================================================

def analisar_tendencia(primeiro_risco, ultimo_risco):
    if ultimo_risco > primeiro_risco:
        return "A missão apresentou tendência de piora."

    elif ultimo_risco < primeiro_risco:
        return "A missão apresentou tendência de melhora."

    else:
        return "A missão permaneceu estável em relação ao início."


# ============================================================
# ÁREA MAIS AFETADA
# ============================================================

def identificar_area_mais_afetada(riscos):
    maior = max(riscos)
    indice = riscos.index(maior)

    return areas_monitoradas[indice], maior


# ============================================================
# PROCESSAMENTO DA MISSÃO
# ============================================================

riscos_ciclos = []

soma_temperatura = 0
soma_comunicacao = 0
soma_bateria = 0
soma_oxigenio = 0
soma_estabilidade = 0

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)

print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")

print("=" * 60)

for numero_ciclo, ciclo in enumerate(dados_missao, start=1):

    temperatura = ciclo[0]
    comunicacao = ciclo[1]
    bateria = ciclo[2]
    oxigenio = ciclo[3]
    estabilidade = ciclo[4]

    soma_temperatura += temperatura
    soma_comunicacao += comunicacao
    soma_bateria += bateria
    soma_oxigenio += oxigenio
    soma_estabilidade += estabilidade

    status_temp, risco_temp, msg_temp = analisar_temperatura(temperatura)
    status_com, risco_com, msg_com = analisar_comunicacao(comunicacao)
    status_bat, risco_bat, msg_bat = analisar_bateria(bateria)
    status_oxi, risco_oxi, msg_oxi = analisar_oxigenio(oxigenio)
    status_est, risco_est, msg_est = analisar_estabilidade(estabilidade)

    risco_areas[0] += risco_temp
    risco_areas[1] += risco_com
    risco_areas[2] += risco_bat
    risco_areas[3] += risco_oxi
    risco_areas[4] += risco_est

    risco_total = (
        risco_temp +
        risco_com +
        risco_bat +
        risco_oxi +
        risco_est
    )

    riscos_ciclos.append(risco_total)

    classificacao = classificar_ciclo(risco_total)

    print(f"\nCICLO {numero_ciclo}")
    print("-" * 60)

    print(f"Temperatura: {temperatura}°C | {status_temp} | {msg_temp}")
    print(f"Comunicação: {comunicacao}% | {status_com} | {msg_com}")
    print(f"Bateria: {bateria}% | {status_bat} | {msg_bat}")
    print(f"Oxigênio: {oxigenio}% | {status_oxi} | {msg_oxi}")
    print(f"Estabilidade: {estabilidade}% | {status_est} | {msg_est}")

    print(f"\nPontuação de risco do ciclo: {risco_total}")
    print(f"Classificação do ciclo: {classificacao}")
    print(f"Recomendação: {gerar_recomendacao(risco_total)}")


# ============================================================
# RELATÓRIO FINAL
# ============================================================

quantidade_ciclos = len(dados_missao)

media_temperatura = soma_temperatura / quantidade_ciclos
media_comunicacao = soma_comunicacao / quantidade_ciclos
media_bateria = soma_bateria / quantidade_ciclos
media_oxigenio = soma_oxigenio / quantidade_ciclos
media_estabilidade = soma_estabilidade / quantidade_ciclos

maior_risco = max(riscos_ciclos)
ciclo_critico = riscos_ciclos.index(maior_risco) + 1

risco_medio = sum(riscos_ciclos) / quantidade_ciclos

ciclos_criticos = 0

for risco in riscos_ciclos:
    if risco >= 6:
        ciclos_criticos += 1

tendencia = analisar_tendencia(
    riscos_ciclos[0],
    riscos_ciclos[-1]
)

area_afetada, pontuacao_area = identificar_area_mais_afetada(
    risco_areas
)

classificacao_final = classificar_ciclo(round(risco_medio))

print("\n")
print("=" * 60)
print("RELATÓRIO FINAL DA MISSÃO")
print("=" * 60)

print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")

print(f"\nQuantidade de ciclos analisados: {quantidade_ciclos}")

print(f"\nMédia de temperatura: {media_temperatura:.2f} °C")
print(f"Média de comunicação: {media_comunicacao:.2f}%")
print(f"Média de bateria: {media_bateria:.2f}%")
print(f"Média de oxigênio: {media_oxigenio:.2f}%")
print(f"Média de estabilidade: {media_estabilidade:.2f}%")

print(f"\nCiclo mais crítico: Ciclo {ciclo_critico}")
print(f"Maior pontuação de risco: {maior_risco}")
print(f"Risco médio da missão: {risco_medio:.2f}")
print(f"Quantidade de ciclos críticos: {ciclos_criticos}")

print(f"\nTendência da missão: {tendencia}")

print("\nPontuação acumulada por área:")

for i in range(len(areas_monitoradas)):
    print(f"{areas_monitoradas[i]}: {risco_areas[i]} pontos")

print(f"\nÁrea mais afetada: {area_afetada}")
print(f"Pontuação da área: {pontuacao_area}")

print(f"\nClassificação final da missão: {classificacao_final}")

print("\nConclusão:")

if classificacao_final == "MISSÃO ESTÁVEL":
    print("A missão permaneceu sob controle durante toda a operação.")

elif classificacao_final == "MISSÃO EM ATENÇÃO":
    print("A missão apresentou instabilidades moderadas que exigem monitoramento contínuo.")

else:
    print("A missão apresentou falhas críticas e requer intervenção imediata.")
