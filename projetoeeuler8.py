import random

def jogar():
    # Lista de palavras do próprio programa
    palavras = ["python", "programacao", "computador", "teclado", "desenvolvimento", "codigo"]
    
    # Escolhe uma palavra aleatoriamente
    palavra_secreta = random.choice(palavras).lower()
    
    # Cria a lista de letras descobertas com '_' para cada letra da palavra
    letras_descobertas = ["_"] * len(palavra_secreta)
    
    # Conjunto para armazenar as letras que o jogador já chutou
    letras_chutadas = set()
    
    tentativas = 6  # Limite de tentativas erradas
    
    print("=== JOGO DA ADIVINHAÇÃO DE PALAVRAS ===")
    print(f"A palavra tem {len(palavra_secreta)} letras.")
    
    while tentativas > 0 and "_" in letras_descobertas:
        print("\nPalavra: " + " ".join(letras_descobertas))
        print(f"Tentativas restantes: {tentativas}")
        if letras_chutadas:
            print(f"Letras já tentadas: {', '.join(sorted(letras_chutadas))}")
        
        chute = input("Digite uma letra: ").strip().lower()
        
        # Validação do chute
        if len(chute) != 1 or not chute.isalpha():
            print("⚠️ Por favor, digite apenas uma única letra válida!")
            continue
            
        if chute in letras_chutadas:
            print("⚠️ Você já chutou essa letra antes. Tente outra!")
            continue
            
        letras_chutadas.add(chute)
        
        # Verifica se a letra está na palavra secreta
        if chute in palavra_secreta:
            print(f"🎯 Boa! A letra '{chute}' existe na palavra!")
            # Atualiza os espaços '_' com a letra acertada na posição correta
            for indice, letra in enumerate(palavra_secreta):
                if letra == chute:
                    letras_descobertas[indice] = chute
        else:
            print(f"❌ Que pena, a letra '{chute}' não está na palavra.")
            tentativas -= 1

    # Fim do jogo
    print("\n" + "="*35)
    if "_" not in letras_descobertas:
        print(f"🎉 Parabéns! Você acertou a palavra: {palavra_secreta.upper()}")
    else:
        print(f"💥 Suas tentativas acabaram! A palavra era: {palavra_secreta.upper()}")
    print("="*35)

if __name__ == "__main__":
    jogar()