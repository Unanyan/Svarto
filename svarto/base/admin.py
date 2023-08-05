from django.contrib import admin
from .models import (
    AboutUs,
    TeamMember,
    WhatWeDoItem,
    NewsItem,
)

admin.site.register(AboutUs)
admin.site.register(TeamMember)
admin.site.register(WhatWeDoItem)
admin.site.register(NewsItem)
