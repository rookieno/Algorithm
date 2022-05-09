# 백준 1181번 단어 정렬
n = int(input())

words = []

for _ in range(n):
    words.append(input())

words = set(words)

sorted_words = sorted(words, key=lambda x:(len(x),x))

for i in sorted_words:
    print(i)
