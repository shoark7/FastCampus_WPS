from django.shortcuts import render, redirect, get_object_or_404
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from .models import Star
from django.contrib import messages
from django.http import HttpResponse, Http404


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.

YOUTUBE_API_SERVICE_NAME = "youtube"
DEVELOPER_KEY = "AIzaSyDgxWoN1d9Y-zp1hOG3HdR2i7aLfWj7BcY"
YOUTUBE_API_VERSION = "v3"

def youtube_search(keyword, page_token, max_results=5,):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
          q=keyword,
          part="id,snippet",
          maxResults=max_results,
          pageToken=page_token,
          type='video',
    ).execute()

    video_id_list = [item['id']['videoId'] for item in search_response['items']]
    str_id_list = ','.join(video_id_list)

    videos_response = youtube.videos().list(
        part='id,snippet,statistics',
        maxResults=max_results,
        pageToken=page_token,
        id=str_id_list,

    ).execute()


    for i, item in enumerate(search_response['items']):
        cur_video_id = item['id']['videoId']
        if Star.objects.filter(video_id=cur_video_id).exists():
            item['is_exist'] = True

        item['statistics'] = {
            'viewCount': videos_response['items'][i]['statistics']['viewCount'],
            'likeCount': videos_response['items'][i]['statistics']['likeCount'],
            'dislikeCount': videos_response['items'][i]['statistics']['dislikeCount'],
        }

    return search_response


import json
def search(request):
    keyword = request.GET.get('keyword')
    page_token = request.GET.get('page_token')
    if keyword:

        response = youtube_search(keyword, page_token)
        # print(json.dumps(response, indent=2, sort_keys=True))

        context = {
            'response': response,
            'keyword': keyword,
        }
    else:
        context = {}
    return render(request, 'video/search.html', context)


"""
    # template : video/search.html
    # url : video/search/
    # view : search
"""


# add_post on my user
def add_star(request):
    try:
        title = request.GET.get('title')
        video_id = request.GET.get('video_id')
        published_date = request.GET.get('published_date')
        image_url = request.GET.get('image_url')
    except:
        messages.warning(request, "꺼지라마!")
        return redirect('video:search')
    else:

        try:
            starred_video = Star.objects.create(
                title=title,
                video_id=video_id,
                published_date=published_date[:10],
                image_url=image_url,
            )
        except:
            messages.info(request, "이미 저장되었습니다. 다른 동영상을 선택해주세요...")
        else:
            messages.info(request, "성공적으로 저장되었습니다.")
        return redirect('video:star_list')





def star_list(request):
    all_stars = Star.objects.all()
    return render(request, 'video/star_list.html', {'all_stars': all_stars})


def star_detail(request, pk):
    error_messages = ''
    try:
        video = get_object_or_404(Star, pk=pk)
    except (Star.DoesNotExist, KeyError, Http404):
        messages.warning(request, "그런 영상 또 없습니다.")
        return redirect('video:star_list')
    else:
        return render(request, 'video/star_detail.html', {'video': video})


def star_delete(request, pk):
    video = Star.objects.get(pk=pk)
    video.delete()
    return redirect('video:star_list')