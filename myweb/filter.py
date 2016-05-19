#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings as original_settings


def settings(request):
    return {'msg': "yangjb's web", "path": request.get_full_path()}
