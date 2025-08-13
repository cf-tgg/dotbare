# config.py --- qutebrowser config -*- mode: pyhon-ts; -*-

config.load_autoconfig(False)
c.aliases = {'GG': 'session-load GG', 'q': 'close', 'qa': 'quit', 'w': 'session-save', 'wconf': 'config-write-py --force', 'wq': 'quit --save', 'wqa': 'quit --save', 'load': 'session-load', 'src': 'config-source'}
c.new_instance_open_target = 'tab'
c.new_instance_open_target_window = 'last-focused'
c.qt.highdpi = True
c.qt.workarounds.disable_hangouts_extension = True
c.content.autoplay = False
c.content.cookies.accept = 'no-3rdparty'
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')
config.set('content.cookies.accept', 'all', 'devtools://*')
config.set('content.geolocation', True, 'https://www.google.com')
config.set('content.geolocation', False, 'https://www.qub.ca')
config.set('content.geolocation', False, 'https://www.tuango.ca')
config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:133.0) Gecko/20100101 Firefox/133.0', 'https://accounts.google.com/*')

c.content.blocking.enabled = True
c.content.blocking.hosts.lists = ['https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts']
c.content.blocking.hosts.block_subdomains = True
c.content.blocking.method = 'auto'
c.content.blocking.adblock.lists = ['https://easylist.to/easylist/easylist.txt', 'https://easylist.to/easylist/easyprivacy.txt', 'https://raw.githubusercontent.com/CrusheerPL/AlleBlockV2/master/AlleBlockV2.txt']
c.content.blocking.whitelist = []

config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')

c.content.javascript.clipboard = 'access'
config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')

config.set('content.local_content_can_access_remote_urls', True, 'file:///home/cf/.local/share/qutebrowser/userscripts/*')
config.set('content.local_content_can_access_remote_urls', True, 'file:///home/cf/Templates/html/startpage/*')
config.set('content.local_content_can_access_file_urls', True, 'file:///home/cf/.local/share/qutebrowser/userscripts/*')
config.set('content.local_content_can_access_file_urls', True, 'file:///home/cf/Templates/html/startpage/*')

config.set('content.media.audio_capture', True, 'https://www.messenger.com/*')
config.set('content.media.audio_capture', True, 'https://www.messenger.com/*/*')
config.set('content.media.audio_capture', True, 'https://www.facebook.com/*')
config.set('content.media.audio_capture', True, 'https://teams.microsoft.com/*')
config.set('content.media.audio_video_capture', True, 'https://teams.microsoft.com')

c.content.media.audio_video_capture = True
config.set('content.media.video_capture', True, 'https://www.messenger.com')
config.set('content.media.video_capture', True, 'https://www.messenger.com/*/*')
config.set('content.media.video_capture', True, 'https://www.facebook.com')
config.set('content.media.video_capture', True, 'https://teams.microsoft.com')
config.set('content.notifications.enabled', True, 'https://www.facebook.com')
config.set('content.notifications.enabled', True, 'https://www.netflix.com')
config.set('content.notifications.enabled', True, 'https://www.reddit.com')
config.set('content.notifications.enabled', True, 'https://teams.live.com')
config.set('content.notifications.enabled', True, 'https://teams.microsoft.com')
config.set('content.notifications.enabled', False, 'https://www.tiktok.com')
c.content.notifications.presenter = 'libnotify'
config.set('content.register_protocol_handler', True, 'https://mail.google.com?extsrc=mailto&url=%25s')
config.set('content.register_protocol_handler', True, 'https://outlook.office.com?mailtouri=%25s')
config.set('content.register_protocol_handler', True, 'https://outlook.live.com?mailtouri=%25s')
config.set('content.register_protocol_handler', False, 'https://mail.proton.me#mailto=%25s')

c.content.user_stylesheets = ['~/Templates/css/root_sensible.css']
c.completion.shrink = True
c.completion.scrollbar.width = 0
c.downloads.location.prompt = True
c.downloads.position = 'bottom'
c.downloads.remove_finished = 3000
c.editor.command = ['emacsclient', '-c', '--socket-name=/run/user/1000/emacs/server', '+{line}:{column}', '{file}', '-f', 'delete-other-windows']
c.hints.border = '1px #0D0D0D #cccccc'
c.scrolling.bar = 'overlay'
c.scrolling.smooth = False
c.statusbar.show = 'never'
c.statusbar.position = 'top'
c.tabs.show = 'switching'
c.tabs.show_switching_delay = 10000
c.url.default_page = 'file:///home/cf/Templates/html/startpage/startpage.html'
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}', '!': 'https://duckduckgo.com/?q=!{}', 'archwiki': 'https://duckduckgo.com/?q=!archwiki {}',  'stract': 'https://stract.com/search?ss=false&sr=N4IgNglg1gpgJiAXAbQLoBoRwgZ0rBFDEAIzAHsBjApNAXyA&q={}&optic=&gl=All'}
c.url.start_pages = 'file:///home/cf/Templates/html/startpage/startpage.html'
c.window.transparent = False
c.zoom.default = '100%'
c.zoom.levels = ['25%', '30%', '35%', '40%', '45%', '50%', '55%', '60%', '65%', '70%', '75%', '80%', '85%', '90%', '95%', '100%', '105%', '110%', '115%', '120%', '125%', '130%', '135%', '140%', '145%', '150%', '155%', '160%', '165%', '170%', '175%', '180%', '185%', '190%', '195%', '200%', '205%', '210%', '215%', '220%', '225%', '230%', '235%', '240%', '245%', '250%', '255%', '260%', '265%', '270%', '275%', '280%', '285%', '290%', '295%', '300%', '305%', '310%', '315%', '320%', '325%', '330%', '335%', '340%', '345%', '350%', '355%', '360%', '365%', '370%', '375%', '380%', '385%', '390%', '395%', '400%', '405%', '410%', '415%', '420%', '425%', '430%', '435%', '440%', '445%', '450%', '455%', '460%', '465%', '470%', '475%', '480%', '485%', '490%', '495%', '500%']
c.colors.completion.fg = '#424242'
c.colors.completion.odd.bg = '#020202'
c.colors.completion.even.bg = '#010101'
c.colors.completion.category.bg = '#020202'
c.colors.completion.category.border.bottom = '#010101'
c.colors.completion.item.selected.fg = '#cfcfcf'
c.colors.completion.item.selected.bg = '#111111'
c.colors.completion.item.selected.border.top = '#111111'
c.colors.completion.item.selected.border.bottom = '#cfcfcf'
c.colors.completion.item.selected.match.fg = '#ffffff'
c.colors.completion.match.fg = '#ffffff'
c.colors.completion.scrollbar.fg = '#000000'
c.colors.completion.scrollbar.bg = '#111111'
c.colors.downloads.system.bg = 'hsl'
c.colors.hints.fg = 'white'
c.colors.hints.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0.4), stop:1 rgba(0, 0, 0, 0.9))'
c.colors.hints.match.fg = '#cbba92'
c.colors.statusbar.normal.bg = '#00020b'
c.colors.statusbar.passthrough.fg = '#4c1e48'
c.colors.statusbar.passthrough.bg = '#190618'
c.colors.tabs.bar.bg = '#111111'
c.colors.tabs.odd.bg = '#121212'
c.colors.tabs.even.bg = '#121212'
c.colors.webpage.bg = '#00020b'
c.colors.webpage.preferred_color_scheme = 'dark'
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.images = 'never'
c.colors.webpage.darkmode.policy.page = 'always'
c.fonts.default_family = 'Iosevka Nerd Font'
c.fonts.default_size = '16pt'
c.fonts.tooltip = 'Iosevka Nerd Font'
c.fonts.contextmenu = 'Iosevka Nerd Font'
c.fonts.web.family.standard = 'Iosevka Nerd Font'
c.fonts.web.family.fixed = 'Iosevka Nerd Font Propo'
c.fonts.web.family.serif = 'CaskaydiaCove Nerd Font Propo'
c.fonts.web.family.sans_serif = 'CaskaydiaCove Nerd Font'
c.fonts.web.family.cursive = 'Iosevka Nerd Font Propo'
c.fonts.web.family.fantasy = 'Fantasque Sans MNerd Font Propo'
c.fonts.web.size.default = 16
c.fonts.web.size.default_fixed = 12
c.fonts.web.size.minimum = 10

# Bindings for normal mode
config.bind('gG', ':tab-give 1')
config.bind('gT', 'cmd-set-text :tab-take 2;;command-accept --rapid')
config.bind('.', 'cmd-repeat-last')
config.bind(',,', 'jseval --quiet --file ~/.config/qutebrowser/userscripts/toggle_visibility.js')
config.bind(',B', ':set statusbar.show never')
config.bind(',D', 'set downloads.location.prompt false')
config.bind(',M', 'hint links spawn --detach mpv {hint-url}')
config.bind(',R', ':spawn --detach st -e readit -c -l en')
config.bind(',U', 'hint links spawn umpv {hint-url}')
config.bind(',b', ':set statusbar.show in-mode')
config.bind(',d', 'set downloads.location.prompt true')
config.bind(',l', 'spawn ytcl {url};;cmd-later 100 spawn ytln {url}')
config.bind(',m', 'spawn --detach mpv {url}')
config.bind(',rf', 'spawn --detach st -e readit -c -l fr && xdotool key alt+h key h;;')
config.bind(',rs', 'hint --rapid links spawn rssadd {hint-url}')
config.bind(',ta', 'cmd-set-text -s :spawn --userscript taskadd')
config.bind(',th', ':spawn --userscript taskadd due:eod pri:H')
config.bind(',tt', 'fake-key <Ctrl+c>;;yank selection;;spawn tts "$(xclip -selection clipboard -o)"')
config.bind(',uM', 'hint --rapid links spawn umpv {hint-url}')
config.bind(',um', 'spawn umpv {url}')
config.bind(',yd', 'spawn ydl {url}')
config.bind(',yt', 'spawn --detach mpv {url}')
config.bind(',yu', 'hint links spawn --detach ydl {hint-url}')
config.bind('0', 'hint links userscript append_hint_url')
config.bind('1', 'zoom 100%')
config.bind('2', 'zoom 200%')
config.bind('3', 'zoom 150%')
config.bind('4', 'zoom 120%')
config.bind('5', 'zoom 80%')
config.bind('6', 'quickmark-load qai')
config.bind('7', 'hint --rapid links spawn ydl {hint-url}')
config.bind('8', 'spawn ydl {url}')
config.bind('9', 'hint links spawn ydl {hint-url}')
config.bind(';D', 'hint --rapid links spawn ydl {hint-url}')
config.bind(';M', 'hint links spawn mpv {hint-url}')
config.bind(';N', 'hint --rapid links spawn mpv {hint-url}')
config.bind(';l', 'hint links spawn ytln {hint-url}')
config.bind('<?', 'set content.user_stylesheets ""')
config.bind('<Alt+Shift+j>', 'zoom-out')
config.bind('<Alt+Shift+k>', 'zoom-in')
config.bind('<Alt+c>', ':fake-key <Ctrl+c>;;yank selection')
config.bind('<Alt+v>', ':fake-key <ctrl+v>')
config.bind('<Backspace>', 'fake-key <Backspace>')
config.bind('<Ctrl+->', 'zoom-out')
config.bind('<Ctrl+=>', 'zoom-in')
config.bind('-', 'zoom-out')
config.bind('=', 'zoom-in')
config.bind('+', "zoom 100%")
config.bind('<Ctrl+a>', 'mode-enter insert;;fake-key <Ctrl+a>;;fake-key <Ctrl+c>;;mode-leave')
config.bind('<Ctrl+i>', 'fake-key <Tab>')
config.bind('<Ctrl+s>', 'search-next')
config.bind('<Ctrl+Alt+i>', 'fake-key <Backtab>')
config.bind('<Alt+w>', 'fake-key <Ctrl+c>;;yank selection')
config.bind('<Ctrl+c>', 'fake-key <Ctrl+c>')
config.bind('<Ctrl+d>', 'scroll-page 0 0.8')
config.bind('<Ctrl+Alt+Shift+e>', 'config-edit')
config.bind('<Ctrl+e>', 'mode-enter insert;;fake-key <End>')
config.bind('<Ctrl+u>', 'scroll-page 0 -0.8')
config.bind('<Ctrl+z>', 'fake-key <Ctrl+z>')
config.bind('<Enter>', 'fake-key <Enter>')
config.bind('<Space>', 'scroll-page 0 0.6')
config.bind('>?', 'set content.user_stylesheets \'["~/Templates/css/root_sensible.css", "~/Templates/css/cgpt.css"]\'')
config.bind('EE', 'fake-key <ctrl+c>;;yank selection;;spawn sleep 0.3;;spawn --detach st -e vimclip')
config.bind('TT', 'tab-only')
config.bind('UU', 'edit-text {url}')
config.bind('WE', 'spawn wikilocale {url} ;; cmd-later 500 open {clipboard}')
config.bind('Y', 'fake-key <Ctrl+c>;;yank selection')
config.bind('d', 'scroll-page 0 0.4')
config.bind('u', 'scroll-page 0 -0.4')
config.bind('<Ctrl+n>', 'fake-key <down>')
config.bind('<Ctrl+p>', 'fake-key <up>')
config.bind('n', 'fake-key <down>')
config.bind('p', 'fake-key <up>')
config.bind('N', 'next-page')
config.bind('P', 'previous-page')
config.bind('td', 'jseval --quiet --file ~/.config/qutebrowser/userscripts/mkdragelm.js')
config.bind('tt', 'fake-key <Ctrl+c>;;yank selection;;spawn tts "$(xclip -selection clipboard -o)"')
config.bind('<Ctrl+g>', 'fake-key <Escape>')

# Bindings for caret mode
config.bind('EE', 'fake-key <ctrl+c>;;yank selection;;spawn sleep 0.3;;spawn --detach st -e vimclip', mode='caret')
config.bind('d', 'fake-key <down>', mode='caret')
config.bind('u', 'fake-key <up>', mode='caret')
config.bind('j', 'move-to-next-line;;scroll-page 0 0.01', mode='caret')
config.bind('k', 'move-to-prev-line;;scroll-page 0 -0.01', mode='caret')
config.bind('tt', 'fake-key <Ctrl+c>;;yank selection;;spawn tts "$(xclip -selection clipboard -o)" ', mode='caret')
config.bind('<Ctrl+a>', 'fake-key <Home>', mode='caret')
config.bind('<Ctrl+e>', 'fake-key <End>', mode='caret')
config.bind('<Ctrl+f>', 'fake-key <Right>', mode='caret')
config.bind('<Ctrl+b>', 'fake-key <Left>', mode='caret')
config.bind('<Ctrl+w>', 'fake-key <Ctrl+x>', mode='caret')
config.bind('<Ctrl+d>', 'fake-key <Delete>', mode='caret')
config.bind('<Alt+w>', 'yank selection;;fake-key <Ctrl+c>', mode='caret')
config.bind('<Alt+a>', 'fake-key <Ctrl+Home>', mode='caret')
config.bind('<Alt+f>', 'fake-key <Ctrl+Right>', mode='caret')
config.bind('<Alt+b>', 'fake-key <Ctrl+Left>', mode='caret')
config.bind('<Alt+e>', 'fake-key <Ctrl+End>', mode='caret')
config.bind('<Alt+d>', 'fake-key <Ctrl+Right>;;fake-key <Ctrl+Left>;;fake-key <Ctrl+x>', mode='caret')
config.bind('<Ctrl+g>', 'mode-leave', mode='caret')
config.bind('tt', 'fake-key <Ctrl+c>;;yank selection;;spawn tts "$(xclip -selection clipboard -o)" ', mode='caret')
config.bind('u', 'scroll-page 0 -0.4', mode='caret')

# Bindings for command mode
config.bind('<Alt+c>', 'fake-key <Ctrl+c>', mode='command')
config.bind('<Alt+m>', 'fake-key <Home>', mode='command')
config.bind('<Alt+v>', 'fake-key <Ctrl+v>', mode='command')
#  config.bind('<Ctrl+->', 'zoom-out', mode='command')
#  config.bind('<Ctrl+=>', 'zoom-in', mode='command')
config.bind('<Ctrl+n>', ':completion-item-focus next', mode='command')
config.bind('<Ctrl+p>', ':completion-item-focus prev', mode='command')
config.bind('<Escape>', 'mode-leave', mode='command')
config.bind('<Ctrl+g>', 'mode-leave', mode='command')

# Bindings for insert mode

## Globs
config.bind('<Escape>', 'mode-leave', mode='insert')
config.bind('<Ctrl+g>', 'mode-leave', mode='insert')
config.bind('<Ctrl+->', 'zoom-out', mode='insert')
config.bind('<Ctrl+=>', 'zoom-in', mode='insert')
config.bind('<Ctrl+Shift+e>', 'scroll-page 0 -0.4', mode='insert')
config.bind('<Ctrl+Shift+y>', 'scroll-page 0 0.4', mode='insert')

## inserts
config.bind('<Alt+p>', 'insert-text {primary}', mode='insert')
config.bind('<Alt+Shift+p>', 'insert-text {primary}', mode='insert')
config.bind('<Tab>', 'fake-key <space>;;fake-key <space>;;fake-key <space>;;fake-key <space>', mode='insert')
config.bind('<Ctrl+Alt+Space>', 'fake-key <Home>;;fake-key <Shift+End>;;fake-key <Ctrl+c>;;fake-key <End>;;fake-key <Return>;;fake-key <Ctrl+v>', mode='insert') # duplicate-line

## open-line
config.bind('<Ctrl+o>', 'fake-key <Shift+Return>;;fake-key <Up>;;fake-key <End>', mode='insert')
config.bind('<Alt+o>', 'fake-key <Home>;;fake-key <Shift+Return>;;fake-key <Up>', mode='insert')
config.bind('<Alt+Shift+o>', 'fake-key <End>;;fake-key <Shift+Return>', mode='insert')

## navigation
config.bind('<Ctrl+a>', 'fake-key <Home>', mode='insert')      # move-to-beginning-of-line
config.bind('<Ctrl+e>', 'fake-key <End>', mode='insert')       # end-of-line
config.bind('<Ctrl+f>', 'fake-key <Right>', mode='insert')     # forward-char
config.bind('<Ctrl+b>', 'fake-key <Left>', mode='insert')      # backward-char
config.bind('<Ctrl+n>', 'fake-key <Down>', mode='insert')      # forward-line
config.bind('<Ctrl+p>', 'fake-key <Up>', mode='insert')        # previous-line
config.bind('<Ctrl+d>', 'fake-key <Delete>', mode='insert')    # delete-char
config.bind('<Ctrl+h>', 'fake-key <Backspace>', mode='insert') # backward-delete-char
config.bind('<Alt+b>', 'fake-key <Ctrl+Left>', mode='insert')  # backward-word
config.bind('<Alt+f>', 'fake-key <Ctrl+Right>', mode='insert') # forward-word

config.bind('<Alt+a>', 'fake-key <Ctrl+Home>', mode='insert') # move-to-text-start
config.bind('<Alt+e>', 'fake-key <Ctrl+End>', mode='insert')  # move-to-end-of-text
config.bind('<Alt+i>', 'fake-key <Home>;;fake-key <Ctrl+Right>;;fake-key <Ctrl+Left>', mode='insert') # back-to-indentation

config.bind('<Alt+c>', 'fake-key <Ctrl+c>', mode='insert')  # copy (st)
config.bind('<Alt+v>', 'fake-key <Ctrl+v>', mode='insert')  # paste (st)
config.bind('<Ctrl+y>', 'fake-key <Ctrl+v>', mode='insert') # yank
config.bind('<Alt+w>', 'fake-key <Ctrl+c>', mode='insert')  # kill-ring-save
config.bind('<Alt+y>', 'fake-key <Home>;;fake-key <Shift+End>;;fake-key <Ctrl+c>;;fake-key <End>', mode='insert') # copy-whole-line

config.bind('<Ctrl+Alt+k>', 'fake-key <Shift+End>;;fake-key <Ctrl+x>', mode='insert') # kill-end-of-line
config.bind('<Ctrl+Alt+w>', 'fake-key <Ctrl+Home>;;fake-key <Shift+End>;;fake-key <Ctrl+c>', mode='insert') # copy-whole-text
config.bind('<Ctrl+Alt+m>', 'fake-key <Shift+End>;;fake-key <Ctrl+c>', mode='insert') # copy-forward-line
config.bind('<Ctrl+Alt+p>', 'fake-key <Shift+Home>;;fake-key <Ctrl+c>', mode='insert') # copy-previous-line

## selection
config.bind('<Ctrl+Shift+f>', 'fake-key <Shift+Right>', mode='insert')     # mark-forward-char
config.bind('<Ctrl+Shift+b>', 'fake-key <Shift+Left>', mode='insert')      # mark-backward-char
config.bind('<Ctrl+Shift+a>', 'fake-key <Shift+Home>', mode='insert')      # mark-beginning-of-line
config.bind('<Ctrl+Shift+e>', 'fake-key <Shift+End>', mode='insert')       # mark-end-of-line

config.bind('<Alt+Shift+f>', 'fake-key <Ctrl+Shift+Right>', mode='insert') # mark-forward-word
config.bind('<Alt+Shift+b>', 'fake-key <Ctrl+Shift+Left>', mode='insert')  # mark-backward-word
config.bind('<Alt+Shift+a>', 'fake-key <Ctrl+Shift+Home>', mode='insert')  # mark-to-beginning-of-text
config.bind('<Alt+Shift+e>', 'fake-key <Ctrl+Shift+End>', mode='insert')   # mark-end-of-text
config.bind('<Alt+Shift+h>', 'fake-key <Shift+Home>', mode='insert')       # mark-beginning-of-line
config.bind('<Ctrl+l>', 'fake-key <Shift+End>', mode='insert')             # mark-end-of-line
config.bind('<Ctrl+Shift+l>', 'fake-key <Shift+End>;;fake-key <Ctrl+x>', mode='insert') # kill-end-of-line

config.bind('<Alt+Shift+@>', 'fake-key <Ctrl+Shift+Right>', mode='insert')                    # mark-word
config.bind('<Ctrl+\'>', 'fake-key <Ctrl+Shift+Right>', mode='insert')                        # mark-word
config.bind('<Ctrl+;>', 'fake-key <Ctrl+Shift+Left>', mode='insert')                          # mark-backward-word
config.bind('<Alt+Space>', 'fake-key <Home>;;fake-key <Ctrl+Shift+End>', mode='insert')       # mark-whole-line
config.bind('<Ctrl+Space>', 'fake-key <Ctrl+Shift+Right>', mode='insert')                     # mark-word
config.bind('<Ctrl+Shift+Space>', 'fake-key <Ctrl+Shift+Left>', mode='insert')                # mark-previous-word

config.bind('<Ctrl+Alt+Shift+a>', 'fake-key <Ctrl+a>', mode='insert') # select all
config.bind('<Ctrl+Alt+a>', 'fake-key <Ctrl+a>', mode='insert')       # select-all

config.bind('<Ctrl+Shift+n>', 'fake-key <Shift+Down>', mode='insert') # mark-forward-line
config.bind('<Ctrl+Shift+p>', 'fake-key <Shift+Up>', mode='insert')   # mark-previous-line
config.bind('<Ctrl+Shift+j>', 'fake-key <Shift+Down>', mode='insert') # mark-forward-line
config.bind('<Ctrl+Shift+k>', 'fake-key <Shift+Up>', mode='insert')   # mark-previous-line

## deletion
config.bind('<Ctrl+k>', 'fake-key <Shift+End>;;fake-key <Ctrl+c>;;fake-key <Delete>', mode='insert') # kill-line
config.bind('<Ctrl+w>', 'fake-key <Ctrl+c>;;fake-key <Ctrl+Backspace>', mode='insert')        # kill-backward-word
config.bind('<Ctrl+u>', 'fake-key <Shift+Home>;;fake-key <Ctrl+x>', mode='insert')            # unix-rubout
config.bind('<Alt+u>', 'fake-key <Ctrl+Shift+Home>;;fake-key <Ctrl+x>', mode='insert')        # kill-to-beginning-of-text
config.bind('<Ctrl+Alt+k>', 'fake-key <Ctrl+Shift+End>;;fake-key <Ctrl+x>', mode='insert')    # kill-to-end-of-text
config.bind('<Ctrl+Shift+h>', 'fake-key <Ctrl+Shift+Left>;;fake-key <Ctrl+c>', mode='insert') # copy-backward-word
config.bind('<Alt+d>', 'fake-key <Ctrl+Right>;;fake-key <Ctrl+Shift+Left>;;fake-key <Ctrl+x>', mode='insert') # kill-word

## Control Chars
config.bind('<Ctrl+i>', 'fake-key <Tab>', mode='insert')
config.bind('<Ctrl+Alt+i>', 'fake-key <Backtab>', mode='insert')
config.bind('<Ctrl+m>', 'fake-key <Return>', mode='insert')
config.bind('<Ctrl+j>', 'fake-key <Shift+Return>', mode='insert')

# Bindings for passthrough mode

## Globs
config.bind('<Ctrl+->', 'zoom-out', mode='passthrough')
config.bind('<Ctrl+=>', 'zoom-in', mode='passthrough')
config.bind('<Ctrl+Shift+e>', 'scroll-page 0 -0.4', mode='passthrough')
config.bind('<Ctrl+Shift+y>', 'scroll-page 0 0.4', mode='passthrough')
config.bind('<Escape>', 'mode-leave', mode='passthrough')
config.bind('<Ctrl+g>', 'mode-leave', mode='passthrough')

## inserts
config.bind('<Alt+Shift+p>', 'insert-text {primary}', mode='passthrough')
config.bind('<Tab>', 'fake-key <Tab>', mode='passthrough')
config.bind('<Ctrl+Alt+Space>', 'fake-key <Home>;;fake-key <Ctrl+Shift+End>;;fake-key <Ctrl+c>;;fake-key <End>;;fake-key <Return>;;fake-key <Ctrl+v>', mode='passthrough') # duplicate-line

## open-line
config.bind('<Ctrl+o>', 'fake-key <Shift+Return>;;fake-key <Up>;;fake-key <End>', mode='passthrough')
config.bind('<Alt+o>', 'fake-key <Home>;;fake-key <Shift+Return>;;fake-key <Up>;;fake-key <Home>', mode='passthrough')
config.bind('<Alt+Shift+o>', 'fake-key <End>;;fake-key <Shift+Return>', mode='passthrough')

## navigation
config.bind('<Ctrl+a>', 'fake-key <Home>', mode='passthrough')      # move-to-beginning-of-line
config.bind('<Ctrl+e>', 'fake-key <End>', mode='passthrough')       # end-of-line
config.bind('<Ctrl+f>', 'fake-key <Right>', mode='passthrough')     # forward-char
config.bind('<Ctrl+b>', 'fake-key <Left>', mode='passthrough')      # backward-char
config.bind('<Ctrl+n>', 'fake-key <Down>', mode='passthrough')      # forward-line
config.bind('<Ctrl+p>', 'fake-key <Up>', mode='passthrough')        # previous-line
config.bind('<Ctrl+d>', 'fake-key <Delete>', mode='passthrough')    # delete-char
config.bind('<Ctrl+h>', 'fake-key <Backspace>', mode='passthrough') # backward-delete-char
config.bind('<Alt+b>', 'fake-key <Ctrl+Left>', mode='passthrough')  # backward-word
config.bind('<Alt+f>', 'fake-key <Ctrl+Right>', mode='passthrough') # forward-word
config.bind('<Alt+a>', 'fake-key <Ctrl+Home>', mode='passthrough') # move-to-text-start
config.bind('<Alt+e>', 'fake-key <Ctrl+End>', mode='passthrough')  # move-to-end-of-text
config.bind('<Alt+i>', 'fake-key <Home>;;fake-key <Ctrl+Right>;;fake-key <Ctrl+Left>', mode='passthrough') # back-to-indentation

config.bind('<Alt+c>', 'fake-key <Ctrl+c>', mode='passthrough')  # copy (st)
config.bind('<Alt+v>', 'fake-key <Ctrl+v>', mode='passthrough')  # paste (st)
config.bind('<Ctrl+y>', 'fake-key <Ctrl+v>', mode='passthrough') # yank
config.bind('<Alt+w>', 'fake-key <Ctrl+c>;;yank selection', mode='passthrough')  # kill-ring-save
config.bind('<Alt+y>', 'fake-key <Home>;;fake-key <Shift+End>;;fake-key <Ctrl+c>;;fake-key <End>', mode='passthrough') # copy-whole-line

config.bind('<Ctrl+Alt+k>', 'fake-key <Shift+End>;;fake-key <Ctrl+x>', mode='passthrough') # kill-end-of-line
config.bind('<Ctrl+Alt+w>', 'fake-key <Ctrl+Home>;;fake-key <Shift+End>;;fake-key <Ctrl+c>', mode='passthrough')
config.bind('<Ctrl+Alt+m>', 'fake-key <Shift+End>;;fake-key <Ctrl+c>', mode='passthrough') # copy-forward-line
config.bind('<Ctrl+Alt+p>', 'fake-key <Shift+Home>;;fake-key <Ctrl+c>', mode='passthrough') # copy-previous-line

## selection
config.bind('<Ctrl+Shift+f>', 'fake-key <Shift+Right>', mode='passthrough')     # mark-forward-char
config.bind('<Ctrl+Shift+b>', 'fake-key <Shift+Left>', mode='passthrough')      # mark-backward-char
config.bind('<Ctrl+Shift+a>', 'fake-key <Shift+Home>', mode='passthrough')      # mark-beginning-of-line
config.bind('<Ctrl+Shift+e>', 'fake-key <Shift+End>', mode='passthrough')       # mark-end-of-line

config.bind('<Alt+Shift+f>', 'fake-key <Ctrl+Shift+Right>', mode='passthrough') # mark-forward-word
config.bind('<Alt+Shift+b>', 'fake-key <Ctrl+Shift+Left>', mode='passthrough')  # mark-backward-word
config.bind('<Alt+Shift+a>', 'fake-key <Ctrl+Shift+Home>', mode='passthrough')  # mark-to-beginning-of-text
config.bind('<Alt+Shift+e>', 'fake-key <Ctrl+Shift+End>', mode='passthrough')   # mark-end-of-text
config.bind('<Alt+Shift+h>', 'fake-key <Shift+Home>', mode='passthrough')       # mark-beginning-of-line
config.bind('<Ctrl+l>', 'fake-key <Shift+End>', mode='passthrough')             # mark-end-of-line
config.bind('<Ctrl+Shift+l>', 'fake-key <Shift+End>;;fake-key <Ctrl+x>', mode='passthrough') # kill-end-of-line

config.bind('<Alt+Shift+@>', 'fake-key <Ctrl+Shift+Right>', mode='passthrough')               # mark-word
config.bind('<Ctrl+\'>', 'fake-key <Ctrl+Shift+Right>', mode='passthrough')                   # mark-word
config.bind('<Ctrl+;>', 'fake-key <Ctrl+Shift+Left>', mode='passthrough')                     # mark-backward-word
config.bind('<Alt+Space>', 'fake-key <Home>;;fake-key <Ctrl+Shift+End>', mode='passthrough')  # mark-whole-line
config.bind('<Ctrl+Space>', 'fake-key <Ctrl+Shift+Right>', mode='passthrough')                # mark-word
config.bind('<Ctrl+Shift+Space>', 'fake-key <Ctrl+Shift+Left>', mode='passthrough')           # mark-previous-word

config.bind('<Ctrl+Alt+Shift+a>', 'fake-key <Ctrl+a>', mode='passthrough') # select all
config.bind('<Ctrl+Alt+a>', 'fake-key <Ctrl+a>', mode='passthrough')       # select-all

config.bind('<Ctrl+Shift+n>', 'fake-key <Shift+Down>', mode='passthrough') # mark-forward-line
config.bind('<Ctrl+Shift+p>', 'fake-key <Shift+Up>', mode='passthrough')   # mark-previous-line
config.bind('<Ctrl+Shift+j>', 'fake-key <Shift+Down>', mode='passthrough') # mark-forward-line
config.bind('<Ctrl+Shift+k>', 'fake-key <Shift+Up>', mode='passthrough')   # mark-previous-line

## deletion
config.bind('<Ctrl+k>', 'fake-key <Shift+End>;;fake-key <Ctrl+c>;;fake-key <Delete>', mode='passthrough') # kill-line
config.bind('<Ctrl+w>', 'fake-key <Ctrl+c>;;fake-key <Ctrl+Backspace>', mode='passthrough')        # kill-backward-word
config.bind('<Ctrl+u>', 'fake-key <Shift+Home>;;fake-key <Ctrl+x>', mode='passthrough')            # unix-rubout
config.bind('<Alt+u>', 'fake-key <Ctrl+Shift+Home>;;fake-key <Ctrl+x>', mode='passthrough')        # kill-to-beginning-of-text
config.bind('<Ctrl+Alt+k>', 'fake-key <Ctrl+Shift+End>;;fake-key <Ctrl+x>', mode='passthrough')    # kill-to-end-of-text
config.bind('<Ctrl+Shift+h>', 'fake-key <Ctrl+Shift+Left>;;fake-key <Ctrl+c>', mode='passthrough') # copy-backward-word
config.bind('<Alt+d>', 'fake-key <Ctrl+Right>;;fake-key <Ctrl+Shift+Left>;;fake-key <Ctrl+x>', mode='passthrough') # kill-word

## Control Chars
config.bind('<Ctrl+i>', 'fake-key <Tab>', mode='passthrough')
config.bind('<Ctrl+Alt+i>', 'fake-key <Backtab>', mode='passthrough')
config.bind('<Ctrl+Return>', 'fake-key <Ctrl+Return>', mode='passthrough')
config.bind('<Ctrl+j>', 'fake-key <Shift+Return>', mode='passthrough')

# Bindings for prompt mode
config.bind('<Escape>', 'mode-leave', mode='prompt')
config.bind('<Ctrl+y>', 'prompt-accept', mode='prompt')
config.bind('<Ctrl+w>', 'rl-filename-rubout', mode='command')

# testing Alt+Return availability
config.bind('<Alt+Return>', 'fake-key <Ctrl+Return>', mode='passthrough')
config.bind('<Alt+Return>', 'fake-key <Ctrl+Return>', mode='insert')
config.bind('<Alt+Return>', 'fake-key <Ctrl+Return>', mode='command')
config.bind('<Alt+c>', 'yank {selection}', mode='insert')
config.bind('<Alt+c>', 'yank {selection}', mode='passthrough')
config.bind('<Alt+p>', 'insert-text {primary}', mode='insert')
config.bind('<Alt+p>', 'insert-text {primary}', mode='passthrough')

# readline bindings in command mode
config.bind('<Ctrl+b>', 'rl-backward-char', mode='command')
config.bind('<Ctrl+h>', 'rl-backward-delete-char', mode='command')
config.bind('<Alt+b>', 'rl-backward-word', mode='command')
config.bind('<Ctrl+a>', 'rl-beginning-of-line', mode='command')
config.bind('<Ctrl+h>', 'rl-delete-char', mode='command')
config.bind('<Ctrl+e>', 'rl-end-of-line', mode='command')
config.bind('<Ctrl+f>', 'rl-forward-char', mode='command')
config.bind('<Alt+Backspace>', 'rl-backward-kill-word', mode='command')
config.bind('<Alt+f>', 'rl-forward-word', mode='command')
config.bind('<Alt+p>', 'insert-text {primary}', mode='command')
config.bind('<Ctrl+k>', 'rl-kill-line', mode='command')
config.bind('<Alt+d>', 'rl-kill-word', mode='command')
config.bind('<Ctrl+u>', 'rl-rubout', mode='command')
config.bind('<Ctrl+U>', 'rl-unix-line-discard', mode='command')
config.bind('<Ctrl+y>', 'rl-yank', mode='command')

# readline bindidngs in prompt mode
config.bind('<Ctrl+b>', 'rl-backward-char', mode='prompt')
config.bind('<Ctrl+h>', 'rl-backward-delete-char', mode='prompt')
config.bind('<Alt+b>', 'rl-backward-word', mode='prompt')
config.bind('<Ctrl+a>', 'rl-beginning-of-line', mode='prompt')
config.bind('<Ctrl+h>', 'rl-delete-char', mode='prompt')
config.bind('<Ctrl+e>', 'rl-end-of-line', mode='prompt')
config.bind('<Ctrl+f>', 'rl-forward-char', mode='prompt')
config.bind('<Alt+Backspace>', 'rl-backward-kill-word', mode='prompt')
config.bind('<Alt+f>', 'rl-forward-word', mode='prompt')
config.bind('<Alt+p>', 'insert-text {primary}', mode='prompt')
config.bind('<Ctrl+k>', 'rl-kill-line', mode='prompt')
config.bind('<Alt+d>', 'rl-kill-word', mode='prompt')
config.bind('<Ctrl+u>', 'rl-rubout', mode='prompt')
config.bind('<Ctrl+U>', 'rl-unix-line-discard', mode='prompt')
config.bind('<Ctrl+y>', 'rl-yank', mode='prompt')
