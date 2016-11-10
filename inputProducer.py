





class InputProducer:
    """
    * Produce sequences of trainning data
    for offline traning the domain independent 
    shared layers.

     
    """

    def __init__(self, K):

        self.num_vids = K # number of 
        # Load trainning samples into memeory for 
        # all given video.
        self.vid_samples = self._vid_samples()


    
    def _samples_from_img(self, img, gt):
        """
        Sample positive and negative samples in an image.
        In offline trainning phase, sample 50 and 200
        positive and negative samples which has IoU > 0.7 and 
        IoU <0.5 respectively in a given frame.

        Returns:
            pos_samples: np.ndarray with shape (50,  ,  , 3)
        """
        pass
    
    def _vid_samples(self):
        """
        Returns samples in videos
        
        Returns:
            vid_samples: list of tuples, with length equal to 
                the number of videos, each element is a 
                length 2 tuple [positive sample, negative samples]
                which are np.ndarry with shape [50*number of frames, , ,3]
                [200*number of frames, , , 3] respectively.
        """

        pass



    def hard_minibatch_mining(self, mdnet, k):
        """
        Generate a batch of sample, in which 96 negative samples
        are hard mined from 1024 negative sample pools, there are 
        32 positive samples.

        Args:
            k: int, iter numbers in offline training porcess.
        Returns:
            batch_sample: np.array with shape []
        """
        
        # Picks corresponding vid 
        vid_idx = k % self.num_vids
        current_vid_samples = self.vid_samples[vid_idx]
        
        # Select positive samples in order
        num_cycles = k // self.num_vids
        
        
    
    def 
        
        
        

        return mini_batch_squences
    
    def sample_roi(self):
        """
        Given a new frame. Returns a list of roi around 
        the previous target location.
        """

        return lsit of rois

