from colorama import *

def name():

    name = f"""\
{Fore.CYAN}
██████╗  █████╗ ██████╗ ██╗  ██╗███╗   ██╗███████╗
██╔══██╗██╔══██╗██╔══██╗██║  ██║████╗  ██║██╔════╝
██║  ██║███████║██████╔╝███████║██╔██╗ ██║█████╗  
██║  ██║██╔══██║██╔═══╝ ██╔══██║██║╚██╗██║██╔══╝  
██████╔╝██║  ██║██║     ██║  ██║██║ ╚████║███████╗
╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝
                      {Style.RESET_ALL}v.1.0 https://github.com/cagrialis/daphne
    """
    description = f"{Fore.RED}{Style.BRIGHT}Description :\n" \
                  f"{Style.RESET_ALL}Daphne is a automatic scanning tool for penetration test. \n" \
                  f"Daphne has CaCrawl, Nmap,  Nikto and Nuclei. \n" \
                  f"You can start these all tools with one command by using Daphne.\n"

    print(name)
    print(description)