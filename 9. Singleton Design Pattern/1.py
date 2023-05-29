class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


# Usage
instance1 = Singleton()
instance2 = Singleton()

print(instance1 is instance2)  # Output: True

"""
By using the Singleton pattern, both instances refer to the same object.
Any changes made to one instance will be reflected in the other.
"""