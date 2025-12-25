
This is the code for the wall display ```HELLO CODE```.

## Create the Code Dictionary
 
*Do this only one time for each title. Right now, I've done this only for Title
26, and that is the only dictionary in the repository.*

Download the relevant code from the [Office of Law Revision
Counsel](https://uscode.house.gov/). Save it as ```usc{titlenumber}.xml```.

Create the code dictionary from your title by running ```python
create_json_dict.py {titlenumber}```.

## Running the Program

```pull-random.py``` picks a random section from the code dictionary
(```CodeDictionary26.json``` for the tax code) and
sends the random section to the LCD screens. 

## Comments About Hardware

On my Pi, the program is set to run on boot.

The code has to reflect the actual LCD screen types and addresses you are using. 

The two LCD screens need to have different addresses, but if you buy two of the
same kind of screen, they'll have the same address. The current code for
sending to the LCD screens reflects that I bridged a particular set of pads to
change the address from 0x27 to 0x26. 


