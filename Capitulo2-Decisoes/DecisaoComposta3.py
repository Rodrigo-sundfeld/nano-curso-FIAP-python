nome = input("Digite o nome do paciente: ").upper()
idade = int(input("Digite a idade do paciente: "))
doencaContagiosa = input("Suspeita de doença infecto-contagiosa? Digite SIM ou NAO --> ").upper()

if idade >= 65 and doencaContagiosa == "SIM":
    print("O paciente, " + nome + " será direcionado para o setor AMARELO COM prioridade.")
elif idade < 65 and doencaContagiosa == "SIM":
    print("O paciente, " + nome + " será direcionado para o setor AMARELO SEM prioridade.")
elif idade >= 65 and doencaContagiosa == "NAO":
    print("O paciente, " + nome + " será direcionado para o setor BRANCO COM prioridade.")
elif idade < 65 and doencaContagiosa == "NAO":
    print("O paciente, " + nome + " será direcionado para o setor BRANCO SEM prioridade.")
else:
    print("ATENÇÃO! RESPONDA PARA DOENÇA INFECTO-CONTAGIOSA SOMENTE SIM OU NAO")
