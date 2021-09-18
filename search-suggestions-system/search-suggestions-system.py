class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        
        products.sort()
        search = products.copy()
        for index, ch in enumerate(searchWord):
            temp = []
            for product in search:
                print(product)
                if len(product)>index and ch==product[index]:
                    temp.append(product)
                
            search = temp.copy()
            ans.append(temp[:3])
            #print(search)
            
            
        return ans