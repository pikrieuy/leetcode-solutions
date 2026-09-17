# 0242. Valid Anagram

- **Difficulty:** Easy
- **Topics:** Hash Table, String, Sorting
- **Link:** [LeetCode #242](https://leetcode.com/problems/valid-anagram/)

---

## Intuisi & Alur Logika

1. **Early Exit:** Jika `len(s) != len(t)`, langsung return `False`.
2. **Frequency Count (Hash Map):**
   - Hitung frekuensi tiap karakter di string `s` dan `t`.
   - Gunakan `dict.get(char, 0) + 1` untuk menghitung tally kemunculan huruf.
   - Bandingkan kesamaan isi kedua dictionary (`countS == countT`).
   - Time: $O(n)$
   - Space: $O(1)$ karena jumlah karakter alfabet maksimal 26.

---

## Solusi Python 3

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS: dict[str, int] = {}
        countT: dict[str, int] = {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        return countS == countT
```
