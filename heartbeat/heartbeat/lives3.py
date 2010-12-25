#!/usr/bin/env python

import time

from google.appengine.api import urlfetch

from google.appengine.api import mail

def startTest(url):
    print 'Content-Type: text/plain'
    print ''
    
    #url = "http://www.youtube.com"
    #result = urlfetch.fetch(url)
    
    #if result.status_code != 200:
    #    alert_count = 0
    #    timeStr = time.strftime("[%Y/%m/%d, %H:%M:%S (+8:00) %a]", time.gmtime(time.time()+8*3600))
    #    print "An alert email for "+url+" has been send at "+timeStr
    #    sendAlert(url, timeStr)
    #else:   
    #    print url+" is alive..."
    #result = urllib2.urlopen(url)
    count = 0
    tryCount = 3
    
    while tryCount > 0:
        result = None
        try:
            result = urlfetch.fetch(url, headers = {'Cache-Control': 'max-age=1'})
            print result.content
        except:
            count += 1    
        tryCount -= 1
    if count > 2:
        timeStr = time.strftime("[%Y/%m/%d, %H:%M:%S (+8:00) %a]", time.gmtime(time.time()+8*3600))
        print "An alert email for "+url+" has been send at "+timeStr + "  " + str(count)
        sendAlert(url, timeStr)
    else:
        print url+" is alive..."

def sendAlert(url, timeStr):
    #Basic setting

    msg = {}
    msg['Subject'] = "Lives3 Heart Beat Alert"
    msg['From'] = "alert@heartbeattest.appspotmail.com"
    msg['To'] = "paullzn@gmail.com,liyuqian79@gmail.com,lywander@gmail.com"
    #msg['To'] = "paullzn@gmail.com"

    body = "[Do Not Reply]\nThis is an alert from Heart-Beat-Test service.\n"
    body += "HBT haven't got any response from " + url
    body += " at "+timeStr + ".\n"
    # body += " for "+str(minute / 60 / 24) + " days " + str(minute % (60 * 24) / 60) + " hours " + str(minute % 60) + " minutes.\n"
    body += "Thanks.\n"
    mail.send_mail(msg['From'], msg['To'], msg['Subject'], body)
        
if __name__ == '__main__':
    startTest("http://www.lives3.net/")