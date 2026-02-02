class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # take two pointer start from zero
        right = 0

        # loop through the nums
        for left in range(len(nums)):
            # check if the left number is equal to right if not we can replace in between number
            if nums[left] != nums[right]:
                print(nums,"first", right)
                # increasing becasue first one need to be unique
                right +=1
                print(nums,"first", right,"left",left)
                # 
                nums[right]= nums[left]
                print(nums,"just check")
            
        return right+1




# second solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1

        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]:
                nums[left]= nums[right]
                left +=1
            
        return left