# Add Voice on Music without Lowering the Volume 
 ___
Who hasn’t been irritated to hear the music volume lowering or even turning off when the GPS voice is heard? One technique is to apply a Gaussian blur to the part of the music sample played along with the voice. To illustrate the effectiveness of this method, we see on the left a text on a sharp image, and on the right a text on the same picture, but blurred: 
 
![Blur example](blur.jpg)
 
We notice that it is easier and less tiring to read the text on the right on the blurred picture than on the sharp image. 
 
It’s about the same thing with music, here is a Python 3.* code allowing to obtain a result once with a simple superimposition of the voice and the music, and once with a blurred musical background with a crescendo entry. Here we assume that the sample rates are the same (if not, see: Documentation) 
 ___
**Tip**: Mute the silent part at the beginning and end of the voice audio. 
