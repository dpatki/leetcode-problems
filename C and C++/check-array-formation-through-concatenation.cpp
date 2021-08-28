//submitted 22/08/2021

class Solution {
public:
    bool canFormArray(vector<int>& arr, vector<vector<int>>& pieces) {
        while(!pieces.empty()) {
            vector<int> shard = pieces.back();
            pieces.pop_back();
            int first = shard[0];
            bool found = false;
            for(int i = 0; i < arr.size(); i++) {
                if (arr[i] == first) {
                    found = true;
                    for(int j = 0; j < shard.size(); j++) {
                        if (arr[i+j] != shard[j]) {
                            return false;
                        }
                    }
                    break; 
                }
            }
            if (!found) {
                return false;
            }
            
        }
        return true;
        
    }
};