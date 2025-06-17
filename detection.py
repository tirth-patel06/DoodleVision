#import the required library to detect the image
import cv2

#We take the path of image
img_path = "E:\doodle bot\A.png"

#Use OpenCV and AruCo to read the image and convert to the array
img = cv2.imread(img_path)
dic = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)
par = cv2.aruco.DetectorParameters()

# Find the corners and ids of AruCo marker
corners, ids, _ = cv2.aruco.detectMarkers(img, dic, parameters=par)

#imp is string to save the center of AruCo marker
#idss is string to save the id of AruCo marker
imp = {}
idss = []

#Adding the id to the idss
for i in ids:
    temp = [i]
    idss+=temp
    
#Take the avg. of coordinates of all the four corners of AruCo and save we can find the center of the Aruco
i = 0
for corner in corners :
    tr, tl, br, bl = corner[0]
    x = idss[i][0]
    imp[x]=(tr+tl+br+bl)/4
    i+=1

#Now from relation of coordinate of values we convert the path in the form of XY plane
path = []
for i in range(len(corners)-1) :
    x1 = imp[i][0]
    y1 = imp[i][1]
    
    x2 = imp[i+1][0]
    y2 = imp[i+1][1]
    
    if(x2>x1):
        temp = ["+x"]
        path+=temp
    elif(x1>x2):
        temp = ["-x"]
        path+=temp
    elif(y2>y1):
        temp = ["-y"]
        path+=temp
    elif(y1>y2):
        temp = ["+y"]
        path+=temp

#Finally, this detect the F,R and L according to the XY plane logic
# F = Start/Forward
# R = Right turn
# L = Left turn
final_path = []
for i in range(len(path)-1) :
    now = path[i]
    nxt = path[i+1]
    
    if i==0:
        final_path+="F"
    
    if now == "+x":
        if nxt == "-y":
            final_path+="R"
        elif nxt == "+y":
            final_path+= "L"
        else:
            final_path+= "F"
            
    if now == "-y":
        if nxt == "-x":
            final_path+="R"
        elif nxt == "+x":
            final_path+= "L"
        else:
            final_path+= "F"
    
    if now == "-x":
        if nxt == "+y":
            final_path+="R"
        elif nxt == "-y":
            final_path+= "L"
        else:
            final_path+= "F"
    
    if now == "+y":
        if nxt == "+x":
            final_path+="R"
        elif nxt == "-x":
            final_path+= "L"
        else:
            final_path+= "F"
            
    if i==(len(path)-2):
        final_path+="E"
    
#Print the string of path detected
print(final_path)