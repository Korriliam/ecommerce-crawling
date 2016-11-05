from __future__ import unicode_literals
# -*- coding: utf8 -*-

__author__ = 'korriliam'
# Pour utiliser un serveur proxy, en particulier avec TOR (obligatoire pour utiliser TOR)
# Serveur privoxy
class ProxyMiddleware(object):
    def process_request(self, request, spider):
        #Redirect our connexion to a tor proxy in order to anonymize our process.
        request.meta['proxy'] = "http://127.0.0.1:8118" #settings.get('HTTP_PROXY')
