# Crie uma lista de plavras sorteadas com base em uma lista de palavras fornecida pelo usuário. A lista de palavras sorteadas deve conter apenas palavras que tenham mais de 5 letras.
import random
palavras = ["python", "programacao", "computador", "teclado", "desenvolvimento", "codigo"]
palavra_secreta =  = random.choice(palavras).lower()
letras_descobertas = ["_"] * len(palavra_secreta)   
if chute in palavra_secreta:
            print(f"🎯 Boa! A letra '{chute}' existe na palavra!")
            # Atualiza os espaços '_' com a letra acertada na posição correta
            for indice, letra in enumerate(palavra_secreta):
                if letra == chute:
                    letras_descobertas[indice] = chute
        else:
            print(f"❌ Que pena, a letra '{chute}' não está na palavra.")
