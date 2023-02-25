import serial


class BasicSerial:

    def __init__(self, path: str, baud_rate: int = 9200, timeout=1) -> None:
        self.serial = serial.Serial(path, baud_rate, timeout=timeout)
        self.serial.open()

    def read_serial(self) -> str:
        return self.serial.read().decode()

    def write_serial(self, string: str):
        self.serial.write(string.encode())
