from sistemaFuzzy import SistemaFuzzy

if __name__ == "__main__":
    sistema = SistemaFuzzy()

    # Exemplo 
    historico = 700  
    renda = 5000    
    divida = 2000   

    resultado_risco = sistema.calcular_risco(historico, renda, divida)
    print(f'O risco calculado é: {resultado_risco:.2f}')
