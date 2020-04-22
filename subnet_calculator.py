#! /usr/bin/env python
"""
This script is a part of a tutorial to build a Python subnet Calculator.

The script accepts string inputs in the following formats:
`192.168.1.0/24` or `192.168.2.0/255.255.255.0`

Example Usage:

    $ python subnet_calc.py 192.168.1.0/26

Output:
    IP Subnet Calculator
    Subnet: 192.168.0.0/24

    Network:   192.168.0.0/24 (Private Internet)
    Netmask:   255.255.255.0 = 24
    Wildcard:  0.0.0.255

    Broadcast: 192.168.0.255
    HostMin:   192.168.0.1
    HostMax:   192.168.0.254
    Hosts/Net: 254
"""
import ipaddress

def main():
    """
    Execution of the script starts here
    """

    # Uncomment the line below the print() welcome message
    print("IP Subnet Calculator")

    # define a variable
    network = input('Network => ')

    # network object
    network_object = ipaddress.ip_network(network, strict=False)
    netmask = str(network_object.netmask)
    netmask_octets = netmask.split('.')

    wilcard_octets = []
    for octet in netmask_octets:
        wildcard = 255 - int(octet)
        wilcard_octets.append(str(wildcard))

    dot = '.'
    wildcard = dot.join(wilcard_octets)

    hosts = list(network_object.hosts())
    first = hosts[0]
    last = hosts[-1]
    num_of_addresses = len(hosts)

    is_private = network_object.is_private

    if is_private:
        print(f'Network:   {network_object} (private network)')
    else:
        print(f'Network:   {network_object}')
    print(f'Netmask:   {network_object.netmask} = {network_object.prefixlen}')
    print(f'Wildcard:  {wildcard}')
    print(f'Broadcast: {network_object.broadcast_address}')
    print(f'HostMin:   {first}')
    print(f'HostMax:   {last}')
    print(f'Hosts/Net: {num_of_addresses}')

    print('Would like to to subdivide that network into smaller networks?\n')

    answer = input()

    if answer.lower() == 'yes':
        print('What size networks would you like them to be?\n')
    else:
        print('Then I have nothing more to offer you')



if __name__ == "__main__": 
    main()
