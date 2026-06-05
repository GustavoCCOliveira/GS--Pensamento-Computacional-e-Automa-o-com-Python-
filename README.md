🚀 PROJETO EDEN 🚀
Global Solution 2026.1
Pensamento Computacional e Automação com Python - 1CCPF - 

------------------------------------------------------------------------------------------------------------------------------------------
📋 Descrição do Projeto

O Projeto APOLLO é um sistema inteligente desenvolvido em Python para simular o monitoramento de uma missão espacial experimental.

O objetivo do sistema é acompanhar diferentes indicadores operacionais da missão, identificar riscos, gerar alertas automáticos, analisar tendências e produzir um relatório final para auxiliar a tomada de decisão da equipe de controle.

O projeto foi desenvolvido utilizando conceitos fundamentais de programação, incluindo:
------------------------------------------------------------------------------------------------------------------------------------------
Matrizes
Listas
Funções
Estruturas de repetição
Estruturas condicionais
Análise de dados
Lógica de decisão

🎯 Objetivo

Simular um centro de controle espacial capaz de:

Monitorar dados da missão;
Analisar múltiplos ciclos operacionais;
Detectar situações de atenção e criticidade;
Calcular níveis de risco;
Gerar recomendações automáticas;
Identificar a área mais afetada da missão;
Avaliar a tendência geral da operação;
Emitir um relatório completo ao final da análise.
------------------------------------------------------------------------------------------------------------------------------------------
🛰️ Dados Monitorados

Cada ciclo da missão contém as seguintes informações:

Índice	Variável
0	Temperatura
1	Comunicação
2	Bateria
3	Oxigênio
4	Estabilidade

Exemplo:

[24, 92, 88, 96, 90]

Representa:

Temperatura: 24°C
Comunicação: 92%
Bateria: 88%
Oxigênio: 96%
Estabilidade: 90%
------------------------------------------------------------------------------------------------------------------------------------------
📊 Áreas Monitoradas

O sistema acompanha cinco áreas críticas da missão:

Temperatura interna
Comunicação com a base
Sistema de energia
Suporte de oxigênio
Estabilidade operacional
------------------------------------------------------------------------------------------------------------------------------------------
⚠️ Regras de Classificação
Temperatura
Faixa	Status
Menor que 18°C	ATENÇÃO
18°C até 30°C	NORMAL
31°C até 35°C	ATENÇÃO
Acima de 35°C	CRÍTICO
------------------------
Comunicação
Faixa	Status
Menor que 30%	CRÍTICO
30% até 59%	ATENÇÃO
60% ou mais	NORMAL
------------------------
Bateria
Faixa	Status
Menor que 20%	CRÍTICO
20% até 49%	ATENÇÃO
50% ou mais	NORMAL
------------------------
Oxigênio
Faixa	Status
Menor que 80%	CRÍTICO
80% até 89%	ATENÇÃO
90% ou mais	NORMAL
------------------------
Estabilidade
Faixa	Status
Menor que 40%	CRÍTICO
40% até 69%	ATENÇÃO
70% ou mais	NORMAL
------------------------------------------------------------------------------------------------------------------------------------------
📈 Sistema de Pontuação
Status	Pontos
NORMAL	0
ATENÇÃO	1
CRÍTICO	2

Pontuação máxima por ciclo:

5 indicadores × 2 pontos = 10 pontos
------------------------------------------------------------------------------------------------------------------------------------------
Pontuação	Classificação
0 a 2	MISSÃO ESTÁVEL
3 a 5	MISSÃO EM ATENÇÃO
6 a 10	MISSÃO CRÍTICA
------------------------------------------------------------------------------------------------------------------------------------------
📉 Tendência da Missão

O sistema compara o risco do primeiro ciclo com o último ciclo.

Possíveis resultados:

Tendência de melhora
Tendência de piora
Tendência estável
------------------------------------------------------------------------------------------------------------------------------------------🔧 Recomendações Automáticas

O sistema gera recomendações automaticamente.

Exemplos:

Verificar controle térmico da missão.
Restabelecer comunicação com a base.
Ativar modo de economia de energia.
Acionar protocolo de suporte à vida.
Reduzir operações não essenciais.
------------------------------------------------------------------------------------------------------------------------------------------
🖥️ Exemplo de Execução
MISSION CONTROL AI

Missão: ALADA Test Alpha
Equipe: Equipe Apollo

CICLO 1
Temperatura: 24°C | NORMAL
Comunicação: 92% | NORMAL
Bateria: 88% | NORMAL
Oxigênio: 96% | NORMAL
Estabilidade: 90% | NORMAL

Pontuação de risco: 0
Classificação: MISSÃO ESTÁVEL
------------------------------------------------------------------------------------------------------------------------------------------
▶️ Como Executar
Clone o repositório:
git clone [https://github.com/SEU-USUARIO/mission-control-ai.git](https://github.com/GustavoCCOliveira/GS--Pensamento-Computacional-e-Automa-o-com-Python-.git)
Execute:
python mission_control.py
------------------------------------------------------------------------------------------------------------------------------------------
👥 Integrantes

Nome:Gustavo Torres de Oliveira

RM: 572952

Nome: Rafael laprega gontijo magalhaes

RM: 561975

