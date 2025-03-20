require 'json'
require_relative 'nature_calc'

mondata = File.open("PokemonStats.txt").readlines
tms = JSON.parse(File.open("moves.json").read)

ls_info = JSON.parse(File.open("learnset.json").read)

def capitalize_words(string)
  string.downcase.split(/(?<=[-\s])/).map(&:capitalize).join.gsub("\\sm", "-M").gsub("\\sf", "-F")
end

def get_moves(moves_array, current_level)
  # Filter moves that can be learned at or below the given level
  available_moves = moves_array.select { |level, _| level <= current_level }
  
  # Take last 4 moves (or all if less than 4)
  available_moves.last(4).map { |_, move| move }
end

def is_integer?(str)
  /\A-?\d+\z/.match?(str)
end

def self.showdown_subs
	{
	    "Bubblebeam": "Bubble Beam",
	    "Doubleslap": "Double Slap",
	    "Solarbeam": "Solar Beam",
	    "Sonicboom": "Sonic Boom",
	    "Poisonpowder": "Poison Powder",
	    "Thunderpunch": "Thunder Punch",
	    "Thundershock": "Thunder Shock",
	    "Ancientpower": "Ancient Power",
	    "Extremespeed": "Extreme Speed",
	    "Dragonbreath": "Dragon Breath",
	    "Dynamicpunch": "Dynamic Punch",
	    "Grasswhistle": "Grass Whistle",
	    "Featherdance": "Feather Dance",
	    "Faint Attack": "Feint Attack",
	    "Smellingsalt": "Smelling Salts",
	    "Roar Of Time": "Roar of Time",
	    "U-Turn": "U-turn",
	    "V-Create": "V-create",
	    "Sand-Attack": "Sand Attack",
	    "Selfdestruct": "Self-Destruct",
	    "Softboiled": "Soft-Boiled",
	    "Vicegrip": "Vise Grip",
	    "Hi Jump Kick": "High Jump Kick",
	}
end

types =  ["None", "Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "????", "Fire", "Water","Grass","Electric","Psychic","Ice","Dragon","Dark"]
mons = {}

mondata.each_with_index do |line, i|
	next if i == 0 or line.include?("?")
	if line.include?("{")
		species = capitalize_words(line.split(": ")[1][0..-4]).strip.gsub("-G", "-Galar").gsub("-A", "-Alola")
		mons[species] = {}

		types = mondata[i + 1].strip

		if types.include?("/")
			types = types.split("/").map {|s| s.downcase.capitalize.gsub("Fight", "Fighting").gsub("Electr", "Electric").gsub("Psychc", "Psychic")}
		else
			types = [types.downcase.capitalize.gsub("Fight", "Fighting").gsub("Electr", "Electric").gsub("Psychc", "Psychic")]
		end

		stats = {}
		stats["hp"] = mondata[i + 2].split("HP ")[1].strip.to_i
		stats["df"] = mondata[i + 3].split("DEF ")[1].strip.to_i
		stats["at"] = mondata[i + 4].split("ATT ")[1].strip.to_i
		stats["sp"] = mondata[i + 5].split("SP ")[1].strip.to_i
		stats["sa"] = mondata[i + 6].split("SPA ")[1].strip.to_i
		stats["sd"] = mondata[i + 7].split("SPD ")[1].strip.to_i


		# p species

		learnset = ls_info[species.upcase.gsub("-GALAR", "-G").gsub("-ALOLA", "-A")]["Level-Up Learnset"]

		learnset.each_with_index do |ls, i|
			ls[1] = capitalize_words(ls[1])
			if showdown_subs[ls[1].to_sym]
				ls[1] = showdown_subs[ls[1].to_sym]
			end

			learnset[i] = ls
		end

		ability = capitalize_words(mondata[i + 18].split("Abilities ")[1].split(",")[0].strip)
		mons[species]["ab"] = ability
		mons[species]["types"] = types
		mons[species]["learnset_info"] = {}
		mons[species]["learnset_info"]["learnset"] = learnset

		if tms[species.upcase.gsub("-GALAR", "-G").gsub("-ALOLA", "-A")]["TM Moves Compatibility"]
			mons[species]["learnset_info"]["tms"] = tms[species.upcase.gsub("-GALAR", "-G").gsub("-ALOLA", "-A")]["TM Moves Compatibility"].map {|m| capitalize_words(m.split(" - ")[1])}
		else
			mons[species]["learnset_info"]["tms"] = []
		end
		mons[species]["bs"] = stats
	end
end




moves_data = File.readlines("moves.txt")
moves = {}

moves_data.each do |line|
	line = line.strip.split("| ")
	move_name = capitalize_words(line[0])
	if showdown_subs[move_name.to_sym]
		move_name = showdown_subs[move_name.to_sym]
	end

	moves[move_name] = {}
	moves[move_name]["basePower"] = line[1].strip.to_i
	
	if line.length == 2
		type = "Normal"
	else
		
		if is_integer?(line[2].strip)
			type = types[line[2].strip.to_i]
		else
			type = line[2].strip.downcase.capitalize.gsub("Electr", "Electric").gsub("Psychc", "Psychic").gsub("Fight", "Fighting")
		end
	end

	moves[move_name]["type"] = type
end

moves_json = moves


trainer_data = File.readlines("trainers.txt")

formatted_sets = {}
pok_names = []

trainer_counts = {}

trainer_data.each_with_index do |line, i|
	if line[0] == "|"
		next
	end

	if line[0] =~ /[[:alnum:]]/   
		line = line.encode('UTF-8', invalid: :replace, undef: :replace).gsub(/[éèêë]/, 'e')
		tr_class = line.split("| ")[1].strip.gsub("\\pk\\mn", "Pkmn").gsub("~2", "")
		tr_name = line.split("| ")[0].strip
		battle_type = line.split("| ")[2].strip + "s"
		gender = line.split("| ")[3].strip.to_i

		tr_title = "#{capitalize_words(tr_class)} #{capitalize_words(tr_name).gsub("Terry", "Blue")}"
		
		if trainer_counts[tr_title]
			trainer_counts[tr_title] += 1
			tr_title += "#{trainer_counts[tr_title]} "
		else
			trainer_counts[tr_title] = 1
		end

		if tr_title[-1] != " "
			tr_title = tr_title + " "
		end
		


		pok_names = []

		if battle_type == "Doubles"
			type_value = 0x80
		else
			if gender == 0
				type_value = 0x88
			else
				type_value = 0x78
			end
		end

		offset = 0
		no_next_pok = !trainer_data[i + offset + 8] or ((trainer_data[i + offset + 8][0] =~ /[[:alnum:]]/ ) or (trainer_data[i + offset + 8][0] == "|")) 
		mon_count = 0

		while !no_next_pok
			pok_lvl = trainer_data[i + offset + 1].strip.split(" ")[0].to_i
			pok_name = capitalize_words(trainer_data[i + offset + 1].strip.split(" ")[1..-1].join(" ").split("@")[0].strip)

			pok_names << pok_name.upcase

			


			pok_name = pok_name.gsub("-G", "-Galar").gsub("-A", "-Alola")


			nature = calculate_nature(tr_name, pok_names, type_value)

			set_name = "Lvl #{pok_lvl} #{tr_title}"

			formatted_sets[pok_name] ||= {}
			formatted_sets[pok_name][set_name] = {}


			
			if pok_name.include?("?")
				no_next_pok = true
				next
			end

			begin
				ability = mons[pok_name]["ab"]
			rescue
				p "#{pok_name} not found on line: #{i}"
				break
			end



			
			sub_index = mon_count
			item = ""

			

			if trainer_data[i + offset + 1].include?("@")
				item = capitalize_words(trainer_data[i + offset + 1].strip.split("@")[1]).gsub("Twistedspoon", "Twisted Spoon").gsub("Brightpowder", "Bright Powder").gsub("Silverpowder", "Silver Powder")
				if item.include?("?")
					item = ""
				end
			end

			ivs = trainer_data[i + offset + 2].split(":")[1].strip.to_i

			move1 = capitalize_words(trainer_data[i + offset + 3].split("- ")[1].strip)
			if showdown_subs[move1.to_sym]
				move1 = showdown_subs[move1.to_sym]
			end

			move2 = capitalize_words(trainer_data[i + offset + 4].split("- ")[1].strip)
			if showdown_subs[move2.to_sym]
				move2 = showdown_subs[move2.to_sym]
			end

			move3 = capitalize_words(trainer_data[i + offset + 5].split("- ")[1].strip)
			if showdown_subs[move3.to_sym]
				move3 = showdown_subs[move3.to_sym]
			end

			move4 = capitalize_words(trainer_data[i + offset + 6].split("- ")[1].strip)
			if showdown_subs[move4.to_sym]
				move4 = showdown_subs[move4.to_sym]
			end

			moves = [move1, move2, move3, move4]
			if move1 == "Learnset"
				moves = get_moves(mons[pok_name]["learnset_info"]["learnset"], pok_lvl )
			end

			set_data =  {
				"evs": {
					"df": 0
				},
				"ivs": {
					"at": ivs,
			        "df": ivs,
			        "hp": ivs,
			        "sa": ivs,
			        "sd": ivs,
			        "sp": ivs
				},
				"item": item,
				"level": pok_lvl,
				"moves": moves,
				"ability": ability,
				"nature": nature,
				"sub_index": sub_index,
				"battle_type": battle_type
			}

			formatted_sets[pok_name][set_name] = set_data



			# p [pok_lvl, pok_name, item, tr_name, battle_type, gender, nature, ability, sub_index, ivs, moves]

			no_next_pok = ((!trainer_data[i + offset + 8]) or (trainer_data[i + offset + 8][0] =~ /[[:alnum:]]/ ) or (trainer_data[i + offset + 8][0] == "|"))
			mon_count += 1
			offset += 7
			
		end
	end
end


npoint = {"poks": mons, "moves": moves_json, "formatted_sets": formatted_sets}

File.write("npoint.json", npoint.to_json)