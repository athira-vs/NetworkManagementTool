#!/usr/bin/python3

from rich.console import Console
from rich.prompt import Prompt
from network_manage import *

while True:

    colour_print("green", f"{'_'*20}MENU{'_'*20}")
    colour_print("green", "[1] Assign IP address")
    colour_print("green", "[2] Delete IP address")
    colour_print("green", "[3] Display IP address")
    colour_print("green", "[4] Display all interfaces")
    colour_print("green", "[5] Configure routing")
    colour_print("green", "[6] Turn On/Off interface")
    colour_print("green", "[7] Add ARP entry")
    colour_print("green", "[8] Delete ARP entry")
    colour_print("green", "[9] Restart network")
    colour_print("green", "[10] Change hostname")
    colour_print("green", "[11] Add DNS server entry")
    colour_print("red", "[12] Exit")

    ch = Prompt.ask("Select an option", choices = [str(x) for x in range(1,13)])
    
    if ch == '1':
        assign_ip_address()
    elif ch == '2':
        delete_ip_address()
    elif ch == '3':
        display_ip_address()
    elif ch == '4':
        display_interfaces()
    elif ch == '5':
        configure_routing()
    elif ch == '6':
        turn_interface_on_off()
    elif ch == '7':
        add_arp_entry()
    elif ch == '8':
        delete_arp_entry()
    elif ch == '9':
        restart_network()
    elif ch =='10':
        change_host_name()
    elif ch == '11':
        add_dns_server_entry()
    elif ch =='12':
        break




