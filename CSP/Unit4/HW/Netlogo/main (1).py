with open('data.txt','r+') as file:
    f = file.readlines()
    nums=[]
    for i in range(len(f)):
        #for j in range(len(f)):
        #    print(f[i][j])
        nums.append(f[i].split())
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            try:
                nums[i][j] = int(nums[i][j])
                if nums[i][j] >= 500:
                    nums[i][j] = nums[i][j]-500
                else:
                    nums[i][j] = nums[i][j]+500
            except:
                print(nums[i][j])
                pass
file.close()

with open("newDataish.txt","w+") as file:
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            file.write(str(nums[i][j])+" ")
file.close()