# This requires PyObjC ti be installed with
# pip install PyObjC

import neovim
import sys
import os

@neovim.plugin
class Marked(object):
    def __init__(self, vim):
        self.vim = vim
        fpath = '/Applications/Marked 2.app/Contents/MacOS/Marked 2'
        self.installed = os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    @neovim.function('StreamBufferToMarked')
    def stream_buffer_to_marked(self, arg):
        if self.installed:
            from AppKit import NSPasteboard
            buffer = "\n".join(self.vim.call('getline','1','$'))
            pb = NSPasteboard.pasteboardWithName_("mkStreamingPreview")
            pb.clearContents()
            pb.setString_forType_(buffer, 'public.utf8-plain-text')

    @neovim.function('IsMarkedInstalled', sync=True)
    def is_marked_installed(self, arg):
        return self.installed

    @neovim.autocmd('FileType', pattern='markdown', eval='expand("<afile>")', sync=True)
    def autocmd_handler(self, filename):
        if self.installed:
            open = self.vim.eval("get(g:,'marked_streaming_open_mapping','<Leader>O')")
            events = self.vim.eval("get(g:,'marked_streaming_events','InsertLeave,CursorHold')")
            self.vim.command(f"nmap <buffer>{open} :silent !open x-marked://stream/<CR>")
            self.vim.command(f"autocmd {events} <buffer> :call StreamBufferToMarked()")
