from curses.ascii import isalpha, isdigit
from unicodedata import digit
import const

#-----------------------------------
def menu():
    print("");
    print("##############################");
    print("# Escolha o tipo de calculo: #");
    print("# 1 - Área do triângulo.     #");
    print("# 2 - Área do quadrado.      #");
    print("# 3 - Área do trapézio.      #");
    print("# 4 - Área do círculo.       #");
    print("# 5 - Área retângulo.        #");
    print("# 6 - Área losango.          #");
    print("# 7 - Circunferência.        #");
    print("##############################");
    print("");

def _medida():
    print("");
    print("Escolha entre: ");
    print("1 - cm");
    print("2 - m");
    print("");

def _filtro(valor):
    a = valor;
    char =set(const.DICI);
    res = ''.join(filter(lambda x: x not in char, a));
    valor = res;
    
    if "." in valor:
            valor = float(valor);
    else:
        valor = valor.replace(",", ".");
        valor = float(valor);
    return valor

def resultado(calculo):
    calculo = str(calculo);
    calculo = calculo.replace(".", ",");
    return calculo
#------------------------------------
#------------------------------------
programa = True
while(programa): 
    
    _medida()
    padrao = int(input("Opção: "));
    if padrao == 1:
        medida = "cm";
    elif padrao == 2:
        medida = "m";
    else:
        print("Inválido! ");
    
    menu()
    x = int(input("Digite a opção: "));
    print("");
    
    if x == 1:
        print("Área do triângulo");
        print("");
        print("Digite os valores abaixo: ");
        print("")
        
        valor = str(input("Valor da base: "));
        valorBase = _filtro(valor)

        valor = str(input("Valor da altura: "));
        print("");
        valorAltura = _filtro(valor) 
        #------------------------------------
        calculo = valorBase * valorAltura / 2;
        #------------------------------------
        resposta = resultado(calculo)
        print("Área resultante: ", resposta, medida,"2");
    
    elif x == 2:
        print("Área do quadrado");
        print("");
        print("Digite o valor abaixo:");
        print("");

        valor = str(input("Valor do lado: "));
        print("");
        ladoQua = _filtro(valor)
        #------------------------------------
        calculo = ladoQua ** 2;
        #------------------------------------
        resposta = resultado(calculo)
        print("Área resultante: ", resposta, medida,"2");

    elif x == 3:
        print("Área Trapézio");
        print("");
        print("Digite os valores abaixo:");
        print("");

        valor = str(input("Valor da base menor: "));
        baseMenor = _filtro(valor)
        
        valor = str(input("Valor da base maior: "));
        baseMaior = _filtro(valor)
        
        valor = str(input("Valor da altura: "));
        print("");
        alturaTra = _filtro(valor)
        #------------------------------------
        calculo = (baseMenor + baseMaior) * alturaTra / 2;
        #------------------------------------
        resposta = resultado(calculo)
        print("Área resultante: ", resposta, medida,"2");

    elif x == 4:
        print("Área do círculo");
        print("");
        print("Escolha o método: ");
        print("1 - Utilizando diâmetro.");
        print("2 - Utilizando raio.");
        print("");
        
        x = int(input("Digite a opção: "));
        print("");
        
        if x == 1:
            print("Digite o valor abaixo:");
            print("");

            valor = str(input("Valor do diâmetro: "));
            diametro = _filtro(valor)
            #------------------------------------
            calculo = (diametro / 2) ** 2 * const.PI;
            #------------------------------------
            resposta = resultado(calculo)
            print("Área do círculo: ", resposta1, medida, "2");
        
        elif x == 2:
            print("Digite o valor abaixo:");
            print("");

            valor = str(input("Valor do raio: "));
            raio = _filtro(valor)
            #------------------------------------
            calculo = const.PI * raio ** 2;
            #------------------------------------
            resposta = resultado(calculo)
            print("Área do círculo: ", resposta, medida, "2");
        else:
            print("Inválido");
            print("");
    
    elif x == 5:
        print("Área do retângulo: ", resposta);

    elif x == 6:
        print("Área do losango: ", resposta);


    elif x == 7:
        print("Circunferência");
        print("");
        print("Escolha o metodo: ");
        print("1 - Utilizando diâmetro.");
        print("2 - Utilizando raio.");
        print("");
        
        x = int(input("Digite a opção: "));
        print("");
        
        if x == 1:
            print("Digite o valor abaixo:");
            print("");

            valor = str(input("Valor do diâmetro: "));
            diametro = _filtro(valor)
            #------------------------------------
            calculo = const.PI * diametro;
            #------------------------------------
            resposta = resultado(calculo);
            print("Circunferência: ", resposta, medida);
        
        elif x == 2:
            print("Digite o valor abaixo:");
            print("");

            valor = str(input("Valor do raio: "));
            raio = _filtro(valor)
            #------------------------------------
            calculo = 2 * const.PI * raio;
            #------------------------------------
            resposta = resultado(calculo);
            print("Circunferência: ", resposta, medida);
        else:
            print("Inválido");
    else:
        print("Menu inválido"); 

    retorno = True;
    while(retorno):
        print("");
        print("Deseja realizar outra operação?[S/N]");
        print("");
        resposta1 = (input("Digite uma das opções dadas: "));
        if resposta1 == "S" or resposta1 == "s":
            programa = True
            retorno = False;
        elif resposta1 == "N" or resposta1 == "n":
            programa = False
            retorno = False;
        else:
            print("Inválido! ");
            print("");
            retorno = True;
