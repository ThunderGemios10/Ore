from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from ore.accounts.views import UserViewSet, current_session, current_session_user
from ore.core.views import NamespaceViewSet, OrganizationViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'namespaces', NamespaceViewSet, base_name='namespace')
router.register(r'users', UserViewSet, base_name='user')
router.register(r'organizations', OrganizationViewSet, base_name='organization')

urlpatterns = router.urls + [
    url(r'^session$', current_session, name='session-detail'),
    url(r'^session\.(?P<format>[a-z0-9]+)$', current_session, name='session-detail'),
    url(r'^session/user$', current_session_user, name='session-user-detail'),
    url(r'^session/user\.(?P<format>[a-z0-9]+)$', current_session_user, name='session-user-detail'),
]
