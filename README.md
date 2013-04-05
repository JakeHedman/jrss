 ___           _        _ _       _   _
|_ _|_ __  ___| |_ __ _| | | __ _| |_(_) ___  _ __
 | || '_ \/ __| __/ _` | | |/ _` | __| |/ _ \| '_ \
 | || | | \__ \ || (_| | | | (_| | |_| | (_) | | | |
|___|_| |_|___/\__\__,_|_|_|\__,_|\__|_|\___/|_| |_|
 ___________________________________________________
|___________________________________________________|

You need to to have:
	Feedparser python module
	Transmission setup to watch a specific dir for new torrents
	Cron to execute the script
	Read the comments in the script to complete the installation


Example cron if you want to check for new uploads every minute:
	*	*	*	*	*	python /Users/username/orss.py
