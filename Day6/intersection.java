import java.util.* ;
import java.io.*;
class Solution {
	public static int findIntersection(LinkedListNode<Integer> headA, LinkedListNode<Integer> headB) {
        Set<LinkedListNode> seen = new HashSet<LinkedListNode>();
        while(headA!=null){
            seen.add(headA);
            headA=headA.next;
        }
        while(headB!=null){
            if(seen.contains(headB)){
                return headB.data;
            }
            else{
                headB=headB.next;
            }
        }
        return -1;
	}
}