from log_parser import ParsedLogs

class LogValidator:
    REQUIRED_NUM_OF_TOKENS = 3
    def __init__(self, log_to_validate: ParsedLogs) -> None:
        self.to_validate = log_to_validate

    def validate(self) -> ParsedLogs:
        """perform validation on log item"""
        self.__check_tokens_number()
        return self.to_validate

    def __check_tokens_number(self) -> None:
        token_count = 0
        for k, v in self.to_validate.items():
            if k == 'log_lvl' and v != 'EMPTY':
                token_count += 1
            if k != 'is_valid' and v:
                token_count += 1
        if token_count >= 3:
            self.to_validate['is_valid'] = True
