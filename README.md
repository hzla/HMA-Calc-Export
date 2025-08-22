For exporting data for Dynamic Calc https://github.com/hzla/Dynamic-Calc

![image](https://github.com/user-attachments/assets/f9810736-6cf9-4540-b330-127344a8ceb1)


# How To Use
Install ruby https://rubyinstaller.org/

Copy the files in this repo into your HMA folder. Copy paste the contents of `hma_scripts.py` into Hex Maniac Advance's automation tool. 

![image](https://github.com/user-attachments/assets/2c739afc-aec2-43de-9b96-f3d2ab63dd3d)

Click `run`

navigate inside your Hex Maniac Advance's folder with command prompt or power shell and run `ruby ./parse.rb`

You will need to install ruby if you don't have it. https://rubyinstaller.org/

This will output a json file called `npoint.json` into the same folder as HMA

copy paste contents of `npoint.json` to the json hosting website npoint.io 
Save your json document and copy the document id in the url 
![image](https://github.com/hzla/pk3ds_for_dynamic_calc/assets/5680299/f8e9dac8-2737-49e9-bce6-914f2bf4a912)

your calc should now be available at: https://hzla.github.io/Dynamic-Calc/?data=COPY_DOCUMENT_ID_TO_HERE&dmgGen=3&gen=3&noSwitch=1&types=3

If you have added in moves or pokemon from past your game's generation, set gen in the url to 8.

replace COPY_DOCUMENT_ID_TO_HERE with your document id you copied earlier

# Further Customization

Again, If you have added in moves or pokemon from past your game's generation, SET GEN IN URL TO 8.

You can set a title for your calc by setting the `title` property in your npoint data source

If you have replaced moves in your rom, you can add a `move_replacements` property.

If you have replaced pokemon, you can add a `poks_replacements` property. 

You can follow this example format 

```
{"title": "YOUR TITLE",
  "move_replacements": {
    "Vice Grip": "Head Smash",
    "Guillotine": "Bullet Punch",
    "Fury Attack": "Bug Buzz",
    "Horn Drill": "Drill Run",
    "Wrap": "Aqua Jet",
    "Fissure": "Earth Power",
    "Smog": "Dark Pulse",
    "Skull Bash": "2x-Ironbash",
    "Sky Attack": "Brave Bird",
    "Thief": "Night Slash",
    "Nightmare": "Ominous Wind",
    "Fury Cutter": "X-Scissor",
    "Stockpile": "Fire Pledge",
    "Arm Thrust": "Force Palm",
    "Ice Ball": "Ice Shard",
    "Astonish": "Shadow Sneak",
    "Air Cutter": "Air Slash",
    "Metal Sound": "Flash Cannon",
    "Sheer Cold": "Draco Meteor",
    "Icicle Spear": "Icicle Crash",
    "Covet": "Dualwingbeat",
  },
  "poks_replacements": {
   "Slowpoke": "Slowpoke-Galar",
   "Slowbro": "Slowbro-Galar",
   "Slowking": "Slowking-Galar",
   "Sneasel": "Sneasel-Hisui",
   "Ditto": "Overqwil",
   "Qwilfish": "Qwilfish-Hisui",
   "Smeargle": "Sneasler",
   "Chimecho": "Melmetal",
   "Far'fetched": "Meltan",
   "Sandshrew": "Sandshrew-Alola",
   "Sandslash": "Sandslash-Alola",
   "Voltorb": "Voltorb-Hisui",
   "Electrode": "Electrode-Hisui",
   "Exeggutor": "Exeggutor-Alola",
   "Growlithe": "Growlithe-Hisui",
   "Arcanine": "Arcanine-Hisui",
   "Raichu": "Raichu-Alola",
  },"poks":{"Bulbasaur":{...auto generated data goes here

```


