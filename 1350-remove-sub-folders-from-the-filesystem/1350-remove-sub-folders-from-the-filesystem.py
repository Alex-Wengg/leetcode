class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        # Initialize the list with the first folder
        result = [folder[0]]

        for f in folder[1:]:
            # If the current folder is not a subfolder of the last folder in the result list
            if not f.startswith(result[-1] + '/'):
                result.append(f)

        return result