class Solution:

    def encode(self, strs):
        res = ""
        word_hash = ""
        hash_hash = ""
        excep = ""
        for word in strs:
            word_hash+=f"{len(word)}"
            if len(word)>=100:
                hash_hash+=f"100"
            elif len(word)>=10 and len(word)<100:
                hash_hash+=f"010"
            else:
                hash_hash+=f"001"
            res+=word
        def parse(s:int):
            if s>=100:
                return "100"
            elif s>=10 and s<100:
                return "010"
            else:
                return "001"
        return res+word_hash+hash_hash+f"{len(strs)}"+parse(len(strs))+f"{len(word_hash)}"+parse(len(word_hash))

    def decode(self, s: str):
        print(s)
        x=0
        if s[-3:]=="001":
            x = 1
        elif s[-3:]=="010":
            x = 2
        elif s[-3:]=="100":
            x = 3
        y=0
        if s[-6-x:-3-x]=="001":
            y = 1
        elif s[-6-x:-3-x]=="010":
            y = 2
        elif s[-6-x:-3-x]=="100":
            y = 3
        res = []
        len_strs = int(s[-6-x-y:-6-x])
        len_word_hash = int(s[-3-x:-3])
        len_hash = len_strs*3
        word_hash = s[len(s)-6-x-y-len_word_hash-len_hash:len(s)-6-x-y-len_hash]
        hash_hash = s[len(s)-6-x-y-len_hash:len(s)-6-x-y]
        print(f"word_hash: {word_hash}, hash_hash: {hash_hash}")
        step=0
        current=0
        freq=0
        part=0
        for i in range(len_strs):
            x = hash_hash[i*3:(i+1)*3]
            if x=="100":
                current=3
            if x=="010":
                current=2
            if x=="001":
                current=1
            freq= word_hash[step:step+current]
            res.append(s[part:part+int(freq)])
            step+=current
            part+=int(freq)
        return res