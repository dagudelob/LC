class Solution():
    def findMedianSortedArrays(self, nums1, nums2):
        merge = []       
        merge = nums1 + (nums2) # fusionar 
        print(f'merged: {merge}')
        merge.sort() # ordenar como llamo a la funsion sort en python? 
        
        print(f'merge sorted: {merge}')
        
        x=int()
        x=len(merge)//2 
        
        
        print(f'x: {x}')
        
        if len(merge)%2==0: # para cuando es par
            print (f'x: {x}, merge[x] {merge[x]}, merge[x+1]: {merge[x+1]} ')
            return (merge[x-1]+merge[x])/2
        else:
            return (merge[x+0.5])
        
print(f'la solucion es {Solution().findMedianSortedArrays([1,2],[3,4])}')

 