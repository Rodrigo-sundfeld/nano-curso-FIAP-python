nomeParticipante = input("Digite o nome do participante do evento: ")
nomeDestinatarioComprovante = input("Digite o nome do destinatário do comprovante de participação: ")
nomeEvento = input("Digite o nome do evento: ")
valorEntrada = float(input("Digite o valor da entrada em R$"))

print("------------- RECIBO DO EVENTO --------------")
print("Declaro para " + nomeDestinatarioComprovante + " que " + nomeParticipante + " esteve presente no evento, "
      + nomeEvento + ", cujo o valor de entrada foi de R$" + str(valorEntrada))