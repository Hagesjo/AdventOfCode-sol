import hashlib
import sys

key = "yzbqklnj"
for i in xrange(sys.maxint):
	if hashlib.md5("%s%s" % (key, i)).hexdigest()[:6] == "000000":
		print i
		break
