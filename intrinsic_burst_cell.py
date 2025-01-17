import izhikevich_cells as izh


class ibCell(izh.izhCell):
    def __init__(self,stimVal):
        # Define Neuron Parameters
        super().__init__(stimVal)
        self.celltype='Intrinsic Burst' # Regular spiking
        self.C=150
        self.vr=-75
        self.vt=-45
        self.k=1.2
        self.a=0.01
        self.b=5
        self.c=-56
        self.d=130
        self.vpeak=50
        self.stimVal = stimVal
    
        
myCell = ibCell(stimVal=4000)        
myCell.simulate()
    
    
if __name__=='__main__':
    izh.plotMyData(myCell)