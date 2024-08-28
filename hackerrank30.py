k = int(input())
room_l = list(map(int, input().split()))
room_s = set(room_l)
captain_sum = (sum(room_s)*k)- sum(room_l)
captain = captain_sum/(k-1)
print(int(captain))

