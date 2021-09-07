from games.minesweeper.models import Minesweeper
from rest_framework import serializers


class MinesweeperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minesweeper
        fields = ['name', 'rows', 'cols', 'mines', 'player']
