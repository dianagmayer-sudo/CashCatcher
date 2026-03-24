from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, UserUpdateForm


def register(request):
    print (request.POST)
    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            return redirect("login")
        else:
            print (form.errors)

    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})

"""
@login_required
def profile_edit(request):

    if request.method == "POST":

        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            request.POST,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect("dashboard")   # ⭐ mai logic UX

    else:

        user_form = UserUpdateForm(instance=request.user)

        profile_form = ProfileUpdateForm(
            instance=request.user.profile
        )

    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }

    return render(
        request,
        "accounts/profile_edit.html",
        context
    )
"""