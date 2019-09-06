class Licence:
    def __init__(self, LicenceKey = "", LicenceType = "", PurchaseDate = "", Name = ""):
        self.__LicenceKey   = LicenceKey
        self.__LicenceType  = LicenceType
        self.__PurchaseDate = PurchaseDate
        self.__Name         = Name

    def SetLicenceKey(self, NewLicenceKey = ""):
        self.__LicenceKey = NewLicenceKey
    def SetLicenceType(self, NewLicenceType = ""):
        self.__LicenceType = NewLicenceType
    def SetPurchaseDate(self, NewPurchaseDate = ""):
        self.__PurchaseDate = NewPurchaseDate
    def SetName(self, NewName = ""):
        self.__Name = NewName

    def GetLicenceKey(self):
        return self.__LicenceKey
    def GetLicenceType(self):
        return self.__LicenceType
    def GetPurchaseDate(self):
        return self.__PurchaseDate
    def GetName(self):
        return self.__Name

class SingleUser(Licence):
    def __init__(self, MACAddress = "", RegistrationDate = ""):
        self.__MACAddress = MACAddress
        self.__RegistrationDate = RegistrationDate
        Licence.__init__(self, LicenceKey = "", LicenceType = "", PurchaseDate = "", Name = "")

    def SetMACAddress(self, NewMACAddress):
        self.__MACAddress = NewMACAddress
    def SetRegistrationDate(self, NewRegistrationDate):
        self.__RegistrationDate = NewRegistrationDate
    def GetMACAddress(self):
        return self.__MACAddress
    def GetREgistrationDate(self):
        return self.__RegistrationDate

class ThreeUser(Licence):
    def __init__(self, NoUsers = 0):
        self.__NoUsers = NoUsers        # NoUsers - number of users
        Licence.__init__(self, LicenceKey = "", LicenceType = "", PurchaseDate = "", Name = "")

    def SetNoUsers(self, NoUsers):
        self.__NoUsers = NoUsers
    def GetNoUsers(self):
        return self.__NoUsers
