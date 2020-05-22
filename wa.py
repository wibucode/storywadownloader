# Copyright wibucode
import os, sys, shutil
os.chdir("/sdcard")
try:
	os.mkdir("StoryWa")
except OSError:
	os.system("clear")
print """\033[92m
 __        ___           _
 \ \      / / |__   __ _| |_ ___  __ _ _ __  _ __
  \ \ /\ / /| '_ \ / _` | __/ __|/ _` | '_ \| '_ \

   \ V  V / | | | | (_| | |_\__ \ (_| | |_) | |_) |
    \_/\_/  |_| |_|\__,_|\__|___/\__,_| .__/| .__/
                                      |_|   |_|
	\033[97mStatus Downloader(Massal)
	Author	: Wibu Code
	Github	: https://github.com/wibucode
 --------------------------------------------------
"""

os.chdir("/sdcard/Whatsapp/Media/.Statuses")
d = os.getcwd()
l = os.listdir(d)
ask = raw_input("\033[92m[\033[97m?\033[92m] Video / Image: \033[97m").lower()
for ls in l:
	if ask == "video":
		if ".mp4" in ls:
			shutil.copy2(ls, "/sdcard/StoryWa")
			print "\033[92mDidownload \033[91m-> \033[97m"+ls
	elif ask == "image":
		if ".jpg" in ls:
			shutil.copy2(ls, "/sdcard/StoryWa")
			print "\033[92mDidownload \033[91m-> \033[97m"+ls
	else:
		print "Pilih video / image?"
		sys.exit()
pass
print "\nHasil nya berada di folder StoryWa"
