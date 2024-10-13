import sys
sys.setrecursionlimit(10**6)

# Read the input
n = int(input())
tree = [[] for _ in range(n+1)]

# Read the edges of the tree
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[min(u, v)].append(max(u, v))

#for parent, children in enumerate(tree):
#    print(f"Parent {parent}: Children {children}")

# Global variables to store heights and required heights
height = [0] * (n+1)
req_height = [0] * (n+1)
removed = 0

# First DFS to compute the height of each node
def compute_height(v, parent):
    max_h = 0
#  print('current vertice: ', v)
#  print('tree[v] - ', tree[v])
    for child in tree[v]:
        if child == parent:
            continue
        max_h = max(max_h, compute_height(child, v))
    height[v] = max_h + 1
    return height[v]

def reqH(v, parent, required):
    global removed
    
    # Calculate the required height for the current node
    req_height[v] = required
    if req_height[v] < 0:
        removed += 1
        print("removed upd: ", removed)
        return
    
    # Get the heights of the children
    child_heights = []
    for child in tree[v]:
        if child != parent:
            child_heights.append(height[child])
    
    if len(child_heights) == 0:
        return  # No children for leaf node
    
    if len(child_heights) == 1:
        # Only one child, directly compute required height for that child
        for child in tree[v]:
            if child != parent:
                new_required = min(height[child], req_height[v] - 1)
                reqH(child, v, new_required)
    else:
        # Two children case: calculate the required height for each child
        child_heights.sort(reverse=True)
        for child in tree[v]:
            if child != parent:
                if height[child] == child_heights[0]:
                    new_required = min(height[child], child_heights[1] + 1, req_height[v] - 1)
                else:
                    new_required = min(height[child], child_heights[0] + 1, req_height[v] - 1)
                reqH(child, v, new_required)


#print(compute_height(1, -1))
compute_height(1, -1)
print(height)
reqH(1, -1, height[1])
print(removed)

  
'''  
# Second DFS to set required heights and count removed vertices
def set_required_height(v, parent, required):
    global removed
    
    # Calculate the required height for the current node
    req_height[v] = required
    if req_height[v] < 0:
        removed += 1
        return
    
    # Get the heights of the children
    child_heights = []
    for child in tree[v]:
        if child != parent:
            child_heights.append(height[child])
    
    if len(child_heights) == 0:
        return  # No children for leaf node
    
    if len(child_heights) == 1:
        # Only one child, directly compute required height for that child
        for child in tree[v]:
            if child != parent:
                new_required = min(height[child], req_height[v] - 1)
                set_required_height(child, v, new_required)
    else:
        # Two children case: calculate the required height for each child
        child_heights.sort(reverse=True)
        for child in tree[v]:
            if child != parent:
                if height[child] == child_heights[0]:
                    new_required = min(height[child], child_heights[1] + 1, req_height[v] - 1)
                else:
                    new_required = min(height[child], child_heights[0] + 1, req_height[v] - 1)
                set_required_height(child, v, new_required)

'''
