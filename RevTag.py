from git import Repo
import os

#get current git repo
repo = Repo(os.path.dirname(os.path.abspath(__file__)))

class GitTagHelper:

    def __init__(self):
        self.repo = self.get_repo()
        self.commits = self.get_commits()

    def get_repo(self):
        return Repo(os.path.dirname(os.path.abspath(__file__)))

    def get_commits(self):
        return self.repo.iter_commits('--all', max_count=10000)

    def add_tag(self, commit, tag):
        if(tag in self.repo.tags):
            return
        else:
            repo.create_tag(tag, commit, message=tag)

    def reverse_iter_commits(self):
        for commit in reversed(list(self.commits)):
            yield commit

    def remove_tag(self, tag):
        repo.delete_tag(tag)

def main():
         
    helper = GitTagHelper()

    rev = 1
    for commit in helper.commits:
        helper.add_tag(commit, 'r' + str(rev))
        rev += 1


if __name__ == '__main__':
    main()