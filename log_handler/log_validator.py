from log_parser import LogParser, ParsedLog


class LogValidator:
    def __init__(self, log_to_validate: ParsedLog, require_quote_id: bool = False) -> None:
        self.to_validate = log_to_validate
        self.require_quote_id = require_quote_id

    def validate(self) -> ParsedLog:
        """Perform validation on a parsed log item."""
        self.__validate_basic_fields()
        return self.to_validate

    def __validate_basic_fields(self) -> None:
        timestamp_ok = bool(self.to_validate.get("timestamp", "").strip())
        level_ok = self.to_validate.get("log_lvl") in LogParser.LOG_LEVELS
        message_ok = bool(self.to_validate.get("message", "").strip())
        quote_ok = True

        if self.require_quote_id:
            quote_ok = bool(self.to_validate.get("quote_id", "").strip())

        self.to_validate["is_valid"] = bool(timestamp_ok and level_ok and message_ok and quote_ok)
