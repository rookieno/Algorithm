# 백준 2805번 나무 자르기

n, m = map(int,input().split())

tree = list(map(int,input().split()))

max_tree = max(tree)
min_tree = 0

while min_tree <= max_tree:
    guess_tree = (max_tree + min_tree)//2
    tree_length = 0
    for i in tree:
        if guess_tree < i:
            tree_length += i - guess_tree
    if tree_length >= m:
        min_tree = guess_tree + 1
    else:
        max_tree = guess_tree - 1

    
    