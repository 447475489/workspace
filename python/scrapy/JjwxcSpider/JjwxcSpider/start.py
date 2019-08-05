#! /usr/bin/env python

import sys

from scrapy import cmdline

print(sys.version)

cmdline.execute("scrapy crawl jjwxc_post".split())
