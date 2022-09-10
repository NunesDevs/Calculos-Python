from curses.ascii import isalpha, isdigit
from unicodedata import digit
import const

menu = True;
while(menu):
    
    print("");
    print("Escolha o tipo de calculo:");
    print("1 - Área do triângulo.");
    print("2 - Área do quadrado.");
    print("3 - Área do trapézio.");
    print("4 - Área do círculo.");
    print("5 - Circunferencia.");
    print("");
    
    x = int(input("Digite a opção: "));
    print("");
    
    if x == 1:
        
        print("Área do triângulo");
        print("");
        print("Digite os valores abaixo: ");
        print("")

        valorBase = str(input("Valor da base: "));
        
        a = valorBase;
        char =set(const.DICI);
        res = ''.join(filter(lambda x: x not in char, a));
        valorBase = res;
        
        if "." in valorBase:
            valorFloat_B = float(valorBase);
        else:
            valorRep_B = valorBase.replace(",", ".");
            valorFloat_B = float(valorRep_B);
        
        valorAltura = str(input("Valor da altura: "));
        print("");
        
        a = valorAltura;
        char = set(const.DICI);
        res = ''.join(filter(lambda x: x not in char, a));
        valorAltura = res;
        
        if "." in valorAltura:
            valorFloat_A = float(valorRep_A);
        else:
            valorRep_A = valorAltura.replace(",", ".");
            valorFloat_A = float(valorRep_A);
        
        calculo = valorFloat_B * valorFloat_A / 2;
        resultado = str(calculo);
        resultadoConvertido = resultado.replace(".", ",");
        print("Área resultante: ", resultadoConvertido);
    
    elif x == 2:
        
        print("Área do quadrado");
        print("");
        print("Digite o valor abaixo:");
        print("");

        ladoQua = str(input("Valor do lado: "));
        print("");
        
        a = ladoQua;
        char =set(const.DICI);
        res = ''.join(filter(lambda x: x not in char, a));
        ladoQua = res;
        
        if "." in ladoQua:
            valorFloat_LQ = float(ladoQua);
        else:
            valorRep_LQ = ladoQua.replace(",", ".");
            valorFloat_LQ = float(valorRep_LQ);
        
        calculo = valorFloat_LQ ** 2;
        resultado = str(calculo);
        resultadoConvertido = resultado.replace(".", ",");
        print("Área resultante: ", resultadoConvertido);

    elif x == 3:

        print("Área Trapézio");
        print("");
        print("Digite os valores abaixo:");
        print("");

        baseMenor = str(input("Valor da base menor: "));
        
        a = baseMenor;
        char =set(const.DICI);
        res = ''.join(filter(lambda x: x not in char, a));
        baseMenor = res;
        
        if "." in baseMenor:
            valorFloat_Bm = float(baseMenor);
        else:
            valorRep_Bm = baseMenor.replace(",", ".");
            valorFloat_Bm = float(valorRep_Bm);
        
        baseMaior = str(input("Valor da base maior: "));
        
        a = baseMaior;
        char =set(const.DICI);
        res = ''.join(filter(lambda x: x not in char, a));
        baseMaior = res;
        
        if "." in baseMaior:
            valorFloat_BM = float(baseMaior);
        else:
            valorRep_BM = baseMaior.replace(",", ".");
            valorFloat_BM = float(valorRep_BM);
        
        alturaTra = str(input("Valor da altura: "));
        print("");
        
        a = alturaTra;
        char =set(const.DICI);
        res = ''.join(filter(lambda x: x not in char, a));
        alturaTra = res;
        
        if "." in alturaTra:
            valorFloat_At = float(alturaTra);
        else:
            valorRep_At = alturaTra.replace(",", ".");
            valorFloat_At = float(valorRep_At);
        
        calculo = (valorFloat_Bm + valorFloat_BM) * valorFloat_At / 2;
        resultado = str(calculo);
        resultadoConvertido = resultado.replace(".",",");
        print("Área resultante: ", resultadoConvertido);

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

            diametro = str(input("Valor do diâmetro: "));
            
            a = diametro;
            char = set(const.DICI);
            res = ''.join(filter(lambda x: x not in char, a));
            diametro = res

            if "." in diametro:
                ValorDiametro = float(diametro);
            else:
                ValorRep_D = diametro.replace(",", ".");
                ValorDiametro = float(ValorRep_D);

            calculo = (ValorDiametro / 2) ** 2 * const.PI;
            resultado = str(calculo);
            resultadoConvertido= resultado.replace(".", ",");

            print("Área do círculo: ", resultadoConvertido);
        
        elif x == 2:
            print("Digite o valor abaixo:");
            print("");

            raio = str(input("Valor do raio: "));
            
            a = raio;
            char = set(const.DICI);
            res = ''.join(filter(lambda x: x not in char, a));
            raio = res;

            if "." in raio:
                ValorRaio = float(raio);
            else:
                ValorRep_R = raio.replace(",", ".");
                ValorRaio = float(ValorRep_R);

            calculo = const.PI * ValorRaio ** 2;
            resultado = str(calculo);
            resultadoConvertido = resultado.replace(".", ",");

            print("Área do círculo: ", resultadoConvertido);
        else:
            print("Inválido");
            print("");
    
    elif x == 5:

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

            diametro = str(input("Valor do diâmetro: "));
            
            a = diametro;
            char = set(const.DICI);
            res = ''.join(filter(lambda x: x not in char, a));
            diametro = a;

            if "." in diametro:
                ValorDiametro = float(diametro);
            else:
                ValorRep_D = diametro.replace(",", ".");
                ValorDiametro = float(ValorRep_D);

            calculo = const.PI * ValorDiametro;
            resultado = str(calculo);
            resultadoConvertido = resultado.replace(".", ",");
            print("Circunferência: ", resultadoConvertido);
        
        elif x == 2:
            print("Digite o valor abaixo:");
            print("");

            raio = str(input("Valor do raio: "));
            
            a = raio;
            char = set(const.DICI);
            res = ''.join(filter(lambda x: x not in char, a));
            raio = a;

            if "." in raio:
                ValorRaio = float(raio);
            else:
                ValorRep_R = raio.replace(",", ".");
                ValorRaio = float(ValorRep_R);

            calculo = 2 * const.PI * ValorRaio;
            resultado = str(calculo);
            resultadoConvertido = resultado.replace(".",",");
            print("Circunferência: ", resultadoConvertido);
        else:
            print("Inválido");
    else:
        print("Menu inválido"); 
    print("");


    retorno = True;

    while(retorno):
        print("Deseja realizar outra operação?");
        print("S");
        print("N");
        print("");

        resposta = input("Digite uma das opções dadas: ");
        if resposta == "S" or "s":
            menu = True;
            retorno = False;
        elif resposta == "N" or "n":
            menu = False;
            retorno = False;
        else:
            print("Inválido! ");
            print("");

            retorno = True;
