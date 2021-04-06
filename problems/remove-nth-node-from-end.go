/** https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    dummy := &ListNode{}
	dummy.Next = head
    
    temp := dummy
    prev := dummy
    for i:=1;;i++{
        if temp.Next != nil{
            temp = temp.Next
             if i > n{
                 prev = prev.Next
            }
        }else{
            break
        }
    }
    prev.Next = prev.Next.Next
    return dummy.Next
    
}
