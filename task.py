class Task:
    def __init__(self, title, description, created_at):
        self.title = title
        self.description = description
        self.created_at = created_at
    
    def to_dictionary(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at,
        }