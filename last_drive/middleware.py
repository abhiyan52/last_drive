import threading

_thread_locals = threading.local()


def get_current_user():
    return getattr(_thread_locals, "user", None)


def set_current_user(user):
    _thread_locals.user = user


class UserDataProtectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = None
        if hasattr(request, "user") and request.user.is_authenticated:
            user = request.user
        set_current_user(user)
        response = self.get_response(request)
        return response
