import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PIL import Image

class ImageResizer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Resizer')
        self.setGeometry(300, 300, 400, 200)
        self.setStyleSheet("background-color: #2b2b2b; color: #ffffff;")

        layout = QVBoxLayout()

        # File selection - select your image
        file_layout = QHBoxLayout()
        self.file_path = QLineEdit(self)
        self.file_path.setStyleSheet("background-color: #3c3f41; border: 1px solid #646464;")
        file_button = QPushButton('Choose Image', self)
        file_button.clicked.connect(self.choose_file)
        file_button.setStyleSheet("background-color: #365880; border: none;")
        file_layout.addWidget(self.file_path)
        file_layout.addWidget(file_button)
        layout.addLayout(file_layout)

        # Width and Height inputs
        size_layout = QHBoxLayout()
        self.width_input = QLineEdit(self)
        self.width_input.setPlaceholderText('Width')
        self.height_input = QLineEdit(self)
        self.height_input.setPlaceholderText('Height')
        self.width_input.setStyleSheet("background-color: #3c3f41; border: 1px solid #646464;")
        self.height_input.setStyleSheet("background-color: #3c3f41; border: 1px solid #646464;")
        size_layout.addWidget(self.width_input)
        size_layout.addWidget(self.height_input)
        layout.addLayout(size_layout)

        # Resize button
        resize_button = QPushButton('Resize and Save', self)
        resize_button.clicked.connect(self.resize_image)
        resize_button.setStyleSheet("background-color: #365880; border: none;")
        layout.addWidget(resize_button)

        self.setLayout(layout)

    def choose_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Choose Image", "", "Image Files (*.png *.jpg *.bmp *.jpeg *.gif)")
        if file_name:
            self.file_path.setText(file_name)

    def resize_image(self):
        input_path = self.file_path.text()
        width = int(self.width_input.text())
        height = int(self.height_input.text())

        if input_path and width and height:
            try:
                img = Image.open(input_path)
                resized_img = img.resize((width, height), Image.LANCZOS)

                save_path, _ = QFileDialog.getSaveFileName(self, "Save Resized Image", "", "PNG (*.png);;JPEG (*.jpg *.jpeg);;BMP (*.bmp)")
                
                if save_path:
                    resized_img.save(save_path)
                    self.show_message("Image resized and saved successfully!")
                else:
                    self.show_message("Save operation cancelled.")
            except Exception as e:
                self.show_message(f"Error: {str(e)}")
        else:
            self.show_message("Please fill in all fields.")

    def show_message(self, message):
        msg = QLabel(message, self)
        msg.setStyleSheet("color: #ffffff; background-color: #4a4a4a; padding: 10px;")
        msg.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(msg)
        msg.show()
        QApplication.processEvents()
        msg.deleteLater()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageResizer()
    ex.show()
    sys.exit(app.exec_())
