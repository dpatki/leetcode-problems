//submitted 01/01/2021
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    if (!head) {
        return false;
    }
    if (!head->next) {
        return false;
    }
    int counter = 0;
    while (head->next) {
        counter++;
        head = head->next;
        if (counter > 10001) {
            return true;
        }
    }
    return false;
}