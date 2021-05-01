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

    @neovim.function('_marked_stream_buffer')
    def stream_buffer(self, arg):
        if self.installed:
            from AppKit import NSPasteboard
            buffer = "\n".join(self.vim.call('getline','1','$'))
            pb = NSPasteboard.pasteboardWithName_("mkStreamingPreview")
            pb.clearContents()
            pb.setString_forType_(buffer, 'public.utf8-plain-text')

    @neovim.autocmd('FileType', pattern='markdown', eval='expand("<afile>")', sync=True)
    def autocmd_handler(self, filename):
        if self.installed:
            open = self.vim.eval("get(g:,'marked_streaming_open_mapping','<Leader>O')")
            events = self.vim.eval("get(g:,'marked_streaming_events','InsertLeave,CursorHold')")
            callback = self.vim.eval("get(g:,'marked_streaming_callback','?x-success=io.alacritty')")
            self.vim.command(f"nmap <buffer>{open} :autocmd {events},BufEnter <buffer> :call _marked_stream_buffer()<CR>:silent !open x-marked://stream/{callback}<CR>:call _marked_stream_buffer()<CR>")
