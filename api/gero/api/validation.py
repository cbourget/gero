class ValidationError(Exception):

    def __init__(self, key, messages):
        if not isinstance(messages, list):
            messages = [messages]

        super().__init__('{}: {}'.format(key, '; '.join(messages)))

        self.key = key
        self.messages = messages

    def dump(self):
        return {
            'key': self.key,
            'errors': self.messages
        }
