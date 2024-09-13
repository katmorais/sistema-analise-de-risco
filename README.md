## Sistema de Análise de Risco Fuzzy

Bem-vindo ao repositório! Este projeto é um Sistema de Análise de Risco Fuzzy, uma aplicação que utiliza lógica fuzzy para avaliar o risco de crédito de clientes com base em três variáveis principais: histórico de crédito, renda mensal e dívida atual. O sistema auxilia instituições financeiras na avaliação da solvência e do risco de crédito dos clientes.

## Propósito

Promover uma ferramenta para análise de risco de crédito utilizando lógica fuzzy.

## Instalação

Para executar o sistema, você precisará instalar as seguintes dependências:

numpy: Biblioteca para operações numéricas.
scikit-fuzzy: Biblioteca para lógica fuzzy em Python.

## Instalação das Dependências

Execute o seguinte comando para instalar as dependências:
```
 pip install numpy scikit-fuzzy
```

## Como Usar o Repositório

Clone o repositório do projeto para sua máquina local:
```
 git clone https://github.com/katmorais/sistema-analise-de-risco.git
```

## Execute o Código

Para calcular o risco usando o código, execute:
Copie o código:
```
 python appy.py
```

## Regras Fuzzy

As regras fuzzy usadas para calcular o risco são:
- Regra 1: Se o histórico de crédito é excelente e a dívida atual é baixa, então o risco é baixo.
- Regra 2: Se o histórico de crédito é bom e a renda mensal é media e a dívida atual é moderada, então o risco é medio.
- Regra 3: Se o histórico de crédito é ruim e a dívida atual é alta, então o risco é alto.
- Regra 4: Se o histórico de crédito é regular e a dívida atual é moderada, então o risco é medio.
- Regra 5: Se o histórico de crédito é ruim e a renda mensal é baixa e a dívida atual é alta, então o risco é alto.

## Funcionamento do Sistema

O sistema é construído com scikit-fuzzy, que permite definir variáveis fuzzy e regras para inferência. As principais etapas são:
- Definir Variáveis e Funções de Pertinência: Configurar as variáveis de entrada e saída e suas funções de pertinência.
- Definir Regras Fuzzy: Estabelecer as regras que relacionam as variáveis de entrada ao risco.
- Simular o Sistema: Fornecer entradas e calcular o risco com base nas regras fuzzy.

## Contribuição

Contribuições são bem-vindas! Para contribuir com o projeto:
Abra um "issue" para relatar problemas ou sugerir melhorias.
Envie um "pull request" com suas alterações.