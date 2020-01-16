from rest_framework import routers

from messages.views import MessagesView

router = routers.SimpleRouter()
router.register('messages', MessagesView, basename='users')

urlpatterns = router.urls
