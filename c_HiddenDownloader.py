### ############################################################################################################
###	#	
### # Author: 			#		The Highway
### # Description: 	#		Downloader File For:  The Binary Highway
###	#	
### ############################################################################################################
### ############################################################################################################
### Imports ###
from common import *
from common import (_addon,_artIcon,_artFanart,_addonPath,_OpenFile)
def download(url,destfile,destpath,useResolver=True):
	import urllib
	#import xbmcgui
	dp='' #dp=xbmcgui.DialogProgress()
	##try: _addon.resolve_url(url)
	##except: pass
	#if useResolver==True:
	#	try: link=urlresolver.HostedMediaFile(url).resolve()
	#	except: link=url
	#else: link=url
	link=url
	if isPath(destpath)==False: os.mkdir(destPath)
	myNote('Starting Download',destfile,100)
	urllib.urlretrieve(link, xbmc.translatePath(os.path.join(destpath,destfile)),lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
	#urllib.urlretrieve(link, xbmc.translatePath(os.path.join(destpath,destfile)), lambda nb, bs, fs: DownloadStatus(nb, bs, fs, dp, download_method, start_time, section, url, img, LabelName, ext, LabelFile))
	myNote('Download Complete',destfile,15000)
	#try: _addon.resolve_url(url)
	#except: pass
def _pbhook(numblocks, blocksize, filesize, url, dp):
	try:
		percent = min((numblocks*blocksize*100)/filesize, 100)
		#dp.update(percent)
	except:
		percent = 100
		#dp.update(percent)
	#if dp.iscanceled(): 
	#	raise Exception("Canceled")
	#	dp.close()
	#