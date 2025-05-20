# menu/middleware.py
from django.shortcuts import redirect


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Разрешить доступ к странице входа и статике
        if request.path in ["/login/", "/static/"] or request.path.startswith("/admin"):
            return self.get_response(request)

        # Проверка авторизации
        if "user_id" not in request.session:
            return redirect("menu:login")

        return self.get_response(request)
