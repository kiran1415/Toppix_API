from django.shortcuts import render
from .models import Toppix , Tags
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .serializers import ToppixSerializer
# Create your views here.



@api_view(['POST'])
def create_toppix(request):
    user = request.user
    data = request.data
    content = data.get('content')
    tags = data.get('tags')
    title = data.get('title')
    category = data.get('category')
    sub_category = data.get('sub_category')
    toppix = Toppix.objects.create(
        user=user,
        file=content,
        title=title,
        category = category,
        sub_category = sub_category,
        )
    if tags is not None:
        for tag_name in tags:
            tag_instance = Tags.objects.filter(name=tag_name).first()
            if not tag_instance:
                tag_instance = Tags.objects.create(name=tag_name)
            toppix.tags.add(tag_instance)
        toppix.save()
    serializer = ToppixSerializer(toppix, many=False)
    return Response(serializer.data)



@api_view(['GET'])
def get_toppix(request,pk):
    try:
        toppix = Toppix.objects.get(pk=pk)
        serializer = ToppixSerializer(toppix,many=False)
        return Response(serializer.data)
    except:
        return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def toppix(request):
    query = request.query_params.get('q')
    if query is None:
        query = ''
    toppixs = Toppix.objects.filter(Q(tag__in=query) | Q(title__contains=query)| Q(category__in=query) | Q(sub_category__in=query))
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(toppixs,request)
    serializer = ToppixSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def delete_toppix(request,pk):
    try:
        toppix = Toppix.objects.get(pk=pk)
        if toppix.user == request.user:
            toppix.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(status = status.HTTP_401_UNAUTHORIZED)
    except:
        return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_like_toppix(request,pk):
    try:
        toppix = Toppix.objects.get(pk=pk)
        print(toppix)        
        toppix.like = toppix.like + 1
        toppix.save() 
        return Response(status = status.HTTP_200_OK)
    except:
        return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_view_toppix(request,pk):
    try:
        toppix = Toppix.objects.get(pk=pk)
        print(toppix)        
        toppix.views = toppix.views + 1
        toppix.save() 
        return Response(status = status.HTTP_200_OK)
    except:
        return Response(status = status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
def create_share_toppix(request,pk):
    try:
        toppix = Toppix.objects.get(pk=pk)
        print(toppix)        
        toppix.shares = toppix.shares + 1
        toppix.save() 
        return Response(status = status.HTTP_200_OK)
    except:
        return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_download_toppix(request,pk):
    try:
        toppix = Toppix.objects.get(pk=pk)
        print(toppix)        
        toppix.downloads = toppix.downloads + 1
        toppix.save() 
        return Response(status = status.HTTP_200_OK)
    except:
        return Response(status = status.HTTP_204_NO_CONTENT)
