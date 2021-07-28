# Woozle
# Programming Concepts Coursework
# June 2021


def display(A, B):
    for C in range(15):
        for D in range(15):
            E = (C * 15) + D
            print(chr(A[E]), end=" ")
        print(" ")
    B = B + 1
    return B


def place(A):
    import random

    B = random.random()
    B = int(B * 75)
    B = B + 75 * (A == "S")
    B = B + 150 * (A == "P")
    return B


def init(A):
    for B in range(15):
        A[B] = 35
        A[B + 210] = 35
        A[B * 15] = 35
        A[(B * 15) + 14] = 35
    return A


def row(A):
    for B in range(15):
        for C in range(15):
            D = (B * 15) + C
            if D == A:
                E = B
    return E


def passed(A, B):
    C = row(B)
    D = C * 15
    E = 0
    for F in range(15):
        if (D + F) == A:
            E = 1
    return E


def check(A, B, C, D, E):
    F = passed(A, B)
    if (F == 1) and (C > D + 5):
        D = C
        E = E + 1
    if E > 1:
        print("Congratulations. You have gone")
        print("round the spinney.")
    else:
        print("Keep going. You have not gone")
        print("round the spinney yet.")
    return D, E


def move(A, B):
    print("Select key and press return to move")
    print("U = Up, D = Down, L = Left, R = Right")
    C = input("Enter key ")
    if C == "U":
        D = A - 15
    if C == "D":
        D = A + 15
    if C == "L":
        D = A - 1
    if C == "R":
        D = A + 1
    if B[D] == 46:
        A = D
    return A


def main():
    # Following 5 lines essential
    SNOW = [46] * 225
    SNOW = init(SNOW)
    TICK = 0
    EVENT = 0
    CIRCLED = 0

    player_1 = place("W")
    player_2 = place("P")
    point_s = place("S")

    # SNOW[player_2] = 80
    # SNOW[player_1] = 87
    # SNOW[point_s] = 83
    # TICK = display(SNOW, TICK)

    # while SNOW[player_1] < 90:
    #     player_1 = move(player_1, SNOW)
    #     SNOW[player_1] = 81
    #     TICK = display(SNOW, TICK)
    #     point_s = SNOW[point_s]
    #     player_1 = SNOW[player_1]
    #     EVENT, CIRCLED = check(player_1, point_s, TICK, EVENT, CIRCLED)
    #     print("Value of CIRCLED is", end=" ")
    #     print(CIRCLED)


    SNOW[player_2] = player_2
    SNOW[player_1] = player_1
    SNOW[point_s] = point_s
    TICK = display(SNOW, TICK)

    while SNOW[player_1] < 225:
        player_1 = move(player_1, SNOW)
        SNOW[player_1] = player_1
        TICK = display(SNOW, TICK)
        point_s = SNOW[point_s]
        player_1 = SNOW[player_1]
        EVENT, CIRCLED = check(player_1, point_s, TICK, EVENT, CIRCLED)
        print("Value of CIRCLED is", end=" ")
        print(CIRCLED)



main()
