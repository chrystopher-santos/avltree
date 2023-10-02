class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Altura inicial do nó é 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def search(self, key):
        return self._search(self.root, key)

   
    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        if node is not None:
            node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self._update_height(z)
        self._update_height(y)

        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self._update_height(y)
        self._update_height(x)

        return x

    def _balance(self, node):
        if node is None:
            return node

        self._update_height(node)

        balance = self._balance_factor(node)

        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # Métodos da Árvore AVL

    def _insert(self, root, key):
        # Método interno para inserção
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        return self._balance(root)

    def _delete(self, root, key):
        # Método interno para exclusão
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            min_node = self._find_min(root.right)
            root.key = min_node.key
            root.right = self._delete(root.right, min_node.key)

        return self._balance(root)

    def _find_min(self, node):
        # Encontra o nó com o valor mínimo na árvore
        while node.left is not None:
            node = node.left
        return node

    def _search(self, root, key):
        # Método interno para pesquisa
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        if node is not None:
            node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self._update_height(z)
        self._update_height(y)

        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self._update_height(y)
        self._update_height(x)

        return x

    def _balance(self, node):
        if node is None:
            return node

        self._update_height(node)

        balance = self._balance_factor(node)

        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node
    
    # Métodos internos da Árvore AVL
    def insert_key(self, key):
        # Método público para inserir uma chave
        self.insert(key)

    def delete_key(self, key):
        # Método público para excluir uma chave
        self.delete(key)

    def search_key(self, key):
        # Método público para pesquisar uma chave
        return self.search(key)

    def inorder_traversal(self, root):
        # Percorre a árvore em ordem
        result = []
        if root:
            result = self.inorder_traversal(root.left)
            result.append(root.key)
            result = result + self.inorder_traversal(root.right)
        return result

    def display(self):
        # Retorna uma lista ordenada dos elementos na árvore
        result = self.inorder_traversal(self.root)
        return result

#Exemplo de uso:
avl_tree = AVLTree()
avl_tree.insert_key(10)
avl_tree.insert_key(20)
avl_tree.insert_key(30)
avl_tree.insert_key(40)
avl_tree.insert_key(50)

print("Árvore AVL após inserção:")
print(avl_tree.display())

avl_tree.delete_key(30)
print("Árvore AVL após exclusão do nó com chave 30:")
print(avl_tree.display())

search_result = avl_tree.search_key(20)
if search_result:
    print("Chave 20 encontrada na árvore.")
else:
    print("Chave 20 não encontrada na árvore.")