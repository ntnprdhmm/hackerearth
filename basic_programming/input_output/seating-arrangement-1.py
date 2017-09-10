from math import fabs

"""
    Given x, find the first multiple of n bigger than x
"""
def find_next_multiple(x, n):
    if x % n == 0:
        return x
    return x + (n - x % n)

"""
    Given x, find the first multiple of n lower than x
"""
def find_previous_multiple(x, n):
    if x % n == 0:
        return x - 12
    return x - (x % n)

"""
    Find the number of the seat next to the given seat number
    and his type
"""
def facing_seat_number(n):
    # find the seat number
    facing_number = find_next_multiple(n, 12) - n + 1 + find_previous_multiple(n, 12)
    # find the type of seat
    seats_diff = fabs(n - facing_number)
    if seats_diff == 1 or seats_diff == 11:
        facing_type = "WS"
    elif seats_diff == 3 or seats_diff == 9:
        facing_type = "MS"
    else:
        facing_type = "AS"

    return facing_number, facing_type

for _ in range(int(input())):
    seat_number = int(input())
    print(' '.join(list(map(str, facing_seat_number(seat_number)))))
