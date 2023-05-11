import YMOperator
from AOperator import Player
import time

player = Player(r'C:\test.mp3')

player.async_play()

time.sleep(5)

player.stop()

time.sleep(3)

player.play()

time.sleep(3)

# import os
# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QFileDialog, QVBoxLayout,
#                              QHBoxLayout, QPushButton, QLabel)
#
#
# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         # Создаем объект Player
#         self.player = None
#
#         # Создаем главное окно
#         self.setWindowTitle('Music Player')
#         self.setGeometry(100, 100, 400, 200)
#
#         # Создаем виджет
#         self.widget = QWidget(self)
#
#         # Создаем вертикальный макет для виджета
#         self.layout = QVBoxLayout(self.widget)
#
#         # Создаем метку для отображения текущего трека
#         self.current_track_label = QLabel('No track selected')
#         self.current_track_label.setAlignment(Qt.AlignCenter)
#         self.layout.addWidget(self.current_track_label)
#
#         # Создаем горизонтальный макет для кнопок
#         self.buttons_layout = QHBoxLayout()
#
#         # Создаем кнопку выбора трека
#         self.select_track_button = QPushButton('Select track', self)
#         self.select_track_button.clicked.connect(self.select_track)
#         self.buttons_layout.addWidget(self.select_track_button)
#
#         # Создаем кнопку запуска трека
#         self.play_button = QPushButton('Play', self)
#         self.play_button.clicked.connect(self.play)
#         self.buttons_layout.addWidget(self.play_button)
#
#         # Создаем кнопку остановки трека
#         self.stop_button = QPushButton('Stop', self)
#         self.stop_button.clicked.connect(self.stop)
#         self.buttons_layout.addWidget(self.stop_button)
#
#         # Добавляем горизонтальный макет для кнопок в вертикальный макет для виджета
#         self.layout.addLayout(self.buttons_layout)
#
#         # Устанавливаем виджет в качестве центрального виджета главного окна
#         self.setCentralWidget(self.widget)
#
#     def select_track(self):
#         # Открываем диалоговое окно выбора файла
#         file_path, _ = QFileDialog.getOpenFileName(self, 'Select file', '',
#                                                    'Audio files (*.mp3 *.wav)')
#
#         # Если файл выбран, создаем объект Player и отображаем имя выбранного файла на метке
#         if file_path:
#             self.player = Player(file_path)
#             self.current_track_label.setText(os.path.basename(file_path))
#
#     def play(self):
#         # Если объект Player создан, запускаем его
#         if self.player:
#             self.player.async_play()
#
#     def stop(self):
#         # Если объект Player создан, останавливаем его
#         if self.player:
#             self.player.stop()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
