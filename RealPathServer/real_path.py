from os import getcwd


class NodeDLinkedList:

    def __init__(self, key=None, follow=None, prev=None):
        super().__init__()
        self.key = key
        self.follow = follow
        self.prev = prev


class DLinkedList:
    """You can get by with the standard deck, but the problem was solved in the framework of the study of data
    structures and algorithms from Cormen, therefore, we use our own written structure"""
    def __init__(self):
        super().__init__()
        self.nil = NodeDLinkedList()

    def insert(self, key):
        new_node = NodeDLinkedList(key=key, follow=self.nil)
        if self.nil.prev is not None:
            new_node.prev = self.nil.prev
            self.nil.prev.follow = new_node
        else:
            new_node.prev = self.nil
            self.nil.follow = new_node
        self.nil.prev = new_node

    def delete(self, del_node):
        curr_node = self.nil.prev
        while curr_node != self.nil:
            if curr_node == del_node:
                del_node.prev.follow = del_node.follow
                del_node.follow.prev = del_node.prev
                del del_node
                return
            curr_node = curr_node.prev

    def _back_list_crowl(self):
        curr_node = self.nil.prev
        while curr_node != self.nil:
            print(curr_node.key)
            curr_node = curr_node.prev

    def __str__(self):
        super().__str__()
        str_ = ''
        curr_node = self.nil.follow
        while curr_node != self.nil:
            str_ += str(curr_node.key)
            curr_node = curr_node.follow
        return str_


class RealPath:

    def __init__(self, path):
        super().__init__()
        self.user_path = path
        self._dll = DLinkedList()
        self._num_remove_segments = 0

    def _fill_DLinkedList(self):
        """If there is a dot at the beginning of the path, it fills pwd"""
        path = self.user_path
        if path[0] == '.' or self._not_dot_or_slash(path[0]):
            path = getcwd() + '/' + path
        for idx in range(0, len(path)):
            self._dll.insert(path[idx])

    def real_path(self):
        """returns the real path"""
        self._fill_DLinkedList()
        nil = self._dll.nil

        curr_symbol = self._dll.nil.prev
        self._clean_end()
        while curr_symbol != nil:
            if curr_symbol.key == '/':
                if curr_symbol.prev.key == '.' and curr_symbol.prev.prev.key == '.' and curr_symbol.prev.prev.prev.key == '/':
                    self._two_dots(curr_symbol)
                elif curr_symbol.prev.key == '.' and curr_symbol.prev.prev.key == '/':
                    self._two_slash_and_dot(curr_symbol)
                elif curr_symbol.prev.key == '/':
                    self._dll.delete(curr_symbol)
                elif self._num_remove_segments:
                    self._remove_segment(curr_symbol)
            curr_symbol = curr_symbol.prev
        self._clean_slash(nil)

        return str(self._dll)

    def _two_dots(self, curr_symbol):
        """if there are two points between slashes, then this is remembered, and the points are deleted"""
        self._dll.delete(curr_symbol)
        self._dll.delete(curr_symbol.prev)
        self._dll.delete(curr_symbol.prev.prev)
        self._num_remove_segments += 1

    def _two_slash_and_dot(self, curr_symbol):
        """if there is a dot between slashes, then the dot and the first slash are deleted"""
        self._dll.delete(curr_symbol)
        self._dll.delete(curr_symbol.prev)

    def _clean_end(self):
        """Preliminary processing"""
        curr_symbol = self._dll.nil.prev
        if curr_symbol.key == '.' and curr_symbol.prev.key == '.' and curr_symbol.prev.prev.key == '/':
            self._dll.delete(curr_symbol)
            self._dll.delete(curr_symbol.prev)
            self._num_remove_segments += 1

    def _remove_segment(self, curr_symbol):
        """segment deletion, if before /../"""
        self._dll.delete(curr_symbol)
        curr_symbol = curr_symbol.prev
        while curr_symbol.key != '/':
            self._dll.delete(curr_symbol)
            curr_symbol = curr_symbol.prev
        self._num_remove_segments -= 1

    def _clean_slash(self, nil):
        """removal of extra slashes at the very end of processing"""
        curr_symbol = nil.prev
        if curr_symbol.key == '/' and curr_symbol.prev != nil:
            self._dll.delete(curr_symbol)
        elif curr_symbol.key == '.' and curr_symbol.prev.key == '/':
            self._dll.delete(curr_symbol)
            self._dll.delete(curr_symbol.prev)

    @staticmethod
    def _not_dot_or_slash(curr_symbol_key):
        return True if curr_symbol_key != '.' and curr_symbol_key != '/' else False
