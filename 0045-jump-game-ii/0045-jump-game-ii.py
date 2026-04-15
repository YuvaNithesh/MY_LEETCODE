class Solution:
    def jump(self, nums):
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            # when we reach the end of current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps