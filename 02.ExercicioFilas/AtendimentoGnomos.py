from collections import deque
fila_de_pedidos = deque() #Criando uma fila

def adicionar_pedido(fila, pedido):#Função para adicionar pedidos
    fila.append(pedido)

adicionar_pedido(fila_de_pedidos, "Martelo Encantado")# Adicionando os pedidos
adicionar_pedido(fila_de_pedidos, "Pinça Teleportadora")
adicionar_pedido(fila_de_pedidos, "Chave de Fenda Sônica")
print("Fila de Pedidos:", list(fila_de_pedidos))

def processar_pedido(fila):#Função para processar o pedido
    if fila:
        return fila.popleft()#Remove e retorna o primeiro pedido
    else:
        return None

pedido_atendido = processar_pedido(fila_de_pedidos)#Processa o próximo pedido
print("Pedido atendido:", pedido_atendido)

def fila_vazia(fila):#Criando uma função para verificar se a fila esta vazia
    return len(fila) == 0

print("Fila está vazia?", fila_vazia(fila_de_pedidos))#Verifica se a fila ainda possui algum pedido
print("Fila de Pedidos Restante:", list(fila_de_pedidos))

while not fila_vazia(fila_de_pedidos):#enquanto houver pedidos a ação dentro do while vai continuar
    pedido = processar_pedido(fila_de_pedidos)#Chama a função para processar o primeiro pedido da fila
    print("Pedido atendido:", pedido)
print("Fila está vazia após atender todos os pedidos?", fila_vazia(fila_de_pedidos)) # Verifica se a fila esta vazia ao final
