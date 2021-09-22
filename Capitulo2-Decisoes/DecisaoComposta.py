nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))

if idade >= 65:
    print("O paciente, " + nome + " possui atendimento PRIORITÁRIO.")
else:
    print("O paciente, " + nome + " NÃO possui atendimento prioritário.")