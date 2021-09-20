from helpers import *
import time


def assign_ip_address():
    ip = Prompt.ask("Enter IPv4 address/mask")
    validate_ipv4(ip.split("/")[0], "ip")
    interface = select_interface()
    print(execute_shell(f"ip address add {ip} dev {interface}"))


def delete_ip_address():
    interface = select_interface()
    ip = Prompt.ask("Select an ip/mask", choices = ip_address_list(interface))
    colour_print("#FFFFFF", execute_shell(f"ip address del {ip} dev {interface}"))


def display_ip_address():
    interface = select_interface()
    colour_print("#FFFFFF", f"IPv4 address of {interface}: {ip_address_list(interface)}")
    print(execute_shell(f"ip -c -br a"))


def display_interfaces():
    #for inter in interface_name_list():
    colour_print("#FFFFFF",interface_name_list())
    colour_print("#FFFFFF", execute_shell("ip l"))


def configure_routing():
    while True:
        configure_routing_menu()
        ch = Prompt.ask("Select an option", choices = [str(x) for x in range(1,5)])
        if ch == '1':
            add_new_route()
        elif ch == '2':
            delete_route()
        elif ch == '3':
            display_route()
        elif ch == '4':
            break


def turn_interface_on_off():
    while True:
        turn_interface_on_off_menu()
        ch = Prompt.ask("Select an option", choices = [str(x) for x in range(1,4)])
        if ch == '1':
            turn_interface_on()
        elif ch == '2':
            turn_interface_off()
        elif ch == '3':
            break


def add_arp_entry():
    ip = Prompt.ask("Enter IPv4 address")
    validate_ipv4(ip, "ip")
    mac = Prompt.ask("Enter MAC address")
    interface = select_interface()
    execute_shell(f"ip n add {ip} lladdr {mac} dev {interface} nud permanent")


def delete_arp_entry():
    colour_print("#FFFFFF", execute_shell(f"ip n show"))
    ip = Prompt.ask("Enter IPv4 address")
    validate_ipv4(ip, "ip")
    interface = select_interface()
    execute_shell(f"ip n delete {ip} dev {interface}")


def restart_network():
    execute_shell(f"systemctl restart networking")
    colour_print("#FFFFFF", execute_shell(f"systemctl status networking"))


def change_host_name():
    host_name = Prompt.ask("Enter new hostname")
    execute_shell(f"hostnamectl set-hostname {host_name}")


def add_dns_server_entry():
    server_ip = Prompt.ask("Enter DNS server", default = "8.8.8.8")
    with open("/etc/resolv.conf", "a") as fd:
        fd.write(f"nameserver {server_ip}\n")
