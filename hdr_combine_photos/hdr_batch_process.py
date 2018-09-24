
import exifread
# Open image file for reading (binary mode)
#path_name = "images/1/sample-00.png"
path_name = "images/android_phone_demo/IMG_20180923_173726.jpg"
f = open(path_name, 'rb')

# Return Exif tags
tags = exifread.process_file(f)
print(tags)


print (type(tags))
print (list(tags.keys()))

for key in tags.keys():
    print (key, geo[key])

print ("--------GPS KEYS-------------------------------")
geo = {i:tags[i] for i in tags.keys() if i.startswith('GPS')}
for key in geo.keys():
    print (key, geo[key])

print ("--------EXIF KEYS-------------------------------")
exif = {i:tags[i] for i in tags.keys() if i.startswith('EXIF')}
for key in exif.keys():
    print (key, exif[key])

#'EXIF ExposureTime'

print('EXIF ExposureTime', exif['EXIF ExposureTime'], type(exif['EXIF ExposureTime']))



'''
'GPS GPSTimeStamp'
'GPS GPSLatitudeRef'
'GPS GPSLongitudeRef'
'GPS GPSProcessingMethod'
'GPS GPSProcessingMethod'
'GPS GPSLatitude'
'GPS GPSLongitude'
'GPS GPSVersionID'
'''
