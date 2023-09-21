def user(role):
    def decorator(func):
        def wrapper(*a,**b):
            if role=="admin":
                return func(*a,**b)
            else:
                raise PermissionError("Athentication denied")
        return wrapper
    return decorator
@user(role="admin")
def admin_administer_only():
    return "admin access granted"

print(admin_administer_only())
    
        