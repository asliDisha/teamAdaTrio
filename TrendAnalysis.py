from pytrends.request import TrendReq
import matplotlib.pyplot as plt
plt.style.use('ggplot')
pytrends = TrendReq(hl='en-US')
all_keywords=['Kalki','India 2','Mirazapur', 'House of the Dragon','Kota factory', 'Maharaj']
timeframes = ['today 1-m', 'now 7-d']
cat = '0'
geo = 'IN'
gprop=''
keywords=['famous movies','famous celebrities','famous songs']

def relative_comparison():
	plt.figure(figsize = (10,8))
	x_pos = np.arange(len(all_keywords))
	pytrends.build_payload (all_keywords, cat, timeframes[0], geo, gprop)
data = pytrends.interest_over_time ()
mean = data.mean()
mean = round(mean/mean.max() * 100,2)

ax1 = plt.subplot2grid((1,2), (0,0), rowspan= 1, colspan= 1)
ax2 = plt.subplot2grid((1,2), (0,1), rowspan= 1, colspan= 1)
for kw in all_keywords:
	ax1.plot(data[kw],label=kw)
ax2.bar(x_pos,mean[0:len(all_keywords)], align='center')
plt.xticks(x_pos, all_keywords)

ax1.set_ylabel('last 1 month')
ax1.set_title('Relative Interest over time')
ax2.set_title('Relative Interest for the Period')
ax1.legend()
plt.show()
relative_comparison()

def rel_queries(i):
	pytrends.build_payload(keywords[i], cat, timeframes[1], geo, gprop)
	data = pytrends.related_queries()
	print(data)

for i in range(len(keywords)):
	rel_queries(i)
			
			