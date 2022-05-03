from mainAPP.models import Match,Player, PlayersMatchData,Team
from django.utils import timezone
from .serializers import FantasyScoreSerializer, MatchListSerializer,GameSquadSerializer
from rest_framework.response import Response
from usermanagerAPP.models import User1
from django.shortcuts import render

class vision11:
    def get_match_list(self):
        matches = Match.objects.filter(time__gt=timezone.now())
        match = MatchListSerializer(matches,many=True)
        return Response({'status':200,'message':'success','data':match.data})

        

    def get_todays_squad(self,team1,team2):
        match = Match.objects.filter(team1=team1,team2=team2)[0]
        if (match.time-timezone.now()).days < 0:
            return Response({'status':404,'message':'Match has started.'})
        if (match.time - timezone.now()).days == 0 and (match.time - timezone.now()).seconds < 15*60:
            return Response({'status':404,'message':'Deadline has passed.'})
        t1 = Team.objects.get(team_name=team1)
        t2 = Team.objects.get(team_name=team2)
        p1 = Player.objects.filter(player_team=t1)
        p2 = Player.objects.filter(player_team=t2)
        gamesquad1 = GameSquadSerializer(p1,many=True)
        gamesquad2 = GameSquadSerializer(p2,many=True)
        return Response({'status':200,'message':'success','team1':gamesquad1.data,'team2':gamesquad2.data})



    def get_fantasy_score(self,url):
        match = Match.objects.get(url=url)
        players = PlayersMatchData.objects.filter(match_url=match)
        serialized_players = FantasyScoreSerializer(players,many=True)
        return Response({'status':200,'message':'success','match':url,'data':serialized_players.data})


    def get_completed_matches(self):
        match = Match.objects.filter(is_match_end=False)
        serialized_matches = MatchListSerializer(match,many=True)
        return Response({'status':200,'message':'success','data':serialized_matches.data})


    def get_Live_matches(self):
        match = Match.objects.filter(is_match_end=False,time__lt=timezone.now())
        serialized_matches = MatchListSerializer(match,many=True)
        return Response({'status':200,'message':'success','data':serialized_matches.data})

    
    def get_upcoming_matches(self):
        match = Match.objects.filter(is_match_end=False,time__gt=timezone.now())
        serialized_matches = MatchListSerializer(match,many=True)
        return Response({'status':200,'message':'success','data':serialized_matches.data})



class vision11_render:
    
    def render_age_adminportal(self,request):
        users = User1.objects.filter(adult=False)
        user_obj = [user for user in users if user.aadhar_image!='']
        return render(request,'admin_age_verification.html',{'data':user_obj})