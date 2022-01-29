import sys
sys.setrecursionlimit(10**6)

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, V, adj):
        # code here
        visited = [False]*V
        lowest = [float("inf")]*V
        time = [float("inf")]*V
        timer = 0
        ans = []
        
        
        def dfs(node,parent):
            nonlocal timer
            
            visited[node]=True
            count = 0
            lowest[node] = time[node] = timer
            timer+=1
            
            for child in adj[node]:
            	if child == parent:
            		continue

                if visited[child]==False:
                    dfs(child,node)
                    count+=1
                    lowest[node] = min(lowest[node],lowest[child])
                    if lowest[child] >= time[node] and parent!=-1:
                    	if node not in ans:
                    		ans.append(node)
                    
                else:
                	lowest[node] = min(lowest[node],time[child])

      
            
            if parent == -1 and count > 1:
                print(node)
                ans.append(node)
                
        
        for i in range(V):
            if visited[i]==False:
                dfs(i,-1)
        
        return sorted(ans) if len(ans) > 0 else [-1]