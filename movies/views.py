from django.http import HttpResponse,Http404
from django.shortcuts import render,get_object_or_404
from .models  import Movie



# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies} )

    #output = ','.join([m.title for m in movies])
   #Select * From movies_movie
    #Movie.objects.filter(release_year=1984)
    #Select *from movies_movie where
    #Movie.objects.get(id=1)
    #return HttpResponse(output)


def detail(request, movie_id):

        movie = get_object_or_404(Movie, pk=movie_id)  #pk=primary key
        return render(request, 'movies/detail.html', {'movie': movie} )
      #return HttpResponse(movie_id)

