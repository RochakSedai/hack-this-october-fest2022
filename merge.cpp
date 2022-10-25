class Solution
{
    public:
        ListNode* merge(ListNode *list1, ListNode *list2)
        {
            if (list1 == NULL) return list2;
            if (list2 == NULL) return list1;
            if (list1->val < list2->val)
            {
                list1->next = merge(list1->next, list2);
                return list1;
            }
            else
            {
                list2->next = merge(list1, list2->next);
                return list2;
            }
        }
    ListNode* mergeTwoLists(ListNode *list1, ListNode *list2)
    {
        return merge(list1, list2);
    }
};