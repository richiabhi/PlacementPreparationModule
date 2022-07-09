def merge(a, b):
    temp = Node(0)
    res = temp
    while a and b:
        if a.data < b.data:
            temp.bottom = a
            a = a.bottom
            temp = temp.bottom
        else:
            temp.bottom = b
            temp = temp.bottom
            b = b.bottom
    temp.bottom = a if a else b
    return res.bottom


def flatten(root):
    #Your code here
    if root is None or root.next is None:
        return root
    root.next = flatten(root.next)
    root = merge(root, root.next)
    return root
