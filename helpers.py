import os
import re
from rich.console import Console
from rich.prompt import Prompt
from ipaddress import ip_network
from ipaddress import ip_address
#from rich.text import Text
#import traceback


console = Console()


def colour_print(colour, string):
    console.print(string, style = f'bold {colour}')


def execute_shell(cmd):
    return os.popen(cmd).read()


def interface_name_list():
    return os.popen("ip -o link show | cut -d':' -f2").read().split()


# Returns a list of ipv4 addresses associated with the given interface
def ip_address_list(interface):
    res = os.popen(f"ip -4 -o a show {interface}").read()
    return re.findall("\d*\.\d*\.\d*\.\d*/\d*", res)


def validate_ipv4(ip, kind = "ip"):
    try:
        if len(ip.split(".")) != 4:
            raise ValueError
        if kind == "network":
            ip_network(ip)
        elif kind == "ip":
            ip_address(ip)
    except ValueError as err:
        colour_print("red", "\n\nERROR!! Not a valid IPv4 address. Try again!")
        console.print_exception()
        print("\n\n")
    except Exception as err:
        #colour_print("red", f"\n\nERROR!!\n{traceback.print_exc()}")
        colour_print("red", "\n\nERROR!!\n")
        console.print_exception()
        print("\n\n")

    return ip


def select_interface():
    return Prompt.ask("Select an interface", choices = interface_name_list())


def configure_routing_menu():
    colour_print("green", f"{'_'*10}ROUTING MANAGEMENT MENU{'_'*10}")
    colour_print("green", "\t[1] Add new route")
    colour_print("green", "\t[2] Delete route")
    colour_print("green", "\t[3] Display route")
    colour_print("red", "\t[4] Return to previous menu")


def add_new_route():
    try:
        net_addr = Prompt.ask("Enter IPv4 network address/mask")
        validate_ipv4(net_addr, "network")
        gateway_ip = Prompt.ask("Enter gateway IPv4 address")
        validate_ipv4(gateway_ip, "ip")
        interface = select_interface()
        execute_shell(f"ip r add {net_addr} via {gateway_ip} dev {interface}")
    except:
        colour_print("red", "ERROR: Cannot process the function. Exiting.")


def delete_route():
    try:
        net_addr = Prompt.ask("Enter IPv4 network address/mask")
        validate_ipv4(net_addr, "network")
        interface = select_interface()
        execute_shell(f"ip r del {net_addr} dev {interface}")
    except:
        colour_print("red", "ERROR: Cannot process the function. Exiting.")
        console.print_exception()


def display_route():
    try:
        colour_print("#FFFFFF", execute_shell("ip r"))
    except:
        console.print_exception()


def turn_interface_on():
    try:
        interface = select_interface()
        execute_shell(f"ip link set dev {interface} up")
    except:
        console.print_exception()


def turn_interface_off():
    try:
        interface = select_interface()
        execute_shell(f"ip link set dev {interface} down")
    except:
        console.print_exception()


def turn_interface_on_off_menu():
    colour_print("green", "\t[1] Turn interface ON")
    colour_print("green", "\t[2] Turn interface OFF")
    colour_print("red", "\t[3] Return to previous menu")

