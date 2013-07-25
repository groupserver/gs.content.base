===================
``gs.content.base``
===================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Core classes for GroupServer Content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2013-07-25
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 New Zealand License`_
  by `OnlineGroups.Net`_.

Introduction
============

The product defines the core class that is used to create `pages`_ for
GroupServer_ sites.

Pages
=====

A ``gs.content.base.SitePage`` is a concrete class that can be used for
creating pages using just ZCML. For example, the help-index is defined in
``gs.help`` using the following::

  <browser:page 
    name="index.html"
    template="browser/templates/help.pt"
    for=".interfaces.IGSHelp"
    class="gs.content.base.SitePage"
    permission="zope.Public"/>

A site page has two properties defined.

``siteInfo``:
  A ``Products.GSContent.view.SiteInfo`` instance representing the current
  class. Like all *info* classes it has a ``name``, ``url``, and ``id``.

``loggedInUserInfo``:
  A ``Products.CustomUserFolder.userinfo.GSUserInfo`` instance,
  representing the currently logged in user. Like all *info* classes it has
  a ``name``, ``url``, and ``id``. In addition it has an ``anonymous``
  property, which is set to ``True`` if the user is not logged in.

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.content.base/
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net/
.. _Michael JasonSmith: http://groupserver.org/p/mpj17/
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/
