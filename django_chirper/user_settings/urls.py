from django.urls import path, reverse_lazy
from . import views
from .views import PasswordChangeView
from .forms import UpdatePasswordForm


urlpatterns = [
    path('', views.settings, name = 'settings'),
    path('account/', views.settings_account, name = 'settings_account'),
    path('account/personalization/', views.settings_account_personalization, name = 'settings_account_personalization'),
    path(
        'password/', 
        PasswordChangeView.as_view(
            template_name = 'settings_password.html',
            form_class = UpdatePasswordForm,
            success_url = reverse_lazy('settings')
        ),
        name = 'settings_password'
    ),
    path('screen_name/', views.settings_screenName, name = 'settings_screenName'),
    path('security_and_account_access/', views.settings_securityAndAccountAccess, name = 'settings_securityAndAccountAccess'),
    path('privacy_and_safety', views.settings_privacyAndSafety, name = 'settings_privacyAndSafety'),
    path('notifications/', views.settings_notifications, name = 'settings_notifications'),
    path('accessibility_display_and_languages', views.settings_accessibilityDisplayAndLanguages, name = 'settings_accessibilityDisplayAndLanguages'),
    path('about/', views.settings_about, name = 'settings_about'),
    path('your_chirper_data/', views.settings_yourChirperData, name = 'settings_yourChirperData'),
    path('your_chirper_data/account/', views.settings_yourChirperData_account, name = 'settings_yourChirperData_account'),
    path('your_chirper_data/gender/', views.settings_yourChirperData_gender, name = 'settings_yourChirperData_gender'),
    path('your_chirper_data/age/', views.settings_yourChirperData_age, name = 'settings_yourChirperData_age'),
    path('phone/', views.settings_phone, name = 'settings_phone'),
    path('add_phone/auth/', views.settings_addPhone_auth, name = 'settings_addPhone_auth'),
    path('add_phone/', views.settings_addPhone, name = 'settings_addPhone'),
    path('delete_phone/', views.settings_deletePhone, name = 'settings_deletePhone'),
    path('email/', views.settings_email, name = 'settings_email'),
    path('add_email/auth/', views.settings_addEmail_auth, name = 'settings_addEmail_auth'),
    path('add_email/', views.settings_addEmail, name = 'settings_addEmail'),
    path('audience_and_tagging/', views.settings_audienceAndTagging, name = 'settings_audienceAndTagging'),
    path('country/', views.settings_country, name = 'settings_country'),
    path('languages/', views.settings_languages, name = 'settings_languages'),
    path('trends/', views.settings_trends, name = 'settings_trends'),
    path('content_preferences/', views.settings_contentPreferences, name = 'settings_contentAndPreferences'),
    path('apps_and_sessions/', views.settings_appsAndSessions, name = 'settings_appsAndSessions'),
    path('profile/', views.settings_profile, name = 'settings_profile')
]