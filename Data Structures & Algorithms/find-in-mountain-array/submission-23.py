class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # search for i
        # devide serach on the two sides 

        l, r=0, mountainArr.length()-1
        while(l<=r):
            middle=(l+r)//2
            if mountainArr.get(middle)>mountainArr.get(middle+1):
                r=middle-1
            else:
                l=middle+1
        
        pick=l
        if target<=mountainArr.get(l):
            if mountainArr.get(0)<=target:
                left, right=0, l
                while(left<=right):
                    ptr=(left+right)//2
                    if mountainArr.get(ptr)>=target:
                        right=ptr-1
                    else:
                        left=ptr+1
                print(left)
                if mountainArr.get(left)==target:
                    return left
                else:
                    if mountainArr.get(mountainArr.length()-1)<=target:
                        print("enter")
                        left, right=l+1, mountainArr.length()-1
                        while(left<=right):
                            ptr=(left+right)//2
                            if mountainArr.get(ptr)>target:
                                left=ptr+1
                            else:
                                right=ptr-1
                        print(left)
                        if left<=mountainArr.length()-1 and mountainArr.get(left)==target:
                            return left     
                    else:
                        return -1   
        return -1
        


    