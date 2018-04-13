import os
import psutil

pid = {}
for i in os.listdir('../../j2sdk-image.java8.release/hottub/data'):
	try:
		with open('../../j2sdk-image.java8.release/hottub/data/{}/server.pid'.format(i)) as f:
			pid[i] = psutil.Process(int(f.read().strip()))
	except:
		pass
while True:
	for i in pid:
		try:
			x = pid[i].cpu_percent(0.1)
			if x > 0:
				print("{} {}".format(i, x))
		except:
			try:
				with open('../../j2sdk-image.java8.release/hottub/data/{}/server.pid'.format(i)) as f:
					pid[i] = psutil.Process(int(f.read().strip()))
			except:
				pass
