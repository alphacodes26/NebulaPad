from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QStatusBar,
    QMessageBox,
    QFileDialog,
    QLabel,
    QPushButton,
)
from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6.QtCore import Qt
import sys
from pathlib import Path


# Resource paths
if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys._MEIPASS)
else:
    BASE_DIR = Path(__file__).resolve().parent / "NebulaPad"


ICONS_DIR = BASE_DIR / "icons"


class AboutWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("About NebulaPad")
        self.setWindowIcon(QIcon(str(ICONS_DIR / "NebulaPad.png")))
        self.setFixedSize(300, 350)

        # Software information
        software_name_label = QLabel("NebulaPad v0.1")

        software_details_label = QLabel(
            "A minimal and intuitive text editor designed to help "
            "you get your work done. \n\n"
            "Made in PySide6, applicable under the LGPL 3.0 License\n\n"
        )
        software_details_label.setWordWrap(True)

        # NebulaPad logo
        logo_label = QLabel()

        pixmap = QPixmap(str(ICONS_DIR / "NebulaPad.png"))

        scaled_pixmap = pixmap.scaled(
            64,
            64,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        logo_label.setPixmap(scaled_pixmap)

        # PySide6 logo
        pyside6_label = QLabel()

        pyside6_pixmap = QPixmap(
            str(ICONS_DIR / "pyside6.png")
        )

        pyside6_scaled = pyside6_pixmap.scaled(
            100,
            40,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        pyside6_label.setPixmap(pyside6_scaled)
        pyside6_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Technology logos layout
        logos_layout = QHBoxLayout()
        logos_layout.setSpacing(20)

        logos_layout.addWidget(pyside6_label)

        # Title font
        font = software_name_label.font()
        font.setPointSize(15)
        font.setBold(True)
        software_name_label.setFont(font)

        # Alignment
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        software_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        software_details_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pyside6_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Close button
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)

        # Layout
        central_widget = QWidget()
        layout = QVBoxLayout()

        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(8)

        self.setCentralWidget(central_widget)
        central_widget.setLayout(layout)

        layout.addWidget(logo_label)
        layout.addWidget(software_name_label)
        layout.addWidget(software_details_label)

        layout.addSpacing(5)

        layout.addWidget(pyside6_label)

        layout.addStretch()
        layout.addWidget(close_button)


class ThemeWindow(QMainWindow):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        self.setWindowTitle("Change Theme")
        self.setWindowIcon(QIcon(str(ICONS_DIR / "NebulaPad.png")))
        self.setFixedSize(300, 200)

        label = QLabel("Change Theme")

        font = label.font()
        font.setPointSize(15)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        dark_mode_btn = QPushButton("Enable Dark Mode")
        dark_mode_btn.clicked.connect(self.enable_dark_mode)

        light_mode_btn = QPushButton("Enable Light Mode")
        light_mode_btn.clicked.connect(self.enable_light_mode)

        layout = QVBoxLayout()

        layout.addWidget(label)

        layout.addWidget(
            dark_mode_btn,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )

        layout.addWidget(
            light_mode_btn,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def enable_dark_mode(self):
        self.main_window.set_theme(True)

    def enable_light_mode(self):
        self.main_window.set_theme(False)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon(str(ICONS_DIR / "NebulaPad.png")))

        self.current_file = None
        self.dark_mode = False

        # Window
        self.update_window_title()

        # Main widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.text_edit = QTextEdit()

        # Actions
        new_action = QAction(
            QIcon(str(ICONS_DIR / "document--plus.png")),
            "New",
            self
        )

        open_action = QAction(
            QIcon(str(ICONS_DIR / "folder-open.png")),
            "Open",
            self
        )

        save_action = QAction(
            QIcon(str(ICONS_DIR / "disk.png")),
            "Save",
            self
        )

        save_as_action = QAction(
            QIcon(str(ICONS_DIR / "document--pencil.png")),
            "Save As",
            self
        )

        quit_action = QAction(
            QIcon(str(ICONS_DIR / "door-open-out.png")),
            "Quit",
            self
        )

        theme_action = QAction(
            QIcon(str(ICONS_DIR / "weather-moon.png")),
            "Set Theme",
            self
        )

        about_action = QAction(
            QIcon(str(ICONS_DIR / "information-italic.png")),
            "About",
            self
        )

        # Shortcuts
        new_action.setShortcut("Ctrl+N")
        open_action.setShortcut("Ctrl+O")
        save_action.setShortcut("Ctrl+S")
        save_as_action.setShortcut("Ctrl+Shift+S")
        quit_action.setShortcut("Ctrl+W")
        theme_action.setShortcut("Ctrl+Alt+T")
        about_action.setShortcut("Ctrl+Alt+A")

        # Connections
        new_action.triggered.connect(self.new_file)
        open_action.triggered.connect(self.open_action)
        save_action.triggered.connect(self.save_action)
        save_as_action.triggered.connect(self.save_as_file)
        theme_action.triggered.connect(self.theme_switch)
        quit_action.triggered.connect(self.close)
        about_action.triggered.connect(self.about_window)

        # Menu bar
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")
        view_menu = menu_bar.addMenu("View")

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addAction(quit_action)

        view_menu.addAction(theme_action)
        view_menu.addAction(about_action)

        # Status bar
        self.status_bar = QStatusBar()
        self.status_bar.showMessage("Welcome to NebulaPad.")
        self.setStatusBar(self.status_bar)

        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.text_edit)

        central_widget.setLayout(layout)

        self.resize(600, 400)

        # Start in light mode
        self.set_theme(False)

    def update_window_title(self):
        if self.current_file:
            file_name = Path(self.current_file).name
            self.setWindowTitle(f"{file_name} - NebulaPad")
        else:
            self.setWindowTitle("Untitled - NebulaPad")

    def new_file(self):
        if self.text_edit.document().isModified():
            msg = QMessageBox.warning(
                self,
                "New File Warning",
                "You have unsaved changes. Creating a new file will discard them. Continue?",
                QMessageBox.StandardButton.Ok |
                QMessageBox.StandardButton.Cancel
            )

            if msg != QMessageBox.StandardButton.Ok:
                return

        self.text_edit.clear()
        self.text_edit.document().setModified(False)

        self.current_file = None
        self.update_window_title()

        self.status_bar.showMessage("New File Created")

    def open_action(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "Text Files (*.txt);;All Files (*)"
        )

        if not file_path:
            return

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                self.text_edit.setPlainText(file.read())

            self.current_file = file_path
            self.text_edit.document().setModified(False)
            self.update_window_title()

            self.status_bar.showMessage(
                f"Opened file {file_path}"
            )

        except Exception as error:
            QMessageBox.critical(
                self,
                "File Open Error",
                f"An unexpected error occurred while opening the file:\n\n{error}"
            )

    def save_action(self):
        if self.current_file:
            if self.save_file(self.current_file):
                self.status_bar.showMessage("File saved.")
        else:
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "Save File",
                "",
                "Text Files (*.txt);;All Files (*)"
            )

            if file_path:
                if self.save_file(file_path):
                    self.status_bar.showMessage("File saved.")

    def save_file(self, file_path):
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.text_edit.toPlainText())

            self.current_file = file_path
            self.text_edit.document().setModified(False)
            self.update_window_title()

            return True

        except Exception as error:
            QMessageBox.critical(
                self,
                "File Save Error",
                f"An unexpected error occurred while saving the file:\n\n{error}"
            )

            return False

    def save_as_file(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            "",
            "Text Files (*.txt);;All Files (*)"
        )

        if not file_path:
            return

        if self.save_file(file_path):
            self.status_bar.showMessage(
                f"File saved as {file_path}"
            )

    def theme_switch(self):
        self.status_bar.showMessage("Changing Theme...")

        self.theme_window = ThemeWindow(self)
        self.theme_window.show()

    def set_theme(self, dark):
        self.dark_mode = dark

        if self.dark_mode:
            self.setStyleSheet("""
                QWidget {
                    background: #202020;
                    color: white;
                }

                QTextEdit {
                    background: #151515;
                    color: white;
                    border: 1px solid #444;
                    padding: 5px;
                }
            """)

            self.status_bar.showMessage("Dark Mode enabled.")

        else:
            self.setStyleSheet("""
                QWidget {
                    background: #f5f5f5;
                    color: black;
                }

                QTextEdit {
                    background: white;
                    color: black;
                    border: 1px solid #bbb;
                    padding: 5px;
                }
            """)

            self.status_bar.showMessage("Light Mode enabled.")

    def about_window(self):
        self.about_win = AboutWindow()
        self.about_win.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()