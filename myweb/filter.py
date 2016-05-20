#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings as original_settings
from util import date_util


def settings(request):
    return {'msg': "yangjb's web", "path": request.get_full_path(), "loveDays": date_util.today_to_loveday_days()}
