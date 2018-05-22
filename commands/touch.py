import command.command
import os


class Touch(command.command.Command):

    def answer(self, agvs, commandManager):
        config = self.commandConfig.get_config()
        try:
            fileName = agvs[0]
            createdFile = open(commandManager.get_full_path() + os.sep + fileName, 'w')
            createdFile.close()
        except IndexError:
            errorText = 'Invalid Arguments!'
            if self.commandConfig.config.has_option(self.lang, "invalidArgument"):
                errorText = config[self.lang]["invalidArgument"]
            print(errorText)
            self.write_help()
