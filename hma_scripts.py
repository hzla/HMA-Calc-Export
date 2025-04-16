# GET LEVELUP DATA

HMAData = open("learnset.json", "w")
HMAData.write('{')
for monIndex in range(1, len(data.pokemon.stats)):
    if data.pokemon.names[monIndex].name != '?':
        HMAData.write('\n\t"' + data.pokemon.names[monIndex].name.replace("\\sm", "-M").replace("\\sf", "-F").upper() + '":\n\t{\n\t\t"Level-Up Learnset":\n\t\t[')
        movesFromLevelLen = 0
        for movesFromLevel in data.pokemon.moves.levelup[monIndex].movesFromLevel:
            if movesFromLevelLen < len(data.pokemon.moves.levelup[monIndex].movesFromLevel) - 1:
                try:
                    HMAData.write('\n\t\t\t[' + str(movesFromLevel.pair.level) + ', "' + data.pokemon.moves.names[movesFromLevel.pair.move].name + '"],')
                except:
                    HMAData.write('\n\t\t\t[' + str(movesFromLevel.level) + ', "' + data.pokemon.moves.names[movesFromLevel.move].name + '"],')

            else:
                try:
                    HMAData.write('\n\t\t\t[' + str(movesFromLevel.pair.level) + ', "' + data.pokemon.moves.names[movesFromLevel.pair.move].name + '"]')
                except:
                    HMAData.write('\n\t\t\t[' + str(movesFromLevel.level) + ', "' + data.pokemon.moves.names[movesFromLevel.move].name + '"]')


            movesFromLevelLen = movesFromLevelLen + 1
        if monIndex < len(data.pokemon.stats) - 1:
            HMAData.write('\n\t\t]\n\t},')
        else:
            HMAData.write('\n\t\t]\n\t}')
HMAData.write('\n}')
HMAData.close()

print("learnsets dumped")


# Get Moves

HMAData = open("moves.txt", "w")
types = ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Water","Grass","Electric","Psychic","Ice","Dragon","Dark"]
for movIndex in range(1, len(data.pokemon.moves.stats.battle)):
    movType = data.pokemon.moves.stats.battle[movIndex].type.replace("~","")
    moveInfo = f"{data.pokemon.moves.names[movIndex].name}| {data.pokemon.moves.stats.battle[movIndex].power}| {movType}\n"
    HMAData.write(moveInfo)

HMAData.close()

#  Get Mondata stats/types

output_file_path = "PokemonStats.txt"

output_data = ""

for (Fakemon, Name) in zip (data.pokemon.stats, data.pokemon.names):
    try:
        output_data += "\n"+str(Name)+"\n"
        if Fakemon.type1 == Fakemon.type2:
            output_data += str(Fakemon.type1)
        else:
            output_data += str(Fakemon.type1) +"/"+ str(Fakemon.type2)
        output_data += "\n\tHP " + str(Fakemon['hp'])+ "\n\tDEF " + str(Fakemon['def']) + "\n\tATT " + str(Fakemon['attack']) + "\n\tSP " + str(Fakemon['speed']) + "\n\tSPA " + str(Fakemon['spatk']) + "\n\tSPD " + str(Fakemon['spdef'])
        output_data += "\n\tCatch Rate " + str(Fakemon.catchRate)
        output_data += "\n\tBase Exp " + str(Fakemon.baseExp)
        output_data += "\n\tEvs "
        #TODO: Add the def evs-----------------------------------------------
        output_data += "\n\t\tHp "+ str(Fakemon.evs.hp) + ", Atk "+ str(Fakemon.evs.atk) + ", Def " +str(getattr(Fakemon.evs, 'def')) +", Spd " + str(Fakemon.evs.spd) + ", Spatk "+ str(Fakemon.evs.Spatk) + ", Spdef "+ str(Fakemon.evs.Spdef)
        output_data += "\n\tHeld Items " + str(Fakemon.item1) + "\t" + str(Fakemon.item2)
        output_data += "\n\tGender Ratio " + str(Fakemon.genderratio)
        output_data += "\n\tHatch Time " + str(Fakemon.steps2hatch)
        output_data += "\n\tBase Friendship " + str(Fakemon.basehappiness)
        output_data += "\n\tGrowth Rate " + str(Fakemon.growthrate)
        if Fakemon.egg1 == Fakemon.egg2:
            output_data += "\n\tEgg Groups "+str(Fakemon.egg1)
        else:
            output_data += "\n\tEgg Groups "+str(Fakemon.egg1) + ", " + str(Fakemon.egg2)
        if Fakemon.ability1 == "-------" and Fakemon.ability2 == "-------":
            output_data += "\n\tAbilities "+ "None"
        elif Fakemon.ability2 == "-------":
            output_data += "\n\tAbilities "+str(Fakemon.ability1)
        else:
            output_data += "\n\tAbilities "+str(Fakemon.ability1) + ", " + str(Fakemon.ability2)
        output_data += "\n\tRunrate " + str(Fakemon.runrate)
        output_data += "\n\tDex Color "+str(Fakemon.dex.color)
        output_data += "\n\tNoflip Dex? "+str(Fakemon.dex.noflip)
        output_data += "\n\n"
    except:
        pass

with open(output_file_path, "w") as output_file:
    output_file.write(output_data)

print("moves dumped")

# Trainers



output_file_path = "trainers.txt"

output_data = ""

for idx, trainer in enumerate(data.trainers.stats):
    try:

        output_data += trainer.name + "| " + trainer['class'] + "| "  + trainer.doubleBattle + "| "  + str(trainer.introMusicAndGender.female)
        if trainer.structType == "Normal":
            for mon in trainer.pokemon:
                output_data += "\n\t" + str(mon.level) + " " + mon.mon
                output_data += "\n\t" + "IVs: " + str(mon.ivSpread * 31 // 255)
                output_data += "\n\t - " + "LEARNSET"
                output_data += "\n\t - " + "LEARNSET"
                output_data += "\n\t - " + "LEARNSET"
                output_data += "\n\t - " + "LEARNSET"
                output_data += "\n"
        elif trainer.structType == "Items":
            for mon in trainer.pokemon:
                output_data += "\n\t" + str(mon.level) + " " + mon.mon + " @" + mon.item 
                output_data += "\n\t" + "IVs: " + str(mon.ivSpread * 31 // 255)
                output_data += "\n\t - " + "LEARNSET"
                output_data += "\n\t - " + "LEARNSET"
                output_data += "\n\t - " + "LEARNSET"
                output_data += "\n\t - " + "LEARNSET"
                output_data += "\n"
        elif trainer.structType == "Moves":
            for mon in trainer.pokemon:
                output_data += "\n\t" + str(mon.level) + " " + mon.mon 
                output_data += "\n\t" + "IVs: " + str(mon.ivSpread * 31 // 255)
                output_data += "\n\t - " + mon.move1
                output_data += "\n\t - " + mon.move2
                output_data += "\n\t - " + mon.move3
                output_data += "\n\t - " + mon.move4
                output_data += "\n"
        elif trainer.structType == "Both":

            for mon in trainer.pokemon:
                    output_data += "\n\t" + str(mon.level) + " " + mon.mon + " @" + mon.item
                    output_data += "\n\t" + "IVs: " + str(mon.ivSpread * 31 // 255)
                    output_data += "\n\t - " + mon.move1
                    output_data += "\n\t - " + mon.move2
                    output_data += "\n\t - " + mon.move3
                    output_data += "\n\t - " + mon.move4
                    output_data += "\n"
        output_data += "\n"
    except:
        pass

with open(output_file_path, "w") as output_file:
        output_file.write(output_data)
print(f"Trainers dumped")


# Number of TMs
num_tms = 50  # First 50 are TMs

# Define your tutor_move_list here
tutor_move_list = [
    "MEGA PUNCH", "SWORDS DANCE", "MEGA KICK", "BODY SLAM", "DOUBLE-EDGE",
    "COUNTER", "SEISMIC TOSS", "MIMIC", "METRONOME", "SOFTBOILED", "DREAM EATER",
    "THUNDER WAVE", "EXPLOSION", "ROCK SLIDE", "SUBSTITUTE"
]

# Define your tm_move_list here
tm_move_list = [
    "FOCUS PUNCH", "DRAGON CLAW", "WATER PULSE", "CALM MIND", "ROAR", "TOXIC", "HAIL", "BULK UP", 
    "BULLET SEED", "HIDDEN POWER", "SUNNY DAY", "TAUNT", "ICE BEAM", "BLIZZARD", "HYPER BEAM", 
    "LIGHT SCREEN", "PROTECT", "RAIN DANCE", "GIGA DRAIN", "SAFEGUARD", "FRUSTRATION", "SOLARBEAM", 
    "IRON TAIL", "THUNDERBOLT", "THUNDER", "EARTHQUAKE", "RETURN", "DIG", "PSYCHIC", "SHADOW BALL", 
    "BRICK BREAK", "DOUBLE TEAM", "REFLECT", "SHOCK WAVE", "FLAMETHROWER", "SLUDGE BOMB", "SANDSTORM", 
    "FIRE BLAST", "ROCK TOMB", "AERIAL ACE", "TORMENT", "FACADE", "SECRET POWER", "REST", "ATTRACT", 
    "THIEF", "STEEL WING", "SKILL SWAP", "SNATCH", "OVERHEAT", "CUT", "FLY", "SURF", "STRENGTH", 
    "FLASH", "ROCK SMASH", "WATERFALL", "DIVE"
]



# Open the file in write mode (this will create or overwrite the file)
with open("moves.json", "w") as HMAData:
    HMAData.write('{')

    # Iterate over each Pokémon
    for monIndex in range(1, len(data.pokemon.stats)):
        if data.pokemon.names[monIndex].name != '?':
            HMAData.write(f'\n\t"{data.pokemon.names[monIndex].name}":\n\t{{\n\t\t"Level-Up Learnset":\n\t\t['.replace("\\sm", "-M").replace("\\sf", "-F"))
            
            # Level-up Learnset (unchanged)
            movesFromLevelLen = 0
            for movesFromLevel in data.pokemon.moves.levelup[monIndex].movesFromLevel:
                if movesFromLevelLen < len(data.pokemon.moves.levelup[monIndex].movesFromLevel) - 1:
                    try:
                        HMAData.write(f'\n\t\t\t["{data.pokemon.moves.names[movesFromLevel.pair.move].name}", {movesFromLevel.pair.level}],')
                    except:
                        HMAData.write(f'\n\t\t\t["{data.pokemon.moves.names[movesFromLevel.move].name}", {movesFromLevel.level}],')   
                else:
                    try:
                        HMAData.write(f'\n\t\t\t["{data.pokemon.moves.names[movesFromLevel.pair.move].name}", {movesFromLevel.pair.level}]')
                    except:
                        HMAData.write(f'\n\t\t\t["{data.pokemon.moves.names[movesFromLevel.move].name}", {movesFromLevel.level}]') 
                movesFromLevelLen += 1

            # TM Moves Compatibility
            HMAData.write('\n\t\t],\n\t\t"TM Moves Compatibility":\n\t\t[')

            # Access TM compatibility data (ModelTupleElement)
            tm_compat_data = data.pokemon.moves.tmcompatibility[monIndex].moves  # Access compatibility data for TMs
            
            tmCompatLen = 0
            for idx, move_name in enumerate(tm_move_list):
                try:
                    is_compatible = tm_compat_data[move_name]  # Check compatibility using move_name

                    # Prefix TMs and HMs with proper numbering
                    if idx < num_tms:
                        move_prefix = f"TM {str(idx + 1).zfill(2)} - "  # TM prefix for first 50 moves
                    else:
                        move_prefix = f"HM {str(idx - num_tms + 1).zfill(2)} - "  # HM prefix for the rest

                    if is_compatible == 1:
                        if tmCompatLen < len([val for val in tm_move_list if tm_compat_data[val] == 1]) - 1:
                            HMAData.write(f'\n\t\t\t"{move_prefix}{move_name}",')
                        else:
                            HMAData.write(f'\n\t\t\t"{move_prefix}{move_name}"')  # No comma for the last one
                        tmCompatLen += 1
                except Exception as e:
                    print(f"Failed to access TM move compatibility for {move_name}: {e}")
            HMAData.write('\n\t\t]')

            # Close current Pokémon data
            if monIndex < len(data.pokemon.stats) - 1:
                HMAData.write('\n\t},')
            else:
                HMAData.write('\n\t}')
    
    HMAData.write('\n}')

print("tms dumped")