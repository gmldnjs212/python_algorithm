# 문제 https://www.acmicpc.net/problem/2164
# 빠른이유 https://wiki.python.org/moin/TimeComplexity

from collections import deque


def test_problem_queue(n):
    deq = deque([i for i in range(1, n+1)])

    while len(deq) > 1:
        deq.popleft()
        deq.append(deq.popleft())
    return deq.popleft()
