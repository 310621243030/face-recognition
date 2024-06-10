import cv2
import numpy as np
import face_recognition

imgModi3 = face_recognition.load_image_file('C:\\face3\\photos\\varsha.jpg')
imgModi3 = cv2.cvtColor(imgModi3, cv2.COLOR_BGR2RGB)
imgTest3 = face_recognition.load_image_file('C:\\face3\\photos\\varsha2.jpg')
imgTest3 = cv2.cvtColor(imgTest3, cv2.COLOR_BGR2RGB)

faceloc3 = face_recognition.face_locations(imgModi3)[0]
encodeModi3 = face_recognition.face_encodings(imgModi3)[0]
cv2.rectangle(imgModi3, (faceloc3[3], faceloc3[0]), (faceloc3[1], faceloc3[2]), (155, 0, 255), 2)

facelocTest3 = face_recognition.face_locations(imgTest3)[0]
encodeTest3= face_recognition.face_encodings(imgTest3)[0]
cv2.rectangle(imgTest3, (facelocTest3[3], facelocTest3[0]), (facelocTest3[1], facelocTest3[2]), (155, 0, 255), 2)

results3 = face_recognition.compare_faces([encodeModi3], encodeTest3)
faceDis3 = face_recognition.face_distance([encodeModi3], encodeTest3)
print(results3, faceDis3)
cv2.putText(imgTest3, f'{results3} {round(faceDis3[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

cv2.imshow('varsha', imgModi3)
cv2.imshow('varsha2', imgTest3)

imgModi4 = face_recognition.load_image_file('C:\\face3\\photos\\jaya.jpg')
imgModi4 = cv2.cvtColor(imgModi4, cv2.COLOR_BGR2RGB)
imgTest4 = face_recognition.load_image_file('C:\\face3\\photos\\jaya2.jpg')
imgTest4 = cv2.cvtColor(imgTest4, cv2.COLOR_BGR2RGB)

faceloc4 = face_recognition.face_locations(imgModi4)[0]
encodeModi4 = face_recognition.face_encodings(imgModi4)[0]
cv2.rectangle(imgModi4, (faceloc4[3], faceloc4[0]), (faceloc4[1], faceloc4[2]), (155, 0, 255), 2)

facelocTest4 = face_recognition.face_locations(imgTest4)[0]
encodeTest4= face_recognition.face_encodings(imgTest4)[0]
cv2.rectangle(imgTest4, (facelocTest4[3], facelocTest4[0]), (facelocTest4[1], facelocTest4[2]), (155, 0, 255), 2)

results4 = face_recognition.compare_faces([encodeModi4], encodeTest4)
faceDis4 = face_recognition.face_distance([encodeModi4], encodeTest4)
print(results4, faceDis4)
cv2.putText(imgTest4, f'{results4} {round(faceDis4[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

cv2.imshow('jaya', imgModi4)
cv2.imshow('jaya2', imgTest4)

imgModi5 = face_recognition.load_image_file('C:\\face3\\photos\\kavin.jpg')
imgModi5 = cv2.cvtColor(imgModi5, cv2.COLOR_BGR2RGB)
imgTest5 = face_recognition.load_image_file('C:\\face3\\photos\\kavin2.jpg')
imgTest5 = cv2.cvtColor(imgTest5, cv2.COLOR_BGR2RGB)

faceloc5 = face_recognition.face_locations(imgModi5)[0]
encodeModi5 = face_recognition.face_encodings(imgModi5)[0]
cv2.rectangle(imgModi5, (faceloc5[3], faceloc5[0]), (faceloc5[1], faceloc5[2]), (155, 0, 255), 2)

facelocTest5 = face_recognition.face_locations(imgTest5)[0]
encodeTest5= face_recognition.face_encodings(imgTest5)[0]
cv2.rectangle(imgTest5, (facelocTest5[3], facelocTest5[0]), (facelocTest5[1], facelocTest5[2]), (155, 0, 255), 2)

results5 = face_recognition.compare_faces([encodeModi5], encodeTest5)
faceDis5 = face_recognition.face_distance([encodeModi5], encodeTest5)
print(results5, faceDis5)
cv2.putText(imgTest5, f'{results5} {round(faceDis5[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

cv2.imshow('kavin', imgModi5)
cv2.imshow('kavin2', imgTest5)

imgModi6 = face_recognition.load_image_file('C:\\face3\\photos\\harini.jpg')
imgModi6 = cv2.cvtColor(imgModi6, cv2.COLOR_BGR2RGB)
imgTest6 = face_recognition.load_image_file('C:\\face3\\photos\\harini2.jpg')
imgTest6 = cv2.cvtColor(imgTest6, cv2.COLOR_BGR2RGB)

faceloc6 = face_recognition.face_locations(imgModi6)[0]
encodeModi6 = face_recognition.face_encodings(imgModi6)[0]
cv2.rectangle(imgModi6, (faceloc6[3], faceloc6[0]), (faceloc6[1], faceloc6[2]), (155, 0, 255), 2)

facelocTest6 = face_recognition.face_locations(imgTest6)[0]
encodeTest6= face_recognition.face_encodings(imgTest6)[0]
cv2.rectangle(imgTest6, (facelocTest6[3], facelocTest6[0]), (facelocTest6[1], facelocTest6[2]), (155, 0, 255), 2)

results6 = face_recognition.compare_faces([encodeModi6], encodeTest6)
faceDis6 = face_recognition.face_distance([encodeModi6], encodeTest6)
print(results6, faceDis6)
cv2.putText(imgTest6, f'{results6} {round(faceDis6[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

cv2.imshow('harini', imgModi6)
cv2.imshow('harini2', imgTest6)


cv2.waitKey(0)
