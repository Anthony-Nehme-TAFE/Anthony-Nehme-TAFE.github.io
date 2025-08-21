sorted = False ##I feel like bubble sorting today false
nums = [12,1,3,9,353453,2,1,1,5,3,6436,23,73,7237,325524353,1,123,1235,125332,6743,854]
while True:
    sorted = True
    for i in range(0,(len(nums)-1)):
        if nums[i]>nums[i+1]:
            sorted = False
            tmp=nums[i+1]
            nums[i+1]=nums[i]
            nums[i]=tmp
    if sorted:break
print(nums)