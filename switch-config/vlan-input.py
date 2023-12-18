vlan_input = input("Enter VLAN list:")
vlan_list = vlan_input.split()
vlan_count = len(vlan_list)
print(vlan_list)
for x in range(vlan_count):
    print("%s: %s" % (x+1, vlan_list[x]) )