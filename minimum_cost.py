"""
Algorithm:
    1. Take two shortest cabels from list
    2. Add up their lengths, and put the new connected cable back in the list instead of two shortest cables
    3. The sum of cables' lengths = the price of their connection.
    4. Repeat the process until we have only one cable left. Add up all connection prices to get final minimum price
"""

import heapq

def get_minimum_cost(cables_lengths):
    heapq.heapify(cables_lengths)

    price = 0

    while len(cables_lengths) > 1:
        shortest_one = heapq.heappop(cables_lengths)
        shortest_two = heapq.heappop(cables_lengths)
        price += shortest_one + shortest_two
        heapq.heappush(cables_lengths, shortest_one + shortest_two)

    return price

cables_lengths = [4, 3, 2, 6]
mininum_cost = get_minimum_cost(cables_lengths)
print(f'Minimum cost for connecting cables is {mininum_cost}')
