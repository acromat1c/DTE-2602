# Imports
from __future__ import annotations  # Needed for typing Node class

#import warnings
from typing import Any

import binarytree
import heapdict


# Node class (do not change)
class Node:
    def __init__(self, data: Any = None, next: None | Node = None):
        self.data = data
        self.next = next


# Add your implementations below, and commit and push the file to your repository


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data: Any) -> None:
        if self.head is None:
            self.head = Node(data=data)
            return
        node = Node(data = data, next = self.head)
        self.head = node
            

    def peek(self) -> Node | None:
        return self.head.data

    def pop(self) -> Node:
        if self.head == None:
            raise IndexError
            return
        self.head = self.head.next


class Queue:
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def enqueue(self, data: Any, node = None) -> None:
        if node == None:self.enqueue(data,node=self.tail);return
        if node.data is None:
            node.data = data
            node.next = Node()
            self.tail = node
            print(node.data)
            return
        self.enqueue(data,node=node.next)

    def peek(self) -> Node | None:
        return self.head.data

    def dequeue(self) -> Node:
        return self.head.data


class EmergencyRoomQueue:
    def __init__(self):
        self.hd = heapdict.heapdict()

    def add_patient_with_priority(self, patient_name: str, priority: int) -> None:
        self.hd[str(patient_name)] = int(priority)

    def update_patient_priority(self, patient_name: str, new_priority: int) -> None:
        self.hd[str(patient_name)] = int(new_priority)

    def get_next_patient(self) -> str:
        print(self.hd.peekitem())


class BinarySearchTree:
    def __init__(self, root: binarytree.Node | None = None):
        self.root = binarytree.Node(root)

    def insert(self, value: float | int, node = None) -> None:
        if node == None:self.insert(value,node=self.root);return
        if node.value >= value:
            if node.right is None:
                node.right = binarytree.Node(value)
                return
            self.insert(value,node=node.right);return
        if node.left is None:
            node.left = binarytree.Node(value)
            return
        self.insert(value,node=node.left);return

    def __str__(self) -> str | None:
        """Return string representation of tree (helper function for debugging)"""
        if self.root is not None:
            return str(self.root)











#if __name__ == "__main__":
    #n = Queue()
    #for i in [1,2,3,4,5,6,7,8,9,10]:    
        #n.enqueue(i)
    #print(n.tail.data)
    # c = EmergencyRoomQueue()
    # c.add_patient_with_priority("jack",5)
    # c.add_patient_with_priority("Hack",5)
    # c.add_patient_with_priority("Kack",2)
    # c.add_patient_with_priority("Lack",9)
    # c.update_patient_priority("lack", 2)
    # c.get_next_patient()
    #h = BinarySearchTree(7)
    #h.insert(5)
    #h.insert(9)
    #h.insert(1)
    #h.insert(2)
    #h.insert(8)
    #h.insert(4)
    #print(h)
