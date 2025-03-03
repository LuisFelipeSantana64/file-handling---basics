# Abrindo e lendo o arquivo "Arvore - EM ORDEM.txt"
with open("Arvore - EM ORDEM.txt", "r") as arq:
    print(arq.read())  # Printa todo o conteúdo do arquivo
    print(arq.tell())  # Mostra o número de caracteres lidos

    arq.seek(0)  # Retorna para o início do arquivo
    print(arq.read(23))  # Lê e printa os primeiros 23 caracteres
    print(arq.tell())  # Mostra o número de caracteres lidos
    print(arq.read())  # Lê e printa o restante do arquivo

# Criando e sobrescrevendo "testando.txt"
with open("testando.txt", "w") as arq2:
    arq2.write("testando no write")  # Sobrescreve no arquivo

# Lendo o arquivo atualizado
with open("testando.txt", "r") as arq2:
    print(arq2.read())  # Mostra o conteúdo atualizado

# Abrindo o arquivo em modo "append" para adicionar texto
with open("testando.txt", "a") as arq2:
    arq2.write(", testando no append")  # Adiciona conteúdo sem sobrescrever

# Lendo novamente para verificar o conteúdo atualizado
with open("testando.txt", "r") as arq2:
    print(arq2.read())  # Mostra o conteúdo atualizado

    print("teste:", arq2.read())  # Não mostrará nada porque o cursor está no final

    arq2.seek(0)  # Retorna para o início do arquivo
    print("teste:", arq2.read())  # Agora printa corretamente o conteúdo
