from config import basic_rules

def message_history_has_been_reset(mess_hist):
    reset_scenario = [{"role": "user", "content": f"Pretend your name is Chattie. {basic_rules}"},
                        {"role": "assistant", "content": "OK"}]
                        
    return mess_hist == reset_scenario
