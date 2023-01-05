class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        node = head
        
        while node:
            nodes.append(node)
            node = node.next
        
        return nodes[len(nodes)//2]
