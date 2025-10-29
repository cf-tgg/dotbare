# Settings :cfg:
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
c.content.prefers_reduced_motion = False
c.content.site_specific_quirks.enabled = True
config.set('content.geolocation', True, 'https://maps.google.com')
config.set('content.geolocation', False, 'https://www.google.com')
config.set('content.geolocation', False, 'https://www.qub.ca')
config.set('content.geolocation', False, 'https://www.tuango.ca')
config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:136.0) Gecko/20100101 Firefox/139.0', 'https://accounts.google.com/*')
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
config.set('content.local_content_can_access_remote_urls', True, 'file:///home/cf/Templates/html/startpage/*')
config.set('content.local_content_can_access_remote_urls', True, 'file:///home/cf/.local/share/qutebrowser/userscripts/*')
config.set('content.local_content_can_access_file_urls', True, 'file:///home/cf/Templates/html/startpage/*')
config.set('content.local_content_can_access_file_urls', False, 'file:///home/cf/.local/share/qutebrowser/userscripts/*')
config.set('content.media.audio_capture', True, 'https://www.messenger.com/*')
config.set('content.media.audio_capture', True, 'https://www.messenger.com/*/*')
config.set('content.media.audio_capture', True, 'https://www.facebook.com/*')
config.set('content.media.audio_capture', True, 'https://teams.microsoft.com/*')
c.content.media.audio_video_capture = True
config.set('content.media.audio_video_capture', True, 'https://teams.microsoft.com')
config.set('content.media.video_capture', True, 'https://www.messenger.com')
config.set('content.media.video_capture', True, 'https://www.messenger.com/*/*')
config.set('content.media.video_capture', True, 'https://www.facebook.com')
config.set('content.media.video_capture', True, 'https://teams.microsoft.com')
config.set('content.notifications.enabled', False, 'https://www.netflix.com')
config.set('content.notifications.enabled', False, 'https://www.reddit.com')
config.set('content.notifications.enabled', False, 'https://www.tiktok.com')
config.set('content.notifications.enabled', True, 'https://teams.live.com')
config.set('content.notifications.enabled', True, 'https://teams.microsoft.com')
config.set('content.notifications.enabled', True, 'https://www.facebook.com')
config.set('content.notifications.enabled', True, 'https://messages.google.com')
config.set('content.notifications.enabled', True, 'https://www.messenger.com')
c.content.notifications.presenter = 'libnotify'
c.content.notifications.show_origin = True
c.content.persistent_storage = 'ask'
c.content.plugins = False
c.content.print_element_backgrounds = True
config.set('content.register_protocol_handler', True, 'https://mail.google.com?extsrc=mailto&url=%25s')
config.set('content.register_protocol_handler', True, 'https://outlook.office.com?mailtouri=%25s')
config.set('content.register_protocol_handler', True, 'https://outlook.live.com?mailtouri=%25s')
config.set('content.register_protocol_handler', True, 'https://mail.proton.me#mailto=%25s')
c.content.user_stylesheets = ['~/Templates/css/style.css', '~/Templates/css/cgpt.css']
c.content.webgl = True
c.completion.shrink = True
c.completion.scrollbar.width = 0
c.downloads.location.prompt = True
c.downloads.position = 'bottom'
c.downloads.remove_finished = 1000
c.editor.command = ['emacsclient', '-s', '/run/user/1000/emacs/server', '-c', '--alternate-editor=\"\"', '+{line}:{column}', '{file}']
c.hints.border = '1px #0D0D0D #00020b'
c.input.forward_unbound_keys = 'all'
c.scrolling.bar = 'overlay'
c.scrolling.smooth = False
c.statusbar.show = 'never'
c.statusbar.position = 'top'
c.tabs.show = 'switching'
c.tabs.show_switching_delay = 8000
c.url.default_page = 'file:///home/cf/Templates/html/startpage/backpage.html'
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}', '!': 'https://duckduckgo.com/?q=!{}', 'archwiki': 'https://duckduckgo.com/?q=!archwiki {}', 'stract': 'https://stract.com/search?ss=false&sr=N4IgNglg1gpgJiAXAbQLoBoRwgZ0rBFDEAIzAHsBjApNAXyA&q={}&optic=&gl=All'}
c.url.start_pages = 'file:///home/cf/Templates/html/startpage/backpage.html'
c.window.transparent = False
c.zoom.default = '100%'
c.zoom.levels = ['25%', '30%', '35%', '40%', '45%', '50%', '55%', '60%', '65%', '70%', '75%', '80%', '85%', '90%', '95%', '100%', '105%', '110%', '115%', '120%', '125%', '130%', '135%', '140%', '145%', '150%', '155%', '160%', '165%', '170%', '175%', '180%', '185%', '190%', '195%', '200%', '205%', '210%', '215%', '220%', '225%', '230%', '235%', '240%', '245%', '250%', '255%', '260%', '265%', '270%', '275%', '280%', '285%', '290%', '295%', '300%', '305%', '310%', '315%', '320%', '325%', '330%', '335%', '340%', '345%', '350%', '355%', '360%', '365%', '370%', '375%', '380%', '385%', '390%', '395%', '400%', '405%', '410%', '415%', '420%', '425%', '430%', '435%', '440%', '445%', '450%', '455%', '460%', '465%', '470%', '475%', '480%', '485%', '490%', '495%', '500%']

# Theme :theme:

## Colors :colors:
c.colors.completion.fg = '#484848'
c.colors.completion.odd.bg = '#000000'
c.colors.completion.even.bg = '#000000'
c.colors.completion.category.bg = '#000000'
c.colors.completion.category.border.bottom = '#121212'
c.colors.completion.item.selected.fg = '#f4f4f4'
c.colors.completion.item.selected.bg = '#121212'
c.colors.completion.item.selected.border.top = '#000000'
c.colors.completion.item.selected.border.bottom = '#121212'
c.colors.completion.item.selected.match.fg = '#f4f4f4'
c.colors.completion.match.fg = '#f4f4f4'
c.colors.completion.scrollbar.fg = '#000000'
c.colors.completion.scrollbar.bg = '#000000'
c.colors.downloads.system.bg = 'hsl'
c.colors.hints.fg = 'rgba(232, 232, 232, 0.85)'
c.colors.hints.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0.4), stop:1 rgba(0, 0, 0, 0.9))'
c.colors.hints.match.fg = '#f8f8f8'
c.colors.prompts.border = '#000000'
c.colors.prompts.bg = '#121212'
c.colors.prompts.selected.fg = '#f4f4f4'
c.colors.prompts.selected.bg = '#242424'
c.colors.statusbar.normal.fg = '#484848'
c.colors.statusbar.insert.fg = '#323232'
c.colors.statusbar.insert.bg = '#000000'
c.colors.statusbar.passthrough.fg = '#484848'
c.colors.statusbar.passthrough.bg = '#121212'
c.colors.statusbar.caret.fg = '#382020'
c.colors.statusbar.caret.bg = '#000000'
c.colors.statusbar.caret.selection.fg = '#3f2020'
c.colors.statusbar.caret.selection.bg = '#0b0000'
c.colors.tabs.bar.bg = '#121212'
c.colors.tabs.odd.bg = '#121212'
c.colors.tabs.even.bg = '#121212'
c.colors.webpage.bg = '#121212'
c.colors.webpage.preferred_color_scheme = 'dark'
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.images = 'never'
c.colors.webpage.darkmode.policy.page = 'always'

## Fonts :fonts:
c.fonts.default_family = 'Iosevka Nerd Font'
c.fonts.default_size = '16px'
c.fonts.tooltip = 'Iosevka Nerd Font'
c.fonts.contextmenu = 'Iosevka Nerd Font'
c.fonts.web.family.standard = 'Iosevka Nerd Font'
c.fonts.web.family.fixed = 'IosevkaTerm Nerd Font'
c.fonts.web.family.serif = 'CaskaydiaCove Nerd Font Propo'
c.fonts.web.family.sans_serif = 'CaskaydiaCove Nerd Font'
c.fonts.web.family.cursive = 'Iosevka Nerd Font Propo'
c.fonts.web.family.fantasy = 'Fantasque Sans MNerd Font Propo'
c.fonts.web.size.default = 16
c.fonts.web.size.default_fixed = 12
c.fonts.web.size.minimum = 10
c.fonts.web.size.minimum_logical = 9

# Keybindings :kbd:

c.bindings.key_mappings = {'<Ctrl+[>': '<Escape>', '<Ctrl+6>': '<Ctrl+^>', '<Ctrl+m>': '<Return>', '<Ctrl+j>': '<Return>', '<Ctrl+i>': '<Tab>', '<Enter>': '<Return>', '<Ctrl+Enter>': '<Ctrl+Return>'}

## Normal Mode :kbd:normal:
config.bind('+', 'zoom 100%')
config.bind(',,', 'jseval --quiet --file ~/.config/qutebrowser/userscripts/toggle_visibility.js')
config.bind(',.', 'jseval --quiet --file ~/.config/qutebrowser/userscripts/iiie.js')
config.bind(',B', ':set statusbar.show never')
config.bind(',D', 'set downloads.location.prompt false')
config.bind(',M', 'hint links spawn --detach mpv {hint-url}')
config.bind(',R', ':spawn --detach st -e readit -c -l en')
config.bind(',U', 'hint links spawn umpv {hint-url}')
config.bind(',b', ':set statusbar.show in-mode')
config.bind(',d', 'set downloads.location.prompt true')
config.bind(',l', 'spawn ytcl {url};;cmd-later 100 spawn ytln {url}')
config.bind(',m', 'spawn --detach mpv {url}')
config.bind(',rf', 'spawn --detach st -e readit -c -l fr')
config.bind(',rs', 'hint --rapid links spawn rssadd {hint-url}')
config.bind(',ta', 'cmd-set-text -s :spawn --userscript taskadd')
config.bind(',th', ':spawn --userscript taskadd due:eod pri:H')
config.bind(',tt', 'fake-key <Ctrl+c>;;yank selection;;spawn tts "$(xclip -selection clipboard -o)"')
config.bind(',uM', 'hint --rapid links spawn umpv {hint-url}')
config.bind(',um', 'spawn umpv {url}')
config.bind(',yd', 'spawn ydl {url}')
config.bind(',yt', 'spawn --detach mpv {url}')
config.bind(',yu', 'hint links spawn --detach ydl {hint-url}')
config.bind('.', 'cmd-repeat-last')
config.bind('0', 'hint links userscript append_hint_url')
config.bind('1', 'zoom 100%')
config.bind('2', 'zoom 185%')
config.bind('3', 'zoom 150%')
config.bind('4', 'zoom 125%')
config.bind('5', 'zoom 85%')
config.bind('6', 'quickmark-load qai')
config.bind('7', 'session-load msgr')
config.bind('8', 'spawn ydl {url}')
config.bind('9', 'hint --rapid links spawn ydl {hint-url}')
config.bind(';D', 'hint --rapid links spawn ydl {hint-url}')
config.bind(';M', 'hint links spawn mpv {hint-url}')
config.bind(';N', 'hint --rapid links spawn mpv {hint-url}')
config.bind(';l', 'hint links spawn ytln {hint-url}')
config.bind('<?', 'set content.user_stylesheets "";;reload')

config.bind('<ctrl-alt-tab>', 'tab-move +')
config.bind('<ctrl-alt-backtab>', 'tab-move -')
config.bind('<ctrl-alt-->', 'tab-move -')
config.bind('<ctrl-alt-=>', 'tab-move +')
config.bind('<ctrl-alt-1>', 'tab-move 1')
config.bind('<ctrl-alt-2>', 'tab-move 2')
config.bind('<ctrl-alt-3>', 'tab-move 3')
config.bind('<ctrl-alt-4>', 'tab-move 4')
config.bind('<ctrl-alt-5>', 'tab-move 5')
config.bind('<ctrl-alt-6>', 'tab-move 6')
config.bind('<ctrl-alt-7>', 'tab-move 7')
config.bind('<ctrl-alt-8>', 'tab-move 8')
config.bind('<ctrl-alt-9>', 'tab-move 9')
config.bind('<ctrl-alt-0>', 'tab-move 10')
config.bind('<alt-backspace>', 'back')
config.bind('<alt-shift-v>', 'scroll-page 0 -0.95')
config.bind('<alt-space>', 'forward')
config.bind('<alt-b>', 'fake-key <Ctrl+Left>')
config.bind('<alt-c>', 'fake-key <Ctrl+c>;;yank selection')
config.bind('<alt-shift-j>', 'zoom-out')
config.bind('<alt-shift-k>', 'zoom-in')
config.bind('<alt-e>', 'spawn emacsclient -s /run/user/1000/emacs/server -c ~/.config/qutebrowser/userscripts/toggle_visibility.js')
config.bind('<alt-l>', 'cmd-set-text -s :open -t')
config.bind('<alt-s>', 'hint all')
config.bind('<alt-v>', 'scroll-page 0 -0.45')
config.bind('<alt-w>', 'fake-key <Ctrl+c>;;yank selection')
config.bind('<alt-x>', 'cmd-set-text :')
config.bind('<alt-y>', 'yank {url:title}')
config.bind('<backspace>', 'scroll-page 0 -0.6')
config.bind('<ctrl+->', 'zoom-out')
config.bind('<ctrl-0>', 'zoom 100%')
config.bind('<ctrl+=>', 'zoom-in')
config.bind('<ctrl-alt-e>', 'config-edit')
config.bind('<ctrl-alt-i>', 'fake-key <Backtab>')
config.bind('<ctrl-alt-p>', 'mode-enter passthrough')
config.bind('<ctrl-shift-Tab>', 'tab-prev')
config.bind('<ctrl-shift-v>', 'scroll-page 0 0.95')
config.bind('<ctrl-tab>', 'tab-next')
config.bind('<ctrl-a>', 'fake-key <Home>')
config.bind('<ctrl-b>', 'fake-key <Left>')
config.bind('<ctrl-c>', 'fake-key <Ctrl+c>;;yank selection')
config.bind('<ctrl-d>', 'fake-key <Delete>')
config.bind('<ctrl-e>', 'fake-key <End>')
config.bind('<ctrl-f>', 'fake-key <Right>')
config.bind('<ctrl-g>', 'clear-keychain ;; search ;; fullscreen --leave')
config.bind('<ctrl-h>', 'cmd-set-text -s :help')
config.bind('<ctrl-i>', 'fake-key <Tab>')
config.bind('<ctrl-l>', 'cmd-set-text -s :open')
config.bind('<ctrl-n>', 'fake-key <Down>')
config.bind('<ctrl-p>', 'fake-key <Up>')
config.bind('<ctrl-q>', 'quit --save')
config.bind('<alt-r>', 'cmd-set-text ?')
config.bind('<alt-s>', 'cmd-set-text /')
config.bind('<ctrl-s>', 'search-next')
config.bind('<ctrl-r>', 'search-prev')
config.bind('<ctrl-v>', 'scroll-page 0 0.45')
config.bind('<ctrl-shift-w>', 'tab-close')
config.bind('<ctrl-x><ctrl-c>', 'quit --save')
config.bind('<ctrl-x>b', 'cmd-set-text -s :buffer')
config.bind('<ctrl-x><ctrl-k>', 'tab-close')
config.bind('<ctrl-x><alt-q>', 'tab-close')
config.bind('<ctrl-x>k', 'tab-close')
config.bind('<ctrl-y>', 'insert-text {primary}')

config.bind('<Space>', 'scroll-page 0 0.6')
config.bind('=', 'zoom-in')
config.bind('-', 'zoom-out')
config.bind('>?', 'set content.user_stylesheets \'["~/Templates/css/style.css", "~/Templates/css/cgpt.css"]\'')
config.bind('EE', ':edit-text selection')
config.bind('F', 'forward')
config.bind('N', 'forward')
config.bind('P', 'back')
config.bind('TT', 'tab-only')
config.bind('U', 'undo')
config.bind('EU', ':edit-url')
config.bind('WE', 'spawn wikilocale {url} ;; cmd-later 500 open {clipboard}')
config.bind('Y', 'fake-key <Ctrl-c>;;yank selection')
config.bind('d', 'scroll-page 0 0.45')
config.bind('gG', ':tab-give 1')
config.bind('gT', 'cmd-set-text :tab-take -k')
config.bind('l', 'back')
config.bind('n', 'fake-key <down>')
config.bind('p', 'fake-key <up>')
config.bind('tt', 'fake-key <Ctrl+c>;;yank selection;;spawn tts "$(xclip -selection clipboard -o)"')
config.bind('u', 'scroll-page 0 -0.45')

# Caret Mode :kbd:caret:
config.bind('<Alt+a>', 'fake-key <Ctrl+Home>', mode='caret')
config.bind('<Alt+b>', 'fake-key <Ctrl+Left>', mode='caret')
config.bind('<Alt+d>', 'fake-key <Ctrl+Right>;;fake-key <Ctrl+Left>;;fake-key <Ctrl+x>', mode='caret')
config.bind('<Alt+e>', 'fake-key <Ctrl+End>', mode='caret')
config.bind('<Alt+f>', 'fake-key <Ctrl+Right>', mode='caret')
config.bind('<Alt+w>', 'yank selection;;fake-key <Ctrl+c>', mode='caret')
config.bind('<Ctrl+a>', 'fake-key <Home>', mode='caret')
config.bind('<Ctrl+b>', 'fake-key <Left>', mode='caret')
config.bind('<Ctrl+d>', 'fake-key <Delete>', mode='caret')
config.bind('<Ctrl+e>', 'fake-key <End>', mode='caret')
config.bind('<Ctrl+f>', 'fake-key <Right>', mode='caret')
config.bind('<Ctrl+g>', 'mode-leave', mode='caret')
config.bind('<Ctrl+n>', 'move-to-next-line', mode='caret')
config.bind('<Ctrl+p>', 'move-to-prev-line', mode='caret')
config.bind('<Ctrl+w>', 'fake-key <Ctrl+x>', mode='caret')
config.bind('EE', 'fake-key <ctrl+c>;;yank selection;;spawn sleep 0.3;;spawn --detach st -e seledit', mode='caret')
config.bind('d', 'fake-key <down>', mode='caret')
config.bind('j', 'move-to-next-line;;scroll-page 0 0.03', mode='caret')
config.bind('k', 'move-to-prev-line;;scroll-page 0 -0.03', mode='caret')
config.bind('tt', 'fake-key <Ctrl+c>;;yank selection;;spawn tts "$(xclip -selection clipboard -o)" ', mode='caret')
config.bind('u', 'fake-key <up>', mode='caret')

## Command Mode :kbd:cmd:
config.bind('<alt-backspace>', 'rl-backward-kill-word', mode='command')
config.bind('<alt-shift-a>', 'fake-key <Ctrl+Shift+Home>', mode='command')
config.bind('<alt-shift-b>', 'fake-key <Ctrl+Shift+Left>', mode='command')
config.bind('<alt-shift-e>', 'fake-key <Ctrl+Shift+End>', mode='command')
config.bind('<alt-shift-f>', 'fake-key <Ctrl+Shift+Right>', mode='command')
config.bind('<alt-shift-h>', 'fake-key <Shift+Home>', mode='command')
config.bind('<alt-b>', 'rl-backward-word', mode='command')
config.bind('<alt-c>', 'fake-key <Ctrl+c>;;yank selection', mode='command')
config.bind('<alt-d>', 'rl-kill-word', mode='command')
config.bind('<alt-f>', 'rl-forward-word', mode='command')
config.bind('<alt-m>', 'completion-item-yank --sel', mode='command')
config.bind('<alt-n>', 'command-history-next', mode='command')
config.bind('<alt-p>', 'command-history-prev', mode='command')
config.bind('<alt-shift-p>', 'insert-text {primary}', mode='command')
config.bind('<alt-u>', 'rl-rubout " "', mode='command')
config.bind('<alt-v>', 'fake-key <Ctrl+v> --global', mode='command')
config.bind('<ctrl-,>', 'command-accept --rapid', mode='command')
config.bind('<ctrl-.>', 'command-repeat', mode='command')
config.bind('<ctrl-shift-a>', 'rl-beginning-of-line', mode='command')
config.bind('<ctrl-shift-b>', 'completion-item-focus prev-category', mode='command')
config.bind('<ctrl-shift-f>', 'completion-item-focus next-category', mode='command')
config.bind('<ctrl-shift-d>', 'completion-item-del', mode='command')
config.bind('<ctrl-shift-c>', 'completion-item-yank', mode='command')
config.bind('<ctrl-shift-w>', 'rl-filename-rubout', mode='command')
config.bind('<ctrl-a>', 'rl-beginning-of-line', mode='command')
config.bind('<ctrl-b>', 'rl-backward-char', mode='command')
config.bind('<ctrl-d>', 'rl-delete-char', mode='command')
config.bind('<ctrl-e>', 'rl-end-of-line', mode='command')
config.bind('<ctrl-f>', 'rl-forward-char', mode='command')
config.bind('<ctrl-h>', 'rl-backward-delete-char', mode='command')
config.bind('<ctrl-k>', 'rl-kill-line', mode='command')
config.bind('<ctrl-n>', 'completion-item-focus next', mode='command')
config.bind('<ctrl-p>', 'completion-item-focus prev', mode='command')
config.bind('<ctrl-u>', 'rl-rubout', mode='command')
config.bind('<ctrl-w>', 'rl-backward-kill-word', mode='command')
config.bind('<ctrl-y>', 'rl-yank', mode='command')
config.bind('<ctrl-g>', 'mode-leave', mode='command')
config.bind('<escape>', 'mode-leave', mode='command')

# Hint Mode :kbd:hint:
config.bind('<ctrl-g>', 'clear-keychain ;; search ;; fullscreen --leave ;; mode-leave', mode='hint')
config.bind('<tab>', 'hint inputs --first', mode='hint')
config.bind('<escape>', 'mode-leave', mode='hint')

# Insert Mode :kbd:insert:
config.bind('<alt-shift-@>', 'fake-key <Ctrl+Shift+Right>', mode='insert')
config.bind('<alt-shift-a>', 'fake-key <Ctrl+Shift+Home>', mode='insert')
config.bind('<alt-shift-b>', 'fake-key <Ctrl+Shift+Left>', mode='insert')
config.bind('<alt-shift-e>', 'fake-key <Ctrl+Shift+End>', mode='insert')
config.bind('<alt-shift-f>', 'fake-key <Ctrl+Shift+Right>', mode='insert')
config.bind('<alt-shift-h>', 'fake-key <Shift+Home>', mode='insert')
config.bind('<alt-shift-o>', 'fake-key <Home>;;fake-key <Backspace>', mode='insert')
config.bind('<alt-space>', 'fake-key <Home>;;fake-key <Ctrl+Shift+End>', mode='insert')
config.bind('<alt-a>', 'fake-key <Ctrl+Home>', mode='insert')
config.bind('<alt-b>', 'fake-key <Ctrl+Left>', mode='insert')
config.bind('<alt-c>', 'fake-key <Ctrl+c>', mode='insert')
config.bind('<alt-d>', 'fake-key <Ctrl+Delete>', mode='insert')
config.bind('<alt-e>', 'fake-key <Ctrl+End>', mode='insert')
# config.bind('<alt-d>', 'fake-key <Ctrl+Right>;;fake-key <Ctrl+Shift+Left>;;fake-key <Delete>', mode='insert')
config.bind('<alt-f>', 'fake-key <Ctrl+Right>', mode='insert')
config.bind('<alt-i>', 'fake-key <Home>;;fake-key <Ctrl+Right>;;fake-key <Ctrl+Left>', mode='insert')
config.bind('<alt-o>', 'fake-key <Home>;;fake-key <Shift+Return>;;fake-key <Up>;;fake-key <Home>', mode='insert')
config.bind('<alt-p>', 'insert-text {primary}', mode='insert')
config.bind('<alt-u>', 'fake-key <Ctrl+Shift+Home>;;fake-key <Ctrl+x>', mode='insert')
config.bind('<alt-v>', 'fake-key <Ctrl+v>', mode='insert')
config.bind('<alt-w>', 'fake-key <Ctrl+c>', mode='insert')
config.bind('<alt-y>', 'fake-key <Home>;;fake-key <Shift+End>;;fake-key <Ctrl+c>;;fake-key <End>', mode='insert')
config.bind("<ctrl-'>", 'fake-key <Ctrl+Shift+Right>', mode='insert')
config.bind('<ctrl-+>', 'zoom 100%', mode='insert')
config.bind('<ctrl-->', 'zoom-out', mode='insert')
config.bind('<ctrl-0>', 'zoom 100%', mode='insert')
config.bind('<ctrl-;>', 'fake-key <Ctrl+Shift+Left>', mode='insert')
config.bind('<ctrl-=>', 'zoom-in', mode='insert')
config.bind('<ctrl-alt-shift-a>', 'fake-key <Ctrl+a>', mode='insert')
config.bind('<ctrl-alt-space>', 'fake-key <Ctrl+Shift+Left>', mode='insert')
config.bind('<ctrl-alt-a>', 'fake-key <Ctrl+Shift+Home>', mode='insert')
config.bind('<ctrl-alt-e>', 'fake-key <Ctrl+Shift+End>', mode='insert')
config.bind('<ctrl-alt-k>', 'fake-key <Shift+End>;;fake-key <Ctrl+x>', mode='insert')
config.bind('<ctrl-alt-m>', 'fake-key <Shift+End>;;fake-key <Ctrl+c>', mode='insert')
config.bind('<ctrl-alt-p>', 'fake-key <Shift+Home>;;fake-key <Ctrl+c>', mode='insert')
config.bind('<ctrl-alt-w>', 'fake-key <Ctrl+Home>;;fake-key <Shift+End>;;fake-key <Ctrl+c>', mode='insert')
config.bind('<ctrl-shift-a>', 'fake-key <Shift+Home>', mode='insert')
config.bind('<ctrl-shift-b>', 'fake-key <Shift+Left>', mode='insert')
config.bind('<ctrl-shift-e>', 'fake-key <Shift+End>', mode='insert')
config.bind('<ctrl-shift-f>', 'fake-key <Shift+Right>', mode='insert')
config.bind('<ctrl-shift-h>', 'fake-key <Ctrl+Shift+Left>;;fake-key <Ctrl+c>', mode='insert')
config.bind('<ctrl-shift-j>', 'fake-key <Shift+Down>', mode='insert')
config.bind('<ctrl-shift-k>', 'fake-key <Shift+Up>', mode='insert')
config.bind('<ctrl-shift-l>', 'fake-key <Shift+End>;;fake-key <Ctrl+x>', mode='insert')
config.bind('<ctrl-shift-n>', 'fake-key <Shift+Down>', mode='insert')
config.bind('<ctrl-shift-p>', 'fake-key <Shift+Up>', mode='insert')
config.bind('<ctrl-space>', 'fake-key <Ctrl+Shift+Right>', mode='insert')
config.bind('<ctrl-a>', 'fake-key <Home>', mode='insert')
config.bind('<ctrl-b>', 'fake-key <Left>', mode='insert')
config.bind('<ctrl-d>', 'fake-key <Delete>', mode='insert')
config.bind('<ctrl-e>', 'fake-key <End>', mode='insert')
config.bind('<ctrl-f>', 'fake-key <Right>', mode='insert')
config.bind('<ctrl-g>', 'clear-keychain ;; search ;; fullscreen --leave ;; mode-leave', mode='insert')
config.bind('<ctrl-h>', 'fake-key <Backspace>', mode='insert')
config.bind('<ctrl-k>', 'fake-key <Shift+End>;;fake-key <Ctrl+x>', mode='insert')
config.bind('<ctrl-n>', 'fake-key <Down>', mode='insert')
config.bind('<ctrl-o>', 'fake-key <Shift+Return>;;fake-key <Up>;;fake-key <End>', mode='insert')
config.bind('<ctrl-p>', 'fake-key <Up>', mode='insert')
config.bind('<ctrl-u>', 'fake-key <Shift+Home>;;fake-key <Ctrl+x>', mode='insert')
config.bind('<ctrl-w>', 'fake-key <Ctrl+Shift+Left>;;fake-key <Ctrl+x>', mode='insert')
config.bind('<ctrl-y>', 'fake-key <Ctrl+v>', mode='insert')
config.bind('<escape>', 'mode-leave', mode='insert')

## Passthrough Mode :kbd:passthrough:
config.bind('<alt-shift-@>', 'fake-key <Ctrl+Shift+Right>', mode='passthrough')
config.bind('<alt-shift-a>', 'fake-key <Ctrl+Shift+Home>', mode='passthrough')
config.bind('<alt-shift-b>', 'fake-key <Ctrl+Shift+Left>', mode='passthrough')
config.bind('<alt-shift-e>', 'fake-key <Ctrl+Shift+End>', mode='passthrough')
config.bind('<alt-shift-f>', 'fake-key <Ctrl+Shift+Right>', mode='passthrough')
config.bind('<alt-shift-h>', 'fake-key <Shift+Home>', mode='passthrough')
config.bind('<alt-shift-o>', 'fake-key <Home>;;fake-key <Backspace>', mode='passthrough')
config.bind('<alt-space>', 'fake-key <Home>;;fake-key <Ctrl+Shift+End>', mode='passthrough')
config.bind('<alt-a>', 'fake-key <Ctrl+Home>', mode='passthrough')
config.bind('<alt-b>', 'fake-key <Ctrl+Left>', mode='passthrough')
config.bind('<alt-c>', 'fake-key <Ctrl+c>', mode='passthrough')
config.bind('<alt-d>', 'fake-key <Ctrl+Right>;;fake-key <Ctrl+Shift+Left>;;fake-key <Delete>', mode='passthrough')
config.bind('<alt-e>', 'fake-key <Ctrl+End>', mode='passthrough')
config.bind('<alt-f>', 'fake-key <Ctrl+Right>', mode='passthrough')
config.bind('<alt-i>', 'fake-key <Home>;;fake-key <Ctrl+Right>;;fake-key <Ctrl+Left>', mode='passthrough')
config.bind('<alt-o>', 'fake-key <Home>;;fake-key <Shift+Return>;;fake-key <Up>;;fake-key <Home>', mode='passthrough')
config.bind('<alt-p>', 'insert-text {primary}', mode='passthrough')
config.bind('<alt-u>', 'fake-key <Ctrl+Shift+Home>;;fake-key <Ctrl+x>', mode='passthrough')
config.bind('<alt-v>', 'fake-key <Ctrl+v>', mode='passthrough')
config.bind('<alt-w>', 'fake-key <Ctrl+c>', mode='passthrough')
config.bind('<alt-y>', 'fake-key <Home>;;fake-key <Shift+End>;;fake-key <Ctrl+c>;;fake-key <End>', mode='passthrough')
config.bind("<ctrl-'>", 'fake-key <Ctrl+Shift+Right>', mode='passthrough')
config.bind('<ctrl-+>', 'zoom 100%', mode='passthrough')
config.bind('<ctrl-->', 'zoom-out', mode='passthrough')
config.bind('<ctrl-0>', 'zoom 100%', mode='passthrough')
config.bind('<ctrl-;>', 'fake-key <Ctrl+Shift+Left>', mode='passthrough')
config.bind('<ctrl-=>', 'zoom-in', mode='passthrough')
config.bind('<ctrl-alt-shift-a>', 'fake-key <Ctrl+a>', mode='passthrough')
config.bind('<ctrl-alt-space>', 'fake-key <Ctrl+Shift+Left>', mode='passthrough')
config.bind('<ctrl-alt-a>', 'fake-key <Ctrl+Shift+Home>', mode='passthrough')
config.bind('<ctrl-alt-e>', 'fake-key <Ctrl+Shift+End>', mode='passthrough')
config.bind('<ctrl-alt-k>', 'fake-key <Shift+End>;;fake-key <Ctrl+x>', mode='passthrough')
config.bind('<ctrl-alt-m>', 'fake-key <Shift+End>;;fake-key <Ctrl+c>', mode='passthrough')
config.bind('<ctrl-alt-p>', 'fake-key <Shift+Home>;;fake-key <Ctrl+c>', mode='passthrough')
config.bind('<ctrl-alt-w>', 'fake-key <Ctrl+Home>;;fake-key <Shift+End>;;fake-key <Ctrl+c>', mode='passthrough')
config.bind('<ctrl-shift-a>', 'fake-key <Shift+Home>', mode='passthrough')
config.bind('<ctrl-shift-b>', 'fake-key <Shift+Left>', mode='passthrough')
config.bind('<ctrl-shift-e>', 'fake-key <Shift+End>', mode='passthrough')
config.bind('<ctrl-shift-f>', 'fake-key <Shift+Right>', mode='passthrough')
config.bind('<ctrl-shift-h>', 'fake-key <Ctrl+Shift+Left>;;fake-key <Ctrl+c>', mode='passthrough')
config.bind('<ctrl-shift-j>', 'fake-key <Shift+Down>', mode='passthrough')
config.bind('<ctrl-shift-k>', 'fake-key <Shift+Up>', mode='passthrough')
config.bind('<ctrl-shift-l>', 'fake-key <Shift+End>;;fake-key <Ctrl+x>', mode='passthrough')
config.bind('<ctrl-shift-n>', 'fake-key <Shift+Down>', mode='passthrough')
config.bind('<ctrl-shift-p>', 'fake-key <Shift+Up>', mode='passthrough')
config.bind('<ctrl-space>', 'fake-key <Ctrl+Shift+Right>', mode='passthrough')
config.bind('<ctrl-a>', 'fake-key <Home>', mode='passthrough')
config.bind('<ctrl-b>', 'fake-key <Left>', mode='passthrough')
config.bind('<ctrl-d>', 'fake-key <Delete>', mode='passthrough')
config.bind('<ctrl-e>', 'fake-key <End>', mode='passthrough')
config.bind('<ctrl-f>', 'fake-key <Right>', mode='passthrough')
config.bind('<ctrl-g>', 'fake-key <Escape>', mode='passthrough')
config.bind('<ctrl-h>', 'fake-key <Backspace>', mode='passthrough')
config.bind('<ctrl-k>', 'fake-key <Shift+End>;;fake-key <Ctrl+x>', mode='passthrough')
config.bind('<ctrl-n>', 'fake-key <Down>', mode='passthrough')
config.bind('<ctrl-o>', 'fake-key <Shift+Return>;;fake-key <Up>;;fake-key <End>', mode='passthrough')
config.bind('<ctrl-p>', 'fake-key <Up>', mode='passthrough')
config.bind('<ctrl-u>', 'fake-key <Shift+Home>;;fake-key <Ctrl+x>', mode='passthrough')
config.bind('<ctrl-w>', 'fake-key <Ctrl+Shift+Left>;;fake-key <Ctrl+x>', mode='passthrough')
config.bind('<ctrl-y>', 'fake-key <Ctrl+v>', mode='passthrough')
config.bind('<ctrl-alt-g>', 'mode-leave', mode='passthrough')
config.bind('<escape>', 'fake-key <Escape>', mode='passthrough')

## Prompt Mode :kbd:prompt:
config.bind('<alt-backspace>', 'rl-backward-kill-word', mode='prompt')
config.bind('<alt-b>', 'rl-backward-word', mode='prompt')
config.bind('<alt-d>', 'rl-kill-word', mode='prompt')
config.bind('<alt-f>', 'rl-forward-word', mode='prompt')
config.bind('<alt-p>', 'insert-text {primary}', mode='prompt')
config.bind('<alt-u>', 'rl-unix-line-discard', mode='prompt')
config.bind('<ctrl-a>', 'rl-beginning-of-line', mode='prompt')
config.bind('<ctrl-b>', 'rl-backward-char', mode='prompt')
config.bind('<ctrl-e>', 'rl-end-of-line', mode='prompt')
config.bind('<ctrl-f>', 'rl-forward-char', mode='prompt')
config.bind('<ctrl-h>', 'rl-backward-delete-char', mode='prompt')
config.bind('<ctrl-k>', 'rl-kill-line', mode='prompt')
config.bind('<ctrl-u>', 'rl-rubout', mode='prompt')
config.bind('<ctrl-w>', 'rl-filename-rubout', mode='prompt')
config.bind('<ctrl-y>', 'rl-yank', mode='prompt')
config.bind('<escape>', 'mode-leave', mode='prompt')
