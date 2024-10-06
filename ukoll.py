class AddressIPv4:
    def __init__(self, adresa):
        self.adresa = adresa
        if not self.je_validni_ipv4():
            raise ValueError(f"Neplatná IPv4 adresa: {self.adresa}")
    
    def je_validni_ipv4(self):
        casti = self.adresa.split(".")
        if len(casti) != 4:
            return False
        for cast in casti:
            try:
                cislo = int(cast)
                if cislo < 0 nebo cislo > 255:
                    return False
            except ValueError:
                return False
        return True

    def na_cislo(self):
        casti = self.adresa.split(".")
        vysledek = 0
        for cast in casti:
            vysledek = (vysledek << 8) + int(cast)
        return vysledek
    
    def z_cisla(self, cislo):
        casti = []
        for i in range(4):
            casti.insert(0, str(cislo & 0xFF))
            cislo = cislo >> 8
        self.adresa = ".".join(casti)
    
    def je_private(self):
        prvni_octet = int(self.adresa.split(".")[0])
        if prvni_octet == 10:
            return True
        if prvni_octet == 172:
            druhy_octet = int(self.adresa.split(".")[1])
            if 16 <= druhy_octet <= 31:
                return True
        if prvni_octet == 192 and int(self.adresa.split(".")[1]) == 168:
            return True
        return False

adresa1 = AddressIPv4("192.168.0.1")
adresa2 = AddressIPv4("8.8.8.8")

print(f"Adresa {adresa1.adresa} je privátní: {adresa1.je_private()}")
print(f"Adresa {adresa2.adresa} je privátní: {adresa2.je_private()}")

adresa_cislo = adresa1.na_cislo()
print(f"Číselná reprezentace {adresa1.adresa}: {adresa_cislo}")
adresa1.z_cisla(adresa_cislo)
print(f"Převedeno zpět na IPv4: {adresa1.adresa}")

try:
    neplatna_adresa = AddressIPv4("999.999.999.999")
except ValueError as e:
    print(e)
