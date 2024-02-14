# Generate Cisco IOS port VLAN config

# Version 0.1 - kickstart (quick and simple)
# Features:
#  - Receives list of VLAN inputs and separate them, put into 48 ports by index
# How to use:
#  1. Write list of VLANs separated by spaces or tabs, Excel column data is not acceptable
#  2. Enter port numbering first digit, eg. Gi2/0/1 (which is 2) or Gi3/0/1 (which is 3)
#  3. Copy and paste the list into the VLAN input prompt.
#  4. Voila 


print("Port naming format (x: 1-4) (y: 1-48): ")
print("1. GigabitEthernetx/0/y (Catalyst 9000 Series / 3650 / Newer models)")
print("2. GigabitEthernet0/y (Catalyst 3560X / 3560G / Older models)")
print("3. FastEthernet0/y (more ancient models) ")
portname_format = input("Select port naming format (1 / 2 / 3) : ")

if portname_format == 1:
    portname = "GigabitEthernet" #include more for stacking options (value x)
elif portname_format == 2:
    portname = "GigabitEthernet0/"
else:
    portname = "FastEthernet0/"
vlan_input = input("Enter VLAN list:")
vlan_list = vlan_input.split()
vlan_count = len(vlan_list)
print("VLAN count : %s" % (str(vlan_count)))
if vlan_count != 48:
    print("VLANs entered is less than 48")
for x in range(vlan_count):
    print("interface %s%s" % (portname, x+1))
    print(" switchport access vlan %s" % (vlan_list[x]))
    print("! ")

