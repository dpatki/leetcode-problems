class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }
        std::map<int, int> things;
        for (int i = 0; i < nums.size(); i++) {
            things[nums[i]] = 1;
        }
        int best = 0;
        int cur = -2000000000;
        int current = 0;
        for (auto i: things) {
            
            if (cur + 1 != i.first) {
                current = 0;
                cur = i.first;
                
            } else {
                cur = i.first;
                current +=1;
                if (current > best) {
                    best = current;
                }
            }
        }
        return best+1;
    }
};