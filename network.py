




class MDNet:
    """
    Class of MDNet, contans the network structure,
    off-line traning method as well as online long
    & short term finetune methods.
    
    """

    def __init__(self):
        """
        Register ops and tensors to default graph.
        """
        
        self.vars_finetune = None
        self.vars_shared = None
        self.track_fail = False

        pass
    
    def train_shared_layers(self):
        """
        Offline porcedure, for traning the domain
        independent layers, i.e. conv layers and fc3-5
        layers.
        """
        pass
    
    def tracking(self):
        """
        In online tracking phase, the multiple branches of 
        domain-specific layers  (fc6k) are replace with a 
        single branch fc6 for a new test sequence.
        
        """
        pass

    
    def 

    def shortterm_finetune(self):
        """
        When the estimated target is classfied as background. 
        Finetune the net using the positives samples in a short
        -term period.
        
        """
        assert self.track_fail
        
        pass
    

    def longterm_finetune(self):
        pass
    


class BBoxRegressor:
    """
    Ridge regressor for bounding
    box estimation.
    """
    def __init__(self):
        """
        Initialize the regressor network.
        """
        pass
    
    def train(self):
        """
        Trains the regressor on the first frame.
        
        """

    def estmate(self):
        """
        Returns the predicted bounding box.
        
        """



    