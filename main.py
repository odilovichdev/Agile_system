from django.core.cache import cache
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.base")
django.setup()


key = "foo"
value = "bar"

cache.set(key, value)
value = cache.get(key)

print(value)