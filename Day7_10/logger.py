class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.level = "INFO"
        return cls._instance

    def set_level(self, level):
        self.level = level

    def log(self, message):
        print(f"[{self.level}] {message}")

logger = Logger()
