class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        height = leftHeight = rightHeight = 0
        if root==None:
            return 0
        elif root.left == None and root.right != None:
            rightHeight = self.getHeight(root.right)+1
        elif root.left != None and root.right == None:
            leftHeight = self.getHeight(root.left)+1 #node 1
        elif root.left != None and root.right != None:#node 3
            leftHeight = self.getHeight(root.left)+1 #node 2, 4
            rightHeight = self.getHeight(root.right)+1 #node 5, 6
        height = max(leftHeight,rightHeight)
        return height
        
        
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
