class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:


        def indices_of_same_elements(lst):
            element_indices = defaultdict(list)
            for index, element in enumerate(lst):
                element_indices[element].append(index)
            return element_indices

        for i, m in enumerate(box):
            prev = 0
            hash_es = indices_of_same_elements(m)
            
            hash_es['*'].append(len(m))
            for hash_i in hash_es['*']:
                set_ = m[prev:hash_i]
                count_hash = set_.count("#")
                count_dots = set_.count(".")

                for j in range(hash_i-1, prev-1, -1):
                    if box[i][j] == '*':
                        continue
                    box[i][j] = '#' if count_hash > 0 else '.'
                    count_hash -= 1


                prev = hash_i

        print(box)
        transposed = [[row[i] for row in box][::-1] for i in range(len(box[0]))]
    
        return transposed