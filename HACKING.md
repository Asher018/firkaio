# How to hack on the codebase

## IDE integration
https://github.com/python-lsp/python-lsp-server

## Boring way
TODO fill this :D
Probably something with pip?
Use repo packages though if you can.

## Cool Guix way
1. [Install Guix (duh).](https://guix.gnu.org/en/manual/devel/en/html_node/Installation.html#Installation)
2. Enter a developer shell with: `guix shell -m guix.scm`

Done, now you can `flask run`

If you also want to use an IDE that supports the Language Server Protocol, use: `guix shell -m guix.scm python-lsp-server kak-lsp`
This assumes Kakoune as text editor. If you aren't using Kakoune, skip `kak-lsp` and look up how to set LSP up.
