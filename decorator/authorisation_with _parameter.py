def authorised(allowed_role):
    def decorator(func):
        def wrapper(user_role):
            if user_role in allowed_role:
                return func(user_role)
            
            else:
                raise PermissionError("unauthorised")
        return wrapper
    return decorator

@authorised("admin")
def resticated_access(user_role):
    return f'{user_role} is granted'

print(resticated_access("admin"))