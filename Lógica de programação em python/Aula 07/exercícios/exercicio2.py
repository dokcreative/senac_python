# exercício TEMPORIZADOR

temporizador = int(input("Informe quando o temporizador vai começar a contagem: "))
duracao = int(input("Informe até quando vai a contagem: "))

for contagem in range(temporizador,duracao + 1):
    print(f"A contagem durou {contagem} segundos!")

# o for repete a variável contagem na quantidade de vezes que ta no range.

              
