class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):

        if self.value is None:
            self.value = value
            print(f"Inserting value {self.value} is {value}")
            return

        # 2) Checking value
        if self.value == value:
            raise ValueError(f"{value} in tree already")
        if self.value > value:
            if self.left:
                print(f"Inserting LEFT recursively {value} for {self.value}")
                self.left.insert(value)
            else:
                self.left = Tree(value)
                print(f"Inserting {self.left.value} LEFT")
        else:
            if self.right:
                print(f"Inserting recursively {value} for {self.value}")
                self.right.insert(value)
            else:
                self.right = Tree(value)
                print(f"Insert {self.right.value} RIGHT")


    def insert_list(self, list_tree):
        if len(list_tree) % 2 == 0:
            raise ValueError(f"{list_tree} invalid list")
        i_max = (len(list_tree) - 3) // 2
        for i in range(i_max+1):
            value = list_tree[i]
            if value is None:
                continue
            left = list_tree[2*i + 1]
            right = list_tree[2*i + 2]
            if left is not None:
                if left >= value:
                    raise ValueError(f"{left} is greatest than {value}")
            if right is not None:
                if right <= value:
                    raise ValueError(f"{right} is less than {value}")

        for i in list_tree:
            if i is None:
                continue
            self.insert(i)


    def print_inorder(self, result_list = None):

        if result_list is None:
            result_list = []

        if self.left:
            self.left.print_inorder(result_list)

        result_list.append(self.value)

        if self.right:
            self.right.print_inorder(result_list)

        print(result_list)
        return result_list

    def min_value(self):
        if self.left:
            return self.left.min_value()
        else:
            return self.value

    def max_value(self):

        if self.right:
            return self.right.max_value()
        else:
            return self.value


    def delete(self, value, parent=None):

        if self.value > value:
            if self.left:
                self.left.delete(value, self)
        elif self.value < value:
            if self.right:
                self.right.delete(value, self)
        else:

            if self.left is None and self.right is None:
                if parent:

                    if parent.left is self:

                        parent.left = None
                    else:

                        parent.right = None

            if self.right and not self.left:
                self.right.value, self.value = self.value, self.right.value
                self.right.delete(self.right.value, self)
                return


            if self.left and not self.right:
                self.left.value, self.value = self.value, self.left.value
                self.left.delete(self.left.value, self)
                return
            if self.left and self.right:
                inorder_successor = self.right.min_value()
                self.value, inorder_successor = inorder_successor, self.value
                self.right.delete(self.value, self)


root = Tree(9)


print("-------")
print("-------")
root.insert(6)
root.insert(13)
root.insert(4)
root.print_inorder()
root.delete(4)
root.print_inorder()