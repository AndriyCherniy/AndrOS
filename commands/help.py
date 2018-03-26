import command.command
import os

class Help(command.command.Command):

    def answer(self,agvs,commandManager):
        print(commandManager.commandConfig.config[commandManager.commandConfig.get_lang()])
        for cmd in commandManager.get_modules():
            helper = cmd.get_helper()
            if len(helper) > 0:
                print(helper)
            else:
                print(cmd.get_command())