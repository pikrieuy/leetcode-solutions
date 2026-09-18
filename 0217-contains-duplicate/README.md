# 0217. Contains Duplicate

- **Difficulty:** Easy
- **Topics:** Array, Hash Table, Sorting
- **Link:** [LeetCode #217](https://leetcode.com/problems/contains-duplicate/)

---

## Intuisi & Alur Logika

1. **Hash Set (Early Exit):**
   - Buat `seen = set()` kosong.
   - Iterasi tiap elemen `num` di `nums`.
   - Jika `num in seen`, langsung return `True` (duplikat ditemukan lebih awal tanpa proses sisa array).
   - Jika belum ada, masukkan ke set `seen.add(num)`.
   - Jika loop selesai tanpa duplikat, return `False`.
   - Time: $O(n)$
   - Space: $O(n)$

2. **Alternative (One-Liner):**
   - `return len(nums) != len(set(nums))`
   - Mengubah list ke set otomatis menghapus duplikat. Jika panjang set lebih kecil dari panjang list asli, ada duplikat.
   - Time: $O(n)$, Space: $O(n)$.

---

## Solusi Python 3

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen: set[int] = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```
