from rest_framework import generics
from .models import Movie, Profile
from .serializers import MovieSerializer, ProfileSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def watch_list(request, username):
    if request.method == 'GET':
        user = User.objects.get(username=username)
        item = Profile.objects.get(user=user)
        items = item.movies.all()
        serializer = MovieSerializer(items, many=True)
        return Response(serializer.data)

@api_view(['POST', 'GET', 'DELETE'])
@permission_classes((IsAuthenticated,))
def watch_list_add(request, pk, username):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'POST':
        try:
            user = User.objects.get(username=username)
            movie = Movie.objects.get(pk=pk)
        except User.DoesNotExist or Movie.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        item = Profile.objects.get(user=user)
        item.movies.add(movie)

        serializer = ProfileSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            user = User.objects.get(username=username)
            movie = Movie.objects.get(pk=pk)
        except User.DoesNotExist or Movie.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        item = Profile.objects.get(user=user)
        item.movies.remove(movie)
        serializer = ProfileSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)







