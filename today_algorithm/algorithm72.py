# 백준 9663번 N-Queen
import sys

def is_promising(i, col):
    k = 1
    flag = True
    while k < i and flag:
        if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
            flag = False
        k += 1
    return flag

def n_queens(i, col):
    n = len(col) - 1
    global cnt
    if is_promising(i,col):
        if i == n:
           cnt += 1 
        #    print(col[1: n+1])
           return
        else:
            for j in range(1, n+1):
                col[i+1] = j
                n_queens(i+1, col)

# 최적화 문제
def queen(row):
    global cnt
    if row == n:
        cnt += 1
        return
    for col in range(n):
        flag = True
        for i in range(row):
            if graph[i] == col or row - i == abs(col - graph[i]):
                flag = False
                break
        if flag:
            graph[row] = col
            queen(row+1)



n = int(sys.stdin.readline())
cnt = 0
graph = [0] * n
n_queens(0, graph)
queen(0)
print(cnt)

# 되추적 backtrack
# 상태 공간 트리 (state space tree) : 탐색 공간을 트리 형태의 구조로 암묵적으로 해석
# 상태 공간: 해답을 탐색하기 위한 탐색 공간
# 최적화 문제라면 모든 상태 공간 트리를 다 방문 해야함
# 백트래킹 기법 : 상태 공간 트리를 깊이우선탐색으로 탐색

# 유망항(promising)을 판단하는 것이 중요
# 방문중인 노드에서 하위 노드가 해답을 발견할 가능성이 있으면 유망
# 하위 노드에서 해답을 발견할 가능성이 없으면 유망하지 않음

# 가지치기(pruning): 유망하지 않으면 하위 트리를 가지치기함

# 유망하냐 안하냐를 판단하는게 포인트

# 백트래킹 알고리즘의 구현
# 상태 공간 트리를 실제로 구현할 필요는 없다.
# 현재 조사중인 가지의 값에 대해 추적만 하면 됨
# python3 로 백트래킹을 풀려면 엄창난 최적화가 필요허다

