# coding=utf-8
from zope.component import createObject
from zope.cachedescriptors.property import Lazy
from Products.Five import BrowserView

class SitePage(BrowserView):
    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)

    @Lazy
    def siteInfo(self):
        retval = createObject('groupserver.SiteInfo', self.context)
        assert retval, 'Could not create the SiteInfo from %s' % self.context
        return retval

