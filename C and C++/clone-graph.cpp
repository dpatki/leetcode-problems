//submitted 01/08/2021
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
private:
  std::unordered_map<int, Node*> potato;
public:
  Node* cloneGraph(Node* node) {
    if (!node) {
        return nullptr;
    }
    return herlpe(node);
  }

  Node* herlpe(Node* node) {
    /*new plan
return ptr to node
bc deeep copy
each elem in the new node-> neighbours needs to be allocd first
if val in potato - then retrn ptr to node
else return ptr to alloc node
    */
    
    if (potato.find(node->val) == potato.end()) {
      
    } else {
        
      return potato[node->val];
    }
    Node* newNode = new Node(node->val);
    potato.insert(make_pair(node->val, newNode));
      
    for (auto & element : node->neighbors) {
     
        newNode->neighbors.push_back(herlpe(element));
    
    }
    return newNode;
    
  }
};