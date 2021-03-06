from __future__ import absolute_import
from django.conf import settings

# -*- coding: utf-8 -*-
__version__ = settings.APP_VERSION
__version_info__ = tuple([int(num) if num.isdigit() else num for num in __version__.replace('-', '.', 1).split('.')])

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.

# This will make sure the celery app is always imported when
# Django starts so that shared_task will use this app.

from .taskapp.celery import app as celery_app

__all__ = ['celery_app']
