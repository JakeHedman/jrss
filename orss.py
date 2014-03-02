import feedparser
import urllib2
from os import listdir

# Shows to autodownload
shows=[
	'Anger.Management',
	'Bates.Motel',
	'Betas',
        'Better.Call.Saul',
	'Californication',
	'Community',
        'Family.Guy',
	'Graceland',
	'Homeland',
        'House.of.Lies',
	'How.I.Met.Your.Mother',
	'Legit',
	'Men.at.Work',
	'Modern.Family',
	'MythBusters',
	'New.Girl',
	'Punkd',
	'Ray.Donovan',
	'Revolution',
	'Royal.Pains',
	'Shameless.US',
	'Suits',
	'The.Big.Bang.Theory',
	'The.Crazy.Ones',
	'The.Following',
	'The.Goldbergs',
        'The.Simpsons',
	'Top.Gear',
	'Top_Gear',
	'Two.and.a.Half.Men',
	'Under.the.Dome',
	'Wilfred',
	'Workaholics',
]


# The filter may match some unwanted shows, double check first
excludes=[
	'Top.Gear.US',
	'DUBBED',
	'dubbed',
	'Dubbed',
	'GERMAN',
	'German',
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

#f = feedparser.parse(rsslink)
for rss in rsslinks:
	f = feedparser.parse(rss)
	for item in f['entries']:
		for show in shows:
			if show in item['title']:
				for include in includes:
					if include in item['title']:
						for exclude in excludes:
							if exclude not in item['title']:
								if item['title'] + ".torrent" not in listdir(torrentpath):
                                                                        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36' }
                                                                        request = urllib2.Request(item['link'], None, headers)
									torrent = urllib2.urlopen(request).read()
									file = open(torrentpath + item['title'] + ".torrent","w+")
									file.write(torrent)
									file.close()
