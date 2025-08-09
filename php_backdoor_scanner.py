import os

# ASCII Art in raw string format
ascii_art = r"""
         ******                                             ***                                     
      ************                                          ***                                **   
      *************                                   ***   ***                                 ****
      ************+              ****      *      *   ***   ***  **        ***        ****          
 *****************::::::      *********  ****    *** ****** **********  *********  **********       
 *****************::::::      ***    *** ****    ***  ***   ***    *** ****    *** ***    ***       
*****************:::::::      ***    *** ****    ***  ***   ***    *** ***     *** ***    ***       
*******:::::::::::::::::      ***    *** ****    ***  ***   ***    *** ***     *** ***    ***       
 *****::::::::::::::::::      ***   **** ****    ***  ***   ***    *** ****   **** ***    ***       
 *****:::::::::::::::::       *********   **********   **** ***    ***   *******   ***    ***       
      :::::::::::::           ***                ***                                                  
      ::::::::: :::           ***               ***                                                  
       :::::::::::            ***            *****                  

                            CREATED BY INSTAGRAM.COM/RIZSKYZII
"""

# Displaying ASCII Art
print(ascii_art)

def is_supported_file(filename):
    # List of file extensions to check (e.g., ".php", ".txt", ".asp", etc.)
    supported_extensions = [
        ".php", ".txt", ".asp", ".sh", ".py", ".js", ".html", ".htm", ".exe", ".dll",
        ".php.fla", ".php.png", ".php.bmp", ".php.tiff", ".php.jpeg", ".php.gif", ".php.jpg", 
        ".php.svg", ".php.psd", ".php.doc", ".php.docx", ".php.xls", ".php.xlsx", ".php.odt", 
        ".php.ppt", ".php.pptx", ".php.mp4", ".php.mkv", ".php.avi", ".php.mov", ".php.mp3", 
        ".php.wav", ".php.flv", ".php.zip", ".php.tar", ".php.rar", ".php.gz", ".php.bz2", 
        ".php.swf", ".php.iso", ".php.apk", ".php.jar", ".php.7z", ".php.bin", ".php.out", 
        ".php.sh", ".php.cgi", ".php.pl", ".php.rb", ".php.bat", ".php.vbs", ".php.js", 
        ".php.json", ".php.ini", ".php.cfg", ".php.ini3", ".php.swc", ".php.ipa", ".php.bak"
    ]
    
    # Check if the file has a valid extension
    for ext in supported_extensions:
        if filename.endswith(ext):
            return True

    return False

def scan_file(file_path):
    # List of backdoor patterns to detect backdoors in various file types
    backdoor_patterns = [
        "eval(", "base64_decode(", "system(", "shell_exec(", "passthru(", "exec(", "assert(", 
        "preg_replace('/.*/e'", "pcntl_exec(", "proc_open(", "popen(", "curl_exec(", "include(", 
        "require(", "eval(gzinflate(", "backdoor_function_1(", "backdoor_function_2(", "suspicious_string_xyz", 
        "suspicious_code_xyz", "shellcode", "document.write(", "iframe src", "window.location", 
        "exec('wget", "base64_encode(", "chmod(", "chown(", "http_request(", "socket_create(", 
        "system('id", "netcat", "bind_shell", "reverse_shell", "nc -e", "phpinfo()", "system('ls", 
        "shell_exec('ls", "proc_open('cat", "fopen('http", "file_get_contents('http", "curl('http", 
        "file_put_contents('http", "system('curl", "file_get_contents('ftp", "cmd.exe", "powershell.exe", 
        "wget http://", "php://input", "php://filter", "php://localhost", "rce://", "cmd|", "shell_exec|", 
        "eval|", "backdoor|", "spyware|", "rootkit|", "malware"
    ]

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            for pattern in backdoor_patterns:
                if pattern in content:
                    return True
    except (UnicodeDecodeError, FileNotFoundError):
        pass

    return False

def scan_single_directory(directory_path):
    backdoor_files = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            if is_supported_file(file_path) and scan_file(file_path):
                backdoor_files.append(file_path)

    return backdoor_files

def scan_all_directories(base_directory):
    backdoor_files = []
    for root, _, _ in os.walk(base_directory):
        backdoor_files.extend(scan_single_directory(root))

    return backdoor_files

if __name__ == "__main__":
    print("=============================================")
    print("           PHP Backdoor Finder")
    print("           SCANNER")
    print("=============================================")
    print("Choose one of the following options:")
    print("1. Scan a specific directory")
    print("2. Scan all directories here")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        directory_to_scan = input("Enter the directory path you want to scan: ")
        backdoor_files = scan_single_directory(directory_to_scan)
    elif choice == "2":
        base_directory = os.getcwd()  # Use current working directory as the starting point
        backdoor_files = scan_all_directories(base_directory)
    else:
        print("Invalid choice.")
        exit()

    result_file = "result.txt"
    with open(result_file, "w") as f:
        if backdoor_files:
            f.write("Suspicious files found:\n")
            for file_path in backdoor_files:
                f.write(file_path + "\n")
            print("Scan results have been saved in the file", result_file)
        else:
            f.write("No suspicious files found in the directory.\n")
            print("No suspicious files found.")
