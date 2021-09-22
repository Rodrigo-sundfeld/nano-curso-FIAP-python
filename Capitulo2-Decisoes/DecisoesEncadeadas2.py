nome = input("Digite o nome do paciente: ").upper()
idade = int(input("Digite a idade do paciente: "))
doencaInfectoContagiosa = input("O paciente possui suspeita de doença infecto-contagiosa? (SIM / NAO) ")

# PRIMEIRO PROBLEMA A SER RESOLVIDO -- POSSUI DOENÇA INFECTO-CONTAGIOSA

if doencaInfectoContagiosa == "SIM":
    print("O paciente " + nome + ", deve ser encaminhado para sala AMARELA --> Isolamento.")
elif doencaInfectoContagiosa == "NAO":
    print("O paciente " + nome + ", deve ser encaminhado para sala BRANCA --> Atendimento normal.")
else:
    print("Responda se o paciente possui suspeita de doença infecto-contagiosa apenas com SIM ou NAO")

# SEGUNDO PROBLEMA A SER RESOLVIDO -- IDADE SUPERIOR A 65 ANOS OU PACIENTE GRAVIDA

if idade > 65:
    print("Paciente " + nome + " COM prioridade.")
else:
    genero = input("Digite o gênero do paciente --> FEMINIMO / MASCULINO --> ").upper()
    if genero == "FEMININO" and idade > 10:
        gravidez = input("A paciente " + nome + ", está grávida? SIM / NAO --> ").upper()
        if gravidez == "SIM":
            print("Paciente " + nome + ", COM prioridade.")
        else:
            print("Paciente " + nome + ", SEM prioridade.")
    else:
        print("Paciente " + nome + ", SEM prioridade")
