from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ore.teams.models import OrganizationTeam
from ore.teams.permissions import OrganizationTeamPermission
from ore.teams.serializers import TeamSerializer, OrganizationTeamSerializer, OrganizationTeamUpdateSerializer


class TeamViewSet(ModelViewSet):

    lookup_field = 'pk'
    serializer_class = TeamSerializer
    permission_classes = [OrganizationTeamPermission]


class OrganizationTeamViewSet(TeamViewSet):

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return OrganizationTeam.objects.as_user(self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            print('OTUS')
            return OrganizationTeamUpdateSerializer

        return OrganizationTeamSerializer