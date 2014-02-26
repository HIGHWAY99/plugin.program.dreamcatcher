### ############################################################################################################
###	#	
### # Project: 			#		Stream Recorder - by The Highway 2014.
### # Author: 			#		The Highway
### # Version:			#		
### # Description: 	#		
###	#	
### ############################################################################################################
### ############################################################################################################
##### Imports #####
import os,sys,string,StringIO,logging,random,array,time,datetime,re
import xbmc,urllib,urllib2,xbmcaddon,xbmcplugin,xbmcgui,xbmcvfs
try: import copy
except: pass
from common import *
from common import (_addon,_plugin,_artIcon,_artFanart,_addonPath,_debugging,deb,debob,fixPath)
import common as CoMMoN
### ############################################################################################################
### ############################################################################################################
SiteName='Dreamcatcher'
SiteTag='Dreamcatcher'
mainSite=''
iconSite=_artIcon
fanartSite=_artFanart
CR='[CR]'
MyBrowser=['User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3']
### ############################################################################################################
### ############################################################################################################
site=addpr('site','')
section=addpr('section','')
url=addpr('url','')
sections={'series':'series','movies':'movies'}
thumbnail=addpr('img','')
fanart=addpr('fanart','')
page=addpr('page','')
### ############################################################################################################
### ############################################################################################################
def AFColoring(t): 
	if len(t)==0: return t
	elif len(t)==1: return cFL(t,'firebrick')
	else: return cFL(cFL_(t,'firebrick'),'mediumpurple')



### ############################################################################################################
### ############################################################################################################
def About(head=''+cFL(SiteName,'blueviolet')+'',m=''):
	m=''
	if len(m)==0:
		m+='IRC Chat:  '+cFL('#XBMCHUB','blueviolet')+' @ '+cFL('irc.Freenode.net','blueviolet')
		m+=CR+'Site Name:  '+SiteName+CR+'Site Tag:  '+SiteTag+CR+'Site Domain:  '+mainSite+CR+'Site Icon:  '+iconSite+CR+'Site Fanart:  '+fanartSite
		#m+=CR+'Age:  Please make sure you are of a valid age to watch the material shown.'
		#m+=CR+CR+'Known Hosts for Videos:  '
		#m+=CR+'* VideoCrazy'
		#m+=CR+'* UploadCrazy'
		m+=CR+CR+'Features:  '
		#m+=CR+'* Browse Shows'
		#m+=CR+'* Browse Episodes'
		#m+=CR+'* Browse Host Links'
		#m+=CR+'* Play Videos with UrlResolver'
		#m+=CR+'* Download Videos with UrlResolver'
		#m+=CR+'* MetaData for Shows and 1st Season Episodes where data is available.'
		#m+=CR+'* MetaData auto-disabled for Anime List - ALL.  This is to prevent hammering with the huge list of nearly 400 shows.'
		m+=CR+CR+'Notes:  '
		#m+=CR+'* '
		#m+=CR+'* '
		m+=CR+''
		m+=CR+ps('ReferalMsg')
		m+=CR+''
		m+=CR+''
		m+=CR+''
	String2TextBox(message=cFL(m,'cornflowerblue'),HeaderMessage=head)
### ############################################################################################################
### ############################################################################################################

DT={}; now=datetime.date.today(); 
DT['year']=now.strftime("%Y"); DT['month']=now.strftime("%m"); DT['day']=now.strftime("%d"); 
debob(DT); 





def setupName(vName,pType):
	if pType=='Video':
		try: pTVShowTitle=xbmc.getInfoLabel('VideoPlayer.TVShowTitle'); 
		except: pTVShowTitle=''; 
		try: pTitle=xbmc.getInfoLabel('VideoPlayer.Title'); 
		except: pTitle=''; 
		if len(pTitle)==0:
			try: pTitle=p.getVideoInfoTag().getTitle(); 
			except: pTitle=''; 
		try: pIMDBno=p.getVideoInfoTag().getIMDBNumber(); pIMDBno=str(pIMDBno).strip(); 
		except: pIMDBno=''; 
		try: pStudio=xbmc.getInfoLabel('VideoPlayer.Studio'); 
		except: pStudio=''; 
		pStudio=pStudio.strip(); pTVShowTitle=pTVShowTitle.strip(); pTitle=pTitle.strip(); 
		if    len(pTitle) > 0: vName+=pTitle
		if   (tfalse(addst('name-tvshowtitle','true'))==True) and (len(pTitle) > 0) and (len(pTVShowTitle) > 0): vName=pTVShowTitle+' - '+vName
		if   (tfalse(addst('name-studio','true'))==True) and (len(pTitle) > 0) and (len(pStudio) > 0): vName=pStudio+' - '+vName
		elif (tfalse(addst('name-studio','true'))==True) and (len(pTitle)==0)  and (len(pStudio) > 0): vName=pStudio+vName
		
	elif pType=='Audio':
		#try: pTitle=p.getMusicInfoTag().getTitle(); 
		try: pTitle=xbmc.getInfoLabel('MusicPlayer.Title'); 
		except: pTitle=''; 
		try: pStudio=xbmc.getInfoLabel('MusicPlayer.Artist'); 
		except: pStudio=''; 
		pTVShowTitle=''; pIMDBno=''; 
		pStudio=pStudio.strip(); pTVShowTitle=pTVShowTitle.strip(); pTitle=pTitle.strip(); 
		if    len(pTitle) > 0: vName+=pTitle
		#if   (tfalse(addst('name-tvshowtitle','true'))==True) and (len(pTitle) > 0) and (len(pTVShowTitle) > 0): vName=pTVShowTitle+' - '+vName
		if   (tfalse(addst('name-artist','true'))==True) and (len(pTitle) > 0) and (len(pStudio) > 0): vName=pStudio+' - '+vName
		elif (tfalse(addst('name-artist','true'))==True) and (len(pTitle)==0)  and (len(pStudio) > 0): vName=pStudio+vName
		
	else: 
		pTVShowTitle=''; pTitle=''; pStudio=''; vName='[Unknown]'; 
		pStudio=pStudio.strip(); pTVShowTitle=pTVShowTitle.strip(); pTitle=pTitle.strip(); 
	p=xbmc.Player(); 
	#pStudio=pStudio.strip(); pTVShowTitle=pTVShowTitle.strip(); pTitle=pTitle.strip(); 
	#if    len(pTitle) > 0: vName+=pTitle
	#if   (tfalse(addst('name-tvshowtitle','true'))==True) and (len(pTitle) > 0) and (len(pTVShowTitle) > 0): vName=pTVShowTitle+' - '+vName
	#if   (tfalse(addst('name-studio','true'))==True) and (len(pTitle) > 0) and (len(pStudio) > 0): vName=pStudio+' - '+vName
	#elif (tfalse(addst('name-studio','true'))==True) and (len(pTitle)==0)  and (len(pStudio) > 0): vName=pStudio+vName
	vName=vName.replace('!','').replace('"','').replace(':','').replace(';','').replace('|','').replace('/','').replace('\\','')
	if tfalse(addst('name-datestamp','true'))==True: vName+=' - ['+DT['year']+'-'+DT['month']+'-'+DT['day']+']'; 
	if   pType=='Video': vName+='.flv'; 
	elif pType=='Audio': vName+='.mp3'; 
	else: vName+='.FLV'; 
	
	vName=vName.strip(); 
	return vName

def startStreamRecord():
	vName=''; vPath=''; p=xbmc.Player(); 
	if   (p.isPlayingVideo()==True): pType='Video'; debob("isPlayingVideo"); vPath=addst('download_folder_default',''); 
	elif (p.isPlayingAudio()==True): 
		pType='Audio'; debob("isPlayingAudio"); vPath=addst('download_folder_audio',''); 
		if len(vPath)==0: vPath=addst('download_folder_default',''); 
	elif (p.isPlaying()==True): pType='Unknown'; debob("isPlaying"); vPath=addst('download_folder_default',''); 
	else: pType=''; debob("Couldn't find anything playing."); vPath=addst('download_folder_default',''); 
	try:
		if (p.isInternetStream()==True): iIS=True; deb("isInternetStream()","True"); 
		else: iIS=False; deb("isInternetStream()","False"); 
	except: iIS=True; deb("isInternetStream()","error"); 
	if (len(vPath) > 0) and (len(pType) > 0) and (iIS==True):
		vPath=fixPath(vPath); deb("vPath",vPath); 
		vUrl=xbmc.Player().getPlayingFile(); deb("vUrl",vUrl); 
		vName=setupName(vName,pType); 
		###
		eod(); DoA("Back"); 
		DownloadThis(vUrl,vName,vPath,False); 
	else: eod(); DoA("Back"); 

def SectionMenu():
	vName=''; vPath=''; p=xbmc.Player(); 
	if   (p.isPlayingVideo()==True): pType='Video'; debob("isPlayingVideo"); vPath=addst('download_folder_default',''); 
	elif (p.isPlayingAudio()==True): 
		pType='Audio'; debob("isPlayingAudio"); vPath=addst('download_folder_audio',''); 
		if len(vPath)==0: vPath=addst('download_folder_default',''); 
	elif (p.isPlaying()==True): pType='Unknown'; debob("isPlaying"); vPath=addst('download_folder_default',''); 
	else: pType=''; debob("Couldn't find anything playing."); vPath=addst('download_folder_default',''); 
	try:
		if (p.isInternetStream()==True): iIS=True; deb("isInternetStream()","True"); 
		else: iIS=False; deb("isInternetStream()","False"); 
	except: iIS=True; deb("isInternetStream()","error"); 
	if (len(vPath) > 0) and (len(pType) > 0) and (iIS==True):
		vPath=fixPath(vPath); deb("vPath",vPath); 
		vUrl=xbmc.Player().getPlayingFile(); deb("vUrl",vUrl); 
		vName=setupName(vName,pType); 
		###
		_addon.add_directory({'mode':'Download','url':vUrl,'destfile':vName,'filetype':pType,'destpath':vPath,'site':site,'section':section},{'title':cFL('Download '+str(pType)+': ','firebrick')+cFL(vName,'mediumpurple')+CR+vUrl},is_folder=True,fanart=fanartSite,img=iconSite)
	###
	_addon.add_directory({'mode':'About','site':site,'section':section},{'title':AFColoring('About')},is_folder=True,fanart=fanartSite,img='http://i.imgur.com/0h78x5V.png') # iconSite
	set_view('list',view_mode=addst('default-view')); eod()

### ############################################################################################################
### ############################################################################################################
def mode_subcheck(mode='',site='',section='',url=''):
	deb('mode',mode); 
	if (mode=='SectionMenu') or (mode=='') or (mode=='main') or (mode=='MainMenu'): SectionMenu()
	elif (mode=='Record'): startStreamRecord()
	## XBMC.Container.Update(plugin://plugin.program.streamrecord/?mode=Record)
	## XBMC.RunPlugin(plugin://plugin.program.streamrecord/?mode=Record)  ## this one seems to work in skins.
	elif (mode=='Download'):
		#try: _addon.resolve_url(url); 
		#except: pass
		#debob([url,addpr('destfile',''),addpr('destpath',''),str(tfalse(addpr('useResolver','true')))]); 
		#DownloadThis(url,addpr('destfile',''),addpr('destpath',''),tfalse(addpr('useResolver','true'))); 
		debob([url,addpr('destfile',''),addpr('destpath',''),'False']); 
		eod(); DoA("Back"); 
		DownloadThis(url,addpr('destfile',''),addpr('destpath',''),False); 
		
	elif (mode=='toJDownloader'): 
		SendTo_JDownloader(url,tfalse(addpr('useResolver','true'))); 
		eod(); DoA("Back"); 
	elif (mode=='About'): About(); eod(); #DoA("Back"); 
	else: myNote(header='Site:  "'+str(site)+'"',msg=str(mode)+' (mode) not found.'); SectionMenu()


mode_subcheck(addpr('mode',''),addpr('site',''),addpr('section',''),addpr('url',''))
### ############################################################################################################
### ############################################################################################################
