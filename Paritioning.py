from Lists import LinkedListFull

def partition(ll,n):
    node = ll.head
    ll.tail = ll.head
    while node:
        nextNode = node.next
        node.next = None
        if node.value < n:
            node.next = ll.head
            ll.head = node
        else:
            ll.tail.next = node
            ll.tail = node
        node = nextNode
    if ll.tail.next is not None:
        ll.tail.next = None


customLL = LinkedListFull.LinkedList()
customLL.generate(10,0,99)
print(customLL)
partition(customLL, 30)
print(customLL)