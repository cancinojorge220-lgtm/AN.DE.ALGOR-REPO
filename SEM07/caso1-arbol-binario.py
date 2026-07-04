# Árbol Binario
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # Insertar un valor en el árbol
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    # Función recursiva para insertar un valor
    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    #  Representación gráfica del árbol
    def display(self):
        def _get_lines(node):
            if not node: return [" "], 0, 0
            left_lines, left_pos, left_width = _get_lines(node.left)
            right_lines, right_pos, right_width = _get_lines(node.right)
            label = str(node.value)
            label_len = len(label)
            lines = [(" " * (left_width + 1)) + label + (" " * (right_width + 1))]
            if node.left and node.right:
                lines.append((" " * left_pos) + "/" + (" " * (left_width - left_pos + 1)) + "\\" + (" " * (right_pos)))
            elif node.left:
                lines.append((" " * left_pos) + "/" + (" " * (left_width - left_pos + label_len)))
            elif node.right:
                lines.append((" " * (left_width + 1)) + "\\" + (" " * (right_width - right_pos)))
            for i in range(max(len(left_lines), len(right_lines))):
                l = left_lines[i] if i < len(left_lines) else " " * left_width
                r = right_lines[i] if i < len(right_lines) else " " * right_width
                lines.append(l + " " * (label_len + 2) + r)
            return lines, left_width + 1 + left_pos, left_width + 1 + right_width + label_len

        lines, _, _ = _get_lines(self.root)
        print("\n1. Representación gráfica del árbol:")
        print("\n".join(lines))

    # Recorridos y Características
    def get_traversal(self, order):
        result = []
        def traverse(node):
            if not node: return
            if order == 'pre': result.append(node.value)
            traverse(node.left)
            if order == 'in': result.append(node.value)
            traverse(node.right)
            if order == 'post': result.append(node.value)
        traverse(self.root)
        return result

    # Características del árbol
    def count_nodes(self, node):
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right) if node else 0

    # Altura del árbol
    def get_height(self, node):
        return 1 + max(self.get_height(node.left), self.get_height(node.right)) if node else -1

    # Cantidad de nodos hoja
    def count_leaves(self, node):
        if not node: return 0
        if not node.left and not node.right: return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

# Ejemplo de uso
values = [50, 30, 70, 20, 40, 60, 80, 10, 25]
tree = BinaryTree()
for v in values:
    tree.insert(v)

# Mostrar resultados
tree.display()
print(f"\n2. Recorridos:")
print(f"Preorden: {tree.get_traversal('pre')}")
print(f"Inorden: {tree.get_traversal('in')}")
print(f"Postorden: {tree.get_traversal('post')}")

print(f"\n3. Características:")
print(f"Número total de nodos: {tree.count_nodes(tree.root)}")
print(f"Altura del árbol: {tree.get_height(tree.root)}")
print(f"Cantidad de nodos hoja: {tree.count_leaves(tree.root)}")