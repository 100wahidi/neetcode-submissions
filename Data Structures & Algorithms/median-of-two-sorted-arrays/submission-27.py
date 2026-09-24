class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        bF = nums1 + nums2
        low = 0
        high = 0
        temp = 1
        if n>m:
            if (n+m)%2!=0:
                low = nums1[(n+m)//2]
                for val in nums2:
                    
                    if val<low and val>nums1[(n+m)//2 - temp]:
                        low=val
                    elif val<low and val<nums1[(n+m)//2 - temp]:
                        low = nums2[(n+m)//2 - temp]
                        temp+=1
                return low
            else:
                low = nums1[(n+m)//2 - 1]
                high = nums1[(n+m)//2]
                for val in nums2:
                    if val<=high and val >=low:
                        high=val
                    if val<=low and val >= bF[(n+m)//2 - 2]:
                        high = low
                        low=val

                return (low+high)/2

        elif n<m:
            if (n+m)%2!=0:
                low = nums2[(n+m)//2]
                for val in nums1:
                    
                    if val<low and val>nums2[(n+m)//2 - temp]:
                        low=val
                    elif val<low and val<nums2[(n+m)//2 - temp]:
                        low = nums2[(n+m)//2 - temp]
                        temp+=1

                return low
            else:
                low = nums2[(n+m)//2 - 1]
                high = nums2[(n+m)//2]
                for val in nums1:
                    if val<=high and val >=low:
                        high=val
                    if val<=low and val >= nums2[(n+m)//2 - 2]:
                        high = low
                        low=val
                    if val<=low and val < nums2[(n+m)//2 - temp-1]:
                        high = nums2[(n+m)//2 - temp]
                        low  = nums2[(n+m)//2 - temp-1]
                return (low+high)/2
        else:
            low = bF[(n+m)//2 - 1]
            high = bF[(n+m)//2]
            for val in nums2:

                if val<high and val >low:
                    high=val
                if val<low and val > nums1[(n+m)//2 - temp-1]:
                    high = low
                    low=val
                if val<=low and val <= nums1[(n+m)//2 - temp-1]:
                    high = bF[(n+m)//2-temp]
                    low  = bF[(n+m)//2-temp-1]
                    temp+=1
                print(low,high)

            return (low+high)/2

        