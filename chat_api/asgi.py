import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.conf import settings  # Asegúrate de usar la configuración correcta.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_api.settings')

application = get_asgi_application()

# Realizar importaciones retrasadas
from rooms.routing import rooms_websocket_urlpatterns
from comments.routing import comments_websocket_urlpatterns
from notification.routing import notifications_websocket_urlpatterns

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
