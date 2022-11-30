class Node:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.child = []

class Tree:
    def __init__(self,root):
        self.root = root

    def addChild(self, node_parent,data):
        c = Node(data)
        c.parent = node_parent
        node_parent.child.append(c)
        return c

    def sums(self, node):
        sums = 0
        if len(node.child)==0:
            return node.data
        for c in node.child:
            sums = sums + self.sums(c)
        return sums + node.data
                
    def sibling(self, node):
        if (node.parent.child==0) or (node.parent.child==1):
            return node.data
        else:
            s = 0
            for c in node.parent.child:
                s = s + c.data
            return s
            
        
    


if __name__ =='__main__':
    val200 = Node(200)
    t = Tree(val200) #Level 0

    #Level 1 parent 200
    val23 = t.addChild(val200, 23) 
    val11 = t.addChild(val200, 11)

    #Level 2 parent 23
    val13 = t.addChild(val23, 13) 
    val57 = t.addChild(val23, 57) 

    #Level 2 parent 11
    val32 = t.addChild(val11, 32) 

    #Level 3 parent 13
    val42 = t.addChild(val13, 42) 
    val51 = t.addChild(val13, 51) 
    val71 = t.addChild(val13, 71) 

    #Level 3 parent 57
    val12 = t.addChild(val57, 12) 
    val15 = t.addChild(val57, 15)

    #Level 3 parent 24
    val33 = t.addChild(val32, 33)
    val8 = t.addChild(val32, 8)

    # No 2. #
    print(f'Total value of node {val200.data} and all of its decendands = {t.sums(val200)}')
 
    # No 3. #
    print(f'Total value of all sibling on node {val33.data} = {t.sibling(val33)}')
