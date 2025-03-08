import os
from django.core.asgi import get_asgi_application

# Configura el módulo de settings antes de cualquier otra importación
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_api.settings')

# Primero inicializa la aplicación Django
django_application = get_asgi_application()

# Luego de inicializar Django, importa todo lo relacionado con Channels
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

# Ahora importa las rutas de WebSocket
from rooms.routing import rooms_websocket_urlpatterns
from comments.routing import comments_websocket_urlpatterns
from notification.routing import notifications_websocket_urlpatterns

application = ProtocolTypeRouter(
    {
        "http": django_application,
        "websocket": AuthMiddlewareStack(
            URLRouter(
                rooms_websocket_urlpatterns + comments_websocket_urlpatterns + notifications_websocket_urlpatterns
            ),
        ),
    }
)