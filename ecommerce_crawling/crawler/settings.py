from __future__ import unicode_literals
# -*- coding: utf8 -*-
from django.conf import settings as d_settings

# Scrapy settings for crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ecommerce_crawling.crawler'

SPIDER_MODULES = ['ecommerce_crawling.crawler.spiders']
NEWSPIDER_MODULE = 'ecommerce_crawling.crawler.spiders'

SECRET_KEY = "secret key value"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'crawler.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'crawler.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'crawler.pipelines.SomePipeline': 300,
#}

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 10.0
AUTOTHROTTLE_MAX_DELAY = 39.0
AUTOTHROTTLE_DEBUG = True # pour activer l'affichage de statistiques supplémentaires

CONCURRENT_REQUESTS = 1

REDIRECT_MAX_TIMES = 3

DOWNLOAD_TIMEOUT = 180


EXTENSIONS = {
    'scrapy.contrib.corestats.CoreStats': 500,
    'scrapy.contrib.logstats.LogStats': 500,
    # 'util.statsToDb.statsToDb': 800,
    'scrapy.contrib.throttle.AutoThrottle': 900,
    # 'util.EndMiddleware.VacuumJobdir':900
}

# DOWNLOADER_MIDDLEWARES = {
#         'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
#         #activation de rotateUserAgents ici. Va attributer user agent different à chaque requête.
# }


RETRY_ENABLED = False # Booléen qui dit si oui on non, si je n'arrive pas à acceder à une page, je réeessaye (non ici)
                        # Si c'était vrai, on ressayerai à l'infini

ROBOTSTXT_OBEY = False # Our bot don't follow robots.txt recommandations. On ne suis pas les recommandations des robots.Txt.

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
INSTALLED_APPS=(
    'ecommerce_crawling.crawler',
)

DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'ecom',
            'USER': 'ecom',
            'PASSWORD': 'ecom',
            'HOST': 'localhost',
            }
    }

d_settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'ecom',
            'USER': 'ecom',
            'PASSWORD': 'ecom',
            'HOST': 'localhost',
            }
    },
    INSTALLED_APPS=(
        'crawler',
    )
    )
