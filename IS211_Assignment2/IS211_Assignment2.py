# -*- coding: utf-8 -*-
"""
Assignment 2
"""

import sys
import csv
import urllib2
import datetime
import logging
import argparse


def main():

    def downloadData(url= 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'):
        """fetches url from link"

        Args:
            data: url link
        """
        data = urllib2.urlopen(url)
        return data

    def processData(data):
        """
        Processes the data from the url in order to create new dict.

        Args:
            csvfile: data file
            mydict = new dict from data file

        Return:
            New Dict with format of id, name, birth day

        """        
        csvfile = csv.DictReader(downloadData())
        mydict = {}
        line = 0
        for row in csvfile:
            try:
                line += 1
                id = row['id']
                name = row['name']
                day, month, year = row['birthday'].split('/')
                birth_date = datetime.date(int(year),int(month), int(day))
                birth_day = datetime.datetime.combine(birth_date, datetime.time())
                mydict[id] = (name, birth_day)
            except ValueError:               
                logging.warning('Error processing line# {} for ID# {}'.format(line - 1, id))                 
                continue
        return mydict
          
    def displayPerson(id, processData):
        """
        Displays the person's info upon request
        """
        msg = ''

        try:
            id_ = str(id)
            name = processData[id_][0]
            birth_day = processData[id_][1].strftime('%Y/%m/%d')
            msg = 'Person #{} is {} and their birthday is {}'.format(id_, name, birth_day)
        except KeyError:
               msg = 'Make sure IDs are 1 through 100'
        return msg

    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='The URL to fetch the CSV file.')
    args = parser.parse_args()
    logging.basicConfig(filename='error.log', filemode='w')

    if args.url:
        csvData = downloadData(args.url)
        personData = processData(csvData)
        message = 'Please enter an ID # for the person. Enter 0 or a negative # to exit program: '

        while True:
            try:
                user = int(raw_input(message))
            except ValueError:
                print 'Invalid input. Please try again.'
                continue
            if user > 0:
                displayPerson(user, personData())
            else:
                print 'Exiting program.'
                sys.exit()
    else:
        print 'Please use --url parameter'

if __name__ == '__main__':
    main()