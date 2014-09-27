import feedparser
import urllib2
from os import listdir

# Shows to autodownload
shows=[
    'anger.management',
    'bates.motel',
    'betas',
        'better.call.saul',
    'californication',
    'community',
        'family.guy',
    'graceland',
    'homeland',
        'house.of.lies',
    'how.i.met.your.mother',
    'legit',
    'men.at.work',
    'modern.family',
    'mythbusters',
    'new.girl',
    'punkd',
    'ray.donovan',
    'revolution',
    'royal.pains',
    'shameless.us',
    'suits',
    'the.big.bang.theory',
    'the.crazy.ones',
    'the.following',
    'the.goldbergs',
        'the.simpsons',
    'top.gear',
    'top_gear',
    'two.and.a.half.men',
    'under.the.dome',
    'wilfred',
    'workaholics',
]


# The filter may match some unwanted shows, double check first
excludes=[
    'top.gear.us',
    'dubbed',
    'german',
]

includes=[
    '720p',
]

# Link to the rss to use
rsslinks=[
        'https://tracker.com/blablabla',
]

# Path where to save .torrent files
torrentpath = "/Users/username/Torrents/" # End with a slash


feedparser.USER_AGENT = "uTorrent 1.6.1.0 uTorrent/1610"

def download(item):
    # Remove items not in shows
    for show in shows:
        if show in item['title'].lower():
            break
    else:
        return
    
    # Remove items not in includes
    for include in includes:
        if not include in item['title'].lower():
            return

    # Remove items in excludes
    for exclude in excludes:
        if exclude in item['title'].lower():
            return

    if item['title'] + ".torrent" in listdir(torrentpath):
        return

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36' }
    request = urllib2.Request(item['link'], None, headers)
    torrent = urllib2.urlopen(request).read()
    file = open(torrentpath + item['title'] + ".torrent", "w+")
    file.write(torrent)
    file.close()

for rss in rsslinks:
    f = feedparser.parse(rss)
    for item in f['entries']:
        download(item)
