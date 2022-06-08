from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, View, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import redirect, render

from core.forms import UserUpdateForm, RegisterForm
from core.models import User


def hello(request):
    return render(request, "base.html")


class UserRegisterView(CreateView):
    template_name = "registration/register.html"
    model = User
    form_class = RegisterForm
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse_lazy("profile", kwargs={"slug": user.username}))


class ProfileDetailView(LoginRequiredMixin, UpdateView):
    template_name = "profile.html"
    queryset = User.objects.prefetch_related("posts")
    form_class = UserUpdateForm
    context_object_name = "user"
    slug_field = "username"

    def get_success_url(self) -> str:
        url = reverse_lazy("profile", kwargs={"slug": self.object.username})
        return url


class FollowView(LoginRequiredMixin, SingleObjectMixin, View):
    model = User
    slug_field = "username"

    def post(self, request, *args, **kwargs):
        follow_user = self.get_object()
        user = request.user
        if follow_user in user.following.all():
            user.following.remove(follow_user)
        else:
            user.following.add(follow_user)
        user.save()
        next = request.GET.get("next")
        if next is not None:
            return redirect(next)
        return redirect(reverse_lazy("profile", kwargs={"slug": follow_user.username}))


class ProfileListView(LoginRequiredMixin, ListView):
    model = User
    template_name: str = "profile_list.html"

    def get_context_data(self, **kwargs):
        search = self.request.GET.get("search", "")
        context = super().get_context_data(**kwargs)
        users = User.objects.search(search)
        if not search:
            users = users.users_without(self.request.user.id)
        context["users"] = users
        return context

