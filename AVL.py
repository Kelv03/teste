class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class ArvoreAVL:

    def __init__(self):
        self.raiz = None


    def altura(self, no):
        if not no:
            return 0
        return 1 + max(self.altura(no.esquerda), self.altura(no.direita))

    def fator_balanceamento(self, no):
        if not no:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        return x

    def rotacao_esquerda(self, x):
        y = x.direita
        T2 = y.esquerda

        y.esquerda = x
        x.direita = T2

        return y

    def inserir(self, no):
        self.raiz = self._inserir(self.raiz, no)

    def _inserir(self, raiz, no):
        # Caso base: se a raiz for None, retorne o novo nó.
        if not raiz:
            return no
        
        # Se a chave do novo nó for menor que a chave da raiz,
        # insira o nó na subárvore esquerda.
        elif no.chave < raiz.chave:
            raiz.esquerda = self._inserir(raiz.esquerda, no)
        
        # Se a chave do novo nó for maior que a chave da raiz,
        # insira o nó na subárvore direita.
        else:
            raiz.direita = self._inserir(raiz.direita, no)
        
        # Calcule o fator de balanceamento do nó raiz para verificar se ele ficou desbalanceado.
        balanceamento = self.fator_balanceamento(raiz)
        
        # Se o nó ficar desbalanceado, existem quatro casos possíveis:

        # Caso 1 - Rotação à direita simples (LL)
        # Ocorre quando a nova chave é inserida na subárvore esquerda da subárvore esquerda do nó raiz.
        if balanceamento > 1 and no.chave < raiz.esquerda.chave:
            return self.rotacao_direita(raiz)
        
        # Caso 2 - Rotação à esquerda simples (RR)
        # Ocorre quando a nova chave é inserida na subárvore direita da subárvore direita do nó raiz.
        if balanceamento < -1 and no.chave > raiz.direita.chave:
            return self.rotacao_esquerda(raiz)
        
        # Caso 3 - Rotação à esquerda-direita (LR)
        # Ocorre quando a nova chave é inserida na subárvore direita da subárvore esquerda do nó raiz.
        # Primeiro, realiza-se uma rotação à esquerda na subárvore esquerda do nó raiz,
        # seguida por uma rotação à direita no nó raiz.
        if balanceamento > 1 and no.chave > raiz.esquerda.chave:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)
        
        # Caso 4 - Rotação à direita-esquerda (RL)
        # Ocorre quando a nova chave é inserida na subárvore esquerda da subárvore direita do nó raiz.
        # Primeiro, realiza-se uma rotação à direita na subárvore direita do nó raiz,
        # seguida por uma rotação à esquerda no nó raiz.
        if balanceamento < -1 and no.chave < raiz.direita.chave:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)
        
        # Retorne o ponteiro da raiz (inalterado)
        return raiz

    def pre_ordem(self, raiz):
        if not raiz:
            return
        print("{0} ".format(raiz.chave), end="")
        self.pre_ordem(raiz.esquerda)
        self.pre_ordem(raiz.direita)

arvore = ArvoreAVL()
raiz = None

chaves = [10, 20, 30, 40, 50, 25, 32, 3, 5, 80, 36, 55, 66, 77, 88, 99, 100, 101, 102, 103, 104, 105, 106, 107]

for chave in chaves:
    no = No(chave)
    raiz = arvore.inserir( no)

print("Imprimir em pré-ordem a árvore AVL:")
arvore.pre_ordem(arvore.raiz)