alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,;._#*\"-+"

def verifica_texto(texto):
    x = 0
    while x < len(texto):
        letra = texto[x]
        achou = False
        y = 0
        while y < len(alfabeto):
            if letra == alfabeto[y]:
                achou = True
            y = y + 1
        if achou == False:
            print("Erro: caractere '" + letra + "' não permitido!")
            raise ValueError
        x = x + 1

def esticar_chave(chave, tamanho):
    resultado = ""
    i = 0
    while len(resultado) < tamanho:
        resultado = resultado + chave[i]
        i = i + 1
        if i == len(chave):
            i = 0
    return resultado

def cifrar(mensagem, chave):
    verifica_texto(mensagem)
    verifica_texto(chave)
    chave_grande = esticar_chave(chave, len(mensagem))
    texto_final = ""
    i = 0
    while i < len(mensagem):
        letra_msg = mensagem[i]
        letra_chave = chave_grande[i]
        pos_msg = 0
        pos_chave = 0
        p = 0
        while p < len(alfabeto):
            if alfabeto[p] == letra_msg:
                pos_msg = p
            if alfabeto[p] == letra_chave:
                pos_chave = p
            p = p + 1
        nova_pos = pos_msg + pos_chave
        while nova_pos >= len(alfabeto):
            nova_pos = nova_pos - len(alfabeto)
        texto_final = texto_final + alfabeto[nova_pos]
        i = i + 1
    return texto_final

def decifrar(mensagem_cifrada, chave):
    verifica_texto(mensagem_cifrada)
    verifica_texto(chave)
    chave_grande = esticar_chave(chave, len(mensagem_cifrada))
    texto_final = ""
    i = 0
    while i < len(mensagem_cifrada):
        letra_cif = mensagem_cifrada[i]
        letra_chave = chave_grande[i]
        pos_cif = 0
        pos_chave = 0
        p = 0
        while p < len(alfabeto):
            if alfabeto[p] == letra_cif:
                pos_cif = p
            if alfabeto[p] == letra_chave:
                pos_chave = p
            p = p + 1
        nova_pos = pos_cif - pos_chave
        while nova_pos < 0:
            nova_pos = nova_pos + len(alfabeto)
        texto_final = texto_final + alfabeto[nova_pos]
        i = i + 1
    return texto_final

def salvar_chave(chave):
    try:
        arquivo = open("chave.txt", "w")
        arquivo.write(chave)
        arquivo.close()
    except:
        print("Erro ao salvar a chave!")

def carregar_chave():
    try:
        arquivo = open("chave.txt", "r")
        conteudo = arquivo.read()
        arquivo.close()
        return conteudo.strip()
    except:
        return ""

def principal():
    print("Alfabeto: " + alfabeto)
    print("1 - Encriptar")
    print("2 - Decriptar")
    escolha = input("Digite 1 ou 2: ")
    if escolha != "1" and escolha != "2":
        print("Opção errada!")
        return
    if escolha == "1":
        msg = input("Mensagem: ")
        chave = input("Chave: ")
        try:
            resultado = cifrar(msg, chave)
            salvar_chave(chave)
            print("Mensagem cifrada: " + resultado)
            print("Chave salva no arquivo.")
        except:
            print("Erro na cifragem!")
    else:
        chave = carregar_chave()
        if chave == "":
            print("Arquivo da chave não encontrado!")
            return
        msg = input("Mensagem cifrada: ")
        try:
            resultado = decifrar(msg, chave)
            print("Mensagem original: " + resultado)
            print("Chave usada: " + chave)
        except:
            print("Erro na decifragem!")

if __name__ == "__main__":
    principal()
