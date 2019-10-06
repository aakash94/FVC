class CustomTransform(object):
    """
    Apply feature selection or any other algorithm or function to the input
    """

    def __init__(self, input_size = 32*32*5, output_size = 16*5*5):
        self.input_size = input_size
        self.output_size = output_size

    def __call__(self, sample):
        return sample