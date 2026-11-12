class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products=sorted(products);lo=0;hi=len(products);answer=[]
        for pos,c in enumerate(searchWord):
            while lo<hi and (len(products[lo])<=pos or products[lo][pos]!=c):lo+=1
            while lo<hi and (len(products[hi-1])<=pos or products[hi-1][pos]!=c):hi-=1
            answer.append(products[lo:min(hi,lo+3)])
        return answer
