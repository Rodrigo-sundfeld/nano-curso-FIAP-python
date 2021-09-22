nome=input("Digite o nome do paciente: ").upper()
idade=int(input("Digite a idade do paciente: "))
doencaInfectoContagiosa=input("Suspeita de doença infecto-contagiosa? SIM / NAO --> ").upper()

while doencaInfectoContagiosa!="SIM" and doencaInfectoContagiosa!="NAO":
    print("Digite apenas --> SIM ou NAO")
    doencaInfectoContagiosa=input("Suspeita de doença infecto-contagiosa? SIM / NAO --> ").upper()

if doencaInfectoContagiosa=="SIM":
    print("Encaminhe o paciente " + nome + " para o ISOLAMENTO")
else:
    print("Encaminha o paciente " + nome + " para sala de espera NORMAL")

if idade > 65:
    print("Paciente COM prioridade!")
else:
    genero=input("Digite o genero do paciente --> MASC / FEM --> ").upper()
    if genero=="FEM" and idade>10:
        gravidez=input("A paciente " + nome + " está gravida? SIM / NAO --> ").upper()
        if gravidez=="SIM":
            print("A paciente " + nome + " possui atendimento PRIORITÁRIO!")
        else:
            print("A paciente " + nome + " NÃO possui atendimento prioritário.")
    else:
        print("Paciente SEM prioridade")