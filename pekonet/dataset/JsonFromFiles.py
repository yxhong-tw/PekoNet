import json

from torch.utils.data import Dataset


# Checked.
class JsonFromFiles(Dataset):
    def __init__(self, config, task, encoding='UTF-8', *args, **kwargs):
        self.file = config.get('data', f'{task}_file_path')
        self.data = []

        with open(file=self.file, mode='r', encoding=encoding) as json_file:
            for line in json_file:
                self.data.append(json.loads(line))


    def __getitem__(self, index):
        return self.data[index]


    def __len__(self):
        return len(self.data)
