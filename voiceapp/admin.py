from django.contrib import admin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import path, reverse
from django.utils.html import format_html
from django.views.generic import TemplateView
from django.views.generic.detail import SingleObjectMixin, DetailView

from .models import User_Voice, Catagory, Audio, Audio_User

from django.shortcuts import redirect, render

from django.http import HttpResponse
from .models import *

from django.contrib.auth.models import Group

@admin.register(User_Voice)
class User_VoiceAdmin(admin.ModelAdmin):
    list_display = ("from_user_name", "to_user_name","voice_file")

@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    # list_display = ("name", "description","created_at")
    Catagory.name

class OrderItemInline(admin.TabularInline):
    model = Audio_User

class Audio_User_View(PermissionRequiredMixin, DetailView):
    permission_required = "voiceapp.view_order"
    template_name = "admin/voiceapp/audio/detail.html"
    model = Audio_User

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **admin.site.each_context(self.request),
            "opts": self.model._meta,
        }

@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ("Catagory_name", "name", "audio_file", "description", "detail")
    list_filter = ["Catagory_name", "name"]
    inlines = [OrderItemInline]

    def get_urls(self):
        return [
            path(
                "<pk>/detail",
                self.admin_site.admin_view(Audio_User_View.as_view()),
                name=f"audios_audio_user_detail",
            ),
            *super().get_urls(),
        ]

    def detail(self, obj: Audio) -> str:
        url = reverse("admin:audios_audio_user_detail", args=[obj.pk])
        return format_html(f'<a href="{url}">📝</a>')

@admin.register(Audio_User)
class Audio_UserAdmin(admin.ModelAdmin):
    list_display = ("Audio_name", "User_name")  

@admin.register(Audio_Group)
class Audio_GroupAdmin(admin.ModelAdmin):
    list_display = ("Audio_name", "Group_name")   

class Fichiers_reçusModel(models.Model):
    class Meta:
        verbose_name_plural = 'Fichiers reçus'
        app_label = 'voiceapp'

def fichiers_reçus_custom_view(request):
    Audios = Audio.objects.all()

    context = {
        "Audios":Audios,
    }

    return render(request, 'voiceapp/fichiers_reçus.html', context)


class Fichiers_reçusModelAdmin(admin.ModelAdmin):
    model = Fichiers_reçusModel

    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('voiceapp/', fichiers_reçus_custom_view, name=view_name),
        ]
admin.site.register(Fichiers_reçusModel, Fichiers_reçusModelAdmin)

class Audio_attribueModel(models.Model):
    class Meta:
        verbose_name_plural = 'Audio_attribue'
        app_label = 'voiceapp'

def audio_attribue_custom_user_view(request):
    audio_ids = Audio_User.objects.filter(User_name_id=request.user.id).values()
    # print('count=',audio_ids.count())
    # print(audio_ids)
    id_list=[]
    for course in audio_ids:
        id_list.append(course['Audio_name_id'])
    print(id_list)

    Audios = Audio.objects.filter(id__in=id_list).values()
    context = {
        "Audios":Audios,
    }

    return render(request, 'voiceapp/audio_attribue.html', context)

class Audio_attribueModelAdmin(admin.ModelAdmin):
    model = Audio_attribueModel

    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('voiceapp/', audio_attribue_custom_user_view, name=view_name),
        ]
admin.site.register(Audio_attribueModel, Audio_attribueModelAdmin)

class CollaborateursModel(models.Model):
    class Meta:
        verbose_name_plural = 'Collaborateurs'
        app_label = 'voiceapp'

def collaborateurs_custom_view(request):
    Groups = Group.objects.all()
    Users = User.objects.all()
    # auth_user_groups = auth_user_groups.objects.all()

    context = {
        "Groups":Groups,
        'Users':Users,
        # 'auth_user_groups':auth_user_groups
    }

    return render(request, 'voiceapp/collaborateurs.html', context)


class CollaborateursModelAdmin(admin.ModelAdmin):
    model = CollaborateursModel

    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('voiceapp/', collaborateurs_custom_view, name=view_name),
        ]
admin.site.register(CollaborateursModel, CollaborateursModelAdmin)

class CatagoryModel(models.Model):
    class Meta:
        verbose_name_plural = 'Tous les audios'
        app_label = 'voiceapp'

def categorys_custom_view(request):
    categorys = Catagory.objects.all()
    # audios = Audio.objects.all()
    # audio_users = Audio_User.objects.all()

    context = {
        "categorys":categorys,
        # 'audios':audios,
        # 'audio_users':audio_users
    }

    return render(request, 'voiceapp/categories.html', context)

class CatagoryModelAdmin(admin.ModelAdmin):
    model = CatagoryModel

    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('voiceapp/', categorys_custom_view, name=view_name),
        ]
admin.site.register(CatagoryModel, CatagoryModelAdmin)