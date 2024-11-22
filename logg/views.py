from django.contrib.auth import authenticate, login
from django.shortcuts import render
#from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from logg.models import User
from logg.models import Profile
from logg.permissions import CustomReadOnly
from logg.serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'logg/index.html')

def hello(request):
    return render(request, 'logg/hello.html')

def inf(request):
    if request.method == 'POST':
        username = request.POST.get('username')
    return render(request, 'logg/inf.html')
def adv(request):
    if request.method == 'POST':
        position = request.POST.get('position')
    return render(request, 'logg/adv.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        position = request.POST['user_type']

        try:
            user = User.objects.get(username=username)
            print(user)
        except:
            messages.error(request, 'Username or password is incorrect')
        user = authenticate(request, username=username, password=password)
        if user is not None :
            if(user.position != position):
                return render(request, 'logg/login.html')
            messages.success(request, 'You are now logged in')
            login(request,user)
            if(position=="influencer"):
                return redirect('inf/')
            else:
                return redirect('adv/')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'logg/login.html')

def sign_up(request):
    if request.method == 'POST':
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
            password=password
        )
        user.save()
        return redirect('/login/')
    return render(request, 'logg/sign_up.html')



# 회원가입
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


# 로그인
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token": token.key}, status=status.HTTP_200_OK)


# 프로필
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly, CustomReadOnly]

# class UserCreate(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
