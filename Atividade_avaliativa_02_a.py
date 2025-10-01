while start_campos:

    match campo:
        case 1:
            try:
                nome = str(input("Digite seu nome:  "))
                campo += 1
            except:
                print("valor nome invalido!")
        case 2:
                try:
                    idade = int(input("DIgite sua idade:   "))
                    campo += 1
                except:
                    print("idade invalida")
        case 3:
              try:
                   peso = float(input("Digite seu peso em kg:  "))
                   start_campos = False
                except:
                   print("peso invalido")

#devolver os dados
print("Seu nome e: ", Nome)
print("Sua idade e:", Idade)
print("Seu peso e:", Peso)   
            