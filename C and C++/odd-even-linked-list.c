//submitted 12/30/2020
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* oddEvenList(struct ListNode* head){
  if (!head) {
    return head;
  }
  if (!head->next) {
    return head;
  }
  if (!head->next->next) {
      return head;
  }
  struct ListNode *first = head;
  struct ListNode *two = head->next;
  struct ListNode *iterate = head;
  while (iterate->next) {
    struct ListNode *next = iterate->next;
    iterate->next = next->next;
    iterate = next;
  }
  struct ListNode *endodd = first->next;
  while (endodd->next) {
    endodd = endodd->next;
  }
  endodd->next = two;
  return head;

}