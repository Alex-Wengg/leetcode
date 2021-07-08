/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    static bool heapComp(ListNode* a, ListNode* b) {
        return a->val > b->val;
}
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        ListNode head(0);
        ListNode *curNode  = &head;
        vector<ListNode*> v;
        
        for (auto i: lists){
            if (i) {
                v.push_back(i);
            }
        }
        make_heap(v.begin(), v.end(), heapComp);

        while(v.size() > 0){
            curNode->next = v.front();
            pop_heap(v.begin(), v.end(), heapComp);
            v.pop_back();
            curNode = curNode->next;
            if (curNode->next){
                v.push_back(curNode->next);
                make_heap(v.begin(), v.end(), heapComp);
                
            
            }
        }
        return head.next;
    }
};