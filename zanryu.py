#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import cookielib
import os
import re
import mechanize
import ConfigParser

from urllib2 import HTTPError


def Regist(name, password, teluser, telemergency, gohometime, building, floor, room, reason, yc, ks):

	#SFSにログインする
	print "SFC login(1of3)"
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.open('https://vu8.sfc.keio.ac.jp/sfc-sfs/index.cgi')
	browser.select_form(nr=0)
	browser.form['u_login'] = name
	browser.form['u_pass'] = password
	res = browser.submit()
	loginURL = res.geturl().split('&')
	loginID = loginURL[1].split('=')
	encodeID = loginID[1]
	conf = os.path.join(os.path.dirname(__file__),'out/out.html')
	f = open(conf, 'w')
	f.write(str(res.read()))
	f.close()

	#研究室のページに移動
	print "Lab page(2of3)"
	browser.open('https://vu9.sfc.keio.ac.jp/sfc-sfs/sfs_class/student/s_class_top.cgi?lang=ja&ks=%s&yc=%s&id=%s'% (ks, yc, encodeID))
	browser.select_form(nr=0)
	res = browser.submit()
	conf = os.path.join(os.path.dirname(__file__),'out/out2.html')
	f = open(conf, 'w')
	f.write(str(res.read()))
	f.close()
	
	#登録する
	print "Registration(3of3)"
	browser.select_form(nr=0)
	browser.form['stay_phone'] = teluser
	browser.form['stay_p_phone'] = telemergency
	browser.form['stay_time'] = gohometime
	browser.form['selectRoom'] = [building,]
	#browser.form['selectFloor'] = [floor,]
	browser.form['stay_room_other'] = room
	browser.form['stay_reason'] = reason
	res = browser.submit()
	conf = os.path.join(os.path.dirname(__file__),'out/index.html')
	f = open(conf, 'w')
	f.write(str(res.read()))
	f.close()

if __name__=='__main__':

	print "Zanryu System is started."

	#config.txtを読み込む
	config = ConfigParser.SafeConfigParser()
	conf = os.path.join(os.path.dirname(__file__),'config.txt')
	config.read([os.path.expanduser(conf)])
	

	#登録する
	Regist(
		config.get('config', 'name'),
		config.get('config', 'password'),
		config.get('config', 'TelUser'),
		config.get('config', 'TelEmergency'),
		config.get('config', 'goHomeTime'),
		config.get('config', 'Building'),
		config.get('config', 'Floor'),
		config.get('config', 'Room'),
		config.get('config', 'Reason'),
		config.get('config', 'yc'),
		config.get('config', 'ks')
	)

	print "Zanryu System is finished."
