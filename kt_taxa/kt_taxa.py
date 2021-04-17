"""
Arquivo principal
"""


def taxa_exercicio(aquisicao, lucro):
    """Retorna a taxa de financiamento no exercício."""
    return round(lucro / aquisicao * 100, 2)


def aquisicao_exercicio(premio, cotacao):
    """Retorna o preço de aquisição do ativo no exercício."""
    return cotacao - premio


def lucro_exercicio(strike, aquisicao):
    """Retorna o lucro no exercício."""
    return round(strike - aquisicao, 2)
