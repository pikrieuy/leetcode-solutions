# 0125. Valid Palindrome

- **Difficulty:** Easy
- **Topics:** Two Pointers, String
- **Link:** [LeetCode #125](https://leetcode.com/problems/valid-palindrome/)

---

## Intuisi & Alur Logika

1. **Filtering & Normalization:**
   - Bersihkan string dari karakter non-alfanumerik menggunakan `char.isalnum()`.
   - Ubah semua huruf menjadi lowercase dengan `char.lower()`.
2. **Palindrome Check:**
   - Gabungkan list karakter yang sudah bersih menjadi string: `clean_s = "".join(clean)`.
   - Cek apakah string sama dengan kebalikannya menggunakan reverse slicing `clean_s[::-1]`.
   - Time: $O(n)$
   - Space: $O(n)$

---

## Solusi Python 3

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = []
        for char in s:
            if char.isalnum():
                clean.append(char.lower())

        clean_s = "".join(clean)
        return clean_s == clean_s[::-1]
```
