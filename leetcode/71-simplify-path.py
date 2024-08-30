class Solution:
    def simplifyPath(self, path: str):
        simple_path = []

        complete_path = path.replace('//', '/').split('/')

        complete_path = [i for i in complete_path if i not in ['', '.']]

        for value in complete_path:
            if value == '..' and len(simple_path) > 0:
                simple_path.pop()
            elif value != '..':
                simple_path.append(value)

        return '/' + '/'.join(simple_path)
