# File Scanner and Cleaner Scripts

This repository contains a set of Python scripts for scanning and cleaning files on a server or local directory, specifically targeting files related to online gambling and backdoor patterns. The scripts utilize keyword scanning to detect and remove harmful files that may pose a security risk.

### Scripts Included:
1. **keyword_gambling_detection_tool.py**
2. **php_backdoor_scanner.py**
3. **judolscanner.py**

### Purpose
The scripts in this repository are designed to:
- Scan files in specified directories for suspicious content, such as gambling-related keywords or backdoor scripts.
- Automatically delete any files that contain harmful or unwanted content.
- Provide an ASCII art logo for a professional touch.
- Support various file types such as `.php`, `.txt`, `.html`, `.py`, `.js`, and others.

### How to Use

1. **delletekeyword.py**  
   This script scans files for keywords related to gambling and deletes any file found with those keywords. It provides the option to scan a specific directory or all directories in the current working directory.

2. **findscanner.py**  
   This script scans files for backdoor patterns in PHP files, detecting potential threats such as `eval()`, `base64_decode()`, and other common backdoor functions. It also allows directory scanning.

3. **judolscanner.py**  
   Similar to the other scripts, this one is focused on scanning for gambling-related keywords, specifically looking for terms associated with gambling websites. It works in the same way, with an option for scanning either specific directories or the current directory.

### Features
- **Keyword Scanning:** Scans files for specific gambling-related keywords and backdoor functions.
- **File Deletion:** Automatically deletes infected files.
- **ASCII Art:** Displays a logo and provides a professional look to the script’s output.
- **Multiple File Formats Supported:** Handles a wide variety of file extensions, including `.php`, `.txt`, `.js`, `.html`, `.py`, and more.
- **File Logging:** Records the results of the scan, including deleted files, in a `result.txt` file.

### Installation
1. Clone this repository to your local machine or server:
    ```bash
    git clone https://github.com/your-repository-url
    ```

2. Navigate to the project folder:
    ```bash
    cd your-project-folder
    ```

3. Run the script:
    ```bash
    python delletekeyword.py
    ```

    Replace `delletekeyword.py` with any other script file name to use them individually.

### Script Options
- **Scan a specific directory**: You will be prompted to enter a directory path to scan.
- **Scan all directories**: The script will scan all directories in the current working directory.

### Example Usage
To scan the current directory and remove any files with gambling-related keywords:
```bash
python delletekeyword.py
