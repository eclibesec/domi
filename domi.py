# created by eclibes security labs 
# domains to ip

import socket
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore, Style
init()
def is_valid_domain(domain):
    if len(domain) > 253 or len(domain) == 0:
        return False
    labels = domain.split('.')
    return all(0 < len(label) <= 63 for label in labels)

def domain_to_ip(domain_name):
    if not is_valid_domain(domain_name):
        return None
    try:
        domain_name.encode('idna')
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except (socket.gaierror, UnicodeError):
        return None
if __name__ == "__main__":
    try:
        print("""
██████╗░░█████╗░███╗░░░███╗██╗
██╔══██╗██╔══██╗████╗░████║██║
██║░░██║██║░░██║██╔████╔██║██║
██║░░██║██║░░██║██║╚██╔╝██║██║
██████╔╝╚█████╔╝██║░╚═╝░██║██║
╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
- domain to ip tools
- developed by eclibes security labs""")
        file_name = input("$ give me your file: ").strip()
        output_file_name = input("$ output filename? : ").strip()

        while True:
            thread_count_str = input("threads > 1-100: ").strip()
            if thread_count_str.isdigit():
                thread_count = int(thread_count_str)
                if 1 <= thread_count <= 100:
                    break
                else:
                    print(f"{Fore.RED}Thread count must be between 1 and 100.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Thread count must be a number.{Style.RESET_ALL}")

        with open(file_name, 'r', encoding='utf-8') as file:
            domains = file.readlines()
        domains = [domain.strip() for domain in domains]
        def process_domain(domain):
            ip_address = domain_to_ip(domain)
            if ip_address:
                print(f"[{Fore.GREEN}{domain} -> {ip_address}{Style.RESET_ALL}]")
                return ip_address
            else:
                print(f"[{Fore.RED}bad -> {domain}{Style.RESET_ALL}]")
                return None

        with ThreadPoolExecutor(max_workers=thread_count) as executor:
            results = executor.map(process_domain, domains)
        with open(output_file_name, 'w', encoding='utf-8') as output_file:
            for result in results:
                if result:
                    output_file.write(f"{result}\n")
        print(f"Data has been saved to '{output_file_name}'")
        with open(output_file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        unique_lines = set(lines)
        with open(output_file_name, 'w', encoding='utf-8') as file:
            file.writelines(unique_lines)
        print(f"Duplicate lines have been removed from '{output_file_name}'")
    except FileNotFoundError:
        print(f"{Fore.RED}File '{file_name}' not found.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
