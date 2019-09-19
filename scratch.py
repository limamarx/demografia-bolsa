import pandas as pd
import folium
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster
from folium import plugins
import numpy

data2018 = pd.read_csv(r'/home/mateus/Documentos/UFRN/Bolsa/datatran2018 (1).csv')
data2017 = pd.read_csv(r'/home/mateus/Documentos/UFRN/Bolsa/datatran2017.csv')
data2019 = pd.read_csv(r'/home/mateus/Documentos/UFRN/Bolsa/datatran2019.csv')

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0



for i in range(0, len(data2017.longitude)):
    if((data2017.longitude[i] > -34.758526 or data2017.longitude[i] < -74.054779) or (data2017.latitude[i]>5.321384 or data2017.latitude[i]< -33.776984)):
        count1 = count1 + 1
    elif((data2017.longitude[i] - int(data2017.longitude[i]) == 0 or data2017.longitude[i] + int(data2017.longitude[i]) == 0)or(data2017.latitude[i] - int(data2017.latitude[i]) == 0 or data2017.latitude[i] + int(data2017.latitude[i]) == 0)):
        count1 = count1 +1
    elif ((data2017.latitude[i] < -14.516233) and (data2017.latitude[i] > -23.962828) and (data2017.longitude[i] < -62.92076 and data2017.longitude[i] > -76.778894)):
        count1 = count1 + 1
    else:
        count2 = count2 + 1


for i in range(0, len(data2018.longitude)):
    if ((data2018.longitude[i] > -34.758526 or data2018.longitude[i] < -74.054779) or (data2018.latitude[i] > 5.321384 or data2018.latitude[i] < -33.776984)):
        count3 = count3 + 1
    elif ((data2018.longitude[i] - int(data2018.longitude[i]) == 0 or data2018.longitude[i] + int(data2018.latitude[i]) == 0) or (data2018.latitude[i] - int(data2018.latitude[i]) == 0 or data2018.latitude[i] + int(data2018.latitude[i]) == 0)):
        count3 = count3 + 1
    else:
        count4 = count4 + 1

for i in range(0, len(data2019.Longitude)):
    if ((data2019.Longitude[i] > -34.945647 or data2019.Longitude[i] < -38.595802) or (data2019.Latitude[i] > -4.821490 or data2019.Latitude[i] < -6.988465)):
        count5 = count5 + 1
    elif ((data2019.Longitude[i] - int(data2019.Longitude[i]) == 0 or data2019.Longitude[i] + int(data2019.Latitude[i]) == 0) or (data2019.Latitude[i] - int(data2019.Latitude[i]) == 0 or data2019.Latitude[i] + int(data2019.Latitude[i]) == 0)):
        count5 = count5 + 1
    else:
        count6 = count6 + 1

print("\nLocalização 2017 dentro dos padrões = ", count2)
print("Localização 2017 fora dos padrões = ", count1)
print("\nLocalização 2018 dentro dos padrões = ", count4)
print("Locacilação 2018 fora dos padrões = ",count3)
print("\nLocalização 2019-RN dentro dos padrões = ", count6)
print("Locacilação 2019-RN fora dos padrões = ",count5)

#========================HEAT MAP 2017==============================

y = data2017.latitude.tolist()
x = data2017.longitude.tolist()

m1 = folium.Map(
    location=[-5.826592, -35.212558],
    zoom_start=8,
    tiles='Stamen Terrain',
    width='70%',
    height='70%'
)

HeatMap(list(zip(y,x))).add_to(m1)
m1.save(r'/home/mateus/Documentos/UFRN/Bolsa/mapa_2017.html')


#========================CLUSTER 2017===============================
locais2017 = data2017[["latitude","longitude"]].values.tolist()
m1cluster = folium.Map(location=[-5.826592, -35.212558],
    zoom_start=8,
    tiles='Stamen Terrain',
    width='70%',
    height='70%')

MarkerCluster(locations = locais2017).add_to(m1cluster)

m1cluster.save(r'/home/mateus/Documentos/UFRN/Bolsa/mapa_2017_cluster.html')
#========================HEAT MAP 2018==============================

y = data2018.latitude.tolist()
x = data2018.longitude.tolist()

m2 = folium.Map(
    location=[-5.826592, -35.212558],
    zoom_start=8,
    tiles='Stamen Terrain',
    width='70%',
    height='70%'
)

HeatMap(list(zip(y,x))).add_to(m2)
m2.save(r'/home/mateus/Documentos/UFRN/Bolsa/mapa_2018.html')
#========================CLUSTER 2018===============================
locais2018 = data2018[["latitude","longitude"]].values.tolist()
m2cluster = folium.Map(location=[-5.826592, -35.212558],
    zoom_start=8,
    tiles='Stamen Terrain',
    width='70%',
    height='70%')

MarkerCluster(locations = locais2018).add_to(m2cluster)

m2cluster.save(r'/home/mateus/Documentos/UFRN/Bolsa/mapa_2018_cluster.html')
#========================HEAT MAP 2019 RN==============================

y = data2019.Latitude.tolist()
x = data2019.Longitude.tolist()

m3 = folium.Map(
    location=[-5.826592, -35.212558],
    zoom_start=8,
    tiles='Stamen Terrain',
    width='70%',
    height='70%'
)

HeatMap(list(zip(y,x))).add_to(m3)
m3.save(r'/home/mateus/Documentos/UFRN/Bolsa/mapa_RN_2019.html')
#========================CLUSTER 2019===============================

locais2019 = data2019[["Latitude","Longitude"]].values.tolist()
m3cluster = folium.Map(location=[-5.826592, -35.212558],
    zoom_start=8,
    tiles='Stamen Terrain',
    width='70%',
    height='70%')

MarkerCluster(locations = locais2019).add_to(m3cluster)

m3cluster.save(r'/home/mateus/Documentos/UFRN/Bolsa/mapa_RN_2019_cluster.html')

#======================================PENTE FINO - 2017==========================================

for i in range(0, len(data2017.longitude)):
    if ((data2017.longitude[i] > -34.758526 or data2017.longitude[i] < -74.054779) or (data2017.latitude[i] > 5.321384 or data2017.latitude[i] < -33.776984)):
        data2017.drop(i,inplace = True)
        print("tirou linha 2017a - ", i)
    elif ((data2017.longitude[i] - int(data2017.longitude[i]) == 0 or data2017.longitude[i] + int(data2017.longitude[i]) == 0) or (data2017.latitude[i] - int(data2017.latitude[i]) == 0 or data2017.latitude[i] + int(data2017.latitude[i]) == 0)):
        data2017.drop(i,inplace = True)
        print("tirou linha 2017b - ", i)
    elif((data2017.latitude[i] < -14.516233) and (data2017.latitude[i] > -23.962828) and (data2017.longitude[i] <-62.920765 and data2017.longitude[i] > -76.778894)):
        data2017.drop(i,inplace = True)
        print("tirou linha 2017c - ", i)
    else:
        print("linha 2017 ok -",i)
#data2017.save(r'/home/mateus/Documentos/UFRN/Bolsa/dadosmodificados2017.csv')

#======================================PENTE FINO - 2018==========================================

for i in range(0, len(data2018.longitude)):
    if ((data2018.longitude[i] > -34.758526 or data2018.longitude[i] < -74.054779) or (data2018.latitude[i] > 5.321384 or data2018.latitude[i] < -33.776984)):
        print("tirou linha 2018 - ", i)
        data2018.drop(i, inplace=True)
    elif ((data2018.longitude[i] - int(data2018.longitude[i]) == 0 or data2018.longitude[i] + int(data2018.longitude[i]) == 0) or (data2018.latitude[i] - int(data2018.latitude[i]) == 0 or data2018.latitude[i] + int(data2018.latitude[i]) == 0)):
        print("tirou linha 2018 - ", i)
        data2018.drop(i, inplace=True)
    else:
        print("linha 2018 ok -", i)


#======================================PENTE FINO - 2019==========================================

for i in range(0, len(data2019.Longitude)):
    if ((data2019.Longitude[i] > -34.758526 or data2019.Longitude[i] < -74.054779) or (data2019.Latitude[i] > 5.321384 or data2019.Latitude[i] < -33.776984)):
        data2019.drop(i, inplace=True)
        print("tirou linha 2019 - ", i)
    elif ((data2019.Longitude[i] - int(data2019.Longitude[i]) == 0 or data2019.Longitude[i] + int(data2019.Longitude[i]) == 0) or (data2019.Latitude[i] - int(data2019.Latitude[i]) == 0 or data2019.Latitude[i] + int(data2019.Latitude[i]) == 0)):
        data2019.drop(i, inplace=True)
        print("tirou linha 2019 - ", i)
    else:
        print("linha 2019 ok -", i)

print("Começando o clean cluster")


#========================CLEAN CLUSTER 2017===============================

locais2017_clean = data2017[["latitude","longitude"]].values.tolist()
m1cluster_clean = folium.Map(location=[-5.826592, -35.212558],
    zoom_start=8,
    tiles='Stamen Terrain',
    width='70%',
    height='70%')

MarkerCluster(locations = locais2017_clean).add_to(m1cluster_clean)

m1cluster_clean.save(r'/home/mateus/Documentos/UFRN/Bolsa/mapa_2017_clean_cluster.html')

#========================CLEAN CLUSTER 2018===============================

locais2018_clean = data2018[["latitude","longitude"]].values.tolist()
m2cluster_clean = folium.Map(location=[-5.826592, -35.212558],
    zoom_start=8,
    tiles='Stamen Terrain',
    width='70%',
    height='70%')

MarkerCluster(locations = locais2018_clean).add_to(m2cluster_clean)

m2cluster_clean.save(r'/home/mateus/Documentos/UFRN/Bolsa/mapa_2018_clean_cluster.html')

#========================CLEAN CLUSTER 2019===============================

locais2019_clean = data2019[["Latitude","Longitude"]].values.tolist()
m3cluster_clean = folium.Map(location=[-5.826592, -35.212558],
    zoom_start=8,
    tiles='Stamen Terrain',
    width='70%',
    height='70%')

MarkerCluster(locations = locais2019_clean).add_to(m3cluster_clean)

m3cluster_clean.save(r'/home/mateus/Documentos/UFRN/Bolsa/mapa_2019_clean_cluster.html')

