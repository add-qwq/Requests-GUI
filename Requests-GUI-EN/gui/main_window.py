from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QComboBox, QLineEdit, QTextEdit, QPushButton,
    QTabWidget, QLabel, QTableWidget, QTableWidgetItem
)
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QIcon
import sys
import os

class RequestWorker(QThread):
    finished = pyqtSignal(dict)

    def __init__(self, method, url, headers, params, data):
        super().__init__()
        self.method = method
        self.url = url
        self.headers = headers
        self.params = params
        self.data = data

    def run(self):
        import requests
        result = {}
        try:
            response = requests.request(
                method=self.method,
                url=self.url,
                headers=self.headers,
                params=self.params,
                data=self.data
            )
            result = {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "text": response.text,
                "error": None
            }
        except Exception as e:
            result["error"] = str(e)
        self.finished.emit(result)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Requests GUI Client")
        self.setGeometry(100, 100, 1000, 800)

        self.set_window_icon()
        
        self.init_ui()
        self.init_connections()

    def set_window_icon(self):
        if getattr(sys, 'frozen', False):
            icon_path = os.path.join(sys._MEIPASS, "gui.ico")
        else:
            icon_path = "gui.ico"

        self.setWindowIcon(QIcon(icon_path))

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        method_layout = QHBoxLayout()
        self.method_combo = QComboBox()
        self.method_combo.addItems(["GET", "POST", "PUT", "DELETE"])
        method_layout.addWidget(QLabel("Method:"))
        method_layout.addWidget(self.method_combo)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter URL (e.g., https://httpbin.org/get)")
        method_layout.addWidget(self.url_input)

        self.send_btn = QPushButton("Send Request")
        method_layout.addWidget(self.send_btn)

        headers_layout = QVBoxLayout()
        headers_layout.addWidget(QLabel("Headers (Key-value pairs, one per line)"))
        self.headers_table = QTableWidget(3, 2)
        self.headers_table.setHorizontalHeaderLabels(["Key", "Value"])
        headers_layout.addWidget(self.headers_table)

        self.tab_widget = QTabWidget()
        self.params_tab = QTextEdit()
        self.params_tab.setPlaceholderText("Enter query parameters (key=value&key=value, or JSON)")
        self.data_tab = QTextEdit()
        self.data_tab.setPlaceholderText("Enter request body (text or JSON)")
        self.tab_widget.addTab(self.params_tab, "Query Parameters")
        self.tab_widget.addTab(self.data_tab, "Request Body")

        response_layout = QVBoxLayout()
        self.status_label = QLabel("Status Code:")
        response_layout.addWidget(self.status_label)
        self.response_headers = QTextEdit()
        self.response_headers.setReadOnly(True)
        self.response_headers.setPlaceholderText("Response headers...") 
        response_layout.addWidget(QLabel("Response Headers:"))
        response_layout.addWidget(self.response_headers)
        self.response_content = QTextEdit()
        self.response_content.setReadOnly(True)
        self.response_content.setPlaceholderText("Response content...")
        response_layout.addWidget(QLabel("Response Content:"))
        response_layout.addWidget(self.response_content)

        main_layout.addLayout(method_layout)
        main_layout.addLayout(headers_layout)
        main_layout.addWidget(self.tab_widget)
        main_layout.addLayout(response_layout)

    def init_connections(self):
        self.send_btn.clicked.connect(self.send_request)

    def send_request(self):
        method = self.method_combo.currentText()
        url = self.url_input.text()
        headers = self._get_headers_from_table()
        params = self._parse_params(self.params_tab.toPlainText())
        data = self.data_tab.toPlainText()

        self.worker = RequestWorker(method, url, headers, params, data)
        self.worker.finished.connect(self.handle_response)
        self.worker.start()

    def _get_headers_from_table(self):
        headers = {}
        for row in range(self.headers_table.rowCount()):
            key_item = self.headers_table.item(row, 0)
            value_item = self.headers_table.item(row, 1)
            if key_item and value_item:
                headers[key_item.text()] = value_item.text()
        from requests.structures import CaseInsensitiveDict
        return CaseInsensitiveDict(headers)

    def _parse_params(self, text):
        if not text:
            return {}
        try:
            import json
            return json.loads(text)
        except:
            params = {}
            for pair in text.split("&"):
                if "=" in pair:
                    k, v = pair.split("=", 1)
                    params[k.strip()] = v.strip()
            return params

    def handle_response(self, result):
        if result.get("error"):
            self.status_label.setText(f"Status Code: Error - {result['error']}")
            self.response_headers.clear()
            self.response_content.setText(f"Error message: {result['error']}")
            return

        self.status_label.setText(f"Status Code: {result['status_code']}")
        headers_text = "\n".join([f"{k}: {v}" for k, v in result['headers'].items()])
        self.response_headers.setText(headers_text)
        content = result['text']
        try:
            import jsbeautifier
            content = jsbeautifier.beautify(content)
        except:
            pass
        self.response_content.setText(content)