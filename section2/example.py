class HistoryList(list):
    def __init__(self, initial_data=list()):
        super().__init__(initial_data)
        self.__history = []
    
    def append(self, item):
        super().append(item)
        self.__history.append(("append", item))

    def pop(self):
        item = super().pop()
        self.__history.append(("pop", item))
    
    def get_history(self):
        return self.__history.copy()
    
    # Question (b)
    def undo(self):
        if len(self.__history) > 0:
            last_op = self.__history.pop()
            if last_op[0] == "append":
                super().pop()
            else: # must be "pop"
                super().append(last_op[1])

    # Question (b) alternative
    def __setitem__(self, index, value):
        old_value = self[index]
        super().__setitem__(index, value)
        self.__history.append(("set", index, old_value))
        # undo method needs to be modified accordingly

if __name__ == "__main__":
    hl = HistoryList([1, 2, 3])
    hl.append("hello")
    hl.insert(1, "world")
    print("#1:", hl)
    print("#2:", hl.get_history())

