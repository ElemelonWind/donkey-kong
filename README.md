# donkey-kong

Making a computer smarter than a chimpanzee (and also humans) by making it good at [human benchmark](https://humanbenchmark.com/) challenges. Install required libraries via requirements.txt. You'll need to install [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) (which does optical character recognition) for the chimp test, and may need to upgrade the selenium (which handles browser automation) based on your Chrome version.

## Chimp Test

This test is a number memory test, where number tiles are shown on a grid and then hidden. The user must then click on the tiles in ascending order of the numbers on them.

Our approach to this involved taking a screenshot of the screen using `pyautogui` and then using `pytesseract` to extract the numbers from the image after segmenting it into individual tiles. We then sorted the numbers and clicked on the tiles in that order in an infinite loop.

## Verbal Memory

This test is another memory test, where words are displayed on the screen and the user must decide if it has been shown before or not.

Our approach to this involved opening the web browser using `selenium` and then extracting the proper components from the webpage. We added all seen words to a set and clicked the corresponding button based on whether the word was in the set or not.

## Reaction Time

This test is a reaction time test, where the user must click on the screen as soon as it turns green.

All we had to do here was check the RGB value of the screen at a certain location and click if it was green. This was slower than we wanted because we coded it in Python, but we can't be bothered to do it in C++ :)
