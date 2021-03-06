# -*-coding:utf-8 -*-
import urllib, urllib2, re, random, time
from ritsu_utils import *
from ritsu_api import *

xoma_db = {}

def load(bot):
  global langreg
  global xoma_db
  global task_db
  xoma_db = bot.load_database('xoma') or {}
#  bot.add_command('iii', command_iiypuk, LEVEL_GUEST)
#  bot.add_command(u'ш', command_iiypuk, LEVEL_GUEST)
  bot.add_command('fr', command_freedos, LEVEL_GUEST)
  bot.add_command('whtask', command_whtask, LEVEL_GUEST)
  bot.add_command(u'делать', command_whtask, LEVEL_GUEST)
  bot.add_command('true', command_true, LEVEL_GUEST)
  bot.add_command(u'инфа', command_true, LEVEL_GUEST)
  bot.add_command('d', command_d, LEVEL_GUEST)
  bot.add_command(u'в', command_d, LEVEL_GUEST)
  bot.add_command('anek', command_anek, LEVEL_GUEST)
  bot.add_command(u'анек', command_anek, LEVEL_GUEST)

def unload(bot):
  pass

def info(bot):
  return 'WWW plugin v1.0.3'

def command_d(bot, room, nick, access_level, parameters, message):
    '''Проверить, лежит ли сайт'''
    if not parameters:
        return
    try:
        link = urllib2.urlopen(urllib2.Request("http://isup.me/" + parameters.encode("idna")), timeout = 20)
	downfor = link.read()
	return u"Сайт " + parameters + (u" в дауне." if "It's not just you!" in downfor else u" работает." if "It's just you" in downfor else u" не сайт вообще.")
    except urllib2.URLError:
	return u"Ошибка запроса."

def command_anek(bot, room, nick, access_level, parameters, message):
  try:
    target = urllib2.urlopen('http://anekdot.odessa.ua/rand-anekdot.php')
    message = target.read().decode('windows-1251')
    target.close()
    try:
       message = message.replace('<div style=\'color: #000000; font-size: 12;background-color:#FFFFFF\'>', '')
       message = message[:re.search('<br>',message).start()]
       message = message.replace('<br />','')
       message = message.strip()
    except:
       return u'Ошибка парсера'
    return message
  except:
    return u'Произошла ошибка.'


def command_true(bot, room, nick, access_level, parameters, message):
  if parameters:
    procent = str(random.randint(1, 100))
    return u'%s процентов(а) истины.' % (procent)

def command_whtask(bot, room, nick, access_level, parameters, message):
  if parameters:
    # parameters = parameters + u', астрал'
    listtask = parameters.split(',')
    number = random.randint(1, len(listtask))
    result = listtask[number-1]
    res = u'Тебе нужно: %s' % (result)
    return res

def command_freedos(bot, room, nick, access_level, parameters, message):
  return "There could be any option from freedos."

def command_iiypuk(bot, room, nick, access_level, parameters, message):
  url = 'http://iiiypuk.me/current-track/'
  try:
    site = urllib2.urlopen('%s'%(url))
  except urllib2.HTTPError, e:
    if e.code == 404:
      return '%s page not found.'%(e.code)
    else:
      return
  rec = site.read().decode("utf-8")
  site.close
  tag = 'title'
  T = re.findall('<%s.*?>(.*?)</%s>'%(tag, tag), rec)
  title = T[0]
  return "%s" % (title)
