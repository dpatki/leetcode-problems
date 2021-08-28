//submitted 19/08/2021
class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int count = 0;
        
        for(int i = 0; i < grid.size(); i++) {
            int prev = 0;
            for(int j = 0; j < grid[0].size(); j++) {
                int curr = grid[i][j];
                if (prev != curr) {
                    count++;
                }
                prev = curr;
            }
            if (prev == 1){
                count++;
            }
        }
        
        for(int j = 0; j < grid[0].size(); j++){
            int prev = 0;
            for (int i = 0; i < grid.size(); i++){
                int curr = grid[i][j];
                if (prev != curr) {
                    count++;
                }
                prev = curr;                
            }
            if(prev == 1){
                count++;
            }
        }
        
        return count;
        
    }
};