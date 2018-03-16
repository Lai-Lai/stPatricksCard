def drawing():
  newPic = makePicture(pickAFile())
  newPic.addArcFilled(white, 158, 53, 15, 15, 0, 360)
  newPic.addArcFilled(white, 151, 65, 30, 30, 0, 360)
  newPic.addArcFilled(white, 145, 90, 45, 45, 0, 360) 
  newPic.addText(white, 25, 80, "Where is the snow?!")  
  show(newPic)
