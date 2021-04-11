import urllib.request
import re


class MCBBSAPI:
    @staticmethod
    def get(fid):
        s = urllib.request.urlopen('https://www.mcbbs.net/forum.php?mod=forumdisplay&fid=' + str(fid)
                                   + '&filter=author&orderby=dateline&forumdefstyle=yes')
        information2 = s.read().decode('utf-8')
        information = re.findall('mod=viewthread&amp;tid=(.*?)&amp;extra=page%3D1%26filter%3Dauthor%26orderby%'
                                 '3Ddateline" (?:.*?)onclick="atarget\\(this\\)" class="s xst">(.*?)</a>', information2)
        return information
