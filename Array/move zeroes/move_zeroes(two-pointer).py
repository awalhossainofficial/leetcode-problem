def move_zerores(nums):
    writePos = 0

    for i,val in enumerate(nums):
        if val != 0:
            nums[writePos], nums[i] = nums[i], nums[writePos]
        
        writePos +=1

nums =[0,1,0,3,12]

print(move_zerores(nums))


