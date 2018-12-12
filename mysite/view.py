#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "bill.li"

from django.shortcuts import redirect

def redirect_view(request):
    response = redirect('/sms/')
    return response

if __name__ == '__main__':
    pass

