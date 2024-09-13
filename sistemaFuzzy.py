import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class SistemaFuzzy:
    def __init__(self):
        # Variaveis de entrada
        self.historico_credito = ctrl.Antecedent(np.arange(0, 11, 1), 'historico_credito')
        self.renda_mensal = ctrl.Antecedent(np.arange(0, 10001, 1), 'renda_mensal')
        self.divida_atual = ctrl.Antecedent(np.arange(0, 10001, 1), 'divida_atual')

        # Variavel de saída
        self.risco = ctrl.Consequent(np.arange(0, 11, 1), 'risco')

        self._definir_funcoes_pertinencia()

        self._definir_regras()

        self.sistema_controle = ctrl.ControlSystem(self.regras)
        self.simulacao = ctrl.ControlSystemSimulation(self.sistema_controle)

    def _definir_funcoes_pertinencia(self):
        # Histórico de Credito
        self.historico_credito['ruim'] = fuzz.trimf(self.historico_credito.universe, [0, 0, 3])
        self.historico_credito['regular'] = fuzz.trimf(self.historico_credito.universe, [0, 3, 6])
        self.historico_credito['bom'] = fuzz.trimf(self.historico_credito.universe, [3, 6, 9])
        self.historico_credito['excelente'] = fuzz.trimf(self.historico_credito.universe, [6, 10, 10])

        # Renda Mensal
        self.renda_mensal['baixa'] = fuzz.trimf(self.renda_mensal.universe, [0, 0, 3000])
        self.renda_mensal['media'] = fuzz.trimf(self.renda_mensal.universe, [2000, 5000, 8000])
        self.renda_mensal['alta'] = fuzz.trimf(self.renda_mensal.universe, [6000, 10000, 10000])

        # Dívida Atual
        self.divida_atual['baixa'] = fuzz.trimf(self.divida_atual.universe, [0, 0, 3000])
        self.divida_atual['moderada'] = fuzz.trimf(self.divida_atual.universe, [2000, 5000, 8000])
        self.divida_atual['alta'] = fuzz.trimf(self.divida_atual.universe, [6000, 10000, 10000])

        # Risco
        self.risco['baixo'] = fuzz.trimf(self.risco.universe, [0, 0, 3])
        self.risco['medio'] = fuzz.trimf(self.risco.universe, [2, 5, 8])
        self.risco['alto'] = fuzz.trimf(self.risco.universe, [6, 10, 10])

    def _definir_regras(self):
        self.regras = [
            ctrl.Rule(self.historico_credito['excelente'] & self.divida_atual['baixa'], self.risco['baixo']),
            ctrl.Rule(self.historico_credito['bom'] & self.renda_mensal['media'] & self.divida_atual['moderada'], self.risco['medio']),
            ctrl.Rule(self.historico_credito['ruim'] & self.divida_atual['alta'], self.risco['alto']),
            ctrl.Rule(self.historico_credito['regular'] & self.divida_atual['moderada'], self.risco['medio']),
            ctrl.Rule(self.historico_credito['ruim'] & self.renda_mensal['baixa'] & self.divida_atual['alta'], self.risco['alto'])
        ]

    def calcular_risco(self, historico, renda, divida):
        self.simulacao.input['historico_credito'] = historico
        self.simulacao.input['renda_mensal'] = renda
        self.simulacao.input['divida_atual'] = divida

        self.simulacao.compute()
        return self.simulacao.output['risco']
