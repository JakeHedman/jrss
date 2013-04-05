import feedparser
import urllib2
from os import listdir

# Shows to autodownload
shows=[
	'Anger.Management',
	'Arrested.Development',
	'Awkward',
	'Blue.Mountain.State',
	'Californication',
	'Community',
	'Cougar.Town',
	'Dexter',
	'Happy.Endings',
	'How.I.Met.Your.Mother',
	'Melissa.And.Joey',
	'Modern.Family',
	'New.Girl',
	'Punkd',
	'Revolution',
	'Royal.Pains',
	'Shameless.US',
	'Suburgatory',
	'Suits',
	'The.Big.Bang.Theory',
	'The.Office.US',
	'The.Following',
	'Top.Gear',
	'Top_Gear',
	'Two.And.A.Half.Men',
	'Wilfred',
	'Workaholics'
]


# The filter may match some unwanted shows, double check first
excludes=[
	'Top.Gear.US',
]

# Link to the rss to use
rsslink = "https://domain.tld/rss"

# Path where to save .torrent files
torrentpath = "/Users/username/torrents/" # End with a slash


f = feedparser.parse(rsslink)

for item in f['entries']:
	for show in shows:
		if show in item['title']:
			for exclude in excludes:
				if exclude not in item['title']:
					if item['title'] + ".torrent" not in listdir(torrentpath):
						torrent = urllib2.urlopen(item['link']).read()
						file = open(torrentpath + item['title'] + ".torrent","w+")
						file.write(torrent)
						file.close()
