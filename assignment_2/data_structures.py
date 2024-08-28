# Imports
from __future__ import annotations  # Needed for typing Node class

#import warnings
from typing import Any

#import binarytree
#import heapdict


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
        self.head = None
        self.tail = None

    def enqueue(self, data: Any) -> None:
        if self.tail == None:
            self.tail = [Node(data=data)]
            self.head = [Node(data=data,next=self.tail)]
            return
        self.tail[0].next = [Node(data=data)]
        self.tail = self.tail[0].next

    def peek(self) -> Node | None:
        return self.head.data

    def dequeue(self) -> Node:
        if self.head == None:
            raise IndexError
            return
        self.head = self.head[0].next


class EmergencyRoomQueue:
    def __init__(self):
        """Initialize emergency room queue, use heapdict as property 'queue'"""
        pass

    def add_patient_with_priority(self, patient_name: str, priority: int) -> None:
        """Add patient name and priority to queue

        # Arguments:
        patient_name:   String with patient name
        priority:       Integer. Higher priority corresponds to lower-value number.
        """
        pass

    def update_patient_priority(self, patient_name: str, new_priority: int) -> None:
        """Update the priority of a patient which is already in the queue

        # Arguments:
        patient_name:   String, name of patient in queue
        new_priority:   Integer, updated priority for patient

        """
        pass

    def get_next_patient(self) -> str:
        """Remove highest-priority patient from queue and return patient name

        # Returns:
        patient_name    String, name of patient with highest priority
        """
        pass


class BinarySearchTree:
    def __init__(self, root: binarytree.Node | None = None):
        """Initialize binary search tree

        # Inputs:
        root:    (optional) An instance of binarytree.Node which is the root of the tree

        # Notes:
        If a root is supplied, validate that the tree meets the requirements
        of a binary search tree (see property binarytree.Node.is_bst ). If not, raise
        ValueError.
        """
        pass

    def insert(self, value: float | int) -> None:
        """Insert a new node into the tree (binarytree.Node object)

        # Inputs:
        value:    Value of new node

        # Notes:
        The method should issue a warning if the value already exists in the tree.
        See https://docs.python.org/3/library/warnings.html#warnings.warn
        In the case of duplicate values, leave the tree unchanged.
        """
        pass

    def __str__(self) -> str | None:
        """Return string representation of tree (helper function for debugging)"""
        if self.root is not None:
            return str(self.root)











if __name__ == "__main__":
    n = Stack()
    for i in [1,2,3,4,5,6,7,8,9,10]:    
        n.push(i)