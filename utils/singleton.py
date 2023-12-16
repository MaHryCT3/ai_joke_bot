class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def reload_instance(cls):
        new_instance = super().__new__(cls)
        cls._instance = new_instance
        return new_instance
