import logging
import re
import sys
import string

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://9anime.to"
GRABBER_API = BASE_URL + "/grabber-api/"
INFO_API = BASE_URL + '/ajax/episode/info'

def get_mp4(id):
    payload = {
        'id': id
    }
    pay = {
    }

    details = requests.get(INFO_API, params=payload)
    details=details.json()
    #print details
    payload['token'] = details['params']['token']
    #print payload
    logging.info("Acquired token %s when requested from id %s" % (payload['token'], payload['id']))
    data = requests.get(GRABBER_API, params=payload)
    data=data.json()['data']
    logging.info("Recieved %i different links for id %s" % (len(data), payload['id']))
    # pay['lnk'] = data[0]['file']
    return data

def getAllEpisodes(link,start,end,count):
    data = {
        "episodes": [],
    }

    i=1
    page = BeautifulSoup(requests.get(link).content,"lxml")

    servers = page.findAll("div", {"class": "server row"})

    data["title"] = page.findAll("h1", {"class": "title"})[0].text

    for server in servers:
        episodes = server.findAll("a")
        for episode in episodes:
            if(i>=start):
                if(count!=0):
                    data['episodes'].append({
                        "id": episode['data-id'],
                        "link": episode['href'],
                        "epNumber": episode['data-base'],
                        "title": data["title"]
                        })
                    count=count-1
            else:
                i=i+1
    #print data
    return data


def append_file(handle, link, episode, qlty):

    if(qlty==0):
        qltyStr="360p"
    elif(qlty==1):
        qltyStr="480p"
    elif(qlty==2):
        qltyStr="720p"
    elif(qlty==3):
        qltyStr="1080p"

    link += ".type=video/mp4"
    episodeNumber = string.rjust(episode['epNumber'],3,"0")
    link += "&title=%s-%s-%s\n" % (episode['title'], episodeNumber, qltyStr)
    handle.write(link)

def get_link(link):
    dwnld_list=[]

    start=input("Enter the starting episode:")
    end=input("Enter the ending episode:")
    count=(end-start)+1
    qlty=input("choose quality u want to download(ex:2):\n"\
            "1.360p\n"\
            "2.480p\n"\
            "3.720p\n"\
            "4.1080p\n")
    qlty=qlty-1

    data=getAllEpisodes(link,start,end,count)
    title=data['title']
    title=str(title)
    outFile = open("dwnld_links.txt",'w')

    for episode in data['episodes']:
        try:
            dwnld_link=get_mp4(episode['id'])[qlty]['file']
            append_file(outFile, dwnld_link, episode, qlty)
        except IndexError:
            qlty=0;
            print "The chosen quality is unavailable dowloading lower quality 360p."
            dwnld_link=get_mp4(episode['id'])[qlty]['file']
            append_file(outFile, dwnld_link, episode, qlty)
            continue

    outFile.close()


url=raw_input("Enter the url of the anime (ex:http://9anime.to/watch/masamune-kun-no-revenge.pyr9):")
get_link(url)
