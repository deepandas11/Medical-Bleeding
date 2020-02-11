from torch.utils.data import Dataset
import json
from PIL import Image


class trainloader(Dataset):
    def __init__(self, base_path='', meta_path='data_aug.json'):

        self.meta_path = meta_path
        self.base_path = base_path

        self.meta_data = json.load(open(self.meta_path))

        # with open(os.path.join('.data_aug.json')) as f:
        #     meta = json.load(f)

        self.images = list(meta.keys())

        

    def __getitem__(self, index):
        assert index <= len(self.images)
        image_file = self.images[index]
        image = Image.open(os.path.join(self.base_path, image_file)).convert("RGB")
        label = self.meta_data[image_file]['label']

        return image, label




    def __len__(self):
