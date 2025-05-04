class WorkingMemoryManager:
    def __init__(self):
        self.working_memory = {}

    def add_to_memory(self, key, value):
        # Add data to working memory
        self.working_memory[key] = value

    def retrieve_from_memory(self, key):
        # Retrieve data from working memory
        return self.working_memory.get(key, None)

    def clear_memory(self):
        # Clear the working memory
        self.working_memory.clear()
