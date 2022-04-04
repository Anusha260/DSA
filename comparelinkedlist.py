def compare_lists(list1, list2):

    if list1 is None and list2 is None:
        return 0
    else:
        nodeA = list1
        nodeB = list2
        while nodeA and nodeB:
            if nodeA.data != nodeB.data:
                return 0
            nodeA = nodeA.next
            nodeB = nodeB.next
        
        if nodeA is None and nodeB is None:
            return 1
        else:
            return 0

