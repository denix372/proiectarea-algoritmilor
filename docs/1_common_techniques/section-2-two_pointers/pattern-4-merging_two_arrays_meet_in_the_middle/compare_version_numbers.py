
class Solution:
    def compare_version(self, version1: str, version2: str) -> int:
        i, j = 0, 0
        n, m = len(version1), len(version2)

        while i < n or j < m:
            num1 = 0
            while i < n and version1[i] != '.':
                num1 = num1 * 10 + int(version1[i])
                i += 1
            
            num2 = 0
            while j < m and version2[j] != '.':
                num2 = num2 * 10 + int(version2[j])
                j += 1
            
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1

            i += 1
            j += 1
        
        return 0

version1 = "1.2"
version2 = "1.10"
print(Solution().compareVersion(version1, version2))