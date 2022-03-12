from collections import deque

c = 11
b = 2

# 코니의 위치 변화
# 11 12 14 17 21 26 ...

# 브라운의 위치 변화 -1 +1 *2 세가지 방법으로 움직일 수 있다.
# 2 (1, 3, 4) (0, 2, 3, 4, 5, 6, 8).... BFS를 사용하면 되겠구나!
# 값이 규칙적으로 변한다 배열 사용!
# 값이 자유자재로 변한다 딕셔너리 사용!
# 실패조건 코니와 브라운의 위치가 0 <= location <= 200000


def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))
    visited = [{} for _ in range(200001)]

    while cony_loc <= 200000:
        cony_loc += time
        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()

            new_time = current_time + 1

            new_position = current_position - 1
            if 0 <= new_position <= 2000000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 2000000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 <= new_position <= 2000000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

        time += 1
    return


print(catch_me(c, b))  # 5가 나와야 합니다!


