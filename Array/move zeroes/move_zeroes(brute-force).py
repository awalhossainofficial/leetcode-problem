def moveZeroes(nums):
    n = len(nums)
    res = [0] * n
    j = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            res[j] = nums[i] 
            j +=1

    return res
nums =[0,1,0,3,12]

print(moveZeroes(nums))