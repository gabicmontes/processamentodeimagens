import youtube_dl
import os.path
import os
import dlib
import cv2
from matplotlib import pyplot as plt
from tqdm import tqdm
import subprocess
import face_recognition
import pickle


def generateEncodings(folderName, labelName, knownEncodings, knownNames):
    for filename in os.listdir(folderName):
        img = face_recognition.load_image_file(folderName + filename)
        boxes = face_recognition.face_locations(img, model = 'cnn')
        encodings = face_recognition.face_encodings(img, boxes)

        for encoding in encodings:
            knownEncodings.append(encoding)
            knownNames.append(labelName)
            
def download_youtube_video(youtube_url, video_filename):
    youtube_url = youtube_url.strip() 
    ydl_opts = {'outtmpl': video_filename}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])


def generateFolderWithFaces(folderName, videoFilename, thresholdFaces = 6, stepFrame = 10):
    detectedFacesCounter = 0
    faces = []
    frameCounter = 0

    videoCapture = cv2.VideoCapture(videoFilename)
    while 1:
        
        frameCounter += 1
        
        success, frame = videoCapture.read()
        
        if success == False or detectedFacesCounter >= thresholdFaces:
            return faces

        if frameCounter % stepFrame != 0:
            continue

        detections = detector(frame, 1)
        for i, detection in enumerate(detections):
            
            x, y = detection.left(), detection.top()
            w, h = detection.right() - detection.left(), detection.bottom() - detection.top()
            faceCrop = frame[y:y + h, x:x + w]
            img_path = folderName + "/" + str(frameCounter) + ".jpg"
            cv2.imwrite(img_path, faceCrop)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 4)
            landmarks = predictor(frame, detection)
            for i in range(0, 68): 
                cv2.circle(frame, (landmarks.part(i).x , landmarks.part(i).y), 4, (0, 0, 255), -1)      
            faces.append(frame)
        
        detectedFacesCounter += len(detections)
        
    videoCapture.release()



yb_url = "https://www.youtube.com/watch?v=xNtt73st7tw&ab_channel=Ohai%E2%99%A7"
file_name1 = "video.mp4"    
    
if os.path.isfile(file_name1) == False:
    download_youtube_video(yb_url, file_name1)
        
folder_name = "Moraes"
if os.path.isdir(folder_name) == False:
    os.mkdir(folder_name)    

shape_predictor_filename = "shape_predictor_68_face_landmarks.dat"
    
detector = dlib.get_frontal_face_detector()
    
predictor = dlib.shape_predictor(shape_predictor_filename)

exampleFaces = generateFolderWithFaces("Berlim/", "video.mp4")

knownEncodings = []
knownNames = []

folderName = "Berlim/"
labelName = "Berlim"
generateEncodings(folderName, labelName, knownEncodings, knownNames)
       

data_encoding = {"encodings": knownEncodings, "names": knownNames}

f = open("face_encodings", "wb")
f.write(pickle.dumps(data_encoding))
f.close()

youtube_url = "https://www.youtube.com/watch?v=pdXEnZ7jrcA&ab_channel=DrViciado"
video_filename = "teste_mila_e_vivi.mp4"

if os.path.isfile(video_filename) == False:
    download_youtube_video(youtube_url, video_filename)


data_encoding = pickle.loads(open("face_encodings", "rb").read())

videoCaptureInput = cv2.VideoCapture(video_filename)

unique_names = set(data_encoding["names"])

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
fps = videoCaptureInput.get(cv2.CAP_PROP_FPS)
videoCaptureOutput = cv2.VideoWriter("output.mp4", fourcc, fps, (1920, 1080))

for i in tqdm(range(0, 200)):
    
    success, frame = videoCaptureInput.read()
        
    if success == False:
        break
        
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    boxes = face_recognition.face_locations(frame, model = 'cnn')
    encodings = face_recognition.face_encodings(frame, boxes)
    
    names = []

   
    for encoding in encodings:
        matches = face_recognition.compare_faces(data_encoding["encodings"], encoding)
        
        matchesId = [i for i, value in enumerate(matches) if value == True]
        
        counts = {}
        for name in unique_names:
            counts[name] = 0  
        for i in matchesId:
            name = data_encoding["names"][i]
            counts[name] += 1
        name = max(counts, key = counts.get)
        names.append(name)

    for ((top, right, bottom, left), name) in zip(boxes, names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 4)
        cv2.putText(frame, name, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 4)
    
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    videoCaptureOutput.write(frame)

videoCaptureInput.release()
videoCaptureOutput.release()


subprocess.call(['ffmpeg', '-y', '-i', 'output.mp4', '-vf', 'fps=10,scale=640:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse', '-loop', '1', 'output.gif'])
