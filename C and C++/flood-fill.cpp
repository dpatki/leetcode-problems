//submitted 21/08/2021
class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        
        vector<vector<int>> stack;
        stack.push_back({sr, sc});
        int stuff = image[sr][sc];
        
        while (!stack.empty()) {
            vector<int> coords = stack.back();
            stack.pop_back();
            if ((coords[0] < 0) || (coords[0] >= image.size()) || (coords[1] < 0) || (coords[1] > image[0].size())) {
                continue;
            }
            if (image[coords[0]][coords[1]] != stuff) {
                continue;
            }
            image[coords[0]][coords[1]] = -1;
            stack.push_back({coords[0] - 1, coords[1]});
            stack.push_back({coords[0] + 1, coords[1]});
            stack.push_back({coords[0], coords[1] - 1});
            stack.push_back({coords[0], coords[1] + 1});     
        }
        
        for(int i = 0; i < image.size(); i++){
            for(int j = 0; j < image[0].size(); j++) {
                if (image[i][j] == -1) {
                    image[i][j] = newColor;
                }
            }
        }
        
        return image;
        
    }
    
};