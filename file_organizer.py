import os
import shutil
import time
from colorama import Fore, Style
import msvcrt as key
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
textfiles = "X"
pythonfiles = "X"
pdffiles = "X"
wordsfiles = "X"
powerfiles = "X"
excelfiles = "X"
compfiles = "X"
images = "X"
audiofiles = "X"
videofiles = "X"
programs = "X"
shortcuts = "X"
allinone = ""
valid_inputs = {b'0', b'1', b'2', b'3', b'4',
                b'5', b'6', b'7', b'8', b'9', b'a', b'b', b'c', b'd'}
valid_inputs1 = {b'1', b'2', b'p', b'q'}
python_folder = ""

user_name = os.getlogin()
desktopdir = f"C:\\Users\\{user_name}\\Desktop\\"


def console():
    os.system('cls')
    print(Fore.BLUE + Style.BRIGHT, """
     ▄▄▄▄▄▄▄ ▄▄▄ ▄▄▄     ▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄    ▄ ▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄
    █       █   █   █   █       █  █       █   ▄  █ █       █       █  █  █ █   █       █       █   ▄  █
    █    ▄▄▄█   █   █   █    ▄▄▄█  █   ▄   █  █ █ █ █   ▄▄▄▄█   ▄   █   █▄█ █   █▄▄▄▄   █    ▄▄▄█  █ █ █
    █   █▄▄▄█   █   █   █   █▄▄▄   █  █ █  █   █▄▄█▄█  █  ▄▄█  █▄█  █       █   █▄▄▄▄█  █   █▄▄▄█   █▄▄█▄
    █    ▄▄▄█   █   █▄▄▄█    ▄▄▄█  █  █▄█  █    ▄▄  █  █ █  █       █  ▄    █   █ ▄▄▄▄▄▄█    ▄▄▄█    ▄▄  █
    █   █   █   █       █   █▄▄▄   █       █   █  █ █  █▄▄█ █   ▄   █ █ █   █   █ █▄▄▄▄▄█   █▄▄▄█   █  █ █
    █▄▄▄█   █▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█  █▄▄▄▄▄▄▄█▄▄▄█  █▄█▄▄▄▄▄▄▄█▄▄█ █▄▄█▄█  █▄▄█▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄█  █▄█

    """, Style.RESET_ALL)
    print(Style.BRIGHT, f"""
    {Fore.WHITE}[1] - {Fore.GREEN}Run with default settings
    {Fore.WHITE}[2] - {Fore.YELLOW}Run with custom settings
    

    {Fore.GREEN}[CURRENT DIRECTORY] - {Fore.RED}{desktopdir}
    {Fore.GREEN}[P] - {Fore.RED}Change Directory
    {Fore.GREEN}[Q] - {Fore.RED}Exit
    """, Style.RESET_ALL)
    user_input = key.getch()
    if user_input in valid_inputs1:
        if user_input == b'1':
            main()
        if user_input == b'2':
            custom()
        if user_input == b'p':
            directorychange()
        if user_input == b'q':
            quit()
    else:
        os.system('cls')
        console()


def custom():
    os.system('cls')
    global textfiles, pythonfiles, pdffiles, wordsfiles, powerfiles, excelfiles, compfiles, images, audiofiles, videofiles, programs, shortcuts, valid_inputs, allinone

    print(Fore.BLUE + Style.BRIGHT, """
     ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄
    █       █       █       █       █   █  █  █ █       █       █
    █  ▄▄▄▄▄█    ▄▄▄█▄     ▄█▄     ▄█   █   █▄█ █   ▄▄▄▄█  ▄▄▄▄▄█
    █ █▄▄▄▄▄█   █▄▄▄  █   █   █   █ █   █       █  █  ▄▄█ █▄▄▄▄▄
    █▄▄▄▄▄  █    ▄▄▄█ █   █   █   █ █   █  ▄    █  █ █  █▄▄▄▄▄  █
    ▄▄▄▄▄█ █   █▄▄▄  █   █   █   █ █   █ █ █   █  █▄▄█ █▄▄▄▄▄█ █
    █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█ █▄▄▄█   █▄▄▄█ █▄▄▄█▄█  █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█

    """, Style.RESET_ALL)

    print(Fore.BLUE + Style.BRIGHT, f"""
    {Fore.WHITE}[1] - {Fore.CYAN}Text files {Fore.RED}[{textfiles}]
    {Fore.WHITE}[2] - {Fore.CYAN}Programming Files (ALL) {Fore.RED}[{pythonfiles}]
    {Fore.WHITE}[3] - {Fore.CYAN}PDF files {Fore.RED}[{pdffiles}]
    {Fore.WHITE}[4] - {Fore.CYAN}Words files {Fore.RED}[{wordsfiles}]
    {Fore.WHITE}[5] - {Fore.CYAN}Power files {Fore.RED}[{powerfiles}]
    {Fore.WHITE}[6] - {Fore.CYAN}Excel files {Fore.RED}[{excelfiles}]
    {Fore.WHITE}[7] - {Fore.CYAN}Compressed files {Fore.RED}[{compfiles}]
    {Fore.WHITE}[8] - {Fore.CYAN}Images {Fore.RED}[{images}]
    {Fore.WHITE}[9] - {Fore.CYAN}Audio files {Fore.RED}[{audiofiles}]
    {Fore.WHITE}[a] - {Fore.CYAN}Video files {Fore.RED}[{videofiles}]
    {Fore.WHITE}[b] - {Fore.CYAN}Programs {Fore.RED}[{programs}]
    {Fore.WHITE}[c] - {Fore.CYAN}Shortcuts {Fore.RED}[{shortcuts}]

    {Fore.WHITE}[d] - {Fore.YELLOW}ALL IN ONE FOLDER {Fore.RED}[{allinone}]


    {Fore.WHITE}[0] - {Fore.RED}RUN PROGRAM

    """, Style.RESET_ALL)
    try:
        user_input = key.getch()
        if user_input in valid_inputs:
            if len(user_input) == 1:
                if user_input == b'1':
                    if textfiles == "X":
                        textfiles = ""
                        os.system('cls')
                        custom()
                    else:
                        textfiles = "X"
                        os.system('cls')
                        custom()
                if user_input == b'2':
                    if pythonfiles == "X":
                        pythonfiles = ""
                        os.system('cls')
                        custom()
                    else:
                        pythonfiles = "X"
                        os.system('cls')
                        custom()
                if user_input == b'3':
                    if pdffiles == "X":
                        pdffiles = ""
                        os.system('cls')
                        custom()
                    else:
                        pdffiles = "X"
                        os.system('cls')
                        custom()
                if user_input == b'4':
                    if wordsfiles == "X":
                        wordsfiles = ""
                        os.system('cls')
                        custom()
                    else:
                        wordsfiles = "X"
                        os.system('cls')
                        custom()
                if user_input == b'5':
                    if powerfiles == "X":
                        powerfiles = ""
                        os.system('cls')
                        custom()
                    else:
                        powerfiles = "X"
                        os.system('cls')
                        custom()
                if user_input == b'6':
                    if excelfiles == "X":
                        excelfiles = ""
                        os.system('cls')
                        custom()
                    else:
                        excelfiles = "X"
                        os.system('cls')
                        custom()
                if user_input == b'7':
                    if compfiles == "X":
                        compfiles = ""
                        os.system('cls')
                        custom()
                    else:
                        compfiles = "X"
                        os.system('cls')
                        custom()
                if user_input == b'8':
                    if images == "X":
                        images = ""
                        os.system('cls')
                        custom()
                    else:
                        images = "X"
                        os.system('cls')
                        custom()
                if user_input == b'9':
                    if audiofiles == "X":
                        audiofiles = ""
                        os.system('cls')
                        custom()
                    else:
                        audiofiles = "X"
                        os.system('cls')
                        custom()
                if user_input == b'a':
                    if videofiles == "X":
                        videofiles = ""
                        os.system('cls')
                        custom()
                    else:
                        videofiles = "X"
                        os.system('cls')
                        custom()
                if user_input == b'b':
                    if programs == "X":
                        programs = ""
                        os.system('cls')
                        custom()
                    else:
                        programs = "X"
                        os.system('cls')
                        custom()
                if user_input == b'c':
                    if shortcuts == "X":
                        shortcuts = ""
                        os.system('cls')
                        custom()
                    else:
                        shortcuts = "X"
                        os.system('cls')
                        custom()
                if user_input == b'd':
                    if allinone == "X":
                        allinone = ""
                        os.system('cls')
                        custom()
                    else:
                        allinone = "X"
                        os.system('cls')
                        custom()
                if user_input == b'0':
                    os.system('cls')
                    main()
                else:
                    pass
            else:
                print(Fore.RED, "Error.")
                time.sleep(1)
                os.system('cls')
                custom()
        else:
            os.system('cls')
            custom()
    except Exception as e:
        print(f"Error: {e}")
        pass


def main():
    os.system('cls')
    global root, python_folder, py_folder, desktopdir

    print(Fore.BLUE + Style.BRIGHT, "Executing program with current settings...")
    for root, dirs, files in os.walk(desktopdir, topdown=True):
        if root == desktopdir:
            for name in files:
                os.chdir(desktopdir)
                if textfiles == True or textfiles == "X":
                    try:
                        if name.endswith('.txt'):
                            txt_folder = os.path.join(desktopdir, "Text Files")
                            if not os.path.exists(txt_folder):
                                os.mkdir(txt_folder)
                            shutil.move(os.path.join(root, name), txt_folder)
                    except:
                        pass
                else:
                    pass
                if pythonfiles == True or pythonfiles == "X":
                    try:
                        if name.endswith('.py') or name.endswith('.pyw'):
                            py_folder = os.path.join(
                                desktopdir, "Python Files")
                            if not os.path.exists(py_folder):
                                os.mkdir(py_folder)
                            shutil.move(os.path.join(root, name), py_folder)
                        if name.endswith('.cpp') or name.endswith('.c++') or name.endswith('.c') or name.endswith('.cc') or name.endswith('.cp') or name.endswith('.cxx') or name.endswith('.h') or name.endswith('.h++') or name.endswith('.hh') or name.endswith('.hpp') or name.endswith('.hxx') or name.endswith('.inc') or name.endswith('.inl') or name.endswith('.ipp') or name.endswith('.tcc') or name.endswith('.tpp'):
                            c_folder = os.path.join(
                                desktopdir, "C++ Files")
                            if not os.path.exists(c_folder):
                                os.mkdir(c_folder)
                            shutil.move(os.path.join(root, name), c_folder)
                        if name.endswith('.java'):
                            java_folder = os.path.join(
                                desktopdir, "Java Files")
                            if not os.path.exists(java_folder):
                                os.mkdir(java_folder)
                            shutil.move(os.path.join(root, name), java_folder)

                    except:
                        pass
                else:
                    pass
                if pdffiles == True or pdffiles == "X":
                    try:
                        if name.endswith('.pdf'):
                            pdf_folder = os.path.join(desktopdir, "PDF Files")
                            if not os.path.exists(pdf_folder):
                                os.mkdir(pdf_folder)
                                shutil.move(os.path.join(
                                    root, name), pdf_folder)
                    except:
                        pass
                else:
                    pass
                if wordsfiles == True or wordsfiles == "X":
                    try:
                        if name.endswith('.docx') or name.endswith('.doc'):
                            docx_folder = os.path.join(
                                desktopdir, "Word Files")
                            if not os.path.exists(docx_folder):
                                os.mkdir(docx_folder)
                            shutil.move(os.path.join(root, name), docx_folder)
                    except:
                        pass
                else:
                    pass
                if powerfiles == True or powerfiles == "X":
                    try:
                        if name.endswith('.pptx') or name.endswith('.ppt') or name.endswith('.key') or name.endswith('.odp') or name.endswith('.pps'):
                            pptx_folder = os.path.join(
                                desktopdir, "PowerPoint Files")
                            if not os.path.exists(pptx_folder):
                                os.mkdir(pptx_folder)
                            shutil.move(os.path.join(root, name), pptx_folder)
                    except:
                        pass
                else:
                    pass
                if excelfiles == True or excelfiles == "X":
                    try:
                        if name.endswith('.xlsx') or name.endswith('.xls'):
                            xlsx_folder = os.path.join(
                                desktopdir, "Excel Files")
                            if not os.path.exists(xlsx_folder):
                                os.mkdir(xlsx_folder)
                            shutil.move(os.path.join(root, name), xlsx_folder)
                    except:
                        pass
                else:
                    pass
                if compfiles == True or compfiles == "X":
                    try:
                        if name.endswith('.zip') or name.endswith('.rar') or name.endswith('.7z') or name.endswith('.arj') or name.endswith('.deb') or name.endswith('.pkg') or name.endswith('.rpm') or name.endswith('.z'):
                            zip_folder = os.path.join(
                                desktopdir, "Compressed Files")
                            if not os.path.exists(zip_folder):
                                os.mkdir(zip_folder)
                            shutil.move(os.path.join(root, name), zip_folder)
                    except:
                        pass
                else:
                    pass
                if images == True or images == "X":
                    try:
                        if name.endswith('.jpg') or name.endswith('.jpeg') or name.endswith('.png') or name.endswith('.gif') or name.endswith('.jfif') or name.endswith('.ico') or name.endswith('.psd'):
                            img_folder = os.path.join(desktopdir, "Images")
                            if not os.path.exists(img_folder):
                                os.mkdir(img_folder)
                            shutil.move(os.path.join(root, name), img_folder)
                    except:
                        pass
                else:
                    pass
                if audiofiles == True or audiofiles == "X":
                    try:
                        if name.endswith('.mp3') or name.endswith('.wma'):
                            mp3_folder = os.path.join(
                                desktopdir, "Audio Files")
                            if not os.path.exists(mp3_folder):
                                os.mkdir(mp3_folder)
                            shutil.move(os.path.join(root, name), mp3_folder)
                    except:
                        pass
                else:
                    pass
                if videofiles == True or videofiles == "X":
                    try:
                        if name.endswith('.mp4') or name.endswith('.avi'):
                            mp4_folder = os.path.join(
                                desktopdir, "Video Files")
                            if not os.path.exists(mp4_folder):
                                os.mkdir(mp4_folder)
                            shutil.move(os.path.join(root, name), mp4_folder)
                    except:
                        pass
                else:
                    pass
                if programs == True or programs == "X":
                    try:
                        if name.endswith('.exe') or name.endswith('.msi') or name.endswith('.bat'):
                            program_folder = os.path.join(
                                desktopdir, "Programs")
                            if not os.path.exists(program_folder):
                                os.mkdir(program_folder)
                            shutil.move(os.path.join(
                                root, name), program_folder)
                    except:
                        pass
                else:
                    pass
                if shortcuts == True or shortcuts == "X":
                    try:
                        if name.endswith('.lnk'):
                            shortcuts_folder = os.path.join(
                                desktopdir, "Shortcuts")
                            if not os.path.exists(shortcuts_folder):
                                os.mkdir(shortcuts_folder)
                            shutil.move(os.path.join(root, name),
                                        shortcuts_folder)
                    except:
                        pass
                else:
                    pass
        else:
            break
        if allinone == True or allinone == "X":
            allfolder = os.path.join(
                desktopdir, "All Folders")
            if not os.path.exists(allfolder):
                os.mkdir(allfolder)
            for item in os.listdir(desktopdir):
                item_path = os.path.join(desktopdir, item)

                if os.path.isdir(item_path):
                    try:
                        shutil.move(item_path, allfolder)
                    except:
                        pass
        else:
            pass
        print("Done.")
        time.sleep(0.5)
        print(Fore.BLUE + Style.BRIGHT,
              "Press any key to leave...", Style.RESET_ALL)
        key.getch()
        os.system('cls')


def directorychange():
    global desktopdir
    os.system('cls')
    print(Fore.BLUE + Style.BRIGHT,
          "Press any key to change directory...", Style.RESET_ALL)
    key.getch()
    os.system('cls')
    print(Fore.BLUE + Style.BRIGHT,
          "Enter the new directory...", Style.RESET_ALL)
    desktopdir = filedialog.askdirectory()
    print(Fore.BLUE + Style.BRIGHT,
          f"""{Fore.GREEN}New Directory : {desktopdir}\n{Fore.YELLOW}Press any key to continue...
          """, Style.RESET_ALL)
    key.getch()
    os.system('cls')
    console()


console()
