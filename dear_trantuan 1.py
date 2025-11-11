from time import sleep
import sys
from colorama import Fore, Style, init

init(autoreset=True)


def printLetter():
    lines = [
        (Fore.MAGENTA + "dear tran tuan,", 1.8),
        ("", 0.5),
        (Fore.YELLOW + "sap vao dong roi em mong anh giu gin suc khoe that tot,", 1.8),
        (Fore.YELLOW + "dung de ban than bi om, em lo ToT", 1.6),
        (Fore.CYAN + "em chuc anh dat duoc tat ca nhung gi minh mong muon", 1.8),
        (Fore.CYAN + "dat thanh tich cao trong cac ky thi sap toi", 1.5),
        (Fore.LIGHTWHITE_EX + "va du co chuyen gi xay ra", 1.2),
        (Fore.LIGHTWHITE_EX + "em van mong anh o noi do se song that tot", 1.6),
        (Fore.LIGHTWHITE_EX + "gap duoc nhung nguoi ma anh muon gap", 1.8),
        ("", 0.5),
        (Fore.LIGHTMAGENTA_EX + "em nho anh em that su muon gap anh", 2.0),
        (
            Fore.LIGHTYELLOW_EX + "em van luon o day va mong anh hanh phuc va binh an",
            1.8,
        ),
        (
            Fore.LIGHTYELLOW_EX
            + "hc tap cung phai de cho ban than nghi ngoi nua anh nha",
            2.3,
        ),
        ("", 0.6),
        (
            Fore.LIGHTCYAN_EX
            + "em khong biet la minh con co hoi nua khong..du sao thi cam on anh vi da doc aa:<",
            1.8,
        ),
    ]

    for line, delay in lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(0.045)
        print()
        sleep(delay)


if __name__ == "__main__":
    printLetter()
