
def solve(arr):
    cnt1 = 0
    cnt2 = 0
    for p in arr:
        if not p:
            continue

        if p[0] == p[len(p) - 1]:
            if p[0] == 'W':
                cnt1 += 1
            elif p[0] == 'B':
                cnt2 += 1

        if cnt1 < cnt2:
            return "Player1"
        else:
            return "Player2"

arr = ["WBW", "BWB"]
print(solve(arr))

'''
GAME THEORY ANALYSIS & PROOF (Misère Play & Parity)

A) Core Mathematical Idea (Compression):
   Assuming optimal play, a player will greedily remove all contiguous boxes of 
   their color to maximize their tempo. Thus, a string like "WWBBBW" is logically 
   equivalent to the alternating sequence "W-B-W".

B) Parity and Zero-Sum Subgames:
   - A pile that starts and ends with different colors (e.g., "W...B") has an even 
     number of compressed blocks. It offers exactly the same number of turns to P1 
     as to P2. Under optimal play, whoever initiates taking boxes from this pile 
     guarantees the opponent gets the final box of that pile. Therefore, these piles 
     are net-zero (Parity 0) and do not influence the final outcome.
     
   - A pile that starts and ends with the same color (e.g., "W...W") has an odd 
     number of blocks. It inherently forces the player of that color to make one 
     additional move compared to their opponent.

C) Misère Play Condition:
   Unlike standard games where the last player to move wins, here the last player 
   to move LOSES. This is equivalent to saying: "The first player who is unable 
   to make a move wins." 
   To win, a player must exhaust their mandatory turns faster than the opponent.
   Therefore, players want to MINIMIZE their extra moves.

D) Winning Condition:
   Let 'a' be the number of extra moves for Player 1 (W) and 'b' for Player 2 (B).
   Because Player 1 starts the game, they are always "half a step" ahead in 
   consuming their mandatory moves. 
   - If a <= b: Player 1 will exhaust their extra moves before or exactly at the 
     same time as Player 2. Since Player 1 exhausts theirs first, Player 2 is left 
     holding the remaining moves and loses. (Player 1 wins).
   - If a > b: Player 1 has too many mandatory extra moves and will be forced to 
     make the final move of the game. (Player 2 wins).
'''