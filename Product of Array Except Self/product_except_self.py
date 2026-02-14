def productExceptSelf(self, nums: List[int]) -> List[int]:
         prefix =1
         suffix = 1
         arr =[]
         for i in nums:
            arr.append(prefix)
            prefix *=i

         for i in range(len(nums)-1, -1, -1):
             arr[i] = suffix * arr[i]
             suffix *=nums[i]
         return arr