import pytest

from exemplo import (calcular_total_compra, calcular_troco, converter_horas_em_minutos, criar_saudacao, contar_caracteres, tem_item_na_lista, pode_entrar_no_evento, calcular_media, converter_km_em_metros, calcular_gorjeta, calcular_idade_apos_anos, calcular_tempo_viagem, converter_celsius_fahreinheit, adicionar_item, aplicar_pagamento, calcular_total, filtrar_por_preco)

# Teste da função para calcular valor total da compra
def test_calcular_total_compra():
    assert calcular_total_compra(2, 3) == 6

# Teste da função para calcular troco
def test_calcular_troco():
    assert calcular_troco(20, 13) == 7

# Teste da função para converter horas em minutos
def test_converter_horas_em_minutos():
    assert converter_horas_em_minutos(2) == 120

# Teste da função para criar saudação
def test_criar_saudacao():
    assert criar_saudacao('ana') == 'Olá ana!'

# Teste da função para contar quantidade de caracteres
def test_contar_caracteres():
    assert contar_caracteres('casa') == 4


# Teste da função para verificar item na lista
def test_tem_item_na_lista():
    assert tem_item_na_lista('arroz', ['arroz', 'feijão']) is True

# Teste da função para verificar idade para entrar no evento
def test_pode_entrar_no_evento():
    assert pode_entrar_no_evento(20) is True

# Teste da função de calcular a média de notas
def test_calcular_media():
    assert calcular_media(10, 2) == 6

# Teste da função de converter KM em metros
def test_converter_km_metros():
    assert converter_km_em_metros(2) == 2000

# Funções de teste com parametrize
# Função de teste para calcular gorjeta

@pytest.mark.parametrize('conta, percentual, esperado', [
    (100, 10, 10),
    (200, 15, 30),
    (150, 12, 18),
    (80, 5, 4)
])
def test_calcular_gorjeta(conta, percentual, esperado):
    assert calcular_gorjeta(conta, percentual) == esperado

# Função de teste para converter celsius em fahrenheit
@pytest.mark.parametrize('celsius, fahrenheit', [
    (0, 32),
    (100, 212),
    (25, 77),
    (-40, -40)
])
def test_converter_celsius_fahrenheit(celsius, fahrenheit):
    assert converter_celsius_fahreinheit(celsius) == fahrenheit

# Função de teste para calcular tempo de viagem
@pytest.mark.parametrize('distancia, velocidade,esperado', [
    (100, 50, 2),
    (300, 100, 3),
    (60, 60, 1),
    (150, 75, 2)
])
def test_calcular_tempo_viagem(distancia, 
velocidade, esperado):
    assert calcular_tempo_viagem(distancia, velocidade) == esperado

# Função para testar idade após tempo
@pytest.mark.parametrize('idade, anos, esperado', [
    (18, 2, 20),
    (25, 5, 30),
    (15, 15, 30), 
    (3, 2, 5)
])
def test_calcular_idade_apos_anos(idade, anos, esperado):
    assert calcular_idade_apos_anos(idade, anos) == esperado 

# Funções de testes com Raises 
def test_calcular_gorjeta_percentual_negativo():
    with pytest.raises(ValueError):
        calcular_gorjeta(100, -10)
        
def test_calcular_gorjeta_valor_negativo():
    with pytest.raises(ValueError):
        calcular_gorjeta(-100, 10)

def test_calcular_tempo_viagem_velocidade_negativa():
    with pytest.raises(ValueError):
        calcular_tempo_viagem(100, -3)

def test_calcular_tempo_viagem_distancia_negativa():
    with pytest.raises(ValueError):
        calcular_tempo_viagem(-100, 3)

def test_calcular_idade_apos_anos_negativo():
    with pytest.raises(ValueError):
        calcular_idade_apos_anos(-5, 5)

#FUNÇÕES UTILIZANDO FIXTURES
@pytest.fixture
def lista_compras():
    return [
        {"nome":"Arroz","preco": 25.00},
        {"nome":"Feijão","preco": 8.50},
        {"nome":"Leite","preco": 6.00},
        {"nome":"Café","preco": 16.00},
    ]
@pytest.fixture
def saldo_inicial():
    return 500.00

# FUNÇÕES DE TESTES COM FIXTURES
# TESTE PARA ADICIONAR ITEM NA LISTA
def test_adicionar_item_na_lista(lista_compras):
    adicionar_item(lista_compras, "Açucar", 5.50)

    assert len(lista_compras)
    assert lista_compras[-1]["nome"] == "Açucar"

#FUNÇÃO DE TESTE PARA CALCULAR VALOR TOTAL DAS COMPRAS
def test_calcular_valor_total_das_compras(lista_compras):
    total = calcular_total(lista_compras)
    assert total == 55.50

# FUNÇÃO DE TESTE PARA FILTRAR PRODUTOS POR PREÇO
def test_filtrar_produtos_por_preco(lista_compras):
    resultado = filtrar_por_preco(lista_compras, 10)

    assert len(resultado) == 2
    assert all(item['preco'] <= 10 for item in resultado)

# FUNÇÃO PARA TESTAR A ATUALIZAÇÃO DO SALDO
def test_pagamento_deve_atualizar_saldo(saldo_inicial):
    novo_saldo = aplicar_pagamento(saldo_inicial, 150)

    assert novo_saldo == 350.00

# FUNÇÃO PARA TESTAR VALOR MAIOR QUE SALDO
def test_pagamento_nao_deve_ultrapassar_saldo(saldo_inicial):
    with pytest.raises(ValueError):
        aplicar_pagamento(saldo_inicial, 600)

# FUNÇÃO PARA TESTAR LISTA DE COMPRAS INDEPENDENTE
def test_lista_deve_ser_independente(lista_compras):
    adicionar_item(lista_compras,"Chocolate", 12)

    assert len(lista_compras) == 5
