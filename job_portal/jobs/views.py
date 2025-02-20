# # # from django.shortcuts import render

# # # def home(request):
# # #     return render(request, 'index.html')  # Renders an index.html template
# # # jobs/views.py
# # from django.shortcuts import render, redirect
# # from django.contrib.auth import login, authenticate
# # from django.contrib import messages
# # from .forms import CustomUserCreationForm

# # def register(request):
# #     if request.method == 'POST':
# #         form = CustomUserCreationForm(request.POST)
# #         if form.is_valid():
# #             # Save the new user
# #             user = form.save(commit=False)
# #             user.set_password(form.cleaned_data['password'])
# #             user.save()

# #             # Authenticate and log the user in
# #             user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
# #             if user is not None:
# #                 login(request, user)
# #                 messages.success(request, "Registration successful!")
# #                 return redirect('home')  # Redirect to home page after successful login
# #             else:
# #                 messages.error(request, "Authentication failed. Please try again.")
# #         else:
# #             messages.error(request, "Form is not valid. Please check the errors.")
# #     else:
# #         form = CustomUserCreationForm()

# #     return render(request, 'jobs/register.html', {'form': form})

# # jobs/views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, logout
# from django.contrib import messages
# from django.contrib.auth.forms import AuthenticationForm
# from .forms import CustomUserCreationForm
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

# User = get_user_model()


# # User Registration View
# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             # Save the new user
#             # user = form.save(commit=False)
#             # user.set_password(form.cleaned_data['password'])  # Hash the password
#             # user.save()
#             user = User(username=username, email=email)
#             user.set_password(password)  # This hashes the password
#             user.save()


#             # Authenticate and log the user in
#             user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "Registration successful!")
#                 return redirect('home')  # Redirect to the home page after successful login
#             else:
#                 messages.error(request, "Authentication failed. Please try again.")
#         else:
#             messages.error(request, "Form is not valid. Please check the errors.")
#     else:
#         form = CustomUserCreationForm()

#     return render(request, 'jobs/register.html', {'form': form})


# # User Login View
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)  # Log the user in
#             messages.success(request, "Login successful!")
#             return redirect('home')  # Redirect to the home page after login
#         else:
#             messages.error(request, "Invalid login credentials. Please try again.")
#     else:
#         form = AuthenticationForm()

#     return render(request, 'jobs/login.html', {'form': form})


# # User Logout View
# def logout_view(request):
#     logout(request)  # Logout the user
#     messages.success(request, "You have been logged out successfully.")
#     return redirect('home')  # Redirect to the home page after logout


# # User Profile (Optional, for profile view/edit)
# def profile(request):
#     return render(request, 'jobs/profile.html')  # Add a template to view and edit user profiles



from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm  # Ensure this form is defined correctly
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# User Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']  # This is password1 in the default UserCreationForm

            # Create the user
            user = User(username=username, email=email)
            user.set_password(password)  # This hashes the password
            user.save()

            # Authenticate and log the user in
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Registration successful!")
                return redirect('home')  # Redirect to the home page after successful login
            else:
                messages.error(request, "Authentication failed. Please try again.")
        else:
            messages.error(request, "Form is not valid. Please check the errors.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'jobs/register.html', {'form': form})


# User Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log the user in
            messages.success(request, "Login successful!")
            return redirect('home')  # Redirect to the home page after login
        else:
            messages.error(request, "Invalid login credentials. Please try again.")
    else:
        form = AuthenticationForm()

    return render(request, 'jobs/login.html', {'form': form})


# User Logout View
def logout_view(request):
    logout(request)  # Logout the user
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')  # Redirect to the home page after logout


# User Profile (Optional, for profile view/edit)
def profile(request):
    return render(request, 'jobs/profile.html')  # Add a template to view and edit user profiles
