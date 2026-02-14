def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        right = nums[-k:] 
        left = nums[:-k] 
        
        newArr = right + left
        # print(right,"and",left,"new",newArr)
        # nums[:] = right + left
        print(nums[:])