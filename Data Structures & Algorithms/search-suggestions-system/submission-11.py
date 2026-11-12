class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products=sorted(products)
        res =[]
        left, right=0, len(products)-1
        # go through searching letters
        def BS(low, high, target,index, Asc:bool):
            if Asc:
                while(low<=high):
                    middle=(low+high)//2
                    if index<=len(products[middle])-1:
                        if products[middle][index]>=target:
                            high=middle-1
                        else:
                            low=middle+1
                    else:
                        low=middle+1


                return low
            else:
                while(low<=high):
                    middle=(low+high)//2
                    if index<=len(products[middle])-1:
                        if products[middle][index]>target:
                            high=middle-1
                        else:
                            low=middle+1
                    else:
                        low=middle+1
                return low-1
        for i, c in enumerate(searchWord):
            left=BS(left, right, c,i, True)
            right=BS(left, right, c,i, False)
            if left>right:
                for k in range(len(searchWord)-i):
                    res.append([])
                return res
            else:
                res.append(products[left:min(right+1, left+3)])
                    
        return res
            
        
