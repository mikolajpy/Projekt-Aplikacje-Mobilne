from django.contrib import admin
from .models import Zabka,Achievements,AssignedAcievments,UserProfile,VisitedZabkas,StoreComment

admin.site.register(Zabka)
admin.site.register(Achievements)
admin.site.register(AssignedAcievments)
admin.site.register(UserProfile)
admin.site.register(VisitedZabkas)
#admin.site.register(Post)
admin.site.register(StoreComment)