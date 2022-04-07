import sys


def postorder_traversal(para_preorder):
    len_pre = len(para_preorder)
    if len_pre <= 1:
        return para_preorder

    for i in range(1, len_pre):
        if para_preorder[i] > para_preorder[0]:
            return postorder_traversal(para_preorder[1: i]) + postorder_traversal(para_preorder[i:]) + [para_preorder[0]]

    return postorder_traversal(para_preorder[1:]) + [para_preorder[0]]


if __name__ == '__main__':
    sys.setrecursionlimit(100000)

    preorder_traversal = []
    while True:
        try:
            preorder_traversal.append(int(sys.stdin.readline()))
        except ValueError:
            break

    out_post = postorder_traversal(preorder_traversal)
    for o in out_post:
        print(o)
