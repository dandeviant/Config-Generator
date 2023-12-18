# Generate Cisco IOS port VLAN config

# Version 0.1 - kickstart (quick and simple)
# Features:
#  - Receives list of VLAN inputs and separate them, put into 48 ports by index
# How to use:
#  1. Write list of VLANs separated by spaces or tabs, Excel column data is not acceptable
#  2. Enter port numbering first digit, eg. Gi2/0/1 (which is 2) or Gi3/0/1 (which is 3)
#  3. Copy and paste the list into the VLAN input prompt.
#  4. Voila 

port_first = input("Port naming first number: ")
print("Port name: GigabitEthernet%s/0/x" % (port_first))
vlan_input = input("Enter VLAN list:")
vlan_list = vlan_input.split()
vlan_count = len(vlan_list)

for x in range(vlan_count):
    print("interface GigabitEthernet%s/0/%s" % (port_first, x+1))
    print(" switchport access vlan %s" % (vlan_list[x]))
    print("! ")
