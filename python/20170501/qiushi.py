import urllib
import urllib2
import re
page =1
url = 'http://www.qiushibaike.com/hot'
user_agent = 'Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)'
headers = {'User-Agent' : user_agent }
try:
 request = urllib2.Request(url,headers = headers)
 response = urllib2.urlopen(request)
 content = response.read().decode('utf-8')
 pattern = re.compile('.*<span>(.*)</span>.*')
 result1 = re.findall(pattern,content)
 for x in result1:
      print x
# item = re.findall(pattern,content)
# print item
except urllib2.URLError, e:
 if hasattr(e,"code"):
  print e.code
 if hasattr(e,"reason"):
  print e.reason
