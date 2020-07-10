class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        # holds value of num at a moment in time i.e action1, action2 etc..
        self.history = []
        # holds the differential values (i.e current value - previous value) for the redo queue (last index is latest undo)
        self.redo_queue = []

    def add(self, num: int):
        self.history.append(self.value)
        self.value += num
        # if there is a redo chain, once a new value is set, the redo step for the next action is voided
        if len(self.redo_queue):
            self.redo_queue.pop(-1)

    def subtract(self, num: int):
        self.history.append(self.value)
        self.value -= num
        # if there is a redo chain, once a new value is set, the redo step for the next action is voided
        if len(self.redo_queue):
            self.redo_queue.pop(-1)

    def undo(self):
        # if there is history to be undone
        if len(self.history):
            # set the differential value from the undo
            self.redo_queue.append(self.value - self.history[-1])
            # set current value as previous value
            self.value = self.history[-1]
            # remove last action from history
            self.history.pop()

    def redo(self):
        # if there actions to be redone
        if len(self.redo_queue):
            # redo the differential change done by the undo
            self.value += self.redo_queue[-1]
            # add current state to history
            self.history.append(self.value)
            # remove last differential from redo chain
            self.redo_queue.pop(-1)

    def bulk_undo(self, steps: int):
        for i in range(steps):
            # if there is nothing left to undo, break
            if not len(self.history):
                break
            self.undo()

    def bulk_redo(self, steps: int):
        for i in range(steps):
            # if there is nothing left to redo, break
            if not len(self.redo_queue):
                break
            self.redo()
