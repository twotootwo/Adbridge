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
from logg.models import User, Advertisement
from logg.permissions import CustomReadOnly
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
import json
from django.shortcuts import render

from django.shortcuts import render
from .models import Advertisement

def ad_list_view(request):
    ads = Advertisement.objects.all()  # Advertisement 테이블의 모든 데이터를 가져옴
    context = {'ads': ads}
    return render(request, 'logg/inf.html', context)


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





# # 회원가입
# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer


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
