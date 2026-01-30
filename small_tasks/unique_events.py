from collections import defaultdict


def unique_events(events_list: list[tuple[int, str]] | None = None) -> dict[int, int]:
    if not events_list:
        return {}
    if not isinstance(events_list, list):
        raise TypeError("Given partam: evnets_list should be list")
    user_events = defaultdict(set)
    for event in events_list:
        user_events[event[0]].add(event[1])
    
    return {k: len(v) for k, v in user_events.items()}



if __name__ == "__main__":
    events = [
        (1, "login"),
        (1, "view"),
        (2, "login"),
        (1, "login"),
        (2, "logout"),
        (2, "login"),
    ]
   
    assert unique_events(events)  == { 1: 2, 2: 2}
    assert unique_events([]) == {}
    try:
        unique_events(1)
        assert False
    except TypeError:
       pass