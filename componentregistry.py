class ComponentRegistry:
    _handlers = {}
    
    @classmethod
    def register(cls,compType):
        def wrapper(func):
            cls._handlers[compType] = func
            return func 
        return wrapper

    @classmethod 
    def get_handler(cls,compType):
        return cls._handlers.get(compType,None)