# Polymorphism concept taken from https://stackoverflow.com/questions/12516/expression-evaluation-and-tree-walking-using-polymorphism-ala-steve-yegge
import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class TreeNode(Node):
    def __init__(self, value, op=None):
        self.right = None
        self.left = None
        self.op = op
        self.value  = value
        
    def evaluate(self):
        
        if None == self.op:
            return int(self.value)
        if self.op == "+":
            return self.left.evaluate() + self.right.evaluate()
        if self.op == "-":
            return self.left.evaluate() - self.right.evaluate()
        if self.op == "*":
            return self.left.evaluate() * self.right.evaluate()
        if self.op == "/":
            return self.left.evaluate() // self.right.evaluate()        
        
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class  TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
    
        ops = set(['+', '-', '*', '/'])
        stack = []
        for value in postfix:
            if value in ops:
                operate = TreeNode(0,value)
                operate.right = stack.pop()
                operate.left = stack.pop()
                stack.append(operate)
            else:
                operate = TreeNode(value)
                stack.append(operate)
        return stack[-1]