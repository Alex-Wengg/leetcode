class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        rec_ingred = { r : i for r, i in zip(recipes, ingredients)}
        supplies = set(supplies)
        visited = set()
        can_make = {} 
        def dfs(recipe):
            # If we've already determined whether we can make this recipe, return the result.
            if recipe in can_make:
                return can_make[recipe]

            can_make[recipe] = False  # Initially mark as False to handle circular dependencies.

            # Check if all ingredients are available or can be made.
            for ingredient in rec_ingred[recipe]:
                if ingredient not in supplies and (ingredient not in rec_ingred or not dfs(ingredient)):
                    return False

            can_make[recipe] = True  # If we reach here, all ingredients are available/makeable.
            return True
        
        cnt = []
        for recipe in recipes:
            if dfs(recipe):
                cnt.append(recipe)
        return cnt