palavra_secreta= 'PERFUME'
digitos=[]
chances= 4



while True:

    if chances<=0:
        print('você perdeu, tente novamente!')
        break
    letra = input('Digite uma letra ').upper()


    if len(letra)>1:
        print('Não valeu! tente novamente digitando apenas uma letra.')
        continue

    digitos.append(letra)
    if letra not in palavra_secreta:

        print(f'Poxa! "{letra}" não se encontra na palavra secreta')


        digitos.pop()



    secreto_temp= ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in digitos:
            secreto_temp+= letra_secreta
        else:
            secreto_temp+='-'

    if secreto_temp== palavra_secreta:

        print('Parabéns, você venceu!')

        break
    else:
        print(f'a palavra_secreta está assim {secreto_temp}')

    if letra not in palavra_secreta:
        chances-= 1
        print(f'você só tem {chances} chances.' )
        