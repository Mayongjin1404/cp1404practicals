
class Project:
    def __init__(self, name, start_date, priority, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.completion = completion

    def is_complete(self):
        return self.completion == 100

    def __str__(self):
        return f"{self.name} ({self.start_date}) - Priority: {self.priority} - Completion: {self.completion}%"

    @classmethod
    def from_string(cls, data_str):
        name, start_date, priority, completion = data_str.split('\t')
        return cls(name, start_date, int(priority), int(completion))
