class SiteVazamento:
    def __init__(self, nome):
        self.nome = nome
        self.senha = False
        self.email = False
        self.telefone = False
        self.nome_completo = False

    def simular_vazamento(self):
        # Solicitar informações sobre o vazamento para cada tipo de dado
        print(f"Simulação de vazamento para o site {self.nome}:")
        self.senha = self.obter_resposta("A senha foi vazada? (1 para Sim, 0 para Não): ")
        self.email = self.obter_resposta("O email foi vazado? (1 para Sim, 0 para Não): ")
        self.telefone = self.obter_resposta("O telefone foi vazado? (1 para Sim, 0 para Não): ")
        self.nome_completo = self.obter_resposta("O nome completo foi vazado? (1 para Sim, 0 para Não): ")

    def obter_resposta(self, mensagem):
        # Garantir que a resposta seja um valor numérico válido (0 ou 1)
        while True:
            try:
                resposta = int(input(mensagem))
                if resposta in [0, 1]:
                    return bool(resposta)
                else:
                    print("Por favor, digite 0 para Não ou 1 para Sim.")
            except ValueError:
                print("Por favor, digite um valor numérico.")

    def calcular_pontuacao(self):
        # Calcular a pontuação com base nas informações de vazamento
        return self.senha * 100 + self.email * 15 + self.telefone * 70 + self.nome_completo * 25

def main():
    # Crie instâncias de sites simulando vazamentos
    sites_vazados = []

    for i in range(3):
        nome_site = input(f"Digite o nome do site {i + 1}: ")
        site = SiteVazamento(nome=nome_site)
        site.simular_vazamento()
        sites_vazados.append(site)

    # Classifique os sites com base na pontuação
    sites_vazados = sorted(sites_vazados, key=lambda site: site.calcular_pontuacao(), reverse=True)

    # Imprima o ranking
    print("\nRanking de Sites Vazados:")
    for i, site in enumerate(sites_vazados, 1):
        print(f"{i}. {site.nome}: {site.calcular_pontuacao()} pontos")

if __name__ == "__main__":
    main()
