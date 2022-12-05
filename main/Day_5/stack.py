class Stack:
    def __init__(self):
        self._crates = []

    def grab_crate(self):
        if len(self._crates) > 0:
            return self._crates.pop()
        else:
            return ""

    def grab_top_crates(self, nr):
        crates = []
        for i in range(0, nr):
            crates.append(self.grab_crate())
        crates.reverse()
        return crates

    def add_crate(self, crate):
        crate = crate.strip()
        self._crates.append(crate)

    def add_crates(self, crates):
        self._crates.extend(crates)

    def show_top_item(self):
        return ''.join(self._crates[-1:])

    def size(self):
        return len(self._crates)

    def reverse_order(self):
        self._crates.reverse()
