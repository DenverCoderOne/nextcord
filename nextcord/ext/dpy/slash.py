from nextcord.application_command import SlashApplicationCommand, SlashApplicationSubcommand, AppCmdCallbackWrapper
from typing import Union


def describe(**kwargs: str) -> Union[SlashApplicationCommand, SlashApplicationSubcommand, "DescribeWrapper"]:
    class DescribeWrapper(AppCmdCallbackWrapper):
        def modify(self, app_cmd: SlashApplicationCommand):
            option_names = {option.functional_name: option for option in app_cmd.options.values()}
            for given_name in kwargs:
                if option := option_names.get(given_name):
                    option.description = kwargs[given_name]
                else:
                    raise ValueError(f"{app_cmd.error_name} Could not find option \"{given_name}\" to describe.")

    def wrapper(func):
        return DescribeWrapper(func)
    return wrapper

