class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # No more carry needed, return immediately
            
            digits[i] = 0  # If it's 9, it becomes 0 and carries 1 to the next left digit
            
        # If we exit the loop, it means all digits were 9 (e.g., [9, 9] -> [0, 0])
        return [1] + digits