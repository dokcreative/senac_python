# Lista com dez espaços inicialmente vazios (representados por 0)
locais = [0,0,0,0,0,0,0,0,3,0]
# Define o número de tentativas
tentativas = 3
print("Bem-vindo ao jogo de caça ao tesouro!")
print("Tente encontrar o tesouro. Você tem 3 tentativas.")
print("Escolha um número entre 0 e 9 para procurar o tesouro.")
# Inicializa o contador de tentativas
contador = 0
# Loop para as tentativas do usuário
while contador != tentativas:
        contador += 1
        palpite = int(input("Escolha um índice para procurar o tesouro: "))  
        if 0 <= palpite <= 9:  # Verifica se o palpite está dentro do intervalo
            if locais[palpite] == 3: # SE O VALOR DA POSIÇÃO DO PALPITE FOR 3, ESTÁ CERTO, POIS É NECESSÁRIO PALPITAR SOBRE EM QUAL POSIÇÃO ESTÁ O VALOR 3.
                print("voce encontrou")
                break
            else:
                print("Não é esse o local do tesouro. Tente novamente.")
        else:
            print("Por favor, insira um número entre 0 e 9.") 


if(contador == tentativas):
    print(f"Suas tentativas acabaram! O tesouro estava no índice .")


# comparar com o código do exercicio1.py
# por que deu 2 tabs abaixo do while?
# por que consegue finalizar o loop sem usar break ou quit no último if?
# erro de lógica - continua o loop mesmo após acertar
# Qual o significado de if 0 <= palpite <= 9: ? 
    #Eu faria: if (palpite >= 0) and (palpite <= 9): 



