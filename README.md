# kt-taxa
Calcula a taxa de financiamento no exercício em uma operação de venda coberta.  
  
## Pré-requisito
Python instalado e disponível no terminal de comando.  
  
## Instalação

```cmd
pip install kt-taxa
```
  
## Uso

```cmd
tx [OPTIONS] [PREMIO] [STRIKE] [COTACAO]
```
Onde:  
PREMIO é o prêmio da opção  
STRIKE é o strike da opção  
COTACAO é a cotação do ativo na montagem da operação  
Exemplo:  
```cmd
tx 0.61 27.18 26.06
6.80%
```
Uma venda coberta com uma call com prêmio de R$ 0,61, strike em R$ 27,18 e cujo ativo está cotado em R$ 26,06 na montagem da operação, retorna uma taxa de financiamento no exercício de 6,80%.  
