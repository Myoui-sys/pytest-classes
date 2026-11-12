# Caclular total de uma compra
def calcular_total_compra(preco, quantidade):
    return preco * quantidade

# Função para calcular troco
def calcular_troco(valor_pago, valor_compra):
    return valor_pago - valor_compra

# Função para converter horas em minutos
def converter_horas_em_minutos(horas):
    return horas * 60

# Função de saudação
def criar_saudacao(nome):
    return "Olá " + nome + "!"

# Função para contar quantidade de caracteres

def contar_caracteres(texto):
    return len(texto)

# Função para verificar item dentro da lista
def tem_item_na_lista(item, lista):
    return item in lista

# Função para verificar idade para entrar no evento
def pode_entrar_no_evento(idade):
    return idade >= 18

# Função para calcular a média de notas

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

# Função para converter KM em metros
def converter_km_em_metros(distancia):
    return distancia * 1000

# FUNÇÕES COM PARAMETRIZE E RAISES
# Função para calcular o valor da gorjeta de uma conta

def calcular_gorjeta(valor_conta, percentual):
    if valor_conta < 0 or percentual < 0:
        raise ValueError('Os valores não podem ser negativos')
    return round(valor_conta * (percentual/100), 2) 

# Função para converter Celsius em Fahrenheit 

def converter_celsius_fahreinheit(celsius):
    return (celsius * 9 / 5) + 32

# Função para calcular tempo de uma viagem pela distância e velocidade

def calcular_tempo_viagem(distancia, velocidade):
    if distancia < 0:
        raise ValueError('A distância não pode ser negativa')

    if velocidade < 0:
        raise ValueError('A velocidade deve ser maior que zero')
    return distancia / velocidade

# Função para calcular idade após X tempo

def calcular_idade_apos_anos(idade_atual, anos):
    if idade_atual < 0 or anos < 0:
        raise ValueError('Idade e período não podem ser negativos')
    return idade_atual + anos

# Função para testes com fixtures
# Função para cadastrar item

def adicionar_item(lista, item, preco):
    if not item.strip(): # Strip remove os caracteres vazios
        raise ValueError("O nome do item não pode ser vazio")

    if preco <= 0:
        raise ValueError("O preço deve ser maior que zero")

    produto = {
        "nome": item,
        "preco": preco
    }

    lista.append(produto)
    return produto

# FUNÇÃO PARA CALCULAR O TOTAL DE UMA LISTA
def calcular_total(lista):
    return round(sum(item['preco'] for item in lista), 2)

# FUNÇÃO PARA APLICAR O PAGAMENTO
def aplicar_pagamento(saldo, valor):
    if valor <= 0:
        raise ValueError('O pagamento deve ser positivo')
    if valor > saldo:
        raise ValueError('Saldo insuficiente')
    return saldo - valor

#FUNÇÃO PARA FILTRAR UM ITEM POR PREÇO
def filtrar_por_preco(lista, limite):
    return [
        item for item in lista
        if item['preco'] <= limite
    ]