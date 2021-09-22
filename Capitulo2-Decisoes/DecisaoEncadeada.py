nome = input("Digite o nome do paciente: ").upper()
idade = int(input("Digite a idade do paciente: "))
doencaInfectoContagiosa = input("O paciente possui suspeita de doença infecto-contagiosa? (SIM / NAO) ").upper()

if idade > 65:
    print("Paciente " + nome + " COM prioridade.")
    if doencaInfectoContagiosa == "SIM":
        print("Paciente " + nome + ", deve ser encaminhado para sala de isolamento AMARELA!")
    elif doencaInfectoContagiosa == "NAO":
        print("Paciente " + nome + ", deve ser encaminhado COM prioridade para sala BRANCA")
    else:
        print("Responda se há suspeita de doença infecto-contagiosa apenas com SIM ou NAO")
else:
    print("Paciente SEM prioridade")
    if doencaInfectoContagiosa == "SIM":
        print("Paciente " + nome + ", deve ser encaminhado para sala de isolamento AMARELA!")
    elif doencaInfectoContagiosa == "NAO":
        print("Paciente " + nome + ", deve ser encaminhado SEM prioridade para sala BRANCA.")
    else:
        print("Responda se há suspeita de doença infecto-contagiosa apenas com SIM ou NAO")