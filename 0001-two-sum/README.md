# 0001. Two Sum

- **Difficulty:** Easy
- **Topics:** Array, Hash Table
- **Link:** [LeetCode #1](https://leetcode.com/problems/two-sum/)

---

## Intuisi & Alur Logika

1. **Brute Force:** Cek semua pasangan `(i, j)` dengan nested loop.
   - Time: $O(n^2)$
   - Space: $O(1)$

2. **Optimasi (Hash Map / One-Pass):**
   - Saat iterasi di elemen $x$, cari sisa target: $diff = target - x$.
   - Cek apakah $diff$ sudah pernah tercatat di dictionary.
   - Jika ada: kembalikan pasangan indeks `[seen[diff], i]`.
   - Jika belum: simpan elemen sekarang ke dictionary `seen[x] = i`.
   - Time: $O(n)$
   - Space: $O(n)$

---

## Solusi Python 3

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
```
