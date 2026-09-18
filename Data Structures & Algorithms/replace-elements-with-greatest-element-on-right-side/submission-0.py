class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = max(arr)
        for i in range(len(arr)):
            if(i+1) == len(arr):
                arr[i] = -1
                break
            if arr[i] == current_max:
                current_max = max(arr[i+1:])
            arr[i] = current_max
        return arr