nivelAcesso=input("Digite seu nivel de acesso--> ADM / USR / GUEST --> ").upper()

if nivelAcesso=="ADM" or nivelAcesso=="USR":
    genero=input("Digite seu genero --> MASC / FEM --> ").upper()
    if nivelAcesso=="ADM":
        if genero=="MASC":
            print("OLÁ ADMINISTRADOR SEJA BEM VINDO!")
        else:
            print("OLÁ ADMINISTRADORA SEJA BEM VINDA!")
    else:
        if genero=="MASC":
            print("OLÁ USUÁRIO SEJA BEM VINDO!")
        else:
            print("OLÁ USUÁRIA SEJA BEM VINDA!")
elif nivelAcesso=="GUEST":
    print("OLÁ VISITANTE SEJA BEM VINDO(A)!")
else:
    print("OLÀ DESCONHECIDO SEJA BEM VINDO(A)!")