from django.core.cache import cache

from apps_config import settings
from categories.models import Category


def get_categories_cache():
    if settings.CACHE_ACTIVATE:
        key = 'categories'
        categories = cache.get(key)
        if categories is None:
            categories = Category.objects.all()
            cache.set(key, categories)
    else:
        categories = Category.objects.all()

    return categories
