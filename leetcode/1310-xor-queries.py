from typing import List

def xor(sublist: List):
    sublist_str = str(sublist).replace('[', '').replace(']', '').replace(',', ' ^')
    return eval(sublist_str)

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]):

        memory = {}
        result = []

        for value in queries:
            if str(value) in memory.keys():
                result.append(memory[str(value)])
            else:
                xor_result = xor(arr[value[0]:value[1] + 1])
                memory[str(value)] = xor_result
                result.append(xor_result)

        return result


arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]

print(Solution().xorQueries(arr, queries))
