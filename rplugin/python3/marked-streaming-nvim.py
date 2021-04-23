import neovim
import sys

@neovim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.function('StreamToMarked')
    def stream_to_marked(self, arg):
        from AppKit import NSPasteboard
        buffer = "\n".join(self.vim.call('getline','1','$'))
        pb = NSPasteboard.pasteboardWithName_("mkStreamingPreview")
        pb.clearContents()
        pb.setString_forType_(buffer, 'public.utf8-plain-text')

