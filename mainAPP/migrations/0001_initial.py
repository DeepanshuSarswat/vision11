# Generated by Django 4.0.3 on 2022-05-06 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('url', models.TextField(primary_key=True, serialize=False, unique=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('time', models.DateTimeField()),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('team1', models.CharField(blank=True, max_length=60, null=True)),
                ('team2', models.CharField(blank=True, max_length=60, null=True)),
                ('is_match_end', models.BooleanField(default=False)),
                ('team1_img', models.TextField(blank=True, null=True)),
                ('team2_img', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('player_name', models.CharField(max_length=50)),
                ('player_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('player_points', models.FloatField(default=7)),
                ('player_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('team_name', models.CharField(max_length=50)),
                ('team_img', models.ImageField(blank=True, null=True, upload_to='team_img')),
                ('team_url', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captain', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='captain', to='mainAPP.player')),
                ('player1', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player1', to='mainAPP.player')),
                ('player10', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player10', to='mainAPP.player')),
                ('player11', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player11', to='mainAPP.player')),
                ('player2', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player2', to='mainAPP.player')),
                ('player3', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player3', to='mainAPP.player')),
                ('player4', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player4', to='mainAPP.player')),
                ('player5', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player5', to='mainAPP.player')),
                ('player6', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player6', to='mainAPP.player')),
                ('player7', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player7', to='mainAPP.player')),
                ('player8', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player8', to='mainAPP.player')),
                ('player9', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='player9', to='mainAPP.player')),
                ('vice_captain', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='vice_captain', to='mainAPP.player')),
            ],
        ),
        migrations.CreateModel(
            name='User_Feature_Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_first_name', models.CharField(max_length=20)),
                ('user_last_name', models.CharField(max_length=20)),
                ('user_email', models.CharField(max_length=50)),
                ('feature_title', models.CharField(max_length=100, null=True)),
                ('feature_des', models.TextField(blank=True, null=True)),
                ('is_seen', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlayersMatchData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runsScored', models.CharField(max_length=4)),
                ('ballsFaced', models.CharField(max_length=4)),
                ('fours', models.CharField(max_length=4)),
                ('sixes', models.CharField(max_length=4)),
                ('strikeRate', models.CharField(max_length=10)),
                ('out', models.BooleanField()),
                ('overs', models.CharField(max_length=4)),
                ('maidens', models.CharField(max_length=4)),
                ('runsGiven', models.CharField(max_length=4)),
                ('wickets', models.CharField(max_length=4)),
                ('wides', models.CharField(max_length=4)),
                ('noBalls', models.CharField(max_length=4)),
                ('economy', models.CharField(max_length=4)),
                ('catches', models.IntegerField()),
                ('runouts', models.IntegerField()),
                ('stumpings', models.IntegerField()),
                ('points', models.FloatField()),
                ('match_url', models.ForeignKey(on_delete=django.db.models.expressions.Case, to='mainAPP.match')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainAPP.player')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='player_team',
            field=models.ManyToManyField(to='mainAPP.team'),
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_fee', models.FloatField(default=1)),
                ('length', models.IntegerField(default=1)),
                ('price_fee', models.FloatField(default=0)),
                ('teams', models.ManyToManyField(to='mainAPP.userteam')),
            ],
        ),
    ]
