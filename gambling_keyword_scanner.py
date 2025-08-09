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

# Displaying ASCII Art
print(ascii_art)

def is_supported_file(filename):
    # List of supported file extensions to check
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
        "europe-east.com/montenegro", 
        "tips taruhan online", "permainan casino gratis", "poker langsung", "roulette langsung", "kemenangan poker", 
        "kalkulator odds taruhan", "poker crypto", "skrip taruhan", "odds blackjack", "platform casino", "rumah poker", 
        "bookie", "afiliasi perjudian", "afiliasi casino", "afiliasi poker", "perjudian esports", "bonus slot", "bonus poker", 
        "strategi mesin slot", "ulasan casino online", "tutorial poker", "tutorial taruhan", "tips sportsbook", 
        "prediksi olahraga", "spin slot gratis", "uang poker", "kecanduan perjudian", "penipuan perjudian", "kecurangan poker", 
        "celah taruhan", "ulasan sportsbook", "bonus sportsbook", "penawaran taruhan", "ulasan sportsbook online", 
        "aturan perjudian", "aturan taruhan olahraga", "opsi taruhan", "bonus taruhan olahraga", "slot mesin menang", 
        "menang mesin slot", "taruhan jackpot", "platform taruhan crypto", "afiliasi perjudian online", 
        "turnamen poker online", "spin gratis perjudian", "casino play instant", "perjudian offline", 
        "kalkulator odds taruhan olahraga", "program afiliasi poker", "program afiliasi perjudian", "tips perjudian olahraga", 
        "aplikasi perjudian mobile", "taruhan bitcoin", "permainan casino gratis", "tips taruhan olahraga", 
        "strategi taruhan odds tinggi", "pembayaran mesin slot", "poker cryptocurrency", "situs poker", "esports gambling", 
        "slot bonuses", "poker bonuses", "slot machine strategy", "online casino review", "poker tutorial", "betting tutorial", 
        "sportsbook tips", "sports predictions", "free slot spins", "poker money", "gambling addiction", "gambling fraud", 
        "poker cheating", "betting loophole", "sportsbook review", "sportsbook bonus", "betting offers", "online sportsbook review", 
        "gambling rules", "sports betting rules", "betting options", "sports betting bonus", "slot machines win", 
        "win slot machines", "jackpot betting", "crypto betting platform", "online gambling affiliate", "poker tournaments online", 
        "gambling free spins", "instant play casino", "offline gambling", "sports betting odds calculator", 
        "poker affiliate program", "gambling affiliate program", "sports gambling tips", "mobile gambling apps", "bitcoin betting", 
        "casino games free", "sports betting advice", "high odds betting strategy", "slot machine payouts", "cryptocurrency poker", 
        "poker sites", "slot99bet", "tokyo77", "slotbet", "slot888bet", "judi slot online", "situs slot gacor", "agen slot88", 
        "slot terbaru", "permainan slot online", "slot server indonesia", "slot jackpot online", "situs casino terpercaya", 
        "slot win", "situs poker online", "situs judi terpercaya", "situs togel online", "slot terbaik", "judi slot terpercaya", 
        "slot gacor gampang menang", "situs betting terpercaya", "judi bola online", "agen judi slot", "judi baccarat", 
        "pokerstars indonesia", "big win slot", "game judi online", "slot88bet", "slot game online", "casino jackpot", 
        "taruhan bola online", "slot video games", "betting tips online", "agen betting terpercaya", "judi bola terpercaya", 
        "slot online terpercaya", "situs slot terbaik", "poker game online", "slot bonus terbesar", "baccarat casino", 
        "online poker game", "blackjack casino", "roulette casino", "free poker game", "live dealer casino", 
        "crypto poker betting", "bitcoin casino", "judi poker indonesia", "slot jackpot terbesar", "poker tournament"     
    ]

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            for pattern in gambling_keywords:
                if pattern.lower() in content.lower():  # Search for pattern without considering case
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
    print("Choose one of the following options:")
    print("1. Scan a specific directory")
    print("2. Scan all directories here")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        directory_to_scan = input("Enter the path of the directory you want to check: ")
        backdoor_files = scan_single_directory(directory_to_scan)
    elif choice == "2":
        base_directory = os.getcwd()  # Use the current working directory as the base directory
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
