from datetime import datetime

class log:
    def __init__(self) -> None:
        now = datetime.now()
        self.current_date = now.strftime("%d-%m-%Y %H:%M:%S")

        self.red = "\033[31m"
        self.green = "\033[32m"
        self.yellow = "\033[33m"
        self.blue = "\033[34m"

        self.end = "\033[0m"

    def error(self, message: str) -> str:
        return f"{self.yellow} {self.current_date} {self.end}|{self.red} ERROR {self.end}| {message}"

    def note(self, message: str) -> str:
        return f"{self.yellow} {self.current_date} {self.end}|{self.blue} NOTE {self.end}| {message}"

    def success(self, message: str) -> str:
        return f"{self.yellow} {self.current_date} {self.end}|{self.green} SUCCESS {self.end}| {message}"