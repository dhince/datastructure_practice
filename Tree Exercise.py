class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, data):
        data.parent = self
        self.children.append(data)

    def get_level(self):
        level = 0
        itr = self.parent

        while itr:
            level += 1
            itr = itr.parent
        return  level

    def print_tree(self):
        pass


def build_tree():
    root = TreeNode(('Nilupul', 'CEO'))

    cto = TreeNode(('Chinmay', 'CTO'))

    infrastructure_head = TreeNode(('Vishwa', 'Infrastructure Head'))
    infrastructure_head.add_child(TreeNode(('Dhaval', 'Cloud Manager')))
    infrastructure_head.add_child(TreeNode(('Abhijit', 'App manager')))

    application_head = TreeNode(('Aamir', 'Application Head'))

    cto.add_child(infrastructure_head)
    cto.add_child(application_head)

    HR_Head = TreeNode(('Gels', 'HR Head'))
    HR_Head.add_child(TreeNode(('Peter', 'Recruitment Manager')))
    HR_Head.add_child(TreeNode(('Waqas', 'Policy Manager')))

    root.add_child(cto)
    root.add_child(HR_Head)

    return root


if __name__ == '__main__':
    tree = build_tree()
