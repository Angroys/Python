from PyQt5.QtWidgets import (
    QApplication,
    QPushButton, 
    QMainWindow, 
    QWidget, 
    QGridLayout, 
    QCheckBox, 
    QFormLayout, 
    QLineEdit,
    QVBoxLayout,
    QLabel
) 
import sys
from excel import AddingBook


class ReadAddWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Books that have been read")
        
        width = 450
        height = 300
        self.setMinimumHeight(height)
        self.setMinimumWidth(width)
        
        self.englishLng = QCheckBox("English")
        self.englishLng.checkState()

        self.romanianLng = QCheckBox("Romanian")
        self.romanianLng.checkState()
        
        self.russianLng = QCheckBox("Russian")
        self.russianLng.checkState()



        self.authorInput = QLineEdit()
        self.bookInput = QLineEdit()
        self.finishedDateInput = QLineEdit()
        self.startingDateInput = QLineEdit()
        self.descriptionInput = QLineEdit()
        self.linkToMediumInputBox = QLineEdit()

        topInputLayout = QFormLayout()
        topInputLayout.addRow("Book name: ", self.bookInput )
        topInputLayout.addRow("Author: ", self.authorInput)
        topInputLayout.addRow("Starting Date: ", self.startingDateInput)
        topInputLayout.addRow("Finished Layout: ", self.finishedDateInput)
        topInputLayout.addRow("Description: ", self.descriptionInput)
        topInputLayout.addRow("Link to Medium: ", self.linkToMediumInputBox)
        
        optionsLayout = QVBoxLayout()
        optionsLayout.addWidget(QLabel("Pick the language you've read the book"))
        optionsLayout.addWidget(self.romanianLng)
        optionsLayout.addWidget(self.englishLng)
        optionsLayout.addWidget(self.russianLng)

        self.buttonDetails = QPushButton("Save Details")
        self.buttonDetails.clicked.connect(self.inputToExcel)
        lowLayout = QFormLayout()
        lowLayout.addWidget(self.buttonDetails)
        # Nest the inner layouts into the outer layout


        mainLayout = QVBoxLayout()
        mainLayout.addLayout(topInputLayout)
        mainLayout.addLayout(optionsLayout)
        mainLayout.addLayout(lowLayout)
        self.setLayout(mainLayout)
        self.setMaximumWidth(width)
        self.setMaximumHeight(height)
#        if englishLng.isChecked():
#            print("Is checked")
    
    def inputToExcel(self):
        addBook = AddingBook()
        
        addBook.setBookName(self.bookInput.text())
        
        addBook.setAuthor(self.authorInput.text())

        addBook.setStartingDate(self.startingDateInput.text())

        addBook.setFinishedDate(self.finishedDateInput.text())
        
        addBook.setDescription(self.descriptionInput.text())
        
        addBook.setLinkToMedium(self.linkToMediumInputBox.text())

        if self.romanianLng.isChecked():
            self.language = "Romanian"
            addBook.setLanguage(self.language)
        elif self.englishLng.isChecked():
            self.language = "English"
            addBook.setLanguage(self.language)        
        elif self.russianLng.isChecked():
            self.language = "Russian"
            addBook.setLanguage(self.language)        
        
        
        saveToExcel = AddingBook()
        saveToExcel.insertRead()


class ToReadAddWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Books to read")
        width = 450
        height = 300
        
        
        self.setMinimumHeight(height)
        self.setMinimumWidth(width)
        
        
        self.englishLng = QCheckBox("English")
        self.englishLng.checkState()

        self.romanianLng = QCheckBox("Romanian")
        self.romanianLng.checkState()
        
        self.russianLng = QCheckBox("Russian")
        self.russianLng.checkState()



        self.authorInput = QLineEdit()
        self.bookInput = QLineEdit()

        topInputLayout = QFormLayout()
        topInputLayout.addRow("Book name: ", self.bookInput )
        topInputLayout.addRow("Author: ", self.authorInput)

        
        optionsLayout = QVBoxLayout()
        optionsLayout.addWidget(QLabel("Pick the language you will read the book, not obligatory: "))
        optionsLayout.addWidget(self.romanianLng)
        optionsLayout.addWidget(self.englishLng)
        optionsLayout.addWidget(self.russianLng)

        self.buttonDetails = QPushButton("Save Details")
        self.buttonDetails.clicked.connect(self.inputToExcel)
        lowLayout = QFormLayout()
        lowLayout.addWidget(self.buttonDetails)
        # Nest the inner layouts into the outer layout


        mainLayout = QVBoxLayout()
        mainLayout.addLayout(topInputLayout)
        mainLayout.addLayout(optionsLayout)
        mainLayout.addLayout(lowLayout)
        self.setLayout(mainLayout)
        self.setMaximumWidth(width)
        self.setMaximumHeight(height)
#        if englishLng.isChecked():
#            print("Is checked")
    
    def inputToExcel(self):
        addBook = AddingBook()
        
        self.book1 = self.bookInput.text()
        addBook.setBookName(self.book1)
        
        self.author = self.authorInput.text()
        addBook.setAuthor(self.author)

        if self.romanianLng.isChecked():
            self.language = "Romanian"
            addBook.setLanguage(self.language)
        elif self.englishLng.isChecked():
            self.language = "English"
            addBook.setLanguage(self.language)        
        elif self.russianLng.isChecked():
            self.language = "Russian"
            addBook.setLanguage(self.language)        
        

        saveToExcel = AddingBook()
        saveToExcel.insertToRead()
        








        
        
        


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        width = 300
        height = 400
        self.setMinimumHeight(height)
        self.setMinimumWidth(width)
        
        
        # Nest the inner layouts into the outer layout
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
                
        layout = QGridLayout()
        self.widget.setLayout(layout)
        

        
        self.btnRead = QPushButton("Add Book that you read")
        self.btnRead.clicked.connect(self.addBookBTN)

        self.btnToRead = QPushButton("Add book to read")    
        self.btnToRead.clicked.connect(self.addToRead)

        layout.addWidget(self.btnRead, 1, 1)
        layout.addWidget(self.btnToRead, 1, 2)



    def addBookBTN(self, checked):
        self.addBookWindow = ReadAddWindow()
        self.addBookWindow.show()
        self.close()

    def addToRead(self, checked):
        self.ToReadWindow = ToReadAddWindow()
        self.ToReadWindow.show()
        self.close()

    




        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())