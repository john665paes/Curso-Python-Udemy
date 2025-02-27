""" 
CONSTANTE: "Variáveis" que não vão mudar
Muitas condições no mesmo 'if' (ruim)
    <- Contagem de complexidade(ruim)
"""

#PARA ALGUMA COISA QUE NÃO SERÁ ALTERADA AO LOGO DO PROGRAMA 
# USAMOS AS LETRAS MAIUSCULAS INDICANDO QUE NÃO RECEBE OUTRO VALOR.
# SÃO VARIÁVEIS CONSTANTES

velocidade = 69 #velocidade atual do carro
local_KM = 90 # KM que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RANGE_RADAR = 1 # A distância onde o radar pega


# Atribui as condições diretamente nas variáveis
velocidade_carro_radar1 = velocidade > RADAR_1 # velocidade maior que permitida
carro_passou_radar1 = local_KM>= (LOCAL_1 - RANGE_RADAR) and \
    local_KM <=(LOCAL_1 + RANGE_RADAR) # checa se o carro passou no radar
carro_multado_radar1 = carro_passou_radar1 and velocidade_carro_radar1 # checa se o radar mutou por velocidade

if velocidade_carro_radar1:
    print(f'Velolidade de {velocidade}Km/h onde o permitido é {RADAR_1}Km')
    print(velocidade_carro_radar1)
if carro_passou_radar1:
    print('Carro Passou no radar 1')
    print(carro_passou_radar1)
if carro_multado_radar1:
    print('Carro multado em radar 1')
    print(carro_passou_radar1)
