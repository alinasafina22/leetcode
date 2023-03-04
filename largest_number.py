'''
2231. Largest Number After Digit Swaps by Parity

You are given a positive integer num. You may swap any two digits of num that have the same parity
(i.e. both odd digits or both even digits).
Return the largest possible value of num after any number of swaps.
'''


class Solution:
    @staticmethod
    def largestInteger(num: int) -> int:
        n = len(str(num))
        arr = [int(i) for i in str(num)]
        odd, even = [], []  # массив с нечетными и четными цифрами
        res = 0

        for i in arr:  # разделяем цифры по массивам
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        even.sort()  # сортируем массивы
        odd.sort()

        for i in range(n):
            if arr[i] % 2 == 0:  # если число четное возвращаем из массива even, иначе, возвращаем из odd
                res = res * 10 + even.pop()
            else:
                res = res * 10 + odd.pop()
        return res


c = Solution()
print(c.largestInteger(1234))
