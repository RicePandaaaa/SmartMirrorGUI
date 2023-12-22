# SmartMirrorGUI
This is a super basic "smart" mirror consisting of a two-way mirror, a Raspberry Pi 4, and a 5 inch LCD display. This project is for me to learn the basics of coding for the Raspberry Pi and building something useful in a more hands-on way. The display is connected to the Raspberry Pi, and the two together are connected to the mirror. A program is run on the Raspberry Pi to display a simple UI that shows the following:
<ul>
  <li>My classes for the day, if any</li>
  <li>Date, time (in 24 hour format), and weekday</li>
  <li>Daily weather data pulled from the Accuweather API</li>
  <ul>
    <li>Location</li>
    <li>High and low temperature</li>
    <li>Chance of rain during day and night (yes/no rather than actual percentages)</li>
  </ul>
  <li>Personalized motivational quote</li>
</ul>

Images and videos of the smart mirror and its testing can be found here: https://drive.google.com/drive/folders/1fKuFB-DmoJCYsCERF0bf0Bkw4F1Ws2tu?usp=sharing

## PyQt5 Version

This version serves as a visual improvement of the [Tkinter version](https://github.com/RicePandaaaa/SmartMirrorGUI/blob/main/README.md#tkinter-version). I consulted [@alexofthewu](https://github.com/alexofthewu) to help create the new UI, and that UI is implemented in this PyQt version.

The code in `qt_main_gui.py` loads the UI stored in `mirror.ui` (which is generated in QT Designer). The code in the program uses PyQt6 but due to incompatabilities with the Raspberry Pi 4, the actual code uses PyQt5. This means that the only changes necessary is to adjust the module name in the `import` statements from "PyQt6" to "PyQt5". Furtherfore, the font sizes are also slightly adjusted (all font sizes reduced by 2, with the exception of the text for the rain chance, which is reduced by 10).

## Tkinter Version
The rest of the files are for the prototype version of the UI. Instead of PyQt6, I used Tkinter to create a very quick and simple UI that displays the same information. 
