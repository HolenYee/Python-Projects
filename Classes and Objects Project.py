class Computer:
    # This is the parent class for all the mac computers
    def __init__(self, name, cpu, gpu, memory, storage):
        self.name = name
        self.cpu = cpu
        self.gpu = gpu
        self.memory = memory
        self.storage = storage

    #This defines the function that prints all the specs of the computer
    def print_specs(self):
        print("Name: {}\nCPU: {}\nGraphics: {}\nMemory: {}\nStorage: {}\n".format(self.name, self.cpu, self.gpu, self.memory, self.storage))

# These are all separate classes for each type of mac that inherits attributes from the parent class
class MacBookAir(Computer):
    def __init__(self, name, cpu, gpu, memory, storage):
        Computer.__init__(self, name, cpu, gpu, memory, storage)

class MacBookPro13(Computer):
    def __init__(self, name, cpu, gpu, memory, storage):
        Computer.__init__(self, name, cpu, gpu, memory, storage)

class MacBookPro16(Computer):
    def __init__(self, name, cpu, gpu, memory, storage):
        Computer.__init__(self, name, cpu, gpu, memory, storage)

class iMac(Computer):
    def __init__(self, name, cpu, gpu, memory, storage):
        Computer.__init__(self, name, cpu, gpu, memory, storage)

class iMacPro(Computer):
    def __init__(self, name, cpu, gpu, memory, storage):
        Computer.__init__(self, name, cpu, gpu, memory, storage)

class MacMini(Computer):
    def __init__(self, name, cpu, gpu, memory, storage):
        Computer.__init__(self, name, cpu, gpu, memory, storage)

# These are all the different versions of each type of mac
air1 = MacBookAir("MacBook Air $999", "8‑Core CPU", "7‑Core GPU", "8GB", "256GB")
air2 = MacBookAir("MacBook Air $1,249", "8-Core CPU", "8-Core GPU", "8GB", "512GB")

pro13_1 = MacBookPro13('MacBook 13" $1,299', "8‑Core CPU", "8-Core GPU", "8GB", "256GB")
pro13_2 = MacBookPro13('MacBook 13" $1,499', "8-Core CPU", "8-Core GPU", "8GB", "512GB")
pro13_3 = MacBookPro13('MacBook 13" $1,799', "2.0GHz Intel Core i5 Quad-Core Processor",
                       "Intel Iris Plus Graphics", "16GB", "512GB")
pro13_4 = MacBookPro13('MacBook 13" $1,999', "2.0GHz Intel Core i5 Quad-Core Processor",
                       "Intel Iris Plus Graphics", "16GB", "1TB")

pro16_1 = MacBookPro16('MacBook 16" $2,399', "2.6GHz 6-Core Processor", "AMD Radeon Pro 5300M",
                       "16GB", "512GB")
pro16_2 = MacBookPro16('MacBook 16" $2,799', "2.3GHz 8-Core Processor", "AMD Radeon Pro 5500M",
                       "16GB", "1TB")

imac1 = iMac('iMac 21.5 inch $1,099', "2.3GHz Dual-Core Processor", "Intel Iris Plus Graphics 640",
             "8GB", "256GB")
imac2 = iMac('iMac 21.5 inch $1,299', "3.6GHz Quad-Core Processor", "Radeon Pro 555X",
             "8GB", "256GB")
imac3 = iMac('iMac 21.5 inch $1,499', "3.0GHz 6-Core Processor", "Radeon Pro 560X",
             "8GB", "256GB")
imac4 = iMac('iMac 27 inch $1,799', "3.1GHz 6-Core Processor", "Radeon Pro 5300",
             "8GB", "256GB")
imac5 = iMac('iMac 27 inch $1,999', "3.3GHz 6-Core Processor", "Radeon Pro 5300",
             "8GB", "512GB")
imac6 = iMac('iMac 27 inch $2,299', "3.8GHz 8-Core Processor", "Radeon Pro 5500 XT",
             "8GB", "512GB")

imacpro1 = iMacPro('iMac Pro $4,999', "3.0GHz 10-core Intel Xeon W processor", "Radeon Pro Vega 56",
                   "32GB", "1TB")

mini1 = MacMini('Mac Mini $699', "8-Core CPU", "8-Core GPU", "8GB", "256GB")
mini2 = MacMini('MacMini $899', "8-Core CPU", "8-Core GPU", "8GB", "512GB")
mini3 = MacMini('MacMini $1,099', "3.0GHz Intel Core i5 6-Core Processor", "Intel UHD Graphics 630",
                "8GB", "512GB")

# This while loop makes it so you can choose which computers you want to see
while True:
    areyou = input("Are you looking for a apple product? Y/N? ")
    # This asks them if they want to continue or end the program
    if areyou.lower() == "y":
        computers = (
        "1) MacBook Air", '2) MacBook Pro 13"', '3) MacBook Pro 16"', "4) iMac", "5) Mac Pro", "6) Mac Mini")
        for computer in computers:
            print(computer)
        # This gives them the list of types of computers
        selection = input("Please check out our selection. Choose number from 1-6: ")
        # This asks them what type they want
        if selection == "1":
            MacBookAir.print_specs(air1)
            MacBookAir.print_specs(air2)
        if selection == "2":
            MacBookPro13.print_specs(pro13_1)
            MacBookPro13.print_specs(pro13_2)
            MacBookPro13.print_specs(pro13_3)
            MacBookPro13.print_specs(pro13_4)
        if selection == "3":
            MacBookPro16.print_specs(pro16_1)
            MacBookPro16.print_specs(pro16_2)
        if selection == "4":
            iMac.print_specs(imac1)
            iMac.print_specs(imac2)
            iMac.print_specs(imac3)
            iMac.print_specs(imac4)
            iMac.print_specs(imac5)
            iMac.print_specs(imac6)
        if selection == "5":
            iMacPro.print_specs(imacpro1)
        if selection == "6":
            MacMini.print_specs(mini1)
            MacMini.print_specs(mini2)
            MacMini.print_specs(mini3)
        # All the versions of the type they want get printed
    if areyou.lower() == "n":
        print("Thank you come again.")
        break
        # The loop breaks if they want to stop looking at computers
