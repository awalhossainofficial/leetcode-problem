def majorityElement(self, nums: List[int]) -> int:
        candid = 0
        count = 0
        for i in nums:
            if count == 0:
                candid = i
                count = 1
            elif candid != i:
                count -=1
            else:
                count +=1
        return candid
