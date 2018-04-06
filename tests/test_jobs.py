# import pytest
# from seeker.job import models


def test_django():
    # from base.settings import settings as base_settings
    from django.conf import settings as django_settings
    print(django_settings.xxx)
    assert 3 == 5
