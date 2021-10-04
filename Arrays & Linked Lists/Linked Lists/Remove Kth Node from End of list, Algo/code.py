class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


    def removeNthNodeFromEnd(head, n):
        first = head
        second = head
        counter = 1

        if head.next is None:
            return None

        #traverse the list and move just the second "n" number of times
        while counter <= n:
            second = second.next
            counter += 1

        if second is None:
            head.value = head.next.value
            head.next = head.next.next
            return head

        #At this point, second will be the tail of the list    
        while second.next is not None:
            second = second.next
            first = first.next

        first.next = first.next.next
        return head