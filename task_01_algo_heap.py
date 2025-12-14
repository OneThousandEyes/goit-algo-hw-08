import heapq
from typing import Iterable, List, Tuple


def min_cost(cables: Iterable[int]) -> tuple[int, List[Tuple[int, int, int]]]:
    """Обчислює мінімальну вартість з'єднання кабелів та план кроків."""
    heap = list(cables)
    if len(heap) <= 1:
        return 0, []

    heapq.heapify(heap)
    total_cost = 0
    steps: List[Tuple[int, int, int]] = []

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        cost = a + b
        total_cost += cost
        steps.append((a, b, cost))
        heapq.heappush(heap, cost)

    return total_cost, steps


cables = [4, 3, 2, 6, 1, 1]
total, plan = min_cost(cables)

print("Мінімальна вартість:", total)
print("Кроки:")
for a, b, cost in plan:
    print(f"{a} + {b} -> {cost}")
