import random
import time

# Solution
def mix_members(member: list) -> dict:
    result = {}
    team_number = 1
    while member:
        member_num = len(member)
        if member_num % 7 < 5 and member_num % 7 != 0 or member_num < 7:
            if member_num % 6 > 5 or member_num == 6:
                target = random.sample(member, 6)
            else:
                target = random.sample(member, 5)
        else:
            target = random.sample(member, 7)
        result[f"{team_number}조"] = target
        member = [i for i in member if i not in target]
        team_number += 1
    return result

# Input
def create_input_data(start, end):
    data = []
    for i in range(start + 1, end + 2):
        data.append(list(map(str, range(1,i))))
    return data

# Output
start = time.time()
teams = []
for data in create_input_data(10, 100):
    teams.append(mix_members(data))
end = time.time()
print(f"{end-start:.5f}초")

# Test
def test_mix_members(team):
    for _, team_member in team.items():
        if len(team_member) < 5 or len(team_member) > 7:
            return False
    return True

cnt = 10
for team in teams:
    result = test_mix_members(team=team)
    print(f"총 인원:{cnt} 조의수:{len(team)} 결과코드:{result}")
    cnt += 1

