class Signal:
    def __init__(self):
        self.stream = ""

    def setup(self):
        with open("input.txt") as f:
            self.stream = f.read()

    def position_start_marker(self):
        for i in range(0, len(self.stream)):
            potential_marker = self.stream[i:i + 4]
            if is_marker_start(potential_marker):
                return i + 4

    def position_start_message(self):
        for i in range(0, len(self.stream)):
            potential_message = self.stream[i:i + 14]
            if is_marker_start(potential_message):
                return i + 14


def is_marker_start(chars):
    for i in range(0, len(chars)):
        leftoverchars = chars[:i] + chars[i + 1:]
        if chars[i] in leftoverchars:
            return False
    return True


if __name__ == '__main__':
    signal = Signal()
    signal.setup()
    print(signal.position_start_marker())
    print(signal.position_start_message())
