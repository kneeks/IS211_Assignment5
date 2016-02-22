#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment3"""

import urllib2
import argparse
import re


def main():


    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='Enter the URL to get the CSV file.')
    args = parser.parse_args()

    if args.url:
        try:
            cntx = downloadData(args.url)
            imgSearch(cntx)
        except:
            print 'The URL entered is invalid.'
    else:
        print '--url and then enter url.'


def downloadData(url):
    """fetches the data from url.

    Args:
        response: open url link to get data
        read: reads data

    Return:
        read data file from url"""
    response = urllib2.urlopen(url)
    read = response.read()
    return read


def imgSearch(url):
    """img percent for the following file"""

    tot = 0
    img = 0

    for row in url:
        tot += 1
        img_ext = ('([.jpg]|[.png]|[.jpeg]|[.gif]|[.JPG]|[.PNG]|[.JPEG]|[.GIF])')
        if re.search(img_ext, row) is not None:
            img += 1

    img_pct = (float(img) / tot) * 100
    pct = 'Image requests account for {0:0.1f}% of all requests'.format(img_pct)
    return pct


def browserSearch(url):
    """processes the browser with the most hits"""
    fox_cnt = 0
    chrome_cnt = 0
    saf_cnt = 0
    ie_cnt = 0
    fox = ('(|[Firefox]|[firefox])')
    chrome = ('(|[Chrome]|[chrome])')
    saf = ('(|[Safari]|[safari])')
    ie = ('(|[Trident]|[trident])')
    
    for row in url:
        if re.search(fox, row):
            fox_cnt += 1
        elif re.search(chrome, row):
            chrome_cnt += 1
        elif re.search(saf, row):
            saf_cnt += 1
        elif re.search(ie, row):
            ie_cnt += 1


if __name__ == "__main__":
    main()