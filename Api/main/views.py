
'''이거는 이제 각 유튜브url 입력하면 나타나는  코드 (광고 현황 표시) '''
import re
from doctest import debug
from django.http import JsonResponse
from googleapiclient.discovery import build
from django.conf import settings
from django.shortcuts import render
from googleapiclient.errors import HttpError
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from .models import Video

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_SERVICE_VERSION = 'v3'
# YouTube API 클라이언트 생성
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_SERVICE_VERSION, developerKey=settings.API_KEY)
#video_json_data ={NULL_MASK}

# 유튜브 링크에서 비디오 ID를 추출하는 함수
def extract_video_id(url):
    video_id_pattern = r'(?:youtube\.com\/(?:[^\/\n\s]*\/\S*\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
    match = re.search(video_id_pattern, url)
    if match:
        return match.group(1)
    else:
        raise ValueError("유효한 YouTube URL이 아닙니다.")


# Django 뷰: YouTube 동영상 데이터 가져오기
def youtube_video_statistics(request):
    # 요청에서 URL 가져오기
    youtube_url ='https://www.youtube.com/watch?v=D2rYY8w2BAQ'
    if not youtube_url:
        return JsonResponse({'error': 'YouTube URL이 필요합니다.'}, status=400)

    # 비디오 ID 추출
    video_id = extract_video_id(youtube_url)

    # YouTube API로 데이터 요청
    response = youtube.videos().list(
        part='statistics',
        id=video_id
    ).execute()
    video_data = response['items'][0]['statistics']
    view_count = video_data.get('viewCount', '정보 없음')
    like_count = video_data.get('likeCount', '정보 없음')
    comment_count = video_data.get('commentCount', '정보 없음')
    # 데이터 추출
    video_dict_data={
        'video_id': video_id,
        'view_count': view_count,
        'like_count': like_count,
        'comment_count': comment_count
    }
    # JSON 응답 반환
    return video_dict_data
'''이거는 이제 한 인플루언서의 유튜브 정보를 나타내는 코드(인플루언서 마이페이지에 뜰 통계) '''
def get_channel_videos_statistics(request):
    try:
        # 요청에서 채널 ID 가져오기
        channel_id = 'UCw-JzmPsjRcbzJLncr4pIIA'
        if not channel_id:
            return JsonResponse({'error': '채널 ID가 필요합니다.'}, status=400)

        # 채널의 동영상 검색
        search_response = youtube.search().list(
            channelId=channel_id,
            part='id',
            maxResults=50,  # 한 번에 가져올 동영상 수 (최대 50개)
            type='video'
        ).execute()

      
        video_ids = [item['id']['videoId'] for item in search_response['items']]
        if not video_ids:
            return JsonResponse({'error': '채널에 동영상이 없습니다.'}, status=404)

        
        videos_response = youtube.videos().list(
            part='statistics',
            id=','.join(video_ids)  # 동영상 ID를 쉼표로 구분하여 전달
        ).execute()
        # 채널의 통계 데이터 가져오기
        channel_response = youtube.channels().list(
            part='statistics',
            id=channel_id
        ).execute()

        channel_statistics = channel_response['items'][0]['statistics']
        subscribers_count = channel_statistics.get('subscriberCount', '0')

        results = []
        total_view_count=0
        total_like_count=0
        for item in videos_response['items']:
            statistics = item['statistics']
            results.append({
                'video_id': item['id'],
                'view_count': statistics.get('viewCount', '0'),
                'like_count': statistics.get('likeCount', '0'),
                'comment_count': statistics.get('commentCount', '0'),
                #'subscribers_count': statistics.get('subscriberCount', '0')
            })
            total_view_count += int(statistics.get('viewCount', '0'))
            total_like_count += int(statistics.get('likeCount', '0'))

        influencers_dict_data={
            'channel_id': channel_id,
            'subscribers_count': subscribers_count,
            'total_view_count': str(total_view_count),
            'total_like_count': str(total_like_count)
        }
        # JSON 응답 반환
        return influencers_dict_data
    except HttpError as e:
        return JsonResponse({'error': 'YouTube API 호출 실패', 'details': str(e)}, status=500)

    except Exception as e:
        return JsonResponse({'error': '서버 오류', 'details': str(e)}, status=500)



'''인스타그램 광고 현황'''
def get_instagram_post_details(request):
    username = settings.INSTAGRAM_USERNAME
    password = settings.INSTAGRAM_PASSWORD

    # Chrome WebDriver 설정
    driver = webdriver.Chrome()
    post_url='https://www.instagram.com/p/DCTSyIEzj3J/'
    if not post_url:
        return JsonResponse({'error': '게시물 URL이 필요합니다'})
    # Instagram 로그인 페이지 열기
    driver.get('https://www.instagram.com/accounts/login/')

    # 로그인 (계정 정보 입력)
    time.sleep(2)  # 페이지 로딩 시간
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')

    username_input.send_keys(username)
    password_input.send_keys(password)

    # 로그인 버튼 클릭
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    time.sleep(5)  # 로그인 후 페이지 로딩 대기'''

    # 개인 계정의 특정 게시물 URL로 이동

    driver.get(post_url)
    #time.sleep(3)

    try:
        likes = driver.find_element(By.XPATH, "//span[contains(@class, 'html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs')]").text
        #comments = driver.find_element(By.XPATH, "//span[@class='C4VMK']").text  # 댓글 수 추출 방법은 게시물 구조에 따라 다를 수 있음
        instagram_dict_data={
            'post_url': post_url,
            'likes': likes,
            # 'comments': comments  # 필요 시 추가
        }
        return instagram_dict_data
    except Exception as e:
        print("정보를 추출할 수 없습니다.", e)
    finally:
        driver.quit()



def index_video_data(request):
    video_data=youtube_video_statistics(request)
    return render(request,'main/ADPageYoutube.html',video_data)
def channel_data(request):
    channel_data= get_channel_videos_statistics(request)
    return render(request,'main/DetailPage.html',channel_data)
def instagram_data(request):
    instagram_data=get_instagram_post_details(request)
    return render(request,'main/ADPageInsta'
    '.html',instagram_data)