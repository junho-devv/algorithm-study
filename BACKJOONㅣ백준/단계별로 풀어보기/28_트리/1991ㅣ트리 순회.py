import sys


def preorder_traversal(para_node):
    global out_1

    if para_node == -18:
        return
    else:
        out_1 += chr(para_node + 64)
        preorder_traversal(tree_n[para_node][0])
        preorder_traversal(tree_n[para_node][1])


def inorder_traversal(para_node):
    global out_2

    if para_node == -18:
        return
    else:
        inorder_traversal(tree_n[para_node][0])
        out_2 += chr(para_node + 64)
        inorder_traversal(tree_n[para_node][1])


def postorder_traversal(para_node):
    global out_3

    if para_node == -18:
        return
    else:
        postorder_traversal(tree_n[para_node][0])
        postorder_traversal(tree_n[para_node][1])
        out_3 += chr(para_node + 64)


if __name__ == '__main__':
    in_n = int(sys.stdin.readline())

    tree_n = [[] for _ in range(in_n + 1)]
    for _ in range(in_n):
        in_a, in_b, in_c = map(str, sys.stdin.readline().split())

        ord_a, ord_b, ord_c = ord(in_a) - 64, ord(in_b) - 64, ord(in_c) - 64
        tree_n[ord_a].append(ord_b)
        tree_n[ord_a].append(ord_c)

    out_1 = ""
    preorder_traversal(1)
    print(out_1)

    out_2 = ""
    inorder_traversal(1)
    print(out_2)

    out_3 = ""
    postorder_traversal(1)
    print(out_3)
