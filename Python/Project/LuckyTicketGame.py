import random

# Step 1: generate  12 unique random tickets
tickets = []
while len(tickets) < 12:
    num = random.randint(1, 100)
    if num not in tickets:
        tickets.append(num)

# Step 2: divide 6-6  unique random tickets
player1 = tickets[:6]
player2 = tickets[6:]


draw_numbers = tickets

print("================>>>> TICKETS :::: ",draw_numbers)
# step 3 : start your game 
print("Game Start!")
print("Player 1:", *player1)
print("Player 2:", *player2)

while len(draw_numbers) > 0:
    draw = random.choice(draw_numbers)
    draw_numbers.remove(draw)
    print("Number drawn:", draw)

    if draw in player1:
        player1.remove(draw)
        print("Player 1 had the number!")

    elif draw in player2:
        player2.remove(draw)
        print("Player 2 had the number!")

    if len(player1) == 0:
        print("Player 1 wins!")
        break
    elif len(player2) == 0:
        print("Player 2 wins!")
        break
