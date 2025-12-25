
This is the code for the wall display "HELLO CODE." 

[View it in action.](https://youtu.be/2RdOh8mkhuI)

## Create the Code Dictionary
 
*Do this only one time for each title. Right now, I've done this only for Title
26, and that is the only dictionary in the repository.*

Download the relevant XML file for the title you have selected from the [Office of Law Revision
Counsel](https://uscode.house.gov/). Save it as ```usc{titlenumber}.xml```.

Create the code dictionary from your title by running ```python
create_json_dict.py {titlenumber}```.

## Running the Program

```pull-random.py``` picks a random section from the code dictionary
(```Code26Dictionary.json``` for the tax code) and
sends the random section to the LCD screens. 

## Considerations re Code and Setup

The code reflects the specific I2C expander chip (PCF8574) and addresses (0x27
and 0x26) for my hardware; yours may differ.

I have added details about setting up the new project in
```setup_new_project.md```, mostly for myself to remember, so it's specific to
my operating system, computer, WiFi network, etc. It shows how to configure
```pull-random.py``` to run on boot, among other things; that's what the
```hellocode.service``` file is for.
