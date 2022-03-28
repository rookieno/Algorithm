# 백준 10828 스택
import sys

n = int(input())

stack = []

for i in range(n):
        order = sys.stdin.readline().split()

        if order[0] == 'push':
                stack.append(int(order[1]))
        
        if order[0] == 'pop':
                if len(stack) != 0:
                        print(stack.pop())
                        
                else:
                        print(-1)
        if order[0] == 'size':
                print(len(stack))
        
        if order[0] == 'empty':
                if len(stack) == 0:
                        print(1)
                else:
                        print(0)
        if order[0] == 'top':
                if len(stack) != 0:
                        print(stack[-1])
                else:
                        print(-1)