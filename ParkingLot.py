import argparse
import sys
from datetime import datetime

import Vehicle


class ParkingLot:
    def __init__(self):
        self.capacity = 0     # Capacity of the Parking Lot
        self.lotId = 0        # Lot ID
        self.occupancy = 0    # Number of slots occupies
        self.name = 'Name'    # To create multiple parking lots

        
    def createParkingLot(self,capacity):
        self.slots = [-1] * capacity
        self.capacity = capacity
        return self.capacity
    
    # Get the available empty slots in a parking lot
    def availableSlot(self):
        for i in range(len(self.slots)):
            if self.slots[i]== -1:
                return i
    
    # 
    def park(self,regNo,color,vehicleType):
        if self.occupancy < self.capacity:
            lotId = self.availableSlot()
            if(vehicleType == 'TwoWheeler'):
                self.slots[lotId] = Vehicle.TwoWheeler(regNo,color)
            if(vehicleType == 'HatchBack'):
                self.slots[lotId] = Vehicle.HatchBack(regNo,color)
            if(vehicleType == 'SuvCar'):
                self.slots[lotId] = Vehicle.SuvCar(regNo,color)
            self.lotId = self.lotId+1
            self.timeIn = datetime.now()
            self.occupancy = self.occupancy + 1
            return lotId+1
        
        else:
            return -1
    
    def moveOut(self,lotId):
        if self.occupancy > 0 and self.slots[lotId-1] != 1:
            self.slots[lotId-1] = -1
           # self.timeOut = datetime.now()replace(microsecond=0)
            self.occupancy = self.occupancy - 1 
           # self.price = priceCharged(self.timeIn, self.timeOut)
           # if (0 < (timeOut - timeIn) <= 2):
           #     charge = 20
           # if( 2 < (timeOut - timeIn) <= 4):
           #     charge = 40

            return True
    
        else: 
            return False

    def priceCharged(self, timeIn, timeOut):
        if (0 < (timeOut - timeIn) <= 2):
            charge = 20
        if( 2 < (timeOut - timeIn) <= 4):
            charge = 40
        return charge

    def status(self):
        print("Slot Number \t Registration Number \t Color")
        for i in range(len(self.slots)):
            if self.slots[i] != -1:
                print(str(i+1) + "\t\t" +str(self.slots[i].regNo) + "\t\t" + str(self.slots[i].color) )
            else:
                continue

    def getRegNoFromColor(self,color):
        regNos=[]

        for i in self.slots:
            if i== -1:
                continue
            if i.color == color:
                regNos.append(i.regNo)
        return regNos

    def getSlotNoFromRegNo(self,regNo):
        for i in range(len(self.slots)):
            if self.slots[i].regNo == regNo:
                return i+1
            else:
                continue
        return -1 
			
    def getgetSlotNoFromColor(self,color):
        slotNos = []

        for i in range(len(self.slots)):
            if self.slots[i].color == color:
                slotNos.append(str(i+1))
        return slotNos

    def getRegNoFromVehicleType(self,vehicleType):
        regNos = []
        for i in self.slots:
            if i == -1:
                continue
            if i.vehicleType == vehicleType:
                regNos.append(i.regNo)
        return regNos

    def getSlotNoFromVehicleType(self,vehicleType):
        slotNos = []
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                continue
            if self.slots[i].vehicleType == vehicleType:
                slotNos.append(str(i+1))
        return slotNos

    def show(self,line):
        if line.startswith('create_parking_lot'):
            n = int(line.split(' ')[1])
            res = self.createParkingLot(n)
            print('Created a parking lot with '+str(res)+' slots')

        elif line.startswith('park'):
            regNo = line.split(' ')[1]
            color = line.split(' ')[2]
            vehicleType = line.split(' ')[3]
            res = self.park(regNo,color,vehicleType)
            if res == -1:
                print("Sorry, parking lot is full")
            else:
                print('Allocated slot number: '+str(res))

        elif line.startswith('leave'):
            leave_slotid = int(line.split(' ')[1])
            status = self.moveOut(leave_slotid)
            if status:
                print('Slot number '+str(leave_slotid)+' is free')

        elif line.startswith('status'):
            self.status()

        elif line.startswith('registration_numbers_for_vehicles_with_colour'):
            color = line.split(' ')[1]
            regnos = self.getRegNoFromColor(color)
            print(', '.join(regnos))

        elif line.startswith('slot_numbers_for_vehicles_with_colour'):
            color = line.split(' ')[1]
            slotnos = self.getSlotNoFromColor(color)
            print(', '.join(slotnos))

        elif line.startswith('slot_number_for_registration_number'):
            regno = line.split(' ')[1]
            slotno = self.getSlotNoFromRegNo(regno)
            if slotno == -1:
                print("Not found")
            else:
                print(slotno)
        elif line.startswith('exit'):
            exit(0)

def main():
    parkinglot = ParkingLot()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action="store", required=False, dest='src_file', help="Input File")
    args = parser.parse_args()
	
    if args.src_file:
        with open(args.src_file) as f:
            for line in f:
                line = line.rstrip('\n')
                parkinglot.show(line)
    else:
        while True:
            line = input("$ ")
            parkinglot.show(line)

if __name__ == '__main__':
    main()