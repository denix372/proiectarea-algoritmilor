class NumArray:

    def __init__(self, nums: list[int]):
        n = len(nums)
        self.prefix = [0] * n
        self.prefix[0] = nums[0]
        for i in range(1, n):
            self.prefix[i] = self.prefix[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]
        


numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2)) # return (-2) + 0 + 3 = 1
print(numArray.sumRange(2, 5)) # return 3 + (-5) + 2 + (-1) = -1
print(numArray.sumRange(0, 5)) # return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3