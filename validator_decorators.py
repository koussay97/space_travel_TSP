
def is_string(func):
    def wrapper(*args, **kwargs):
        value = kwargs.get('value', args[0] if len(args)>0 else None)
        if not isinstance(value,str):
            raise TypeError(f"in the functuion {func.__name__}, expected a string but got {type(value).__name__}") 
        return func(*args, **kwargs)
    return wrapper

def is_float(func): 
    def wrapper(*args, **kwargs):
        value = kwargs.get('value', args[0] if len(args)>0 else None)
        if not isinstance(value,(float,int)):
            raise TypeError(f"in the functuion {func.__name__}, expected a float but got {type(value).__name__}") 
        return func(*args, **kwargs)
    return wrapper
def is_valid_dict_of_air_friction_forces(func):
    def wrapper(*args, **kwargs):
        dict_value= kwargs.get('value',args[0]if len(args)>0 else None)
        if not isinstance(dict_value, dict):
            raise TypeError(f"in function {func.__name__} expected a dictionary with key : str and val :int or float but got {type(dict_value).__name__}")
        if len(dict_value) != 10:
            raise TypeError(f"in function {func.__name__} we must have 10 planet names and values but we got {len(dict_value)}")
        for key,value in dict_value.items():
            if key not in {"Sun","Mercury","Earth","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto","Venus" }:
                raise ValueError(f"in function {func.__name__} we have got an unknown planet {key}")        
        return func(*args, **kwargs)
    return wrapper    