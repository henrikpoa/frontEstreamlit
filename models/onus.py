class Onus:

    def __init__(self, onu_number, ip, vlan_name, vlan_id, serial, pon, vlan_ger, vlan_id3, vlan_name3,
                 vlan_id4, vlanName4):          
        self.onu_number = onu_number
        self.ip = ip
        self.vlan_name = vlan_name
        self.vlan_id = vlan_id
        self.serial = serial
        self.pon = pon
        self.vlan_ger = vlan_ger
        self.vlan_id3 = vlan_id3
        self.vlan_name3 = vlan_name3
        self.vlan_id4 = vlan_id4
        self.vlan_name4 = vlanName4
        
    def to_dict(self):        
        return {
            'onu_number': self.onu_number,
            'ip' : self.ip,
            'vlan_name' : self.vlan_name,
            'vlan_id' : self.vlan_id,
            'serial' : self.serial,
            'pon': self.pon,
            'vlan_ger' : self.vlan_ger,
            'vlan_id3': self.vlan_id3,
            'vlan_name3': self.vlan_name3,
            'vlan_id4': self.vlan_id4,
            'vlanName4': self.vlan_name4
        }