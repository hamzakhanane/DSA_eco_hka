def mergeTwoLists(l1, l2):
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
                return l2
        elif l2 is None:
                return l1
        head_node, add_node, take_node = l2, l2, l1
        if l1.val <= l2.val:
            add_node, head_node = l1, l1
            take_node = l2
        while take_node is not None:
            if add_node.next is None:
                add_node.next = take_node
                return head_node
            else:
                if take_node.val <= add_node.next.val:
                    temp_take = take_node.next
                    temp_add = add_node.next
                    add_node.next = take_node
                    take_node.next = temp_add
                    take_node = temp_take
            add_node = add_node.next
        return head_node