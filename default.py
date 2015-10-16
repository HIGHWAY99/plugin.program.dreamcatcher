### ############################################################################################################
###	#	
### # Project: 			#		Dreamcatcher - by The Highway 2014.
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
		m+='IRC Chat:  '+cFL('#The_Projects','blueviolet')+' @ '+cFL('irc.snoonet.org:6667','blueviolet')
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
		#m+=CR+ps('ReferalMsg')
		m+=CR+'For more information visit the forum:  '+cFL('http://forums.addons.center/thread/190-dreamcatcher-addon/','blueviolet')
		m+=CR+''
		m+=CR+''
	String2TextBox(message=cFL(m,'cornflowerblue'),HeaderMessage=head)
### ############################################################################################################
### ############################################################################################################

DT={}; now=datetime.date.today(); 
DT['year']=now.strftime("%Y"); DT['month']=now.strftime("%m"); DT['day']=now.strftime("%d"); 
debob(DT); 





def setupName(vName,pType,vUrl):
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
		vName=vName.strip(); 
		if    len(pTitle) > 0: vName+=pTitle
		vName=vName.strip(); 
		if   (tfalse(addst('name-tvshowtitle','true'))==True) and (len(pTitle) > 0) and (len(pTVShowTitle) > 0): vName=pTVShowTitle+' - '+vName
		vName=vName.strip(); 
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
		vName=vName.strip(); 
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
	vName=vName.replace('!','').replace('"','').replace(':','').replace(';','').replace('|','').replace('/','').replace('\\','').replace('  ',' ')
	vName=vName.replace('[B]','').replace('[/B]','').replace('[I]','').replace('[/I]','').replace('[CR]','').replace('[/COLOR]','')
	for C1 in ["aliceblue","antiquewhite","aqua","aquamarine","azure","beige","bisque","black","blanchedalmond","blue","blueviolet","brown","burlywood","cadetblue","chartreuse","chocolate","coral","cornflowerblue","cornsilk","crimson","cyan","darkblue","darkcyan","darkgoldenrod","darkgray","darkgreen","darkkhaki","darkmagenta","darkolivegreen","darkorange","darkorchid","darkred","darksalmon","darkseagreen","darkslateblue","darkslategray","darkturquoise","darkviolet","deeppink","deepskyblue","dimgray","dodgerblue","firebrick","floralwhite","forestgreen","fuchsia","gainsboro","ghostwhite","gold","goldenrod","gray","green","greenyellow","honeydew","hotpink","indianred ","indigo  ","ivory","khaki","lavender","lavenderblush","lawngreen","lemonchiffon","lightblue","lightcoral","lightcyan","lightgoldenrodyellow","lightgrey","lightgreen","lightpink","lightsalmon","lightseagreen","lightskyblue","lightslategray","lightsteelblue","lightyellow","lime","limegreen","linen","magenta","maroon","mediumaquamarine","mediumblue","mediumorchid","mediumpurple","mediumseagreen","mediumslateblue","mediumspringgreen","mediumturquoise","mediumvioletred","midnightblue","mintcream","mistyrose","moccasin","navajowhite","navy","none","oldlace","olive","olivedrab","orange","orangered","orchid","palegoldenrod","palegreen","paleturquoise","palevioletred","papayawhip","peachpuff","peru","pink","plum","powderblue","purple","red","rosybrown","royalblue","saddlebrown","salmon","sandybrown","seagreen","seashell","sienna","silver","skyblue","slateblue","slategray","snow","springgreen","steelblue","tan","teal","thistle","tomato","turquoise","violet","wheat","white","whitesmoke","yellow","yellowgreen"]: vName=vName.replace('[COLOR '+C1+']','')
	vName=vName.strip(); 
	if tfalse(addst('name-datestamp','true'))==True: vName+=' - ['+DT['year']+'-'+DT['month']+'-'+DT['day']+']'; 
	vName=vName.strip(); 
	if   pType=='Video': 
		if   '.mpg' in vUrl: vName+='.mpg'; 
		elif '.mpeg' in vUrl: vName+='.mpeg'; 
		elif '.mp4' in vUrl: vName+='.mp4'; 
		elif '.avi' in vUrl: vName+='.avi'; 
		elif '.wmv' in vUrl: vName+='.wmv'; 
		elif '.flv' in vUrl: vName+='.flv'; 
		#elif '.' in vUrl: vName+='.'; 
		else: vName+='.flv'; 
	elif pType=='Audio': 
		if   '.mp3' in vUrl: vName+='.mp3'; 
		elif '.ogg' in vUrl: vName+='.ogg'; 
		elif '.mid' in vUrl: vName+='.mid'; 
		elif '.midi' in vUrl: vName+='.midi'; 
		elif '.wav' in vUrl: vName+='.wav'; 
		else: vName+='.mp3'; 
	else: 
		if   '.bmp' in vUrl: vName+='.bmp'; 
		elif '.jpg' in vUrl: vName+='.jpg'; 
		elif '.jpeg' in vUrl: vName+='.jpeg'; 
		elif '.png' in vUrl: vName+='.png'; 
		elif '.gif' in vUrl: vName+='.gif'; 
		elif '.psd' in vUrl: vName+='.psd'; 
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
		vName=setupName(vName,pType,vUrl); 
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
		vName=setupName(vName,pType,vUrl); 
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
		destpath=addpr('destpath','')
		if len(destpath)==0: destpath=addst('download_folder_default','')
		debob([url,addpr('destfile',''),destpath,'False']); 
		eod(); DoA("Back"); 
		DownloadThis(url,addpr('destfile',''),destpath,False); 
		
	elif (mode=='ResolveAndDownload'):
		destpath=addpr('destpath','')
		if len(destpath)==0: destpath=addst('download_folder_default','')
		debob([url,addpr('destfile',''),destpath,'False']); 
		eod(); DoA("Back"); 
		try: import urlresolver
		except: myNote('Problem','unable to import: urlresolver',15000); debob(['Problem','unable to import: urlresolver']); return
		try:
			oUrl=''+url
			url=urlresolver.HostedMediaFile(url).resolve()
		except: myNote('Problem','resolving url',15000); debob(['Problem','resolving url',oUrl,url]); return
		DownloadThis(url,addpr('destfile',''),destpath,False); 
		
	elif (mode=='toJDownloader'): 
		SendTo_JDownloader(url,tfalse(addpr('useResolver','true'))); 
		eod(); DoA("Back"); 
	elif (mode=='About'): About(); eod(); #DoA("Back"); 
	else: myNote(header='Site:  "'+str(site)+'"',msg=str(mode)+' (mode) not found.'); SectionMenu()


mode_subcheck(addpr('mode',''),addpr('site',''),addpr('section',''),addpr('url',''))
### ############################################################################################################
### ############################################################################################################
