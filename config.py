from utils.suggester import SuggestionBoard
from utils.jsonx import JSONx


class colors:

    success = 0x34c789

    error = 0xff005c

    warning = 0x006aff


class emojis:

    success = "<:success:889206855321157683>"

    error = "<:error:911240678342819870>"

    warning = "<:warning:889206830637666334>"


class internal:

    modules_to_not_load = []


db = JSONx("./jsondb/db.json")
