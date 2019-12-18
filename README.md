<img src=activity/src-carbonic.svg width=25%>

# carbonic-activity (r1)
A sugar activity derived from [carbonic](https://github.com/srevinsaju/carbonic)
which manipulates IUPAC name of Hydrocarbons, to define the structural formula.
It helps students to understand the various IUPAC name nomenclature in carbon 
structure

## Installation
* Clone the source
```git clone https://github.com/srevinsaju/carbonic-activity.git ~/Activities/Carbonic.activity```
### TODO: 
* Release a flatpak package

## Screenshots
![Screenshot of Carbonic](screenshots/screenshot1.png)
![Screenshot of Carbonic](screenshots/screenshot2.png)
![Screenshot of Carbonic](screenshots/screenshot3.png)
![Screenshot of Carbonic](screenshots/screenshot4.png)

## Features
Refer [carbonic](https://github.com/srevinsaju/carbonic) for more information

## Language
Basic IUPAC names are used for compiling,
carbonic AI uses a syntax to manipulate correctly. Refer [README.md at carbonic](https://github.com/srevinsaju/carbonic)
for more information.
The API Nomencalture is as follows:
* All alkanes, for example, `heptane`, `methane`, `pentane` can be given as-is
* All alkenes and alkynes, if the Double/Triple Bond position is not mentioned assumes the second position
  - c.f, `heptene`, `propene`
* All alkenes and alkynes can be appended with `n-` to give the bond position
  - c.f, `3-heptene` gives a heptene structure with double bond on 3rd Carbon Atom
* All functional groups like alcohol, ketone, carboxylic acid are functional in beta state.
  - c.f, `propanoic acid`, `2-hexanoic acid` , `ethanol`, etc.
* For hydrocarbon functional groups like `methyl`, `ethyl`, it requires square brackets `[]`
  - c.f `[2-methyl]pentane`, `[2-methyl,3-ethyl]5-dodecene`, etc.
NOTE: for pure hydrocarbon functional groups, use ascending order, i.e, `methyl`, `ethyl`, `propyl` ...
* Cyclic hydrocarbons and benzene can be used by appending `cyclo` to the beginning
  - c.f `cyclohexane`, `benzene`

## Future Plans
* [ ] Add suppport for Anthracine, Naphthalene compounds.
* [ ] Add exceptions to check for errors in inputed IUPAC code, currently, it manipulates whatever is inputted. The output maybe wrong if the user input doesn't follow syntax, _see [README.md at carbonic](https://github.com/srevinsaju/carbonic)_

## License
### Carbonic core 

```
carbonic on github by @srevinsaju
(c) 2019 by Srevin Saju (srevinsaju.github.io)
CARBONIC CORE AI
CONVERTS IUPAC NAMES TO CARBON STRUCTURES
SRC ON https://github.com/srevinsaju/carbonic

ALL CODE IS LICENSED UNDER GNU-AGPLv3 LICENSE. READ LICENSE FOR MORE INFORMATION

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, version 3.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

```
### Carbonic Sugar Activity 

```
carbonic-activity on github by @srevinsaju
(c) 2019 by Srevin Saju (srevinsaju.github.io)
CARBONIC-SUGAR ACTIVITY
CONVERTS IUPAC NAMES TO CARBON STRUCTURES
SRC ON https://github.com/srevinsaju/carbonic-activity

ALL CODE IS LICENSED UNDER GNU-GPLv3 LICENSE. READ LICENSE FOR MORE INFORMATION

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
```


