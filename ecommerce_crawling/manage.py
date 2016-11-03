#!/usr/bin/python2.7
_author__ = 'Guillaume Le Bihan'

import os
import sys
#redirect the Django conf to our scrappy settings file.
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce_crawling.crawler.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
