from django.forms.widgets import NullBooleanSelect
from django.shortcuts import render
from requests.sessions import session
from docutils.utils.math.latex2mathml import mo
from scipy.interpolate import interp1d
from Movies.models import Movies as MoviesModel
from .forms import add_movie_form
from Movies.models import Movies as MovieModel
from tmdbv3api import TMDb, Movie, TV, Trending, Discover,Account,Authentication
import requests
from django.http import HttpResponseRedirect
import pprint

apikey = '56db406e58392c2ff59a312e7368fc82'
REQUEST_TOKEN = requests.get('https://api.themoviedb.org/3/authentication/token/new?api_key='+apikey).json()
img = 'http://image.tmdb.org/t/p/original/{your image poster path}'
tmdb = TMDb()
tmdb.api_key = apikey
movie = Movie()
tv = TV()
discover = Discover()
account = Account()
auth = Authentication(username="harsha_amir",password="harsha2608")
details = account.details()

def Movies(request):
    popular = movie.popular()
    pplrobj = []
    for p in popular:
        pplrobj.append(p)

    pplrobj = pplrobj

    mov = discover.discover_movies({
            'primary_release_date.gte': '2020-01-01',
            'sort_by': 'primary_release_date.asc'
        })
    latest_movies = requests.get('https://api.themoviedb.org/3/movie/latest?api_key='+apikey).json()

    trnd = requests.get('https://api.themoviedb.org/3/trending/movie/week?api_key='+apikey)
    
    toprated = movie.top_rated()
    tprobj = []
    for p in toprated:
        tprobj.append(p)
    
    s = movie.search("Gangs of New York")
    recommend = movie.recommendations(s[0].id)
    for i in recommend:
        print("Adding %s (%s) to watchlist." % (i.title, i.release_date))
        account.add_to_watchlist(details.id, i.id, "movie")
    context = {
        'recommend':recommend,
        'dest':latest_movies,
        'trndobj':trnd.json(),
        'pplrobj': pplrobj,
        'tprobj': tprobj,
    }
    return render(request, 'index.html',context)

def add_movie(request):
    pass

def movie_details(request, movie_id):
    movobj = movie.details(movie_id)

    similar = movie.similar(movie_id)
    similar_genres = movie.recommendations(movie_id)

    smlrobj = []
    for result in similar:
        smlrobj.append(result)
    for result in similar_genres:
        smlrobj.append(result)    
        
    search = movie.search(movie_id)
    for res in search:
        if res:
            smlrobj.append(res)
        else:
            pass

    search = tv.search(movie_id)
    for res in search:
        if res:
            smlrobj.append(res)
        else:                
            pass

    smlrobj = smlrobj
    datee = movobj.release_date
    datee = str(datee)[:4]
    try:
        trailer = movie.videos(movie_id)[0]['key']
    except:
        trailer = "Not available"
    cast = movie.credits(movie_id)
    cast = cast['cast']
    actors  = []
    for actor in cast:
        actors.append(actor)

    genre = movobj.genres
    genres = []
    for i in genre:
        genres.append(i['name'])
    context = {
            'actors':actors,
            'trailer':trailer,
            'datee':datee,
            'genres':genres,
            'movobj': movobj,
            'smlrobj': smlrobj,
        }
    return render(request, '../templates/Movies/movie_details.html', context)

def search_details(request):
    searchinput = request.GET.get('searchinput')
    #expected value should be in the form of yyyy-mm-dd
    if searchinput[1] == ".":
        mov = discover.discover_movies({
            'vote_average.gte': searchinput,
            'sort_by': 'vote_average.asc'
        })
        srchobj = []
        for i in mov:
            srchobj.append(i)
        context = {
            'srchobj': srchobj
        }
        return render(request, '../templates/Movies/search_details.html', context)
    
    #expected value is float
    elif searchinput[4] == '-':
        mov = discover.discover_movies({
            'primary_release_date.gte': searchinput,
            'sort_by': 'primary_release_date.asc'
        })
        srchobj = []
        for i in mov:
            srchobj.append(i)
        context = {
            'srchobj': srchobj
        }
        return render(request, '../templates/Movies/search_details.html', context) 


    else:
        search = movie.search(searchinput)

        srchobjmovie = []
        for res in search:
            if res:
                srchobjmovie.append(res)
            else:
                pass


        show = tv.search(searchinput)
        srchobjtv = []
        for result in show:
            if result:
                srchobjtv.append(result)
            else:
                pass

        srchobj = []
        for i in srchobjmovie:
            srchobj.append(i)
        for i in srchobjtv:
            srchobj.append(i)

        srchobj = srchobj

        context = {
            'srchobj': srchobj
        }
        return render(request, '../templates/Movies/search_details.html', context)

def login(request):

    uname = request.POST.get('uname')
    pwd = request.POST.get('pwd')

    REQUEST_TOKEN = requests.get('https://api.themoviedb.org/3/authentication/token/new?api_key='+apikey).json()

    return HttpResponseRedirect('https://www.themoviedb.org/authenticate/'+REQUEST_TOKEN["request_token"]+'?redirect_to=http://127.0.0.1:5001')

def logout(request):
    session_payload = { "request_token": REQUEST_TOKEN["request_token"] }
    #url = "localhost:8000"
    #requests.post(url, data=session_payload)
    SESSION_ID = requests.post('https://api.themoviedb.org/3/authentication/session/new?api_key='+apikey, session_payload).json() 
    print(SESSION_ID)
    print("--------------------------------")
    #params={key: value}
    #requests.delete(url, params={key: value}, args)
    session_delete_payload = {  "session_id":  SESSION_ID["session_id"]   }

    delete_response = requests.delete('https://api.themoviedb.org/3/authentication/session?api_key='+apikey, params=session_delete_payload).json()
    
    #print(delete_response)

    if(delete_response["success"] == True):
        return HttpResponseRedirect('http://127.0.0.1:5001') 
    else:
        return HttpResponseRedirect(request.path_info)
