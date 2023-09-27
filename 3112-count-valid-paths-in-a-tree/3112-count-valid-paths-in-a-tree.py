from typing import List, Dict, Set
import math

class Solution:
    def __init__(self):
        self.Father = dict()
        self.next = defaultdict(list)
        self.primes = set()
        self.global_count = 0

    def FindFather(self, x: int) -> int:
        if self.Father[x] != x:
            self.Father[x] = self.FindFather(self.Father[x])
        return self.Father[x]

    def Union(self, x: int, y: int) -> None:
        x = self.Father[x]
        y = self.Father[y]
        if x < y:
            self.Father[y] = x
        else:
            self.Father[x] = y

    def Eratosthenes(self, n: int) -> Set[int]:
        q = [0] * (n+1)
        primes = set()
        for i in range(2, int(math.sqrt(n))+1):
            if q[i] == 1:
                continue
            j = i * 2
            while j <= n:
                q[j] = 1
                j += i

        for i in range(2, n+1):
            if q[i] == 0:
                primes.add(i)

        return primes

    def isPrime(self, x: int) -> bool:
        return x in self.primes

    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        self.primes = self.Eratosthenes(n)

        for i in range(1, n+1):
            self.Father[i] = i

        for edge in edges:
            a, b = edge
            self.next[a].append(b)
            self.next[b].append(a)
            if not self.isPrime(a) and not self.isPrime(b):
                if self.FindFather(a) != self.FindFather(b):
                    self.Union(a, b)

        Map = defaultdict(int)
        for i in range(1, n+1):
            Map[self.FindFather(i)] += 1

        for p in self.primes:
            arr = []
            for nxt in self.next[p]:
                if not self.isPrime(nxt):
                    arr.append(Map[self.FindFather(nxt)])
            total = sum(arr)
            sum_val = sum(x * (total-x) for x in arr)
            self.global_count += sum_val // 2 + total

        return self.global_count
