Pages
=====

.. currentmodule:: gs.content.base

A :class:`gs.content.base.SitePage` is a concrete class that can
be used for creating pages in GroupServer. 


.. py:class:: gs.content.base.SitePage(context, request)
   
   A page on a GroupServer site

   :param context: The context of the page
   :param request: The current HTTP request

   .. py:attribute:: siteInfo

      A :class:`Products.GSContent.view.SiteInfo` instance
      representing the current site. Like all *info* classes it
      has a ``name``, ``url``, and ``id``.

   .. py:attribute:: loggedInUserInfo

      A :class:`Products.CustomUserFolder.userinfo.GSUserInfo`
      instance, representing the currently logged in user. Like
      all *info* classes it has a ``name``, ``url``, and
      ``id``. In addition it has an ``anonymous`` property, which
      is set to ``True`` if the user is not logged in.

Example
-------

It can be used with just ZCML. For example, the help-index is
defined in :mod:`gs.help`:

.. code-block:: xml

   <browser:page 
     name="index.html"
     template="browser/templates/help.pt"
     for=".interfaces.IGSHelp"
     class="gs.content.base.SitePage"
     permission="zope.Public"/>

The *Login* page (in :mod:`gs.login`) is one of the few that
directly sub-classes :class:`gs.content.base.SitePage`:

.. code-block:: python

   from gs.content.base import SitePage

   class GSLoginView(SitePage):
       def __init__(self, context, request):
           super(GSLoginView, self).__init__(context, request)
           self.state = None

Most of the pages on GroupServer inherit from either
:class:`gs.group.base.GroupPage` or
:class:`gs.profile.base.ProfilePage`.
