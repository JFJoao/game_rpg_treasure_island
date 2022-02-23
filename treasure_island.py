print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is search the treasure.")
#Write your code below this line 👇
name = input(print("Qual seu nome aventureiro(a)?"))
choose_1 = input(print(f"Nobre {name} qual melhor tipo de urso, Urso preto, Urso pardo ou existem dois tipos de pensamentos aqui ?")) .lower()
if choose_1 == "urso preto":
    print("Você nao me parece muito confiavel. Volte por onde veio.")
elif choose_1 == "urso pardo":
    print("Sabia que nao deveria falar com um forasteiro.")
elif choose_1 == "existem dois tipos de pensamentos aqui.":
    print(f"Ó sábio {name}, por favor siga passagem em segurança por nossas estradas.")
else:
    print("Não consigo compreender vossas falas.")
choose_2 = print(f"Precisamos continuar por essa estrada, mas ela esta inundada, o que devemos fazer Mestre {name} ? Aguardar ou nadar, e abrir caminho ?") .lower()
if choose_2 == "aguardar":
    print("Vossa sabedoria nos salvou mais uma vez, as aguas eram uma armadilha e agora podemos proseguir em segurança.")
elif choose_2 == "nadar":
    print(f"Assim como Booba em a locomativa que podia, as coisas nao sairam como esperado, não é mesmo {name} ?")
else:
    print("Não consigo entender vosso idioma, ó forasteiro.")
choose_3 = input(print(f"Apos continuar por nosso caminho chegamos ao salão do tesouro, mas devemos escolher sabiamente qual porta devemos"
                       f" escolher, E então Alic... quer dizer {name} em qual porta devemos nos aventurar ? Verde, amarela ou a vermelha ?")) .lower()
if choose_3 == "verde":
    print("Quen Quen Queeeeeun, este é o salao do tempo e voce esta aprisionado, nem mesmo uma equipe da swat poderia tirar voce daqui agora.")
elif choose_3 == "amarela":
    print(f'''
    Você é o sabio das profecias, somente uma mente astuta seria capaz de encontrar tal tesouro, ó grande {name} por favor aceite essas montanhas de preciosidades.)
                 ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
          jgs `"""""""`
          ''')
elif choose_3 == "Vermelho":
    print("Se procuras o tesouro ? Esta no lugar certo, todas essas pessoas tambem procuraram ... e falharam, agora sao suas companheiras de cela, puxe uma cadeira e sintasse a vontade ")
else:
    print("Falar no idioma dos antigos nao ira lhe ajudar aqui, escolha uma das alternativas.")
