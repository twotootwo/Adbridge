from warnings import catch_warnings

from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
#from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from logg.models import User, Advertisement, Profile
from logg.permissions import CustomReadOnly
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
import json
from django.shortcuts import render

from django.shortcuts import render
from .models import Advertisement

def ad_list_view_inf(request):
    ads = Advertisement.objects.all()  # Advertisement 테이블의 모든 데이터를 가져옴
    context = {'ads': ads}
    return render(request, 'logg/inf.html', context)

#수정해야하는 부분
def ad_list_view_adv(request):
    profs = Profile.objects.all()
    context = {'profs': profs}
    return render(request, 'logg/adv.html', context)

class StartView(TemplateView):
    template_name = 'logg/hello.html'
    def get(self,request,*args, **kwargs):
        print("hello")
        context = super().get_context_data(**kwargs)
        return self.render_to_response(context)

class InfluenceView(TemplateView):
    template_name = 'logg/inf.html'
    def get(self,request,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.render_to_response(context)

class AdvertiseView(TemplateView):
    template_name = 'logg/adv.html'
    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.render_to_response(context)

class PostingView(TemplateView):
    template_name = 'logg/postform.html'
    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.render_to_response(context)
    def post(self, request, *args, **kwargs):
        try:
            thumbnail = request.FILES.get('thumbnail')
            ad_title = request.POST.get('ad-title')
            product_name = request.POST.get('ad-product')
            category = request.POST.get('category')
            sns = request.POST.get('sns')
            min_budget = request.POST.get('min_budget')
            max_amount = request.POST.get('max_budget')
            details = request.POST.get('details')
            product_image = request.FILES.get('details_image')

            ad = Advertisement.objects.create(
                user = request.user,
                thumbnail=thumbnail,
                title=ad_title,
                sns = sns,
                category = category,
                product_name=product_name,
                description=details,
                min_budget=min_budget,
                max_budget=max_amount,
                product_image=product_image
            )

            ad.save()
            return render(request, 'logg/postform.html')
        except Exception as e:
            print(f"Error occurred: {e}")  # 오류 내용 출력
            return render(request, 'logg/postform.html', {'error': 'An error occurred while saving the advertisement.'})

        return render(request, 'logg/postform.html')

class LoginView(TemplateView):
    template_name = 'logg/login.html'
    def get(self,request,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self,request,*args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        position = request.POST['user_type']
        print(username, password, position)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if (user.position != position):
                return render(request, 'logg/login.html')
            messages.success(request, 'You are now logged in')
            login(request, user)
            if (position == "influencer"):
                return redirect('inf/')
            else:
                return redirect('adv/')
        else:
            print("********************************")
            messages.error(request, 'Username or password is incorrect')
            return render(request, 'logg/login.html')

class SignupView(TemplateView):
    template_name = 'logg/sign_up.html'
    def get(self,request,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.render_to_response(context)
    def post(self,request,*args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email', ' ')
        nickname = request.POST.get('nickname')
        field = request.POST.get('field')
        position = request.POST.get('user_type')
        if password != confirm_password:
            return render(request, 'logg/sign_up.html')
        user = User.objects.create_user(
            username=username,
            position=position,
            password = password
            )
        user.save()
        return redirect('/login/')

class MypageView(TemplateView):
    template_name = 'logg/mypage.html'
    def get(self,request,*args, **kwargs):
        try:
            profile = Profile.objects.get(user=request.user)  # Profile 객체 가져오기
        except Profile.DoesNotExist:
            profile = None
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        return self.render_to_response(context)
    def post(self,request,*args, **kwargs):
        user = request.user
        profile = request.FILES.get('profile')
        content = request.POST.get('category')
        platform = request.POST.get('sns')
        urls = request.POST.get('link')
        min_budget = request.POST.get('min-budget')
        max_budget = request.POST.get('max-budget')
        text_box = request.POST.get('text-box')

        prof, created = Profile.objects.get_or_create(
            user=user,  # user를 기준으로 프로필 조회
            defaults={
                'img': profile,
                'content': content,
                'platform': platform,
                'urls': urls,
                'min_budget': min_budget,
                'max_budget': max_budget,
                'text_box': text_box,
            }
        )
        #UPDATE
        if not created:
            if profile:
                prof.img = profile
            prof.content = content
            prof.platform = platform
            prof.urls = urls
            prof.min_budget = min_budget
            prof.max_budget = max_budget
            prof.text_box = text_box
            prof.save()

        if(user.position=="influencer"):
            return redirect("/login/inf/")
        else:
            return redirect("/login/adv/")

#광고주 마이페이지
class MypageViewAdv(TemplateView):
    template_name = 'logg/mypage_adv.html'
    def get(self,request,*args, **kwargs):
        try:
            profile = Profile.objects.get(user=request.user)  # Profile 객체 가져오기
        except Profile.DoesNotExist:
            profile = None
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        return self.render_to_response(context)
    def post(self,request,*args, **kwargs):
        user = request.user
        profile = request.FILES.get('profile')
        content = request.POST.get('category')
        platform = request.POST.get('sns')
        min_budget = request.POST.get('min-budget')
        max_budget = request.POST.get('max-budget')
        text_box = request.POST.get('text-box')

        prof, created = Profile.objects.get_or_create(
            user=user,  # user를 기준으로 프로필 조회
            defaults={
                'img': profile,
                'content': content,
                'platform': platform,
                'min_budget': min_budget,
                'max_budget': max_budget,
                'text_box': text_box,
            }
        )
        #UPDATE
        if not created:
            if profile:
                prof.img = profile
            prof.content = content
            prof.platform = platform
            prof.urls = ''
            prof.min_budget = min_budget
            prof.max_budget = max_budget
            prof.text_box = text_box
            prof.save()

        if(user.position=="influencer"):
            return redirect("/login/inf/")
        else:
            return redirect("/login/adv/")
#인플루언서 상세페이지
def detailInf(request,id):
    adv = get_object_or_404(Advertisement,id = id)
    context = {'ad_data':adv }
    return render(request,'logg/detail.html',context)

#광고주 상세페이지
def detailAdv(request,id):
    inf = get_object_or_404(Profile,id = id)
    context = {'inf_data': inf}
    return render(request,'logg/detail_adv.html',context)



# # 로그인
# class LoginView(generics.GenericAPIView):
#     serializer_class = LoginSerializer
#
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         token = serializer.validated_data
#         return Response({"token": token.key}, status=status.HTTP_200_OK)


# 프로필
# class ProfileView(generics.RetrieveUpdateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     # permission_classes = [IsAuthenticatedOrReadOnly, CustomReadOnly]

# class UserCreate(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
