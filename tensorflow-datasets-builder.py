import tensorflow_datasets as tfds
import os
import random

emoji_names = [
  "beaming-face.png",
  "cloud.png",
  "face-spiral.png",
  "flushed-face.png",
  "grimacing-face.png",
  "grinning-face.png",
  "grinning-squinting.png",
  "heart.png",
  "pouting-face.png",
  "raised-eyebrow.png",
  "relieved-face.png",
  "savoring-food.png",
  "smiling-heart.png",
  "smiling-horns.png",
  "smiling-sunglasses.png",
  "smiling-tear.png",
  "smirking-face.png",
  "tears-of-joy.png",
]

class EmojiDataset(tfds.core.GeneratorBasedBuilder):
    VERSION = tfds.core.Version('0.1.0')

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            supervised_keys=('image', 'label'),
            features=tfds.features.FeaturesDict({
                'image': tfds.features.Image(shape=(400, 400, 4)),
                'label': tfds.features.ClassLabel(names=emoji_names), # Define your class names here
            }),
        )

    def _split_generators(self, dl_manager):
        # Load and return data splits
        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                gen_kwargs={'data_dir': './images'}
            ),
        ]

    def _generate_examples(self, data_dir):
        # Iterate through directories and yield (image, label) pairs
        for filename in random.shuffle(os.listdir(data_dir)):
            if (not filename.endswith("png")):
               continue
            image_path = os.path.join(data_dir, filename)
            yield filename, {
                'image': image_path,
                'label': emoji_names[int(filename.split("-")[0])],
            }

tfds.builder("emoji_dataset")



