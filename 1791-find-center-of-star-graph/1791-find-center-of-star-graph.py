class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # approach 1
        # we use a hashmap to store the count of all the edges appearing 
        # the center node is the node with the count == lenght of the list 
        # i.e. it should appear in all the edge pairs
        
        hashmap = {}
        
        for edge_list in edges:
            e1, e2 = edge_list
            
            hashmap[e1] = hashmap.get(e1, 0) + 1
            hashmap[e2] = hashmap.get(e2, 0) + 1
            
        for node, count in hashmap.items():
            if count == len(edges):
                return node
        return -1
            
            