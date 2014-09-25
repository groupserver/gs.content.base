# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2013, 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from zope.component import createObject
from zope.cachedescriptors.property import Lazy
from Products.Five import BrowserView


class SitePage(BrowserView):
    def __init__(self, context, request):
        super(SitePage, self).__init__(context, request)

    @Lazy
    def siteInfo(self):
        retval = createObject('groupserver.SiteInfo', self.context)
        assert retval, 'Could not create the SiteInfo from '\
            '%s' % self.context
        return retval

    @Lazy
    def loggedInUserInfo(self):
        retval = createObject('groupserver.LoggedInUser', self.context)
        assert retval, 'Could not create the user-info for the logged '\
            'in user from %s' % self.context
        return retval
