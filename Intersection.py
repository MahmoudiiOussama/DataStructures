from Lists import LinkedListFull


def intersection(llA,llB):
    if llA.tail is not llB.tail:
        return None

    lenA = len(llA)
    lenB = len(llB)
    shorter = llA if lenA < lenB else llB
    longer = llA if lenA > lenB else llB
    diff = len(longer) - len(shorter)
    longLL = longer.head
    shortLL = shorter.head
    for i in range(diff):
        longLL =longLL.next

    while shortLL is not longLL:
        shortLL = shortLL.next
        longLL = longLL.next
    return shortLL







def addSameNode(llA,llB,value):
    newnode = LinkedListFull.Node(value)
    llA.tail.next = newnode
    llA.tail = newnode
    llB.tail.next = newnode
    llB.tail = newnode



llA = LinkedListFull.LinkedList()
llB = LinkedListFull.LinkedList()
llA.generate(3,0,10)
llB.generate(4,0,10)

addSameNode(llA,llB,11)
addSameNode(llA,llB,14)
print(llA)
print(llB)

print(intersection(llA,llB))


