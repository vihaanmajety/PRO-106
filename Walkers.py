import cv2


# Create our body classifier
print(cv2.data.haarcascades)
# "/Users/vihaan/Downloads/PRO-106-ProjectTemplate-main/" 
body_classifier=cv2.CascadeClassifier("haarcascade_fullbody.xml")

# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')
## print( "frames-"+ int(cv2.CAP_PROP_FRAME_COUNT));
# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Pass frame to our body classifier
    bodies=body_classifier.detectMultiScale(gray,1.2,3)
    
    # Extract bounding boxes for any bodies identified
    
    for (x,y,w,h) in bodies:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
       cv2.imshow(frame)

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
