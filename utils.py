from config import BASIC_RULES

def message_history_has_been_reset(mess_hist):
    reset_scenario = [{"role": "user", "content": f"Pretend your name is Chattie. {BASIC_RULES}"},
                        {"role": "assistant", "content": "OK"}]

    return mess_hist == reset_scenario
