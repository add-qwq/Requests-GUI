# English:
# Requests-GUI - Unofficial GUI Client for Requests  

![GitHub release (latest by date)](https://img.shields.io/github/v/release/add-qwq/Requests-GUI?style=flat-square)  
![GitHub stars](https://img.shields.io/github/stars/add-qwq/Requests-GUI?style=flat-square)  
![Python version](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)  
![License](https://img.shields.io/github/license/add-qwq/Requests-GUI?style=flat-square)  

**Unofficial community-maintained** GUI client for the popular Python HTTP library [Requests](https://github.com/psf/requests). Convert complex command-line HTTP requests into an intuitive visual interface, supporting common methods like GET/POST/PUT/DELETE, and featuring bilingual (Chinese/English) versions.  


## 🌟 Key Features  
- **Multi-Method Support**: Switch between GET/POST/PUT/DELETE via a dropdown menu.  
- **Flexible Input**:  
  - **Query Parameters**: Accepts both key-value pairs (`key=value&key=value`) and JSON format.  
  - **Request Body**: Supports raw text or JSON input.  
- **Smart Headers**: Edit headers in a table (Key-Value pairs), auto-converted to Requests' `CaseInsensitiveDict`.  
- **Response Visualization**: Displays status codes, formatted headers, and beautified response content (JSON/HTML auto-formatting via `jsbeautifier`).  
- **Async Requests**: Uses PyQt's `QThread` to prevent UI freezing during network calls.  
- **Bilingual Support**: Two separate code folders:  
  - `Requests-GUI-EN`: English interface.  
  - `Requests-GUI-CN`: Simplified Chinese interface.  


## 🚀 Quick Start

### Option 1: Download Prebuilt EXE (Recommended)
No Python or dependencies required:
1. Go to [Releases page](https://github.com/add-qwq/Requests-GUI/releases).
2. Download `Requests-GUI-EXE.zip` and extract it.
3. After extraction, you will see: `Requests-GUI-EN.exe` (English) or `Requests-GUI-CN.exe` (Chinese).
4. Select one version and double-click to run.


### Option 2: Run from Source Code  
For developers or custom needs:  

#### Prerequisites  
- Python 3.8+  
- Required packages:  
  ```bash  
  pip install pyside6 requests jsbeautifier  
  ```  

#### Steps  
1. Download the source code:  
   - Click `Code → Download ZIP` on the [GitHub repo](https://github.com/add-qwq/Requests-GUI) (no Git needed).  
   - Extract the ZIP file.  

2. Run the program (choose Chinese or English version):
   - **English version**:
     ```bash
     cd Requests-GUI/Requests-GUI-EN
     python main.py
     ```
   - **Chinese version**:
     ```bash
     cd Requests-GUI/Requests-GUI-CN
     python main.py
     ```
   - Of course, you can also directly double-click main.py to run.


## 📦 Package into EXE (Custom Build)  
Use `pyinstaller` to create a standalone EXE (install via `pip install pyinstaller` first).  

### Example Command (Chinese Version):  
```bash  
# Navigate to the Chinese source folder  
cd Requests-GUI/Requests-GUI-CN  

# Package (Windows)  
pyinstaller -w -F -i gui.ico --add-data "gui.ico;." main.py  

# Parameters:  
# -w: Hide console window (for GUI apps).  
# -F: Generate a single EXE file.  
# -i gui.ico: Set window icon.  
# --add-data "gui.ico;.": Include the icon file in the EXE (Windows uses `;`).  
```  

**Note for macOS/Linux**: Replace `;` with `:` in `--add-data` (e.g., `--add-data "gui.ico:."`).  


## 🖥 Interface Overview  
![English Interface](https://github.com/add-qwq/Requests-GUI/blob/main/GUI-EN.png?raw=true)  
*(Click to view full-size. The Chinese version has identical functionality with translated labels.)*  


## 📘 Usage Examples  

### Example 1: Sending a GET Request with Query Parameters  
**Goal**: Send a GET request to `https://httpbin.org/get` with parameters `name=John&age=30`.  

**Steps**:  
1. Select `GET` from the method dropdown.  
2. Enter `https://httpbin.org/get` in the URL field.  
3. Go to the **Query Parameters** tab and enter `name=John&age=30` (or JSON `{"name": "John", "age": 30}`).  
4. (Optional) Add a header: `User-Agent: Requests-GUI-EN` in the Headers table.  
5. Click **Send Request**.  

**Expected Response**:  
- Status code: `200 OK`.  
- Response content will show `args` with the parameters:  
  ```json  
  {  
    "age": "30",  
    "name": "John"  
  }  
  ```  


### Example 2: Sending a POST Request with Form Data  
**Goal**: Submit form data `username=admin&password=secret` to `https://httpbin.org/post`.  

**Steps**:  
1. Select `POST` from the method dropdown.  
2. Enter `https://httpbin.org/post` in the URL field.  
3. Go to the **Request Body** tab and enter `username=admin&password=secret`.  
4. Add a header: `Content-Type: application/x-www-form-urlencoded`.  
5. Click **Send Request**.  

**Expected Response**:  
- Status code: `200 OK`.  
- Response content will show `form` with the submitted data:  
  ```json  
  {  
    "password": "secret",  
    "username": "admin"  
  }  
  ```  


### Example 3: Sending a POST Request with JSON Data  
**Goal**: Send JSON `{"email": "user@example.com", "active": true}` to `https://httpbin.org/post`.  

**Steps**:  
1. Select `POST` from the method dropdown.  
2. Enter `https://httpbin.org/post` in the URL field.  
3. Go to the **Request Body** tab and enter:  
   ```json  
   {"email": "user@example.com", "active": true}  
   ```  
4. Add a header: `Content-Type: application/json`.  
5. Click **Send Request**.  

**Expected Response**:  
- Status code: `200 OK`.  
- Response content will show `json` with the submitted data (auto-beautified).  


### Example 4: Handling Request Errors  
**Goal**: Test error handling with an invalid URL.  

**Steps**:  
1. Select any method (e.g., `GET`).  
2. Enter `https://invalid-domain.com` in the URL field.  
3. Click **Send Request**.  

**Expected Response**:  
- Status code will show an error (e.g., `ConnectionError`).  
- Response content will display the detailed error message (e.g., "Could not resolve host").  


## 📜 License  
This project is licensed under the [Apache License 2.0](https://github.com/add-qwq/Requests-GUI/blob/main/Requests-GUI-CN/LICENSE).  


## 🙋 Contributing & Feedback  
- **Bug Reports/Feature Requests**: Submit an [Issue](https://github.com/add-qwq/Requests-GUI/issues).  
- **Code Contributions**: Fork the repo, make changes, and submit a PR.  
- **Localization**: Add new languages by translating the UI text in `main_window.py`.  


---


# 中文：
# Requests-GUI - Requests 的非官方图形化客户端  

![GitHub release (latest by date)](https://img.shields.io/github/v/release/add-qwq/Requests-GUI?style=flat-square)  
![GitHub stars](https://img.shields.io/github/stars/add-qwq/Requests-GUI?style=flat-square)  
![Python version](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)  
![License](https://img.shields.io/github/license/add-qwq/Requests-GUI?style=flat-square)  

**非官方社区维护**的 Python HTTP 库 [Requests](https://github.com/psf/requests) 图形化客户端。将复杂的命令行 HTTP 请求转换为直观的可视化界面，支持 GET/POST/PUT/DELETE 等常用方法，并提供中英双语版本。  


## 🌟 核心功能  
- **多方法支持**：通过下拉菜单切换 GET/POST/PUT/DELETE。  
- **灵活输入**：  
  - **查询参数**：支持键值对（`key=value&key=value`）或 JSON 格式。  
  - **请求体**：支持纯文本或 JSON 输入。  
- **智能请求头**：通过表格编辑请求头（键值对），自动转换为 Requests 的 `CaseInsensitiveDict`（键不区分大小写）。  
- **响应可视化**：显示状态码、格式化响应头，并通过 `jsbeautifier` 自动美化 JSON/HTML 响应内容。  
- **异步请求**：使用 PyQt 的 `QThread` 实现异步发送，避免界面卡顿。  
- **双语支持**：两个独立代码文件夹：  
  - `Requests-GUI-EN`：英文界面。  
  - `Requests-GUI-CN`：简体中文界面。  


## 🚀 快速开始  

### 方式 1：下载预打包 EXE（推荐）  
无需安装 Python 或依赖：  
1. 前往 [Releases 页面](https://github.com/add-qwq/Requests-GUI/releases)
2. 下载 `Requests-GUI-EXE.zip` 并解压
3. 解压后会看到： `Requests-GUI-EN.exe`（英文）或 `Requests-GUI-CN.exe`（中文）
4. 选择一个版本，双击运行 


### 方式 2：从源代码运行  
适合开发者或需要自定义的用户：  

#### 环境要求  
- Python 3.8 及以上  
- 安装依赖：  
  ```bash  
  pip install pyside6 requests jsbeautifier  
  ```  

#### 步骤  
1. 下载源代码：  
   - 在 [GitHub 仓库](https://github.com/add-qwq/Requests-GUI) 点击 `Code → 下载 ZIP`（无需 Git）。  
   - 解压 ZIP 文件。  

2. 运行程序（选择中英文版本）：  
   - **英文版本**：  
     ```bash  
     cd Requests-GUI/Requests-GUI-EN  
     python main.py  
     ```  
   - **中文版本**：  
     ```bash  
     cd Requests-GUI/Requests-GUI-CN  
     python main.py  
     ```  
   - 当然，也可以直接双击main.py运行

## 📦 打包为 EXE（自定义发布）  
使用 `pyinstaller` 生成独立 EXE（先通过 `pip install pyinstaller` 安装）。  

### 打包命令示例（中文版本）：  
```bash  
# 进入中文源代码目录  
cd Requests-GUI/Requests-GUI-CN  

# 打包（Windows）  
pyinstaller -w -F -i gui.ico --add-data "gui.ico;." main.py  

# 参数说明：  
# -w：隐藏控制台窗口（图形界面程序推荐）。  
# -F：生成单个 EXE 文件（而非目录）。  
# -i gui.ico：指定窗口图标。  
# --add-data "gui.ico;."：将图标文件打包到 EXE 中（Windows 使用分号 `;`）。  
```  

**macOS/Linux 注意**：`--add-data` 中路径分隔符改为冒号 `:`（如 `--add-data "gui.ico:."`）。  


## 🖥 界面概览  
![中文界面](https://github.com/add-qwq/Requests-GUI/blob/main/GUI-CN.png?raw=true)  
*(点击查看原图。英文版本功能与中文一致，仅界面文本为英文。)*  


## 📘 使用示例  

### 示例 1：发送带查询参数的 GET 请求  
**目标**：向 `https://httpbin.org/get` 发送参数 `name=张三&age=20`。  

**步骤**：  
1. 下拉菜单选择 `GET`。  
2. 在 URL 输入框填写 `https://httpbin.org/get`。  
3. 切换到「查询参数」选项卡，输入 `name=张三&age=20`（或 JSON `{"name": "张三", "age": 20}`）。  
4. （可选）在请求头表格添加 `User-Agent: Requests-GUI-CN`。  
5. 点击「发送请求」。  

**预期响应**：  
- 状态码：`200 OK`。  
- 响应内容中 `args` 字段显示参数：  
  ```json  
  {  
    "age": "20",  
    "name": "张三"  
  }  
  ```  


### 示例 2：发送表单数据的 POST 请求  
**目标**：向 `https://httpbin.org/post` 提交表单 `username=test&password=123456`。  

**步骤**：  
1. 选择 `POST`。  
2. URL 填写 `https://httpbin.org/post`。  
3. 切换到「请求体」选项卡，输入 `username=test&password=123456`。  
4. 添加请求头 `Content-Type: application/x-www-form-urlencoded`。  
5. 点击「发送请求」。  

**预期响应**：  
- 状态码：`200 OK`。  
- 响应内容中 `form` 字段显示提交的数据：  
  ```json  
  {  
    "password": "123456",  
    "username": "test"  
  }  
  ```  


### 示例 3：发送 JSON 数据的 POST 请求  
**目标**：向 `https://httpbin.org/post` 发送 JSON `{"email": "test@example.com", "is_vip": true}`。  

**步骤**：  
1. 选择 `POST`。  
2. URL 填写 `https://httpbin.org/post`。  
3. 切换到「请求体」选项卡，输入：  
   ```json  
   {"email": "test@example.com", "is_vip": true}  
   ```  
4. 添加请求头 `Content-Type: application/json`。  
5. 点击「发送请求」。  

**预期响应**：  
- 状态码：`200 OK`。  
- 响应内容中 `json` 字段显示提交的 JSON（自动格式化）。  


### 示例 4：处理错误请求（如无效 URL）  
**目标**：测试工具对错误 URL 的处理。  

**步骤**：  
1. 选择任意方法（如 `GET`）。  
2. 输入错误 URL `https://invalid-url.example.com`。  
3. 点击「发送请求」。  

**预期响应**：  
- 状态码显示错误信息（如 `连接错误`）。  
- 响应内容显示详细错误（如 DNS 解析失败）。  


## 📜 许可证  
本项目采用 [Apache 2.0 许可证](https://github.com/add-qwq/Requests-GUI/blob/main/Requests-GUI-CN/LICENSE)。  


## 🙋 贡献与反馈  
- **问题反馈/功能建议**：提交 [Issue](https://github.com/add-qwq/Requests-GUI/issues)。  
- **代码贡献**：Fork 仓库，修改后提交 PR。  
- **多语言支持**：通过翻译 `main_window.py` 中的界面文本添加新语言。
