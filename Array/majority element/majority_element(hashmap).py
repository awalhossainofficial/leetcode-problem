def majorityElement(self, nums: List[int]) -> int:
        store = dict()
        

        for i in nums:
            if i not in store:
                store[i] = 1
            else:
                store[i] +=store.get(i)
         
        val = max(store, key=store.get)

        return val


