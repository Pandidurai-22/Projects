#coding : utf - 8
#Form implementation generated from reading ui file ' D : \ opencv \ ui \ Gujarathi lang_recognition \ demo2.ui '
#4
#Created by : PyQts UI code generator 5.11.3
#1
# WARNING ! All changes made in this file will be lost !
from PyQt5 import QtCore , QtGui , QtWidgets
import numpy as np
from keras.preprocessing import image # 1 . preprocessing an image
from keras.layers import Dense
from keras.models import model from json
from keras.models import Sequential # 4 . adding layers in a sequential order
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import BatchNormalization
from keras.layers import Dropout
class Ui_MainWindow ( object ) :
def setupli ( self , Mainwindow ) :
MainWindow.setObject Name ( " MainWindow " )
MainWindow.resize ( 800 , 600 )
self.centralwidgetQtWidgets.QWidget ( MainWindow )
self.centralwidget.setObjectName ( " centralwidget " )
self . Browse Image = QtWidgets.QPushButton ( self.centralwidget )
self.BrowseImage.setGeometry ( QtCore.QRect ( 160 , 370 , 151 , 51 ) )
self.BrowseImage.setObjectName ( " Browse Image " )
self.imagelbl = OtWidgets.Olabel ( self.centralwidget )
self.imagelbl.setGeometry ( QtCore.QRect ( 200 , 80 , 361 , 261 ) )
self.imageLbl.setFrame Shape ( QtWidgets.QFrame.Box )
self.imagelbl.setText ( " " )
self.imageLbl.setObjectName ( " imageLb1 " )
self.label 2 QtWidgets.QLabel ( self.centralwidget )
self.label 2.set Geometry ( QtCore.QRect ( 110 , 20 , 621 , 20 ) )
fontQtGui.QFont ( )
font.setFamily ( " Courier New " )
font.setPointSize ( 14 )
font.setBold ( True )
font.setWeight ( 75 )
self.label 2.setFont ( font )
self.label_2.setObject Name ( " label_2 " )
self.Classify QtWidgets.QPushButton ( self.centralwidget )
self.classify.setGeometry ( QtCore.QRect ( 160 , 450 , 151 , 51 ) )
self.Classify.setObjectName ( " Classify " )
self.label = QtWidgets.Qlabel ( self.centralwidget )
self.label.set Geometry ( QtCore.QRect ( 430 , 370 , 111 , 16 ) )
self.label.setObject Name ( " label " )
self . Training = QtWidgets.QPushButton ( self.centralwidget )
self.Training set Geometry ( Ot.Core.ORect ( 400 , 450 , 151 , 51 ) ) .
self.Training.setObjectName ( " Training " )
self.textEdit QtWidgets.QTextEdit ( self.centralwidget )
self.textEdit.setGeometry ( QtCore.QRect ( 400 , 390 , 211 , 51 ) )
self.textEdit.setObjectName ( " textEdit " )
MainWindow.setCentralWidget ( self.centralwidget )
self.menubar QtWidgets.QMenuBar ( MainWindow )
self.menubar.setGeometry ( QtCore.QRect ( 0 , 0 , 800 , 26 ) )
self.menubar.setObjectName ( " menubar " )
MainWindow.setMenuBar ( self.menubar )
self.statusbar = QtWidgets.QStatusBar ( MainWindow )
self.statusbar.setObjectName ( " statusbar " )
MainWindow.setStatusBar ( self.statusbar )

self.retranslateUi ( MainWindow )
QtCore.QMetaObject.connectSlotsByName ( MainWindow )

self.BrowseImage.clicked.connect ( self.loadImage )

self.classify.clicked.connect ( self.classifyFunction )

self . Training.clicked.connect ( self.trainingFunction ) 

def retranslateUi ( self , MainWindow ) :
translate QtCore.QCoreApplication.translate
MainWindow.setWindowTitle ( _translate ( " MainWindow " , " MainWindow " ) )
self.Browse Image.setText ( translate ( " MainWindow " , " Browse Image " ) )
self.label 2.setText ( _translate ( " MainWindow " , " GUJARATI CHARACTER RECOGNITION USING CNN " ) )
self.classify.setText ( _translate ( " MainWindow " , " Classify " ) )
self.label.setText ( _translate ( " MainWindow " , " Recognized Clasa " ) )
self.Training.setText ( _translate ( " MainWindow " , " Training " ) )

def loadImage ( self ) :
fileName , ■ QtWidgets.QFileDialog.getOpenFileName ( None , " Select Image " ,
" Image Files ( * .png * .jpg |)
file Name , 
= QtWidgets.QFileDialog.getOpenFileName ( None , " Select Image " ,
if fileName : If the user gives a file
print ( fileName )
self.file - fileName
pixmap = QtGui.QPixmap ( fileName ) Setup pixmap with the provided image
pixmap = pixmap.scaled ( self.imageLbl.width ( ) , self.imagelbl.height ( ) , QtCore.Qt . KeepAspect Ratio ) Scale pixmap
self.imagelbl.setPixmap ( pixmap ) Set the pixmap onto the label
self.imageLbl.setAlignment ( QtCore.Qt.AlignCenter ) Align the label to center
json_file open ( ' model.json ' , ' r ' )
loaded_model_json = json_file.read ( )


 def classifyFunction ( self ) :
 json_file open ( ' model.json ' , ' I ' )
loaded_model_json = json_file.read ( )
json_file.close ( )
loaded_model = model_from_json ( loaded_model_json )
load weights into new model
loaded_model.load_weights ( " model.h5 " )
print ( " Loaded model from disk " ) ;
label - [ " sunna " , " ek " , " das " , " be " , " tran " , " char " , " panc " , " cha " , " sat "
" nav " , " ALA " , " ANA " , " B " , " BHA "]
#label = [ " fifty " , " fivehundred " , " hundred " , " ten " , " twenty " , " twohundred " ]
path2 = self.file
print ( path2 )
test_image = image.load_img ( path2 , target_size = ( 128 , 128 ) )
test_image image . img_to_array ( test_image )
test image = np.expand_dims ( test_image , axis = 0 )
result = loaded_model.predict ( test_image )

fresult np.max ( result )
label2 = label [ result.argmax () ]
print(label2)
self.textEdit.setText(label2)

def trainingFunction ( self ) :
self.textEdit.setText ( " Training under process ... " )
#basic cnn
model = Sequential ()
model.add ( Conv2D ( 32 , kernel_size = ( 3 , 3 ) , activation = ' relu ' ,
model.add ( MaxPooling2D ( pool_size = ( 2 , 2 ) ) )
model.add ( BatchNormalization())
model.add ( Conv2D ( 64 , kernel_size = ( 3 , 3 ) , activation = ' relu ' ) )
model.add ( MaxPooling2D ( pool_size = ( 2 , 2 ) ) )
model.add ( BatchNormalization ( ) )
model.add ( Conv2D ( 64 , kernel_size = ( 3 , 3 ) , activation = ' relu ' ) )
model.add ( MaxPooling2D ( pool_size = ( 2 , 2 ) ) )
model.add ( BatchNormalization ( ) )
model.add(Conv2D / 96 . kernel size = ( 3.3 ) . activation = 'relu'))
model.add ( MaxPooling2D ( pool_size = ( 2 , 2 ) ) )
model.add ( BatchNormalization ( ) )
model.add ( Conv2D ( 32 , kernel_size = ( 3 , 3 ) , activation = ' relu ' ) )
model.add ( MaxPooling2D ( pool_size = ( 2 , 2 ) ) )
model.add ( BatchNormalization ( ) )
model.add ( Dropout ( 0.2 ) )
model.add ( Flatten ( ) )
model.add ( Dense ( 128 , activation = ' relu ' ) )
model.add ( Dropout ( 0.5 ) )
model.add(Dense(45, activation = ' softmax ' ) )

model.compile(optimizer = 'adam', loss = 'catgorical_crossentropy',metrics =

train_datagen = ImageDataGenerator(rescale = None,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
                                   
                                   
test_datagen = Image DataGenerator ( rescale = 1./255 )
training set = train_datagen.flow_from_directory ( ' D :
/ MasterClass / Artificial_Intelligence)
target_size = ( 128 , 128 ) ,
batch_size = 8 ,
class_mode = ' categorical ' ) i


#print ( test_datagen ) ;
labels ( training_set.class_indices )
print ( labels )

test_set = test_datagen.flow_from_directory ( ' D : / MasterClass / Artificial_Intelligence
targetarget_size = ( 128,128),
batchbatch_size = 8 ,
class_mode = 'categorical')

labels2 = ( test_set.class_indices )
print ( labels2 )
# self.textEdit.setText ( labels2 )
model.fit_generator ( training_set ,
steps_per_epoch = 100 ,
epochs - 10 ,
validation data = test_set
validation stens = 125 )

if
#Part 3 Making new predictions
model_json - model.to_json()
with open ( " model.json " , " w " ) as json_file :
json_file.write ( model_json )
# serialīze weights to HDF5
model.save_weights ( " model.h5 " )
print ( " Saved model to disk " )
self.textEdit.setText ( " Saved model to disk " )

if name = " __main__ ":
import sys
app QtWidgets.QApplication ( sys.argv )
MainWindow = QtWidgets.QMainWindow ()
ui = Ui_MainWindow ( )
ui.setupUi ( MainWindow )
MainWindow.show ( )
sys.exit ( app.exec_())
