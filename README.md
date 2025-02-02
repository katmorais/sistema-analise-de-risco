## Sistema de Análise de Risco Fuzzy

Bem-vindo ao repositório do Sistema de Análise de Risco Fuzzy! Este projeto é uma aplicação que emprega lógica fuzzy para avaliar o risco de crédito de clientes, considerando três variáveis principais: Histórico de Crédito, Renda Mensal e Dívida Atual. A ferramenta foi desenvolvida para apoiar instituições financeiras na avaliação da solvência e no gerenciamento do risco de crédito, proporcionando uma análise mais precisa e detalhada.

## Propósito

O propósito deste projeto é fornecer uma ferramenta avançada para análise de risco de crédito, utilizando lógica fuzzy para interpretar e avaliar dados financeiros. O sistema permite uma avaliação mais eficaz e informada da capacidade de crédito dos clientes, ajudando as instituições a tomar decisões mais seguras e precisas.

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
```
 python appy.py
```

## Descrição das Variáveis

### Variáveis de Entrada

1. **Histórico de Crédito (`historico_credito`)**
   - **Descrição**: Avalia a experiência anterior do cliente com crédito.
   - **Intervalo**: De 0 a 10.
   - **Categorias**:
     - `ruim` (0-3)
     - `regular` (0-6)
     - `bom` (3-9)
     - `excelente` (6-10)

2. **Renda Mensal (`renda_mensal`)**
   - **Descrição**: Reflete a renda mensal atual do cliente.
   - **Intervalo**: De 0 a 10.000.
   - **Categorias**:
     - `baixa` (0-3.000)
     - `media` (2.000-8.000)
     - `alta` (6.000-10.000)

3. **Dívida Atual (`divida_atual`)**
   - **Descrição**: Representa o nível atual de dívida do cliente.
   - **Intervalo**: De 0 a 10.000.
   - **Categorias**:
     - `baixa` (0-3.000)
     - `moderada` (2.000-8.000)
     - `alta` (6.000-10.000)

### Variável de Saída

- **Risco (`risco`)**
  - **Descrição**: Avalia o risco de crédito do cliente com base nas variáveis de entrada.
  - **Intervalo**: De 0 a 10.
  - **Categorias**:
    - `baixo` (0-3)
    - `medio` (2-8)
    - `alto` (6-10)
      
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

## Exemplo de Uso

Aqui está um exemplo de como usar o sistema:
```
from sistemaFuzzy import SistemaFuzzy

if __name__ == "__main__":
    sistema = SistemaFuzzy()


    historico = 700  
    renda = 5000    
    divida = 2000   

    resultado_risco = sistema.calcular_risco(historico, renda, divida)
    print(f'O risco calculado é: {resultado_risco:.2f}')
```

## Contribuição

Contribuições são bem-vindas! Para contribuir com o projeto:
Abra um "issue" para relatar problemas ou sugerir melhorias.
Envie um "pull request" com suas alterações.
