import pytest
from tree import Tree

tree_list = [8, 5, 11, 4, 7, 10, 15]

class TestTree:

    def test_insert(self):
        result = []
        self.obj_tree = Tree(8)
        self.obj_tree.insert(5)
        self.obj_tree.insert(11)
        self.obj_tree.insert(4)
        self.obj_tree.insert(7)

        before_adding = self.obj_tree.print_inorder()
        self.obj_tree.insert(10)
        self.obj_tree.insert(15)

        after_adding = self.obj_tree.print_inorder()
        assert before_adding != after_adding



    def test_min(self):
        self.obj_tree = Tree(8)
        self.obj_tree.insert(5)
        self.obj_tree.insert(11)
        self.obj_tree.insert(4)
        self.obj_tree.insert(7)
        self.obj_tree.insert(10)
        self.obj_tree.insert(15)
        assert self.obj_tree.min_value() == 4

    def test_max(self):
        self.obj_tree = Tree(8)
        self.obj_tree.insert(5)
        self.obj_tree.insert(11)
        self.obj_tree.insert(4)
        self.obj_tree.insert(7)
        self.obj_tree.insert(10)
        self.obj_tree.insert(15)
        assert self.obj_tree.max_value() == 15

    def test_delete(self):
        self.obj_tree = Tree(8)
        self.obj_tree.insert(5)
        self.obj_tree.insert(11)
        self.obj_tree.insert(4)

        before_deleting = self.obj_tree.print_inorder()
        self.obj_tree.delete(5)
        after_deleting = self.obj_tree.print_inorder()
        assert before_deleting != after_deleting