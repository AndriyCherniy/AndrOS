import command.command
import os

class Changelog(command.command.Command):
    def answer(self, agvs, commandManager):
        print(open(os.getcwd() + os.sep + "changelog.txt", "r").read())