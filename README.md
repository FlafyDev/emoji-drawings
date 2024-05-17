# Emoji drawings dataset <img src="images/0-shalev-1705925374511.png" width="50" height="50" />

This dataset features **4,945** grayscaled human-made drawings of emojis.  
Each image is ARGB PNG 400x400.  


## Instructions
All the dataset is located in the `images` directory.  

The labels of each emoji image is embedded in the file name, formatted like:
```
[emoji-index]_[creator]_[time].png
```

`[emoji-index]` - The index of the emoji from the table below. (0-17)  
`[creator]` - The person who drew the image.  
`[time]` - Time of being drawn. Milliseconds since the Epoch.  

#### For example:
```
0-shalev-1705925374511.png
```
`0` - Emoji index 0: 😁  
`shalev` - Created by "shalev"  
`1705925374511` - Was drawn on GMT Monday, January 22, 2024 12:09:34.511 PM  

## Using with Tensorflow Datasets
### Locally
Copy the Python file `emoji_drawings_tfds_builder.py` to your project's directory and add 
```py
import emoji_drawings_tfds_builder
```
to your Python file.

### In colab
Copy the contents of the file `emoji_drawings_tfds_builder.py` into a code block and run it.

### Usage
Then you'll be able to use Emoji Drawings as a tfds dataset:
```py
(ds_train, ds_valid, ds_test), ds_info = tfds.load(
    'emoji_dataset',
    split = ["train[:80%]", "train[80%:90%]", "train[90%:]"],
    shuffle_files=True,
    as_supervised=True,
    with_info=True
)
```

###### [More info for how to load custom tfds datasets](https://www.tensorflow.org/datasets/add_dataset#tldr)


## Emojis

| Index         | Emoji         | Name          | Example       |
| ------------- | ------------- | ------------- | ------------- |
| 0  | 😁 | beaming-face | <p align="center"><img src="images/0-shalev-1705823877063.png" width="70" height="70" /></p>
| 1  | ☁️ | cloud | <p align="center"><img src="./images/1-wakatta-1706048579289.png" width="70" height="70" /></p>
| 2  | 😵‍💫 | face-spiral | <p align="center"><img src="images/2-wakatta-1705954099082.png" width="70" height="70" /></p> 
| 3  | 😳 | flushed-face | <p align="center"><img src="./images/3-shalev-1705825991057.png" width="70" height="70" /></p>
| 4  | 😬 | grimacing-face | <p align="center"><img src="./images/4-shalev-1705824714843.png" width="70" height="70" /></p>
| 5  | 😃 | grinning-face | <p align="center"><img src="./images/5-shalev-1706034794303.png" width="70" height="70" /></p>
| 6  | 😆 | grinning-squinting | <p align="center"><img src="./images/6-shalev-1705785879599.png" width="70" height="70" /></p>
| 7  | ❤️ | heart | <p align="center"><img src="./images/7-shalev-1705996335618.png" width="70" height="70" /></p>
| 8  | 😡 | pouting-face | <p align="center"><img src="./images/8-wakatta-1706010757359.png" width="70" height="70" /></p>
| 9  | 🤨 | raised-eyebrow | <p align="center"><img src="./images/9-wakatta-1706049142874.png" width="70" height="70" /></p>
| 10 | 🤨 | relieved-face | <p align="center"><img src="./images/10-shalev-1705829852673.png" width="70" height="70" /></p>
| 11 | 😋 | savoring-food | <p align="center"><img src="./images/11-shalev-1705916445226.png" width="70" height="70" /></p>
| 12 | 😍 | smiling-heart | <p align="center"><img src="./images/12-shalev-1705920124671.png" width="70" height="70" /></p>
| 13 | 😈 | smiling-horns | <p align="center"><img src="./images/13-shalev-1705827136626.png" width="70" height="70" /></p>
| 14 | 😎 | smiling-sunglasses | <p align="center"><img src="./images/14-Ido-1705927330157.png" width="70" height="70" /></p>
| 15 | 🥲 | smiling-tear | <p align="center"><img src="./images/15-shalev-1705909083401.png" width="70" height="70" /></p>
| 16 | 😏 | smirking-face | <p align="center"><img src="./images/16-shalev-1705790032841.png" width="70" height="70" /></p>
| 17 | 😂 | tears-of-joy | <p align="center"><img src="./images/17-Biton-1706010508860.png" width="70" height="70" /></p>

# Credits:
| Emojis drawn | Name |
| ------------|------|
| 2064 | shalev |
| 817 | wakatta |
| 707 | Ido |
| 170 | Gil |
| 166 | kashkash |
| 153 | Biton |
| 150 | Hello |
| 77 | Name |
| 75 | Zohar |
| 69 | superyehezkel |
| 64 | Asaflevi |
| 60 | Brkzr |
| 33 | Dvir |
| 29 | Smadi |
| 28 | Nir |
| 23 | Bruh |
| 20 | S_x |
| 16 | Guy |
| 16 | deeznats |
| 15 | Yonatan |
| 15 | Ruth |
| 15 | Lulu |
| 14 | bigwolman |
| 10 | Liel |
| 10 | Adir |
| 8 | ThickNi__a |
| 8 | Liran |
| 8 | Alon |
| 7 | s_x |
| 7 | Asaflotz |
| 7 | Ariel |
| 6 | Whfkykgkg |
| 6 | Tyb |
| 6 | Omer |
| 5 | Yosi |
| 5 | UriMishkin |
| 5 | Ofir |
| 5 | Ofek |
| 4 | shani |
| 4 | Poopoolol |
| 4 | Itay |
| 4 | Hadar |
| 4 | Eyal |
| 3 | roprop |
| 3 | Ori |
| 3 | Dydya |
| 3 | amit |
| 2 | Yael |
| 2 | hdhdbdb |
| 2 | avivHamagniv |
| 2 | Argh |
| 2 | Arbel |
| 1 | yuval |
| 1 | sjjsjs |
| 1 | Biton2 |
