# PyQt5_Calculator

GUI Calculator in Python using PyQt5 Library.


![Python Calculator 2023-05-24 00-56-43](https://github.com/gupta07ayush/PyQt5_Calculator/assets/29086241/9783e641-1cb1-4435-a111-f41c767616d8)


## GUI implementation steps

- Create a label to show the numbers and the output and set its geometry
- Align the label text from right side and increase the font size of it
- Create push buttons for the numbers from 0 to 9 and set their geometry in the proper order
- Create operator push button example for addition, subtraction etc
- Add a color effect to the equals button to highlight it

## Back end implementation steps

- Add action to each button
- Inside the actions of each button except the equals to action, append the text of the label with the respective number or the operator
- Inside the equals to action get the text of the label and start the try except block
- Inside the try block use eval method on the label text to get the ans and set the answer to the label
- Inside the except block set “Wrong Input” as text
- For delete action make the last character removed from the label and for the clear action set the whole text to blank.

https://github.com/gupta07ayush/PyQt5_Calculator/assets/29086241/e7325b83-fedc-4d2b-a440-839d2fa9c2ab
