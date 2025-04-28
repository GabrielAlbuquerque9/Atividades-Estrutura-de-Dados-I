torre_de_cristais = []#Crio uma pilha vazia

def empilhar_cristal(pilha, cristal):#Função para empilhar o cristal
    pilha.append(cristal)#Adiciona o cristal ao topo da pilha

empilhar_cristal(torre_de_cristais, "Cristal do Passado")#Empilhamento dos cristais, sendo que o ultimo deles ficará em primeiro na pilha
empilhar_cristal(torre_de_cristais, "Cristal do Presente")
empilhar_cristal(torre_de_cristais, "Cristal do Futuro")

print("Pilha de Cristais:", torre_de_cristais)

def desempilhar_cristal(pilha):#Função para desempilhar o cristal, sendo removido sempre o do topo (o ultimo adicionado)
    if pilha:
        return pilha.pop()#Remove e retorna o cristal do topo (final da lista)
    else:
        return None#Retorna None se a pilha estiver vazia

def pilha_vazia(pilha):#Função para verificar se a pilha esta vazia
    return len(pilha) == 0 #Retorna True se o tamanho da pilha for 0 ou False caso contrario

cristal_utilizado = desempilhar_cristal(torre_de_cristais) #para retirar o cristal do topo da pilha
print("Cristal utilizado no ritual:", cristal_utilizado)

print("Pilha restante de Cristais:", torre_de_cristais)#imprime a pilha atual

while not pilha_vazia(torre_de_cristais):#desempilhar os cristais restantes um por um
    cristal_utilizado = desempilhar_cristal(torre_de_cristais)
    print("Cristal utilizado no ritual:", cristal_utilizado)

print("A pilha está vazia?", pilha_vazia(torre_de_cristais))#Verifica se a pilha esta vazia
