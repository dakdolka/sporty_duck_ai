from core.container import container


def provide(name: str):
    return lambda: getattr(container, name)

get_conversation_orchestrator = provide("conversation_orchestrator")