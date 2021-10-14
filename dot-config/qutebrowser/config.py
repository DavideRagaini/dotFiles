config.load_autoconfig()
# ======================= Imports ============= {{{
import dracula  # User Interface
from os import environ  # User Defined Bindings

# }}}
# ======================= User Defined Bindings ============= {{{
c.bindings.commands["normal"] = {
    ",a": "hint links spawn --detach dmpv aplay '{hint-url}'",
    ",c": "hint links spawn clipf '{hint-url}'",
    ",e": "hint links spawn --detach dmpv enqueue '{hint-url}'",
    ",p": "hint links spawn --detach dmpv eplay '{hint-url}'",
    ",s": 'config-cycle content.user_stylesheets ~/.config/qutebrowser/dracula.css ""',
    ",t": "hint links spawn transadd '{hint-url}'",
    ",v": 'hint links spawn funnel "{hint-url}"',
    ",z": "zoom 200",
    ",V": 'hint links spawn + environ["BROWSER"] + {hint-url}',
    ",\\": 'spawn dmenuhandler "{url}"',
    "<y><o>": "yank inline [[{url}][{title}]]",
}
# }}}
# ======================= User Interface ============= {{{
dracula.blood(c, {"spacing": {"vertical": 4, "horizontal": 4}})
c.downloads.location.suggestion = "both"
c.downloads.position = "bottom"
c.downloads.remove_finished = 20000
c.scrolling.smooth = False
c.session.lazy_restore = True
c.statusbar.show = "in-mode"
c.tabs.last_close = "default-page"
c.tabs.position = "bottom"
c.tabs.show = "multiple"
c.tabs.show_switching_delay = 10000
startpage = "file://" + environ["HOME"] + "/.local/src/startpage/index.html"
c.url.default_page = startpage
c.url.start_pages = [startpage]
c.window.title_format = (
    "{private}{perc}[{scroll_pos}]:{current_url}{title_sep}{current_title}"
)
# }}}
# ======================= Search Engines ============= {{{
c.url.searchengines = {"DEFAULT": "https://searx.nevrlands.de/search?q={}"}
c.url.searchengines = {
    "DEFAULT": "https://searx.nevrlands.de/search?q={}",
    "a": "https://wiki.archlinux.org/?search={}",
    "d": "https://duckduckgo.com/?q={}",
    "g": "https://www.google.com/search?q={}",
    "s": "https://startpage.com/sp/search?query={}",
    "w": "https://en.wikipedia.org/?search={}",
    "y": "https://www.youtube.com/results?search_query={}",
}
# }}}
# ======================= Redline Insert Mode ============= {{{
# Awesome way to open vim from qutebrowser
c.editor.command = [
    environ["TERMINAL"],
    "-e",
    environ["EDITOR"],
    "-f",
    "{file}",
    "-c",
    "normal {line}G{column0}1",
]
c.bindings.commands["insert"] = {
    "<Ctrl-h>": "fake-key <Backspace>",
    "<Ctrl-a>": "fake-key <Home>",
    "<Ctrl-e>": "fake-key <End>",
    "<Ctrl-b>": "fake-key <Left>",
    "<Mod1-b>": "fake-key <Ctrl-Left>",
    "<Ctrl-f>": "fake-key <Right>",
    "<Mod1-f>": "fake-key <Ctrl-Right>",
    "<Ctrl-p>": "fake-key <Up>",
    "<Ctrl-n>": "fake-key <Down>",
    "<Mod1-d>": "fake-key <Ctrl-Delete>",
    "<Ctrl-d>": "fake-key <Delete>",
    "<Ctrl-w>": "fake-key <Ctrl-Backspace>",
    "<Ctrl-u>": "fake-key <Shift-Home><Delete>",
    "<Ctrl-k>": "fake-key <Shift-End><Delete>",
    "<Ctrl-x><Ctrl-e>": "edit-text",
}
# }}}
# ======================= Security Settings ============= {{{
c.auto_save.session = True
c.content.autoplay = False
c.content.canvas_reading = False
c.content.cookies.accept = "no-3rdparty"
c.content.geolocation = False
c.content.headers.accept_language = "en-US,en;q=0.5"
c.content.headers.custom = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}
c.content.headers.user_agent = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/92.0"
)
c.content.javascript.can_access_clipboard = False
c.content.webgl = False
c.content.webrtc_ip_handling_policy = "default-public-interface-only"
# }}}
# ======================= Folders & Files ============= {{{
fileselect_cmd = ["st", "-e", "fu", "selection-path {}"]
c.fileselect.folder.command = fileselect_cmd
c.fileselect.multiple_files.command = fileselect_cmd
c.fileselect.single_file.command = fileselect_cmd
# }}}
