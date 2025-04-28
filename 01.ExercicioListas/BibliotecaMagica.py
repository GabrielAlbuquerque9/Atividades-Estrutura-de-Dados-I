catalogo_magico = [] #Criando a lista chamada "catalogo_magico"

def adicionar_livro(catalogo, livro): #Função para adicionar os livros pedidos
    catalogo.append(livro) #".append" é utilizado para adicionar um item ao final de uma lista
adicionar_livro(catalogo_magico, "O Feitiço da Lua Crescente")
adicionar_livro(catalogo_magico, "A Jornada do Unicórnio Perdido")
adicionar_livro(catalogo_magico, "Segredos da Floresta Encantada")
print("Catálogo Mágico:", catalogo_magico)

def buscar_livro(catalogo, indice):#Retorna um livro do catalogo com base na sua posição na lista
    return catalogo[indice] #"[indice]" é a posição do livro na lista

livro_posicao_1 = buscar_livro(catalogo_magico, 1)# Busca o livro na posição 1
print("Livro na posição 1:", livro_posicao_1)

catalogo_magico.remove("A Jornada do Unicórnio Perdido")#".remove" Remove o livro "A Jornada do Unicórnio Perdido"
print("Catálogo Atualizado:", catalogo_magico)#Visualizar o novo catalogo

def verificar_livro(catalogo, livro):#Define uma função para verificar se o livro existe
    return livro in catalogo

presente = verificar_livro(catalogo_magico, "Segredos da Floresta Encantada") # Verifica se "Segredos da Floresta Encantada" esta no catalogo
print("Segredos da Floresta Encantada está no catálogo?", presente)
