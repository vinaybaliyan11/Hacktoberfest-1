//https://practice.geeksforgeeks.org/problems/reorder-list/1

class gfg {
    Node reorderlist(Node head) {
        if(head == null || head.next == null || head.next.next == null) {
            return head;
        }
        helper(head, head);
        return head;
    }
    public Node helper(Node node, Node head) {
        if(node.next == null) {
            node.next = head.next;
            head.next = node;
            return node.next;
        }
        head = helper(node.next, head);
        if(head == null) {
            return null;
        }
        else {
            node.next = head.next;
            head.next = node;
            if(node.next == node) {
                node.next = null;
                return null;
            }
            else if(node.next.next == node) {
                node.next.next = null;
                return null;
            }
            else {
                return node.next;
            }
        }
    }
}
