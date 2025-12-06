import os
import sys
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTreeView, QLabel, QFrame
)
from PyQt6.QtGui import QFileSystemModel, QFont
from PyQt6.QtCore import QDir, pyqtSignal, QModelIndex


class FileExplorer(QWidget):
    """A simple file explorer widget."""
    file_selected = pyqtSignal(str)

    def __init__(self, path="."):
        super().__init__()
        self.current_path = path

        self.setMinimumWidth(250)
        self.setMaximumWidth(400)
        self.setStyleSheet("""
            QWidget {
                background-color: #001122;
                color: #00ffaa;
            }
            QTreeView {
                border: 1px solid #00ff41;
                background-color: #000011;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 5, 5, 0)
        
        self.tree_view = QTreeView()
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.currentPath())
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(QDir.currentPath()))
        self.tree_view.doubleClicked.connect(self.on_double_click)
        
        # Hide unnecessary columns
        self.tree_view.setColumnHidden(1, True)
        self.tree_view.setColumnHidden(2, True)
        self.tree_view.setColumnHidden(3, True)
        
        layout.addWidget(self.tree_view)
        
    def on_double_click(self, index: QModelIndex):
        path = self.model.filePath(index)
        if not self.model.isDir(index):
            self.file_selected.emit(path)