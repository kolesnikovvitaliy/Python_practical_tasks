def split_rope(root, k):
    if root is None:
        return None
    
    if root.left is not None:
        if k < root.left.length:
            root.left = split_rope(root.left, k)
            root = rotate_right(root)
        elif k > root.left.length:
            root.right = split_rope(root.right, k - root.left.length - 1)
            root = rotate_left(root)
    
    return root

class RopeNode:
    def __init__(self, s):
        self.left = None
        self.right = None
        self.val = s
        self.length = len(s)
        
def rotate_right(node):
    if node is None or node.left is None:
        return node
    
    new_root = node.left
    node.left = new_root.right
    new_root.right = node
    
    return new_root

def build_rope(s):
    root = RopeNode(s)
    return root

def concatenate(rope1, rope2):
    if rope1 is None:
        return rope2
    if rope2 is None:
        return rope1
    root = RopeNode(rope1.val + rope2.val)
    root.length = rope1.length + rope2.length
    root.left = rope1
    root.right = rope2
    return root

def find_substring(root, i, j):
    if root is None or j < i:
        return ""
    if i == 0 and j == root.length - 1:
        return root.val
    if j < root.left.length:
        return find_substring(root.left, i, j)
    elif i >= root.left.length:
        return find_substring(root.right, i - root.left.length, j - root.left.length)
    else:
        left_substr = find_substring(root.left, i, root.left.length - 1)
        right_substr = find_substring(root.right, 0, j - root.left.length)
        return left_substr + right_substr

def split_rope(root, k):
    if root is None:
        return None, None
    if k == 0:
        return None, root
    if k == root.length:
        return root, None
    if root.left is not None:
        if k < root.left.length:
            root.left = split_rope(root.left, k)
            root = rotate_right(root)
        elif k > root.left.length:
            root.right = split_rope(root.right, k - root.left.length - 1)
            root = rotate_left(root)
    else:
        left_part = root.left
        right_part = root.right
        root.left = None
        root.right = None
    root.length = get_length(root)
    return left_part, right_part

def get_length(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return len(root.val)
    if root.left is None:
        return len(root.val) + get_length(root.right)
    if root.right is None:
        return len(root.val) + get_length(root.left)
    return len(root.val) + get_length(root.left) + get_length(root.right)

def perform_operations(s, operations):
    root = build_rope(s)
    for op in operations:
        i, j, k = op.split()
        i = int(i)
        j = int(j)
        k = int(k)
        if i > j or i < 0 or j >= root.length or k < 0 or k > root.length - (j - i + 1):
            continue
        left, mid_right = split_rope(root, i)
        mid, right = split_rope(mid_right, j - i + 1)
        left, right = split_rope(root, k)
        root = concatenate(concatenate(left, mid), right)
    return root.val

# Входные данные
s = "hlelowrold"
operations = ["1 1 2", "6 6 7"]

# Выполнение операций
result = perform_operations(s, operations)

# Вывод результата
print(result)  # Вывод: helloworld