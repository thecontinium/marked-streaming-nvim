# Streaming markdown from NeoVim to Marked

This implements [marked streaming preview](https://marked2app.com/help/Streaming_Preview.html) for markdown file types in neovim.
The call to stream the buffer including the extraction of the text in the buffer and streaming to marked is asynchronous.
The python code was adapted from [A Keyboard Maestro Trick](https://marked2app.com/sendy/w/i6GdkJnJmiQbVUQe4S763i7g)


This is dependent on the python library PyObjC being installed in the same environment as pynvim and assumes marked is installed in the normal Applications directory.
This can be achieved on install 'at build' by using the following in your chosen installation method.

``` viml
    call system(join([fnamemodify(g:python3_host_prog,":p:h"),"pip install -U pyobjc"],"/"))
```

The following global variables with their defaults can be set to configure behaviour.

``` vim
    let g:marked_streaming_open_mapping = '<Leader>O'
    let g:marked_streaming_events = 'InsertLeave,CursorHold'
    let g:marked_streaming_callback = '?x-success=io.alacritty'
```

