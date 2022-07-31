from Lists import LinkedListFull


def sum(llA,llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedListFull.LinkedList()
    while n1 or n2:
        results = carry
        if n1:
            results += n1.value
            n1 = n1.next
        if n2:
            results += n2.value
            n2 = n2.next
        ll.add(int(results % 10))
        carry = results / 10
    return ll 


llA = LinkedListFull.LinkedList()
llA.generate(3,1,6)
llB = LinkedListFull.LinkedList()
llB.generate(3,2,6)
print(llA,"vs",llB)


print(sum(llA,llB))
