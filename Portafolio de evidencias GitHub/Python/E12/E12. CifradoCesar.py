from argparse import ArgumentParser
import detectEnglish

def encriptar():
    message = input("Ingresa tu mensaje: ")
    espacios = 1
    while espacios > 0:
        clave = input('Ingresa tu palabra clave para cifrar: ')
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)
    translated = ''
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key

            #print(translatedIndex)

            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol

    return (translated)


def desencriptar():
    message = input("Ingresa tu mensaje: ")
    espacios = 1
    while espacios > 0:
        clave = input('Ingresa tu palabra clave para descifrar: ')
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)
    translated = ''
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol

    return (translated)

def hackeo ():
    message = input('Ingresa el mensaje: ')
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    for key in range(len(SYMBOLS)):
        translated = ''
        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                translated = translated + SYMBOLS[translatedIndex]
            else:
                translated = translated + symbol


        if detectEnglish.isEnglish(translated):
            print()
            print("Posible frase en español: ")
            return translated

def parseArguments():
    parser = ArgumentParser()
    parser.add_argument("--modo",dest="modo", help = "e encripta un pensaje, d desencripta un mensaje, c crackea un mensaje")
    #parser.add_argument("--msg",dest="mensaje",help="Escribe el mensaje para encriptar o desencriptar"
    return parser.parse_args()


opc = parseArguments()
if opc.modo == "e" :
    print(encriptar())
if opc.modo == "d":
    print(desencriptar())
if opc.modo == "c":
    print(hackeo())
