from collections import deque

names = input("Enter players separated by commas: ")
players = deque(name.strip() for name in names.split(",") if name.strip())

passes = int(input("Number of passes: "))

while len(players) > 1:
    for i in range(passes):
        player = players.popleft()
        players.append(player)

    eliminated = players.popleft()
    print(eliminated, "is out")

if players:
    print("Winner:", players[0])
else:
    print("No players")
