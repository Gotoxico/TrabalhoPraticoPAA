import unicodedata


#Função para retirar acentos
def remover_acentos(texto):
    # Normaliza o texto para decompor os caracteres acentuados
    texto = unicodedata.normalize('NFKD', texto)
    # Filtra apenas os caracteres que não são marcas diacríticas
    texto_sem_acentos = ''.join(c for c in texto if not unicodedata.combining(c))
    return texto_sem_acentos