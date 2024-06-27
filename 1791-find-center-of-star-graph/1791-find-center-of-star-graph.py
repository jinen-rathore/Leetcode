class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """# approach 1
        # we use a hashmap to store the count of all the edges appearing 
        # the center node is the node with the count == lenght of the list 
        # i.e. it should appear in all the edge pairs
        
        # Time complexity = O(N)
        
        # we create a hashmap to store the count of all the edges
        hashmap = {}
        
        # Iterating over the edges list 
        for edge_list in edges:
            e1, e2 = edge_list
            
            # adding in the hashmap 
            # hashmap.get(e1, 0) + 1 => what is does is
            # get the count from the hashmap of the existing element
            # if not found return 0
            hashmap[e1] = hashmap.get(e1, 0) + 1
            hashmap[e2] = hashmap.get(e2, 0) + 1
        
        # iterating over the hashmap and checking who has length equal to edges list length 
        for node, count in hashmap.items():
            if count == len(edges):
                return node
        return -1"""
            
        # Approach 2
        # intution: if it is a center node then it will appear in all the edges pairs
        
        # so we check only 2 edge pairs and the common element is the center node
        
        # Time Complexity = O(1)
        
        e1, e2 = edges[0], edges[1]
        
        if e1[0] in e2:
            return e1[0]
        else:
            return e1[1]
        
            