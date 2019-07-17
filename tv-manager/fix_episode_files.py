# coding: utf-8
import csv
# HINT: what do these modules do? How can we use them below?
import glob
import os


# This function gives us the full list of CSV files
def get_csv_filenames():
    return glob.glob('*.csv')


# Create a key for our dictionary
def make_episode_key(show, season, ep_num):
    return (show.title(), season, ep_num)


# Get the list of all video files
def get_video_filenames():
    return glob.glob('shows/*')

# MakeDir should create a directory if we need it
def make_dir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)


# Get show title, season, episode number, and file extension from a filename
def get_video_info_from_filename(filename):
    filename = os.path.basename(filename) # ???
    filename = filename.lower()
    show, ep_id, extn = filename.rsplit('.', 2) # What does this do?
    show = show.replace('.', ' ')
    show = show.title()
    ep_id = ep_id[1:] # What does this do?
    season, ep_num = ep_id.split('e', 1)
    season = str(int(season)) # What in the WORLD is this for?
    ep_num = str(int(ep_num)) # AGAIN!?
    return (show, season, ep_num, extn)

csv_files = get_csv_filenames()

episode_titles = {}

# This loop populates our dictionary of episode titles
for filename in csv_files:
    csvfile = open(filename)
    reader = csv.DictReader(csvfile)

    for row in reader:
        if len(row) == 6: # only process rows with all fields
            show_title = filename[0:-4]
            season = row['season']
            ep_num = row['episode']
            ep_title = row['title']
            if season is not None and ep_num is not None:
                ep_key = make_episode_key(show_title, season, ep_num)
                episode_titles[ep_key] = ep_title

print "This is the title info I've processed:"
for key, title in episode_titles.items():
    print "%s: '%s'" % (key, title)

# This loop renames our files
for filename in get_video_filenames():
    show_title, season, ep_num, extn = get_video_info_from_filename(filename)
    ep_key = make_episode_key(show_title, season, ep_num)
    if ep_key not in episode_titles:
        continue
    ep_title = episode_titles[ep_key]
    make_dir(show_title)
    season_dir = "%s/Season %s" % (show_title, season)
    make_dir(season_dir)
    new_filename = "%s/%s - %s.%s" % (season_dir, ep_num, ep_title, extn)

    # TODO: replace this print statement with something that does the actual
    # renaming
    print "Renaming '%s' to '%s'" % (filename, new_filename)
    os.rename(filename, new_filename)
