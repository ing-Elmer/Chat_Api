import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

# Establecer la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_api.settings')

# Obtener la aplicación ASGI de Django (esto maneja las solicitudes HTTP)
application = get_asgi_application()

# Retrasar la importación de las rutas de WebSocket para evitar la carga temprana de modelos
from rooms.routing import rooms_websocket_urlpatterns
from comments.routing import comments_websocket_urlpatterns
from notification.routing import notifications_websocket_urlpatterns

# Configurar el enrutamiento para HTTP y WebSocket
application = ProtocolTypeRouter(
    {
        "http": application,  # Las solicitudes HTTP se manejan con la aplicación Django normal
        "websocket": AuthMiddlewareStack(  # Las solicitudes WebSocket requieren autenticación
            URLRouter(
                rooms_websocket_urlpatterns + comments_websocket_urlpatterns + notifications_websocket_urlpatterns
            ),
        ),
    }
)
