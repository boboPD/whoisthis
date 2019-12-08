class CharacterData:
    def __init__(self):
        self.full_names = set()
        self.names_to_lines_mapping = {}

    def add_line_for_name(self, first_name, full_name, line):
        is_multipart_name = first_name != full_name
        if first_name not in self.names_to_lines_mapping:
            print("Found name: " + full_name)
            self.names_to_lines_mapping[first_name] = (full_name, [line], is_multipart_name)
            self.full_names.add(full_name)
        else:
            fn, lines, isfullname = self.names_to_lines_mapping[first_name]
            lines.append(line)

            if isfullname == False and is_multipart_name == True:
                print(f"{fn}, {isfullname}, {first_name}, {full_name}")
                self.full_names.remove(fn)
                self.full_names.add(full_name)
                isfullname = is_multipart_name
                fn = full_name

            self.names_to_lines_mapping[first_name] = (fn, lines, isfullname)
    
    def get_lines_for_character(self, name):
        name = name.strip().split(" ")[0]

        if name in self.names_to_lines_mapping:
            fn, lines, isfullname = self.names_to_lines_mapping[name]
            return lines
        else:
            raise ValueError(f"Name: {name} not found in db")

    def get_all_character_names(self):
        return list(self.full_names)