from modeltranslation.translator import translator, TranslationOptions
from .models import (
    AboutUs,
    TeamMember,
    WhatWeDoItem,
    NewsItem,
)


class AboutUsTranslationOptions(TranslationOptions):
    fields = ("text",)


translator.register(AboutUs, AboutUsTranslationOptions)


class TeamMemberTranslationOptions(TranslationOptions):
    fields = ("name", "role")


translator.register(TeamMember, TeamMemberTranslationOptions)


class WhatWeDoItemTranslationOptions(TranslationOptions):
    fields = ("title", "description")


translator.register(WhatWeDoItem, WhatWeDoItemTranslationOptions)


class NewsItemTranslationOptions(TranslationOptions):
    fields = ("content", "additional_text")


translator.register(NewsItem, NewsItemTranslationOptions)
