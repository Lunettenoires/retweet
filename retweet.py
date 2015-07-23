#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys
import tweepy

class Twitter:
    '''Twitter class'''
    def __init__(self):
        '''Constructor of the Twitter class'''
        consumer_key = "Y72DI8YcAAtZQLv5YK9gV1VA3"
        consumer_secret = "MOCUH66xd5vRIddAc226xqHu8BGxvR6VoBei868UmQen62pW37"
        access_token = "2601681162-bfvNqsSeQgvHmTQNncUl2pUh6OCSNihtEZpH1Wn"
        access_token_secret = "kGtrXXD3Aog5SMjaL87sl5avDl8utyAAw8Mwk9k4gRQV9"
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.secure = True
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        self.main()

    def main(self):
        '''lalalal'''
        # get the 20 last tweets
        __lasttweets = self.api.user_timeline('journalduhacker')
        __lasttweetidfile = 'lastsenttweetid'

        if os.path.exists(__lasttweetidfile) and os.path.isfile(__lasttweetidfile):
            # a file with the last sent tweet id exists, using it
            with open(__lasttweetidfile) as __desc:
                __lasttweetid = int(__desc.read())
            print("dernier tweet envoyé:{}").format(__lasttweetid)
        else:
            # no previously sent tweet, get the first one (last of the list)
            __lasttweetid = __lasttweets[-1].id
        # extract the last 20 tweet ids
        __lasttweetids = [__tweet.id for __tweet in __lasttweets]
        __lasttweetids.reverse()
        print(__lasttweetids)
        print("derniers tweets:{}").format(' '.join([unicode(__j) for __j in __lasttweetids]))
        if __lasttweetid in __lasttweetids:
            __tweetstosend = __lasttweetids[__lasttweetids.index(__lasttweetid):]
            __tweetstosend.remove(__lasttweetid)
            print("tweets à envoyer:{}").format(' '.join([unicode(__j) for __j in __tweetstosend]))
            #for __i in __lasttweetids:
            #    self.api.retweet(__i)
            # if we really sent tweets, store the last one
            if len(__tweetstosend) != 0:
                with open(__lasttweetidfile, 'w') as __desc:
                    __desc.write(unicode(__tweetstosend[-1]))

if __name__ == '__main__':
    Twitter()
    sys.exit(0)
