# def get_profile(request):
#     if request.user.is_anonymous:
#         if not request.session.exists(request.session.session_key):
#             request.session.create()
#         profile, created = Profile.objects.get_or_create(session=request.session.session_key)
#         return profile
#
#     return Profile.objects.get(user=request.user)
