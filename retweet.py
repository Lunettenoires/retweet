#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import os.path
import sys
import tweepy

from waitamoment import WaitAMoment

class Twitter:
    '''Twitter class'''
    def __init__(self):
        '''Constructor of the Twitter class'''
        __pathtoconf = sys.argv[-1]
        if not os.path.exists(__pathtoconf):
            print('the path you provided for yaspe configuration file does not exists')
            sys.exit(1)
        if not os.path.isfile(__pathtoconf):
            print('the path you provided for yaspe configuration is not a file')
            sys.exit(1)
        __config = ConfigParser.ConfigParser()
        try:
            with open(__pathtoconf) as __conffile:
                __config.readfp(__conffile)
                if __config.has_section('main'):
                    self.user_to_retweet = __config.get('main','screen_name_of_the_user_to_retweet')
                    consumer_key = __config.get('main','consumer_key')
                    consumer_secret = __config.get('main','consumer_secret')
                    access_token = __config.get('main','access_token')
                    access_token_secret = __config.get('main','access_token_secret')
        except (ConfigParser.Error, IOError, OSError) as __err:
            print(__err)
            sys.exit(1)

        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.secure = True
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        self.main()

    def main(self):
        '''lalalal'''
        # get the 20 last tweets
        __lasttweets = self.api.user_timeline(self.user_to_retweet)
        __lasttweetidfile = 'lastsenttweetid'

        if os.path.exists(__lasttweetidfile) and os.path.isfile(__lasttweetidfile):
            # a file with the last sent tweet id exists, using it
            with open(__lasttweetidfile) as __desc:
                __lasttweetid = int(__desc.read())
            print("last sent tweet:{}").format(__lasttweetid)
        else:
            # no previously sent tweet, get the first one (last of the list)
            __lasttweetid = __lasttweets[-1].id
        # extract the last 20 tweet ids
        __lasttweetids = [__tweet.id for __tweet in __lasttweets]
        __lasttweetids.reverse()
        print("last tweets:{}").format(' '.join([unicode(__j) for __j in __lasttweetids]))
        if __lasttweetid in __lasttweetids:
            __tweetstosend = __lasttweetids[__lasttweetids.index(__lasttweetid):]
            __tweetstosend.remove(__lasttweetid)
            print("tweets to send:{}").format(' '.join([unicode(__j) for __j in __tweetstosend]))
            for __i in __tweetstosend:
                try:
                    self.api.retweet(__i)
                    print("tweet {} sent!").format(unicode(__i))
                except (tweepy.error.TweepError) as __err:
                    print("{}").format(unicode(__err))
                WaitAMoment()
            # if we really sent tweets, store the last one
            if len(__tweetstosend) != 0:
                with open(__lasttweetidfile, 'w') as __desc:
                    __desc.write(unicode(__tweetstosend[-1]))

if __name__ == '__main__':
    Twitter()
    sys.exit(0)
