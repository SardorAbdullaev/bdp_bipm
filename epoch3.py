import vgg16# reload(vgg16)
from vgg16 import Vgg16
vgg = Vgg16()

images_path = "~/data/images_224/"
batch_size=64

batches = vgg.get_batches(images_path+'train')
val_batches = vgg.get_batches(images_path+'valid')

vgg.finetune(batches)
vgg.fit(batches,val_batches, nb_steps=5000, nb_epoch=3)