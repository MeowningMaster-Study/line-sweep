class AVLNode:
    def __init__(self, segment):
        self.segment = segment
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, segment):
        self.root = self._insert(self.root, segment)

    def _insert(self, node, segment):
        if node is None:
            return AVLNode(segment)

        if segment.p1 < node.segment.p1:
            node.left = self._insert(node.left, segment)
        else:
            node.right = self._insert(node.right, segment)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and segment.p1 < node.left.segment.p1:
            return self._rotate_right(node)

        if balance < -1 and segment.p1 > node.right.segment.p1:
            return self._rotate_left(node)

        if balance > 1 and segment.p1 > node.left.segment.p1:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and segment.p1 < node.right.segment.p1:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
