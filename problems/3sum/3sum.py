
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    r = []
    
    nums.sort()
    d = {i: nums[i] for i in range(len(nums))}
    print(nums)
    for i in range(len(nums)-2):
        if i > 0 and d[i] == d[i-1]:
            pass
        else:
            j0 = i+1
            for j in range(j0, len(nums)-1):
    

                if j > j0 and d[j] == d[j-1]:
                    pass

                else:                            
                    k0 = j+1
                    for k in range(k0, len(nums)):
                        if k > k0 and d[k] == d[k-1]:
                            pass
                        else:
                            if d[i]+d[j]+d[k]==0:
                                r.append( [ d[i], d[j], d[k] ] )
    return r

def threeSum1(nums):
    r = []     
        nums.sort()
        d = {i: nums[i] for i in range(len(nums))}
        for i in range(len(nums)-2):
            if i > 0 and d[i] == d[i-1]:
                pass
            else:
                p1 = i+1
                p2 = len(nums)-1
                while p1<p2:
                    if d[i]+d[p1]+d[p2] == 0:
                        r.append( [ d[i], d[p1], d[p2] ] )
                        p1+=1
                        while p1 < p2 and d[p1] == d[p1-1]:
                            p1+=1
                            
                        p2-=1
                        while p2 > p1 and d[p2] == d[p2+1]:
                            p2-=1
                    elif d[i]+d[p1]+d[p2] > 0:
                        p2-=1
                    else:
                        p1+=1
                        
        return r
