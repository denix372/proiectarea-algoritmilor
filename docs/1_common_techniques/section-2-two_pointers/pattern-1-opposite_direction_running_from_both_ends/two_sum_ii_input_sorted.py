class Solution:
    def two_sum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            total = numbers[i] + numbers[j]
            if total < target:
                i += 1
            elif total > target:
                j -= 1
            else:
                return [i + 1, j + 1]

numbers = [2,7,11,15]
target = 9
print(Solution().twoSum(numbers, target))