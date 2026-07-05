from core.container import container


def provide(name: str):
    return lambda: getattr(container, name)

get_entry_service = provide("entry_service")
get_conversation_service = provide("conversation_service")