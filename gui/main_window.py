# 主窗口界面（支持多语言）
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QComboBox, QLineEdit, QTextEdit, QPushButton,
    QTabWidget, QLabel, QTableWidget, QTableWidgetItem
)
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QIcon
import sys
import os

class RequestWorker(QThread):
    # 与原代码一致，无变化
    finished = Signal(dict)

    def __init__(self, method, url, headers, params, data):
        super().__init__()
        self.method = method
        self.url = url
        self.headers = headers
        self.params = params
        self.data = data

    def run(self):
        # 与原代码一致，无变化
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
        # 初始化语言配置（默认中文）
        self.current_lang = "zh"  # 可选 "zh" 或 "en"
        self.lang_dict = self._load_language_dict()  # 加载多语言字典
        
        self.setWindowTitle(self.lang_dict[self.current_lang]["window_title"])
        self.setGeometry(100, 100, 1000, 800)
        
        self.set_window_icon()
        self.init_ui()
        self.init_connections()

    def _load_language_dict(self):
        # 定义中英文文本映射
        return {
            "zh": {
                "window_title": "Requests GUI 客户端",
                "method_label": "方法:",
                "send_btn": "发送请求",
                "url_placeholder": "输入 URL（如 https://httpbin.org/get）",
                "headers_label": "Headers (键值对，每行一个)",
                "headers_key": "键",
                "headers_value": "值",
                "params_tab": "查询参数",
                "params_placeholder": "输入查询参数（键=值&键=值，或 JSON）",
                "data_tab": "请求体",
                "data_placeholder": "输入请求体（文本或 JSON）",
                "response_status": "状态码：",
                "response_headers_label": "响应头：",
                "response_headers_placeholder": "响应头...",
                "response_content_label": "响应内容：",
                "response_content_placeholder": "响应内容...",
                "error_status": "状态码：错误 - ",
                "error_content": "错误信息：",
                "switch_btn": "Switch Language"
            },
            "en": {
                "window_title": "Requests GUI Client",
                "method_label": "Method:",
                "send_btn": "Send Request",
                "url_placeholder": "Enter URL (e.g., https://httpbin.org/get)",
                "headers_label": "Headers (Key-Value pairs, one per line)",
                "headers_key": "Key",
                "headers_value": "Value",
                "params_tab": "Query Parameters",
                "params_placeholder": "Enter query parameters (key=value&key=value, or JSON)",
                "data_tab": "Request Body",
                "data_placeholder": "Enter request body (text or JSON)",
                "response_status": "Status Code:",
                "response_headers_label": "Response Headers:",
                "response_headers_placeholder": "Response headers...",
                "response_content_label": "Response Content:",
                "response_content_placeholder": "Response content...",
                "error_status": "Status Code: Error - ",
                "error_content": "Error message:",
                "switch_btn": "切换语言"
            }
        }

    def set_window_icon(self):
        # 与原代码一致，无变化
        if getattr(sys, 'frozen', False):
            icon_path = os.path.join(sys._MEIPASS, "gui.ico")
        else:
            icon_path = "gui.ico"
        self.setWindowIcon(QIcon(icon_path))

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # 方法选择布局（动态文本）
        method_layout = QHBoxLayout()
        method_layout.addWidget(QLabel(self.lang_dict[self.current_lang]["method_label"]))
        
        self.method_combo = QComboBox()
        self.method_combo.addItems(["GET", "POST", "PUT", "DELETE"])
        method_layout.addWidget(self.method_combo)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText(self.lang_dict[self.current_lang]["url_placeholder"])
        method_layout.addWidget(self.url_input)

        self.send_btn = QPushButton(self.lang_dict[self.current_lang]["send_btn"])
        method_layout.addWidget(self.send_btn)

        # 语言切换按钮
        self.lang_switch_btn = QPushButton(self.lang_dict[self.current_lang]["switch_btn"])
        method_layout.addWidget(self.lang_switch_btn)

        # Headers布局（动态文本）
        headers_layout = QVBoxLayout()
        headers_layout.addWidget(QLabel(self.lang_dict[self.current_lang]["headers_label"]))
        
        self.headers_table = QTableWidget(3, 2)
        self.headers_table.setHorizontalHeaderLabels([
            self.lang_dict[self.current_lang]["headers_key"],
            self.lang_dict[self.current_lang]["headers_value"]
        ])
        headers_layout.addWidget(self.headers_table)

        # 标签页（动态文本）
        self.tab_widget = QTabWidget()
        self.params_tab = QTextEdit()
        self.params_tab.setPlaceholderText(self.lang_dict[self.current_lang]["params_placeholder"])
        self.data_tab = QTextEdit()
        self.data_tab.setPlaceholderText(self.lang_dict[self.current_lang]["data_placeholder"])
        self.tab_widget.addTab(self.params_tab, self.lang_dict[self.current_lang]["params_tab"])
        self.tab_widget.addTab(self.data_tab, self.lang_dict[self.current_lang]["data_tab"])

        # 响应布局（动态文本）
        response_layout = QVBoxLayout()
        self.status_label = QLabel(self.lang_dict[self.current_lang]["response_status"])
        response_layout.addWidget(self.status_label)
        
        self.response_headers = QTextEdit()
        self.response_headers.setReadOnly(True)
        self.response_headers.setPlaceholderText(self.lang_dict[self.current_lang]["response_headers_placeholder"])
        response_layout.addWidget(QLabel(self.lang_dict[self.current_lang]["response_headers_label"]))
        response_layout.addWidget(self.response_headers)
        
        self.response_content = QTextEdit()
        self.response_content.setReadOnly(True)
        self.response_content.setPlaceholderText(self.lang_dict[self.current_lang]["response_content_placeholder"])
        response_layout.addWidget(QLabel(self.lang_dict[self.current_lang]["response_content_label"]))
        response_layout.addWidget(self.response_content)

        main_layout.addLayout(method_layout)
        main_layout.addLayout(headers_layout)
        main_layout.addWidget(self.tab_widget)
        main_layout.addLayout(response_layout)

    def init_connections(self):
        self.send_btn.clicked.connect(self.send_request)
        self.lang_switch_btn.clicked.connect(self.switch_language)  # 绑定语言切换事件

    def switch_language(self):
        # 切换语言（中<->英）
        self.current_lang = "en" if self.current_lang == "zh" else "zh"
        # 更新所有UI文本
        self._update_ui_text()

    def _update_ui_text(self):
        # 更新窗口标题
        self.setWindowTitle(self.lang_dict[self.current_lang]["window_title"])
        # 更新方法标签
        for widget in self.findChildren(QLabel):
            if widget.text() in [self.lang_dict["zh"]["method_label"], self.lang_dict["en"]["method_label"]]:
                widget.setText(self.lang_dict[self.current_lang]["method_label"])
        # 更新发送按钮
        self.send_btn.setText(self.lang_dict[self.current_lang]["send_btn"])
        # 更新URL输入占位符
        self.url_input.setPlaceholderText(self.lang_dict[self.current_lang]["url_placeholder"])
        # 更新Headers标签
        for widget in self.findChildren(QLabel):
            if widget.text() in [self.lang_dict["zh"]["headers_label"], self.lang_dict["en"]["headers_label"]]:
                widget.setText(self.lang_dict[self.current_lang]["headers_label"])
        # 更新Headers表格列标题
        self.headers_table.setHorizontalHeaderLabels([
            self.lang_dict[self.current_lang]["headers_key"],
            self.lang_dict[self.current_lang]["headers_value"]
        ])
        # 更新标签页标题
        self.tab_widget.setTabText(0, self.lang_dict[self.current_lang]["params_tab"])
        self.tab_widget.setTabText(1, self.lang_dict[self.current_lang]["data_tab"])
        # 更新参数和请求体占位符
        self.params_tab.setPlaceholderText(self.lang_dict[self.current_lang]["params_placeholder"])
        self.data_tab.setPlaceholderText(self.lang_dict[self.current_lang]["data_placeholder"])
        # 更新响应状态标签
        self.status_label.setText(self.lang_dict[self.current_lang]["response_status"])
        # 更新响应头标签
        for widget in self.findChildren(QLabel):
            if widget.text() in [self.lang_dict["zh"]["response_headers_label"], self.lang_dict["en"]["response_headers_label"]]:
                widget.setText(self.lang_dict[self.current_lang]["response_headers_label"])
        # 更新响应头占位符
        self.response_headers.setPlaceholderText(self.lang_dict[self.current_lang]["response_headers_placeholder"])
        # 更新响应内容标签
        for widget in self.findChildren(QLabel):
            if widget.text() in [self.lang_dict["zh"]["response_content_label"], self.lang_dict["en"]["response_content_label"]]:
                widget.setText(self.lang_dict[self.current_lang]["response_content_label"])
        # 更新响应内容占位符
        self.response_content.setPlaceholderText(self.lang_dict[self.current_lang]["response_content_placeholder"])
        # 更新切换按钮文本
        self.lang_switch_btn.setText(self.lang_dict[self.current_lang]["switch_btn"])

    def send_request(self):
        # 与原代码一致，无变化
        method = self.method_combo.currentText()
        url = self.url_input.text()
        headers = self._get_headers_from_table()
        params = self._parse_params(self.params_tab.toPlainText())
        data = self.data_tab.toPlainText()

        self.worker = RequestWorker(method, url, headers, params, data)
        self.worker.finished.connect(self.handle_response)
        self.worker.start()

    def _get_headers_from_table(self):
        # 与原代码一致，无变化
        headers = {}
        for row in range(self.headers_table.rowCount()):
            key_item = self.headers_table.item(row, 0)
            value_item = self.headers_table.item(row, 1)
            if key_item and value_item:
                headers[key_item.text()] = value_item.text()
        from requests.structures import CaseInsensitiveDict
        return CaseInsensitiveDict(headers)

    def _parse_params(self, text):
        # 与原代码一致，无变化
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
        # 动态错误提示文本
        if result.get("error"):
            self.status_label.setText(f"{self.lang_dict[self.current_lang]['error_status']}{result['error']}")
            self.response_headers.clear()
            self.response_content.setText(f"{self.lang_dict[self.current_lang]['error_content']}{result['error']}")
            return

        # 动态状态码文本
        self.status_label.setText(f"{self.lang_dict[self.current_lang]['response_status']}{result['status_code']}")
        headers_text = "\n".join([f"{k}: {v}" for k, v in result['headers'].items()])
        self.response_headers.setText(headers_text)
        
        content = result['text']
        try:
            import jsbeautifier
            content = jsbeautifier.beautify(content)
        except:
            pass
        self.response_content.setText(content)