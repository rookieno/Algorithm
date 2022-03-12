p = int(input())
c = list(range(1, 101))


def up_down(target, array):
    cur_min = 1
    cur_max = len(array)
    cur_guess = (cur_min + cur_max) // 2
    while target not in range(cur_max + 1): # 범위 안의 숫자가 아니면 다시!
        print('1~100 사이의 숫자를 입력해주세요.')
        target = int(input())
    while cur_min <= cur_max:
        if cur_guess == target: # 정답일 때
            print(cur_guess)
            return print('성공')
        elif cur_guess < target: # 타겟 넘버가 더 클 때
            print(cur_guess)
            answer = input()
            if answer != '업':
                print('거짓말')
                continue  # 아래 코드 수행하지 않고 조건 판단문으로 점프!
            cur_min = cur_guess + 1
        else: # 타겟 넘버가 더 작을 때
            print(cur_guess)
            answer = input()
            if answer != '다운':
                print('거짓말')
                continue # 아래 코드 수행하지 않고 조건 판단문으로 점프!
            cur_max = cur_guess - 1
        cur_guess = (cur_min + cur_max) // 2

    return


up_down(p, c)
