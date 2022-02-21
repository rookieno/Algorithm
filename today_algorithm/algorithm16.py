def solution(participant, completion):
    participant.sort()
    completion.sort()
    dict = zip(participant, completion)

    for p,c in dict:
        if p != c:
            return p
    return participant.pop()


a = ["mislav", "stanko", "mislav", "ana"]
b = ["stanko", "ana", "mislav"]

print(solution(a, b))