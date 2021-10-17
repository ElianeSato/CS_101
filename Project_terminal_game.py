#! python3
# Mortgage calculator: Caixa

def informar_dados_financiamento():
      recursos_proprios = float(input("Informar o valor dos recursos_proprios: "))
      financiado = float(input("Informar o valor a financiar: "))
      juros_balcao = float(input("Informar a taxa de juros vigente: "))
      juros_reduzidos = float(input("Informar a taxa de juros negociada: "))
      prazo = int(input("Informar o prazo do financiamento (em meses): "))
      return (recursos_proprios, financiado, juros_balcao, juros_reduzidos, prazo)


class Dados_financiamento:
      def __init__(self, recursos_proprios, financiado, juros_balcao, juros_reduzidos, prazo):
            self.recursos_proprios = recursos_proprios
            self.financiado = financiado
            self.juros_balcao = (juros_balcao/100) / 12
            self.juros_reduzidos = (juros_reduzidos/100) / 12
            self.seguro = 0.00053298
            self.prazo = prazo
            self.preco = self.recursos_proprios + self.financiado

# class Encargo(Dados_financiamento):
#       encargo_count = 0
#       encargo_restante = 0
#       def __init__(self, mes, amortizacao):
#             super().__init__()
#             self.mes = mes
#             self.amorticao = amortizacao
#             Encargo.encargo_count += 1
#             self.id = Encargo.encargo_count
#             self.encargo_restante = Dados_financiamento.prazo
#
#       def encargo_mensal(self):
#             juros = (self.saldo * self.juros_reduzidos) # 8189.63
#             self.saldo += juros
#             prestacao = self.amorticao + juros #12078.53
#             valor_seguro = self.saldo * self.seguro
#             encargo = prestacao + valor_seguro # 12829.19
#             Encargo.encargo_restante -= 1
#             print(f'Encargo n. {self.id}    Mês: {self.mes}\n'
#                   f' Saldo inicial: R$ {self.saldo:6.2f}\n'
#                   f' Prestação: R$ {prestacao:6.2f}\n'
#                   f' Juros: R$ {juros:6.2f} taxa: {self.juros_reduzidos}\n'
#                   f' Seguro: R$ {valor_seguro:6.2f}\n'
#                   f' Valor do encargo: R$ {round(encargo,2):6.2f}\n'
#                   f' Prestações pagas: {Encargo.encargo_count}\n'
#                   f' Prestações restantes: {Encargo.encargo_restante}')



#financiamento = Dados_financiamento(567000,1400000, 8.5000, 7.02, 0.00053298,360)
recursos_proprios, financiado, juros_balcao, juros_reduzidos, prazo = informar_dados_financiamento()
financiamento = Dados_financiamento(recursos_proprios, financiado, juros_balcao, juros_reduzidos, prazo)

# encargo_2020_out = Encargo('2020/outubro', 3888.88)
# print(encargo_2020_out.recursos_proprios)



# TODO: extraordinary payments
data = ""
amortizacao = 0
novo_saldo = 0
novo_prazo = 0
nova_prestacao = 0

# TODO: total interest paid