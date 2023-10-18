import asyncio

async def JournalWatcher(actionsList):
    while not Dead("self"):
        for action in actionsList:
            if InJournal(".{}".format{action}, Name("self")):
                ClearJournal()
                return action


