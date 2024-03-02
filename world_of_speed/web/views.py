from django.shortcuts import render

from world_of_speed.profile_app.models import Profile


def index(request):
    has_profile = Profile.objects.first()

    # if has_profile is None:
    #     # return create_profile(request)

    context = {
        'has_profile': has_profile,
    }

    return render(request, 'web/index.html', context=context)

    # context = {
    #     'has_profile': has_profile,
    # }
    # return render(request, 'web/index.html', context=context)





