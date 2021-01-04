#!/usr/bin/python

"""
Class IT implements 'fluent interface' pattern.
Returning 'self' in most of it's method allows chaining method calls over single instance:
    it = IT([1,5,3,4,6,2])
    it.add(10).add(11).reverse().pop_min()

# Test sorting algorithm performance:
import random

data = [random.randint(0,100000) for x in range(0, 1000)]
for x in range(5):
    it = IT(data)
    %timeit it.quick_sort()
    it = IT(data)
    %timeit it.swap_sort()
    it = IT(data)
    %timeit it.selection_sort()
    it = IT(data)
    %timeit it.sort()
"""

from typing import List, Optional, Sequence


class IT:
    def __init__(self, data: Sequence[int]):
        self.sequence: List[int] = [int(item) for item in data]
        self.curr_item = 0

    def __repr__(self):
        repr_string = f'{self.sequence[0]} .. {self.sequence[-1]}' if self.size() > 10 else f'{self.sequence}'
        return f'<IT : {repr_string} of size {self.size()}>'

    def __next__(self):
        try:
            self.curr_item += 1
            return self.sequence[self.curr_item - 1]
        except IndexError as error:
            raise StopIteration from error

    def __iter__(self):
        while self.curr_item < self.size() + 1:
            yield self.__next__()

    def add(self, item: int) -> 'IT':
        self.sequence.append(int(item))
        return self

    def pop(self) -> 'IT':
        self.sequence.pop()
        return self

    def show(self) -> 'IT':
        print(self.sequence)
        return self

    def get_all(self) -> List[int]:
        return self.sequence

    def reverse(self) -> 'IT':
        buf = []
        [buf.insert(0, x) for x in self.sequence]
        self.sequence = buf
        return self

    def sum(self) -> int:
        res = 0
        [res := res + x for x in self.sequence]
        return res

    def size(self) -> int:
        res = 0
        [res := res + 1 for x in self.sequence]
        return res

    def sort(self) -> 'IT':
        self.sequence.sort()
        return self

    def get_max(self) -> int:
        max_x = 0
        [max_x := x for x in self.sequence if x > max_x]
        return max_x

    def pop_max(self) -> int:
        max_x = self.get_max()
        self.sequence.remove(max_x)
        return max_x

    def get_min(self) -> int:
        min_x = self.sequence[0]
        [min_x := x for x in self.sequence if x <= min_x]
        return min_x

    def pop_min(self) -> int:
        min_x = self.get_min()
        self.sequence.remove(min_x)
        return min_x

    def _qsort(self, seq: List[int]) -> List[int]:
        if len(seq) < 2:
            return seq

        base_el = seq[0]
        left = []
        right = []
        for x in seq[1:]:
            if x < base_el:
                left.append(x)
                continue
            right.append(x)
        return self._qsort(left) + [base_el] + self._qsort(right)

    def quick_sort(self) -> 'IT':
        self.sequence = self._qsort(self.sequence)
        return self

    def swap_sort_recurred(self) -> Optional['IT']:
        """Rapidly riches Python recursion limit."""
        for ix, el in enumerate(self.sequence):
            try:
                if self.sequence[ix + 1] < el:
                    self.sequence.insert(ix, self.sequence[ix + 1])
                    self.sequence.pop(ix + 2)
                    break
            except IndexError:
                return

        self.swap_sort()
        return self

    def swap_sort(self) -> Optional['IT']:
        while True:
            for ix, el in enumerate(self.sequence):
                try:
                    if self.sequence[ix + 1] < el:
                        self.sequence.insert(ix, self.sequence[ix + 1])
                        self.sequence.pop(ix + 2)
                        break
                except IndexError:
                    return self

    def _s_sort(self, unsorted: List[int], emerging: List[int]) -> Optional[List[int]]:
        if self.size() == 0:
            return

        emerging.append(self.pop_min())
        self._s_sort(unsorted, emerging)
        return emerging

    def selection_sort(self) -> 'IT':
        self.sequence = self._s_sort(self.sequence, [])
        return self

    def mean(self) -> float:
        return self.sum() / self.size()

    def median(self) -> float:
        self.sort()
        ln = self.size()
        if ln % 2 == 0:
            return self.sequence[ln // 2] + self.sequence[ln // 2 - 1] / 2
        return self.sequence[ln // 2]

    def deduplicate(self) -> 'IT':
        buf = []
        [buf.append(x) for x in self.sequence if x not in buf]
        self.sequence = buf
        return self
