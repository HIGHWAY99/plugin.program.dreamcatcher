### ############################################################################################################
###	#	
### # Author: 			#		The Highway
### # Description: 	#		Config File For:  
###	#	
### ############################################################################################################
### ############################################################################################################
### Imports ###
import xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs
import os,sys,string,StringIO,logging,random,array,time,datetime,re
#from t0mm0.common.addon import Addon
#try: 		from t0mm0.common.addon 				import Addon
#except: 
#	try: from c_t0mm0_common_addon 				import Addon
#	except: pass
try: 			from addon.common.addon 				import Addon
except:
	try: 		from t0mm0.common.addon 				import Addon
	except: 
		try: from c_t0mm0_common_addon 				import Addon
		except: pass
### Plugin Settings ###
def ps(x):
	if (x=='_addon_id') or (x=='addon_id') or (x=='_plugin_id') or (x=='plugin_id'): return 'plugin.program.dreamcatcher'
	try: 
		return {
			'__plugin__': 					"Dreamcatcher"
			,'__authors__': 				"[COLOR white]The[COLOR tan]Highway[/COLOR][/COLOR]"
			,'__credits__': 				""
			,'_domain_url': 				""
			,'word': 								""
			,'word0': 							""
			,'word1': 							""
			,'word2': 							""
			,'word3': 							""
			,'word4': 							""
			,'word5': 							""
			,'word6': 							""
			,'word7': 							""
			,'word8': 							""
			,'word9': 							""
			,'content_movies': 			"movies"
			,'content_tvshows': 		"tvshows"
			,'content_seasons': 		"seasons"
			,'content_episodes': 		"episodes"
			,'content_links': 			"list"
			,'default_section': 					'anime'
			,'section.wallpaper':					'wallpapers'
			,'section.tv': 								'tv'
			,'section.movies': 						'movies'
			,'section.anime': 						'anime'
			,'section.animesub': 					''
			,'section.animedub': 					''
			,'section.animesubmovies': 		''
			,'section.animesubseries': 		''
			,'section.animedubmovies': 		''
			,'section.animedubseries': 		''
			,'section.anime': 						''
			,'sep': 								os.sep
			,'special.home': 				'special:'+os.sep+os.sep+'home'
			,'special.home.addons': 'special:'+os.sep+os.sep+'home'+os.sep+'addons'+os.sep
			,'_addon_path_art': 		"art"
			,'_addon_path_scr': 		"scr"
			,'_addon_path_snd': 		"snd"
			,'_addon_path_bgm': 		"bgm"
			,'_database_name': 			"animefate"
			,'default_art_ext': 		'.png'
			,'default_cFL_color': 	'cornflowerblue'
			,'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
			,'cMI.showinfo.url': 							'XBMC.Action(Info)'
			,'cMI.jDownloader.addlink.url':		'XBMC.RunPlugin(plugin://plugin.program.jdownloader/?action=addlink&url=%s)'
			,'filemarker': ''
			,'iiHubIrc': 'http://i.imgur.com/V3jly5Y.png' # #XBMCHUB IRC chat.freenode.net/6667 - Transperant
			,'fiHubIrc': 'http://i.imgur.com/UtL1F8j.png' # #XBMCHUB IRC chat.freenode.net/6667
			,'iiMenuMoviesTV': 'http://i.imgur.com/dP5BuiD.png' #'http://www.live365.com/userdata/67/62/9886267/stationlogo276x155.jpg' # highway near water (nice)
			,'fiMenuMoviesTV': 'http://s9.postimg.org/6izlt73n3/1011445_473021149448994_84427075_n.jpg' # xbmchub freetv ad
			,'iiMenuLiveStreams': 'http://i.imgur.com/OMI5OV9.png' #'http://i.imgur.com/LdJzy5M.png' #'http://media.kcrg.com/images/128241+-+PRV+-+LCL+METRO+HWY+30+GOES+4+LANES+-+03_11_2003+-+11.52.25.jpg' # highway trucks
			,'fiMenuLiveStreams': 'http://th02.deviantart.net/fs41/PRE/i/2009/026/7/3/highway1_by_mikkesh.jpg' # highway night slowmotion  lighting
			,'iiMenuMisc': 'http://i.imgur.com/XMClMrQ.png' #'https://si0.twimg.com/profile_images/1880386140/logo-square.jpg' # XBMCHUB 3rd party addons logo /w white bg
			,'fiMenuMisc': 'http://www.mirrorservice.org/sites/addons.superrepo.org/Frodo/.metadata/plugin.video.tv-release.jpg' # blue raindrop xbmchub backdrop
			,'iiMenuOthers': 'http://i.imgur.com/om8NvNt.png' #'http://media.lifehealthpro.com/lifehealthpro/article/2012/04/13/SocialMediaHighway-resize-380x300.JPG' # wet highway
			,'fiMenuOthers': 'http://i.imgur.com/N8TFtcq.jpg' # highway /w sun thru clouds
			,'iiMenuImages': 'http://i.imgur.com/5p3Ae3l.png' #'http://i.imgur.com/xWw3Pps.png' #'http://www.cartertoons.com/toons/AdoptedHighway.jpg' # adopt a highway (temp image)
			,'fiMenuImages': 'http://i.imgur.com/N8TFtcq.jpg' # highway /w sun thru clouds
			,'iiMenuAudio': 'http://i.imgur.com/qkPliwr.png' #'http://www.autoaubaine.com/administration/special/images/dossier/1936917557_f849782d8b.jpg' # highway with music notes
			,'fiMenuAudio': 'http://img6.joyreactor.cc/pics/post/full/%23Music%26Atmosphere-%D1%80%D0%B0%D0%B7%D0%BD%D0%BE%D0%B5-d-pulse-on-a-highway-to-saturn-870016.jpeg' # 
			,'iiMenuAnime': 'http://i.imgur.com/xWw3Pps.png' #'http://www.geocities.ws/eruku313/Animehighway_pic.jpg' # Anime Girl on bike
			,'fiMenuAnime': 'http://media.animevice.com/uploads/0/4479/413662-181755.jpg' # HSotD Highway
			,'iiMenuSports': 'http://i.imgur.com/ZoCDJj5.png'
			,'fiMenuSports': ''
			,'iiMenuAdult': 'http://i.imgur.com/6iGVGlK.png'
			,'fiMenuAdult': ''
			#,'ii': '' # 
			#,'fi': '' # 
			#,'ii': '' # 
			#,'fi': '' # 
			#,'ii': '' # 
			#,'fi': '' # 
			#,'ii': '' # 
			#,'fi': '' # 
			#,'ii': '' # 
			#,'fi': '' # 
			#,'ii': '' # 
			#,'fi': '' # 
			#,'ii': '' # 
			#,'fi': '' # 
			#,'': ''
			,'ReferalMsg': 'My XBMC-HUB Refferal Code - http://www.xbmchub.com/forums/register.php?referrerid=15468  [CR]Please use it to register if you don\'t have an account.  It not\'s not much but it can help me out.  '
			,'WhatRFavsCalled': 'Favs: '
		}[x]
	except: return ''







### ############################################################################################################
### ############################################################################################################
