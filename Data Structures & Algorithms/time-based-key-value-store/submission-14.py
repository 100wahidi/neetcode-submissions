class TimeMap:

    def __init__(self):
        self.Database={"mouad":("happy",1)}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.Database:
            self.Database[key]=[("",0)]
            L = self.Database[key]+[(value,timestamp)]
            self.Database[key]=L
        else:
            self.Database[key].append((value,timestamp))
            
        # else:
        #     arr=self.Database[key]
        #     l, r=0, len(arr)-1
        #     while(l<r):
        #         mid = (l+r)//2
        #         if arr[mid][1]<=timestamp:
        #             l=mid+1
        #         else:
        #             r=mid
            
        #     self.Database[key]=arr[:l+1]+[(value, timestamp)]+arr[l+1:]            
        
    def get(self, key: str, timestamp: int) -> str:
        if key in self.Database:
            arr=self.Database[key]
            # search for the biggest min de timestamp
            if self.Database[key][-1][1]<=timestamp:
                return self.Database[key][-1][0]
            l, r=0, len(arr)-1
            while(l<r):
                mid = (l+r)//2
                if arr[mid][1]<=timestamp:
                    l=mid+1
                else:
                    r=mid
            if self.Database[key][l][1]>timestamp:
                return self.Database[key][l-1][0]
            return self.Database[key][l][0]

        return ""
        
        
