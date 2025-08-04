RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def format_port_results(results):
    formatted = "Port Scan Results:\n"
    formatted += "{:<8}{:<15}{:<10}\n".format("Port", "Service", "Status")
    formatted += "-" * 35 + "\n"
    for port, service, banner, status in sorted(results):
        if status:
            formatted += f"{RED}{port:<8}{service:<15}{'Open':<10}{RESET}\n"
            if banner:
                for line in banner.splitlines():
                    formatted += f"{GREEN}{'':<8}{line}{RESET}\n"
    return formatted