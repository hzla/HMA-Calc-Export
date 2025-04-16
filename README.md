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

If you have added in moves from past your game's generation, set gen in the url to 8.

replace COPY_DOCUMENT_ID_TO_HERE with your document id you copied earlier


