from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("TerminalWidget")
def TerminalWidget(content, session, headers, pageObj):
    '''
    {
     "type": "TerminalWidget",
     "mode": "edit",
     "content": {
          "startScript": "ls",
          "comp_id": "MgP4av3xdTbG2St1qpYeD"
     },
     "iteration": 0,
     "hash": 2,
     "saveVersion": 7
}
    '''
    return "<h2>I'm a simple TerminalWidget Component</h2>"
