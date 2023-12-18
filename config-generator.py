# stackcount = int(input("Enter number of stack: ") )
# print("Stack of %s" % (stackcount))

port_first = input("Port naming first number: ")
print("Port name: GigabitEthernet%s/0/x" % (port_first))
vlan_input = input("Enter VLAN list:")
vlan_list = vlan_input.split()
vlan_count = len(vlan_list)

for x in range(vlan_count):
    print("interface GigabitEthernet%s/0/%s" % (port_first, x+1))
    print(" switchport access vlan %s" % (vlan_list[x]))
    print("! ")

# vlan_input = input("Enter VLAN list:")
# vlan_list = vlan_input.split()
# vlan_count = len(vlan_list)
# print(vlan_list)
# for x in range(vlan_count):