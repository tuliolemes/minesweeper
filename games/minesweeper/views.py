from django.contrib.auth.models import Group
from rest_framework import viewsets
from games.minesweeper.serializers import MinesweeperSerializer
from games.minesweeper.models import Minesweeper


class MinesweeperViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Minesweeper.objects.all()
    serializer_class = MinesweeperSerializer
