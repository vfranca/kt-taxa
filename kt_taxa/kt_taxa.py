"""
Arquivo principal
"""


def risco(premio_opcao, preco_ativo):
    return round(preco_ativo - premio_opcao, 2)


def taxa(premio_opcao, risco):
    return premio_opcao / risco * 100
