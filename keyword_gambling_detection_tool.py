import os

# ASCII Art
ascii_art = """
                                                                                                                 
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
			
def is_supported_file(filename):
    # List of file extensions to check
    supported_extensions = [
        ".php", ".txt", ".asp", ".sh", ".py", ".js", ".html", ".htm", ".exe", ".dll",
        ".json", ".xml", ".csv", ".log", ".pdf", ".docx", ".xlsx", ".pptx", ".odt", 
        ".rtf", ".md", ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", 
        ".webp", ".eps", ".psd", ".ai", ".indd", ".ppt", ".xls", ".doc", ".mobi", 
        ".epub", ".azw3", ".json", ".html", ".htm", ".css", ".scss", ".xml", ".yaml", 
        ".yaml", ".tex", ".texi", ".db", ".sql", ".sqlite", ".sqlite3", ".log", 
        ".mp3", ".wav", ".flac", ".aac", ".ogg", ".mp4", ".mov", ".avi", ".mkv", 
        ".webm", ".flv", ".zip", ".rar", ".tar", ".gz", ".7z", ".iso", ".apk", 
        ".dmg", ".deb", ".rpm", ".pkg"
    ]
    
    for ext in supported_extensions:
        if filename.endswith(ext):
            return True

    return False

def scan_file(file_path):
    gambling_keywords = [
        "slot thailand", "slot gacor", "judi online", "casino online", "taruhan bola", "poker online",
        "idnplay", "agen judi", "betting site", "live casino", "jackpot", "betting odds", "crypto gambling",
        "slot gacor terpercaya", "slot gacor terbaik", "slot gacor big win", "slot gacor paling mudah menang", 
        "slot gacor auto win", "slot jackpot gacor", "slot gacor bonus besar", "slot gacor terbaru", 
        "slot gacor untuk pemula", "slot gacor rtp tinggi", "slot maxwin gacor", "situs slot gacor 2023", 
        "link slot gacor terpercaya", "agen slot gacor", "permainan slot gacor", "situs slot gacor terpercaya", 
        "situs slot online resmi", "situs slot jackpot terbesar", "agen slot terpercaya Indonesia", 
        "situs slot tanpa potongan", "link situs slot terpercaya", "platform slot online terbaik", 
        "game slot online populer", "daftar situs slot online", "provider slot terpercaya", "aplikasi slot online terbaik", 
        "slot online dengan RTP tertinggi", "slot gacor hari ini live", "slotgacor", "slotgacorahariini", 
        "slotgacorgampangmenang", "slotgacormaxwin", "slotonline", "slotonlineterpercaya", "slotthailand", "slot777", 
        "slot888", "slotvip", "slot4d", "agenslot", "agenslotterpercaya", "situsslotresmi", "situsslotterpercaya", 
        "linkslotgacor", "slotbonusnewmember", "slotjackpotterbesar", "slotpragmatic", "slothabanero", "rtslot", 
        "rtpliveslot", "slotluarnegeri", "toto4d", "totomacau", "totosgp", "totohk", "prediksiangga", "prediksitoto", 
        "angkajitu", "angkamainhk", "livedrawsgp", "datasgphariini", "resulttogel", "resulthk", "pasarantogel", 
        "bandartogel", "togelterpercaya", "togehariini", "situstoto", "nana4d", "toto88", "agen4d", "judionline", 
        "judionlineterpercaya", "agenjudionline", "situsjuditerpercaya", "situsjudislot", "casinoonline", 
        "pokeronlineuangasli", "dominoqq", "taruhanonline", "judibola", "sbobetresmi", "bandarjudibola", "situsroletonline", 
        "qqonline", "tontonime", "desamahjong", "gantidomain", "kadinidairi", "veniceareamls", "techonday", "aigtpkit", 
        "polychromantium", "insuncorp", "starzinx", "infocravings", "newsfiltres", "shop.temuansemper", "orangemasjid", 
        "pontocine", "fdcs.uccuyosl", "cgm.coor", "sbci.jamindustries", "sc.fismec", "mobileappdev-websvc.ottawa", 
        "europe-east.com/montenegro"
    ]

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            for pattern in gambling_keywords:
                if pattern.lower() in content.lower():  # Search pattern without case sensitivity
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
    print("           Keyword Gambling Script SCANNER")
    print("           2025")
    print("=============================================")
    print(ascii_art)  # Display ASCII logo
    print("Please select an option:")
    print("1. Scan a specific directory")
    print("2. Scan all directories here")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        directory_to_scan = input("Enter the directory path you want to check: ")
        backdoor_files = scan_single_directory(directory_to_scan)
    elif choice == "2":
        base_directory = os.getcwd()  # Using current working directory as the base
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
            print("Scan results have been saved to", result_file)
        else:
            f.write("No suspicious files were found in the directory.\n")
            print("No suspicious files found.")
