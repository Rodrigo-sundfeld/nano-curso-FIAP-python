nome = input("Digite o nome do paciente: ").upper()
idade = int(input("Digite a idade do paciente: "))
doencaContagiosa = input("Possui suspeita de doença infecto-contagiosa? ").upper()

if idade >= 65:
    print("O paciente, " + nome + " possui atendimento PRIORITÁRIO.")
elif doencaContagiosa == "SIM":
    print("O paciente, " + nome + " possui atendimento PRIORITÁRIO e deve aguardar na sala RESERVADA!")
else:
    print("O paciente, " + nome + " NÃO possui atendimento prioritário.")