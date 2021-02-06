class Configuration:
    def __init__(self):
        super(Configuration, self).__init__()
        self.trained_model = './weights/craft_mlt_25k.pth'
        self.text_threshold = 0.7
        self.low_text = 0.4
        self.link_threshold = 0.4
        self.cuda = True
        self.canvas_size = 1280
        self.mag_ratio = 1.5
        self.poly = False
        self.show_time = False
        self.test_folder = './input'
        self.refine = False
        self.refiner_model = './weights/craft_refiner_CTW1500.pth'
        self.result_folder = './result'
