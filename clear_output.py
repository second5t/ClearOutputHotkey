import idaapi
import ida_kernwin

class ClearOutputPlugin(idaapi.plugin_t):
    flags = idaapi.PLUGIN_KEEP
    comment = "A plugin to clear the output window"
    help = "Press Ctrl+X to clear the Output Window"
    wanted_name = "Clear Output"
    wanted_hotkey = "Ctrl+X"

    def init(self):
        print("[ClearOutputPlugin] Plugin initialized.")

        if ida_kernwin.add_hotkey("Ctrl+X", self.clear_output):
            print("[ClearOutputPlugin] Hotkey Ctrl+X registered.")
        else:
            print("[ClearOutputPlugin] Failed to register Ctrl+X hotkey.")

        return idaapi.PLUGIN_KEEP

    def run(self, arg):
        self.clear_output()

    def term(self):
        ida_kernwin.del_hotkey("Ctrl+X")
        print("[ClearOutputPlugin] Plugin terminated.")

    def clear_output(self):
        """Clears the Output Window"""
        idaapi.msg_clear()
        print("[ClearOutputPlugin] Output window cleared.")
        self.timer = idaapi.register_timer(1000, self.remove_clear_message)

    def remove_clear_message(self):
        idaapi.msg_clear()
        return -1

def PLUGIN_ENTRY():
    return ClearOutputPlugin()
