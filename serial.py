"""Python serial number generator."""

class SerialGenerator:

    def __init__(self, start=0):
        self.start = start
        self.next = start

    def generate(self):
        if self.next == self.start:
            result = self.start
            self.next += 1
        else:
            result = self.next
            self.next += 1
        return result
            
    def reset(self):
        self.next = self.start
        return ''

serial = SerialGenerator(start=100)
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.reset())
print(serial.generate())
    # """Machine to create unique incrementing serial numbers.


    


    # >>> serial.generate()
    # 100

    # >>> serial.generate()
    # 101

    # >>> serial.generate()
    # 102

    # >>> serial.reset()

    # >>> serial.generate()
    # 100
    # """

