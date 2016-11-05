from __future__ import unicode_literals
 -*- coding: utf8 -*-

__author__ = "korriliam"

import random
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from scrapy import log
from crawler_v1.models import UserAgents

'''
    Mainly inspired from http://tangww.com/2013/06/UsingRandomAgent/
    Pioche un user agent en base de données, et en attribut un à la requête avant qu'elle soit téléchargée
    Activé grâce au fichier settings
'''

class RotateUserAgent(UserAgentMiddleware):
    user_agent_list = []
    user_agent = ""
    def __init__(self, user_agent=''):
        ua = UserAgents.objects.values()
        for elmt in ua:
            self.user_agent_list.append(elmt['uaString'])

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        if ua:
            request.headers.setdefault('User-Agent', ua)
            # Add desired logging message here.
            spider.log(
                u'User-Agent: {} {}'.format(request.headers.get('User-Agent'), request),
                level=log.DEBUG
            )
    #the default user_agent_list composes chrome,I E,firefox,Mozilla,opera,netscape
    #for more user agent strings,you can find it in http://www.useragentstring.com/pages/useragentstring.php
