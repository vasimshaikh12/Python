# 🎲 LuckyTicketGame

A simple Python-based game where two players compete using randomly generated tickets. The first player to match all of their ticket numbers with the drawn numbers wins!

---

## 📌 Game Rules

1. 12 unique random numbers between 1 and 100 are generated.
2. These numbers are split into two sets of 6 tickets — one for each player.
3. A random number is drawn from the remaining pool.
4. If the drawn number matches a player's ticket, it is removed from their list.
5. The game continues until one player clears all their tickets.
6. That player is declared the winner!

---

## 🧑‍💻 Code Walkthrough

```python
# Step 1: Generate 12 unique random tickets
# Step 2: Assign 6 tickets each to Player 1 and Player 2
# Step 3: Randomly draw numbers from the ticket pool
# Step 4: Remove matched tickets from players' lists
# Step 5: Announce the winner
