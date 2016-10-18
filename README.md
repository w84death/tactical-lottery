# P1X TACTICAL LOTTERY

Simple app for our PGA booth so customers can win some awesome prizes.

## Prizes
- 1x Racja Zywnosciowa (makaron)
- 8x light stick
- 10x rozpalka
- 80x suchary SU-1

## App frontend design

Pictures with all the prizes. 
Under each picture there is a little fake LED.
Each LED is blinking in round. Quite fast.
Then there is a button: "The lucky button".
After pressing the prize that have LED turned on in that moment is the wining one.
Prizes that are no longer available will be desatureted and LED hidden.

## App backend design

### Technology
- Python3
- Qt5

### Managing prizes
- (OPTION A) a text file with prize_id and count 
- (OPTION B) sqlite database with prizes, pictures, count