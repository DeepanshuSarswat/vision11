from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from mainAPP.repository import vision11, vision11_render

# Create your views here.


def RenderHomePage(request):
    '''
    This method is used for
    rendering home page.
    '''
    return render(request, 'home.html')


@login_required(login_url='/accounts/login')
def RenderDashboard(request):
    '''
    This method is used for
    rendering dashboard page.
    '''
    try:
        return vision11_render.render_dashboard(request)
    except:
        return redirect('/')


@login_required(login_url='/accounts/login')
def RenderTodaysMatches(request):
    '''
    This method is used for
    rendering Today's Matches page.
    '''
    return render(request, 'Scheduled_matches.html')


def RenderAgeVerificationAdmin(request):
    if request.user.is_authenticated and request.user.is_staff:
        return vision11_render().render_age_adminportal(request)
    return redirect('/')


class GetAgeVerificationRequests(APIView):
    def get(self,request):
        try:
            if request.user.is_authenticated and request.user.is_staff:
                return vision11().get_age_verification_requests()
            return Response({'status':403,'message':'Invalid Credentials for admin.'})
        except:
            return Response({'status':500,'message':'something went wrong.'})



class GetFeatureRequests(APIView):
    def get(self,request):
        try:
            if request.user.is_authenticated and request.user.is_staff:
                return vision11().get_features_requests()
            return Response({'status':403,'message':'Invalid Credentials for admin.'})
        except:
            return Response({'status':500,'message':'something went wrong.'})


def Set_Seen_FeatureRequest(request,fid):
    try:
        if request.user.is_authenticated and request.user.is_staff:
            return vision11().set_seen_fr(fid)
        return redirect('/')
    except:
        return redirect('/')

class Set_End_Match(APIView):
    def get(self,request,mid):
        try:
            if request.user.is_authenticated and request.user.is_staff:
                return vision11().set_match_end(mid)
        except:
            return Response({'status':200,'message':'Invalid request'})

@login_required(login_url='/accounts/login')
def RenderTeamSelection(request,mid):
    '''
    This method is used for
    rendering Team selection page.
    '''
    try:
        return vision11().render_team_selection(request,mid)
    except:
        return redirect('/')

@login_required(login_url='/accounts/login')
def RenderContestPage(request,mid):
    '''
    This method is used for
    rendering Contest page.
    '''
    try:
        return vision11_render().render_contest(request,mid)
    except:
        return redirect('/createteam/match='+str(mid))


@login_required(login_url='/accounts/login')
def RenderUserContest(request):
    '''
    This method is used for
    rendering User Contest page.
    '''
    try:
        return vision11_render().render_usercontest(request)
    except:
        return redirect('/')


@login_required(login_url='/accounts/login')
def RenderContestDetails(request,cid):
    '''
    This method is used for
    rendering Contest details page.
    '''
    try:
        return vision11_render().render_contestdetails(request,cid)
    except Exception as e:
        print(e)
        return redirect('/mycontests')


@login_required(login_url='/accounts/login')
def RenderPlayerMatchData(request,mid):
    '''
    This method is used for
    rendering Player Match data page.
    '''
    try:
        if request.user.is_staff:
            return vision11_render().render_player_matchdata(request,mid)
        return redirect('/')
    except Exception as e:
        return redirect('/staff')



@login_required(login_url='/accounts/login')
def RenderUserTeam(request,mid,tid):
    '''
    This method is used for
    rendering User Team page.
    '''
    try:
        return vision11_render().render_userteam(request,mid,tid)
    except:
        return redirect('/createteam/match='+str(mid))


@login_required(login_url='/accounts/login')
def Updateplayermatchdata(request,mid,pid):
    try:
        if request.user.is_staff:
            return vision11_render().update_player_matchdata(request,mid,pid)
        return redirect('/')
    except Exception as e:
        return redirect('/staff')

def handler_404(request, exception=None):
    '''
        view to handle 404 error
        attached in project level
        urls.py (vision11.urls)
    '''
    data = {}
    return render(request, '404error.html', data)




def handler_500(request,  exception=None):
    '''
        view to handle 500 error
        attached in project level
        urls.py (vision11.urls)
    '''
    data = {}
    return render(request, '500error.html', data)




def Save_Suggestion_Form(request):
    '''
        View Function to save suggesition
        in corresponding model
    '''
    try:
        if request.user.is_authenticated:
            return vision11().save_suggestion_form(request)
        return redirect('/')
    except:
        return redirect('/')




class GetTodaysMatchesListAPI(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return vision11().get_match_list()
        return Response({'status':403,'message':'Please authenticate yourself.'})





class GetFantasyScoreAPI(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            try:
                return vision11().get_fantasy_score(request.data['url'])
            except:
                return Response({'status':500,'message':'Something went wrong please try again after some time.'})
        return Response({'status':403,'message':'Please authenticate yourself.'})





class GetTodaysSquadList(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            try:
                return vision11().get_todays_squad(request.data['team1'],request.data['team2'],request.data['match'])
            except Exception as e:
                print(e)
                return Response({'status':404,'message':'Either No contest available or timeline expired.'})
        return Response({'status':403,'message':'Please authenticate yourself.'})




class GetCompletedMatchesList(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            try:
                return vision11().get_completed_matches()
            except:
                return Response({'status':500,'message':'something went wrong.'})
        return Response({'status':403,'message':'Please authenticate yourself.'})




class GetLiveMatchesList(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            try:
                return vision11().get_Live_matches()
            except:
                return Response({'status':500,'message':'something went wrong.'})
        return Response({'status':403,'message':'Please authenticate yourself.'})




class GetUpcomingMatchesList(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            try:
                return vision11().get_upcoming_matches()
            except:
                return Response({'status':500,'message':'something went wrong.'})
        return Response({'status':403,'message':'Please authenticate yourself.'})




def RenderStaffPage(request):
    try:
        if request.user.is_authenticated and request.user.is_staff:
            return render(request,'staff_page.html')
        return redirect('/')
    except:
        return redirect('/')



def RenderMatchJoinedContest(request,mid):
    try:
        if request.user.is_authenticated:
            return vision11_render().render_match_joined_contest(request,mid)
        return redirect('/accounts/login')
    except:
        return HttpResponseBadRequest('Either you have not joined any contest or try again later.')
        




@login_required(login_url='/accounts/login')
def CreateUserTeam(request):
    try:
        return vision11().create_user_team(request.data)
    except:
        return redirect('/')




class FinalizeUserTeam(APIView):
    def post(self,request):
        try:
            if request.user.is_authenticated:
                return vision11().create_user_team(request.data,request.user)
            return Response({'status':403,'message':'unauthorized access please authenticated yourself.'})
        except:
            return Response({'status':500,'message':'something went wrong.'})




class ContestCreateJoinAPI(APIView):
    def post(self,request):
        try:
            if request.user.is_authenticated:
                return vision11().create_contest(request.data,request.user)
            return Response({'status':403,'message':'please authenticate yourself.'})
        except:
            return Response({'status':500,'message':'something went wrong.'})



class ContestSearchAPI(APIView):
    def post(self,request):
        try:
            if request.user.is_authenticated:
                return vision11().search_contest(request.data)
            return Response({'status':403,'message':'please authenticate yourself.'})
        except:
            return Response({'status':500,'message':'something went wrong.'})



class ContestJoinAPI(APIView):
    def post(self,request):
        try:
            if request.user.is_authenticated:
                return vision11().join_contest(request.data,request.user)
            return Response({'status':403,'message':'please authenticate yourself.'})
        except Exception as e:
            print(e)
            return Response({'status':500,'message':'something went wrong.'})



@login_required(login_url='/accounts/login')
def RenderUpdateTeam(request,mid,tid):
    try:
        return vision11_render().render_update_team(request,mid,tid)
    except Exception as e:
        return redirect('/')



class TeamUpdateHandler(APIView):
    def post(self,request):
        if not request.user.is_authenticated:
            return Response({'status':403,'message':'Please authenticate yourself.'})
        try:
            return vision11().update_user_team(request.data,request.user)
        except:
            return Response({'status':500,'message':'something went wrong.'})



class GetContestWinnerListPrice(APIView):
    def get(self,request,cid):
        if not request.user.is_authenticated:
            return Response({'status':403,'message':'Please authenticate yourself.'})
        try:
            return vision11().get_contest_winnerlist_price(cid)
        except:
            return Response({'status':500,'message':'something went wrong.'})