

       
#use pylab
%pylab

#import 
from pylab import *
from mpl_toolkits.basemap import Basemap
from scipy.stats import gaussian_kde

#turn interactive mode off
ioff()


#import coordinates data and set to long and lat
finalloc = final.loc[(final['coordinates.coordinates'].notnull()) | (final['place.bounding_box.coordinates'].notnull()),['place.bounding_box.coordinates']] 
latlong = np.squeeze(np.apply_along_axis(mean,2,np.array(finalloc.iloc[:,0].tolist())))
latitude = latlong[:,0]
longitude = latlong[:,1]      

#create map density color guide
xy = np.vstack([latitude,longitude])
z = gaussian_kde(xy)(xy)

z = z*10000

#Draw map
#fig = plt.figure(figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
map = Basemap()
map.drawcoastlines()
#ax = fig.add_axes([0.05,0.05,0.9,0.9])
map.scatter(latitude,longitude, s=20, edgecolor='', color=z)

#check graph
plt.gcf()
#save graph
plt.savefig('/home/ubuntu/Desktop/Plot.pdf')
plt.show()



#Draw map
#fig = plt.figure(figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
m = Basemap()
m.drawcoastlines()
m.drawcountries()
#ax = fig.add_axes([0.05,0.05,0.9,0.9])
x,y = m(latitude,longitude)  
m.scatter(x,y, s=10, edgecolor='', color=z)
m.colorbar(label='Point Density x10e5')
plt.title("World")

#save graph
plt.savefig('/home/ubuntu/Desktop/PlotWorld.png')
#plt.show()
plt.clf()


#brazil
m = Basemap(projection='merc',llcrnrlat=-35,urcrnrlat=5,
            llcrnrlon=-75,urcrnrlon=-30,lat_ts=20,resolution='i')
m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.drawrivers(color='lightblue')
# draw parallels and meridians.
parallels = np.arange(-90.,91.,5.)
# Label the meridians and parallels
m.drawparallels(parallels,labels=[False,True,True,False])
# Draw Meridians and Labels
meridians = np.arange(-180.,181.,10.)
m.drawmeridians(meridians,labels=[True,False,False,True])
m.drawmapboundary(fill_color='white')
plt.title("Brazil")
x,y = m(latitude,longitude)  
m.scatter(x,y, s=50, edgecolor='', color=z)
plt.savefig('/home/ubuntu/Desktop/PlotBrazil.png')
#plt.show()

plt.clf()

#works with merc
m = Basemap(projection='merc',llcrnrlat=20,urcrnrlat=50,
            llcrnrlon=-130,urcrnrlon=-60,lat_ts=20,resolution='i')
m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.drawrivers(color='lightblue')
# draw parallels and meridians.
parallels = np.arange(-90.,91.,5.)
# Label the meridians and parallels
m.drawparallels(parallels,labels=[False,True,True,False])
# Draw Meridians and Labels
meridians = np.arange(-180.,181.,10.)
m.drawmeridians(meridians,labels=[True,False,False,True])
m.drawmapboundary(fill_color='white')
plt.title("USA")
x,y = m(latitude,longitude)  
m.scatter(x,y, s=50, edgecolor='', color=z)
plt.savefig('/home/ubuntu/Desktop/PlotUSA.png')
#plt.show()

plt.clf()
