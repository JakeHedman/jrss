#coding: utf-8

from configobj import ConfigObj
from opster import command
import feedparser
import os
import requests

HOME = os.getenv('USERPROFILE') or os.getenv('HOME')
CONF_PATH = os.path.join(HOME, '.jrssrc')

def write_template_config():
    conf = ConfigObj(
        CONF_PATH,
        create_empty=True,
        write_empty_values=True
    )

    conf['torrent_files_path'] = '/mnt/hdd0/torrent_files/'
    conf['shows'] = ['the.big.bang.theory', 'modern.family']
    conf['exclude'] = ['german', 'dubbed']
    conf['filter'] = ['720p']
    conf['rss_url'] = "http://example.com/rss?passkey=secret"

    conf.write()

def get_conf():
    if os.path.exists(CONF_PATH):
        return ConfigObj(CONF_PATH)
    else:
        write_template_config()
        print("Wrote example config to {0}".format(CONF_PATH))
        exit(0)

CONF = get_conf()

def download(item):
    # Remove items not in shows
    for show in CONF['shows']:
        if show.lower() in item['title'].lower():
            break
    else:
        return
    
    # Remove items not in filter 
    for include in CONF['filter']:
        if not include.lower() in item['title'].lower():
            return

    # Remove items in exclude
    for exclude in CONF['exclude']:
        if exclude.lower() in item['title'].lower():
            return

    if item['title'] + ".torrent" in os.listdir(CONF['torrent_files_path']):
        return
    
    torrentpath = os.path.join(CONF['torrent_files_path'],
                               item['title'] + '.torrent')
    with open(torrentpath, 'w+') as fh:
        res = requests.get(item['link'])
        if not res.ok:
            return

        for block in res.iter_content(1024):
            if not block:
                break
            fh.write(block)

@command()
def main():
    f = feedparser.parse(CONF['rss_url'])
    for item in f['entries']:
        download(item)
