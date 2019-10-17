import cv2 
  
# Function to extract frames 
def FrameCapture(path): 
      
    # Path to video file 
    video = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # video object to extract to extract frames
        success, image = video.read() 
  
        # Saves the frames with per frame-count 
        cv2.imwrite("output/frame%d.jpg" % count, image) 
        count += 1
  
# Driver Code 
if __name__ == '__main__': 
    
    video_path = "video/opencv.mp4"
    FrameCapture(video_path) 

