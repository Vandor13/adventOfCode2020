class Allergens:
    def __init__(self, filename: str):
        self.allergens = set()
        self.ingredients = set()
        self.ingredients_to_allergen = dict()
        self.allergen_lists = []
        self.ingredient_lists = []
        self.read_file(filename)
        self.determined_ingredients = set()
        self.determined_allergens = set()

    def read_file(self, filename: str):
        with open(filename, "r") as file:
            raw_lines = file.readlines()
        for line in raw_lines:
            line = line.rstrip(")\n")
            raw_ingredients, raw_allergens = line.split("(")
            ingredients = raw_ingredients.split()
            allergens = raw_allergens.replace(",", "").split()
            allergens.remove("contains")
            for allergen in allergens:
                self.allergens.add(allergen)
            for ingredient in ingredients:
                self.ingredients.add(ingredient)
            self.ingredient_lists.append(ingredients)
            self.allergen_lists.append(allergens)

    def determine_ingredient_allergens(self):
        while len(self.allergens) > 0:
            allergens_found = []
            # print(self.allergens)
            print(self.ingredient_lists)
            for allergen in self.allergens:
                ingredient_sets = []
                for i in range(len(self.allergen_lists)):
                    if allergen in self.allergen_lists[i]:
                        ingredient_sets.append(set(self.ingredient_lists[i]))
                ingredient = determine_common_element(ingredient_sets)
                if ingredient:
                    print("Allergen", allergen, "is in food", ingredient)
                    self.remove_ingredient(ingredient)
                    allergens_found.append(allergen)
                    self.ingredients_to_allergen[ingredient] = allergen
            for allergen in allergens_found:
                self.allergens.remove(allergen)

    def remove_ingredient(self, ingredient):
        self.ingredients.remove(ingredient)
        for ingredient_list in self.ingredient_lists:
            if ingredient in ingredient_list:
                ingredient_list.remove(ingredient)

    def determine_number_of_non_allergic_ingredients(self):
        print("There are", len(self.ingredients), "foods without allergens")
        no_of_apperances = 0
        for ingredient_list in self.ingredient_lists:
            no_of_apperances += len(ingredient_list)
        print("They appear", no_of_apperances, "times.")

    def determine_canonical_dangerous_ingredient_list(self):
        values = list(self.ingredients_to_allergen.items())
        values = sorted(values, key=lambda value: value[1])
        ingredients = [x for x, y in values]
        values_string = ",".join(ingredients)
        print("Canonical Dangerous Ingredient List:")
        print(values_string)



def determine_common_element(sets) -> str:
    if len(sets) < 1:
        return None
    merged_set = sets[0]
    for i in range(1, len(sets)):
        merged_set = merged_set & sets[i]
    if len(merged_set) == 1:
        return merged_set.pop()
    else:
        return None


allergen_object = Allergens("input21.txt")
allergen_object.determine_ingredient_allergens()
allergen_object.determine_number_of_non_allergic_ingredients()
allergen_object.determine_canonical_dangerous_ingredient_list()
