import sys


def preorder_traversal(para_in_start, para_in_end, para_post_start, para_post_end):
    if para_in_start > para_in_end or para_post_start > para_post_end:
        return

    parent_node = postorder_traversal[para_post_end]
    out_pre.append(parent_node)

    num_left = left_node[parent_node] - para_in_start
    num_right = para_in_end - left_node[parent_node]

    preorder_traversal(para_in_start, para_in_start + num_left - 1, para_post_start, para_post_start + num_left - 1)
    preorder_traversal(para_in_end - num_right + 1, para_in_end, para_post_end - num_right, para_post_end - 1)


if __name__ == '__main__':
    in_n = int(sys.stdin.readline())
    inorder_traversal = list(map(int, sys.stdin.readline().split()))
    postorder_traversal = list(map(int, sys.stdin.readline().split()))

    left_node = [0 for _ in range(in_n + 1)]
    for n in range(in_n):
        left_node[inorder_traversal[n]] = n

    out_pre = []
    preorder_traversal(0, in_n - 1, 0, in_n - 1)
    print(*out_pre)
