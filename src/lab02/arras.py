def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums)==0:
        return ValueError
    mx=-float('inf')
    mn=float('inf')
    for x in nums:
        if x>mx:
            mx=x
        if x<mn:
            mn=x
    return(mn,mx)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    res=[]
    for x in mat:
        if not isinstance(x,(list,tuple)):
            return TypeError
        for y in x:
            res.append(y)
    return res            