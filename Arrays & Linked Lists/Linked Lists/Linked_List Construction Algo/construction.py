class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        self.insertBefore(self.head, node)
        #This section is commented out as an alternative to calling the insertbefore method
        # node.next = self.head

        # self.head.prev = node
        # self.head = node
        

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
        
        self.insertAfter(self.tail, node)
        #This section is commented out as an alternative to calling the insertafter method
        # node.prev = self.tail

        # self.tail.next = node
        # self.tail = node

    def insertBefore(self, node, nodetoinsert):
        if nodetoinsert == self.head and nodetoinsert == self.tail:
            return
        self.remove(nodetoinsert)
        nodetoinsert.prev = node.prev
        nodetoinsert.next = node

        if node.prev is None:
            self.head = nodetoinsert
        else:
            node.prev.next = nodetoinsert

        node.prev == nodetoinsert

    def insertAfter(self, node, nodetoinsert):
        if nodetoinsert == self.head and nodetoinsert == self.tail:
            return
        self.remove(nodetoinsert)
        nodetoinsert.prev = node
        nodetoinsert.next = node.next

        if node.next is None:
            self.tail = nodetoinsert
        else:
            node.next.prev = nodetoinsert
        
        node.next = nodetoinsert


    def insertAtPosition(self, Position, nodetoinsert):
        if Position == 1:
            self.setHead(nodetoinsert)
            return 
            
        node = self.head
        CurrentPosition = 1

        while node is not None and CurrentPosition != Position:
            node = node.next
            CurrentPosition += 1
        
        if node is not None:
            self.insertBefore(node, nodetoinsert)
        else:
            self.setTail(nodetoinsert)

        

    def removeNodesWithValue(self, value):
        node = self.head
        
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removebindingsNode(node)

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    
    def removebindingsNode(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        node.prev = None
        node.next = None