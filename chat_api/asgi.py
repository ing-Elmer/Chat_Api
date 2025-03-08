import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_api.settings')

application = get_asgi_application()

from rooms.routing import rooms_websocket_urlpatterns
from comments.routing import comments_websocket_urlpatterns
from notification.routing import notifications_websocket_urlpatterns

# Usar el puerto proporcionado por la variable de entorno PORT
port = os.getenv('PORT', 8000)  # Usa 8000 como fallback si no está definido

application = ProtocolTypeRouter(
    {
        "http": application,
        "websocket": AuthMiddlewareStack(
            URLRouter(
                rooms_websocket_urlpatterns + comments_websocket_urlpatterns + notifications_websocket_urlpatterns
            ),
        ),
    }
)

