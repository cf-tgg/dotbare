# config.py --- qutebrowser config -*- mode: python-ts; -*-

# Global Settings

config.load_autoconfig(False)

c.aliases = {'GG': 'session-load GG', 'q': 'close', 'qa': 'quit', 'w': 'session-save', 'wconf': 'config-write-py --force', 'wq': 'quit --save', 'wqa': 'quit --save', 'load': 'session-load', 'src': 'config-source'}
c.new_instance_open_target = 'tab'
c.new_instance_open_target_window = 'last-focused'
c.qt.highdpi = True
c.qt.workarounds.disable_hangouts_extension = True

c.scrolling.smooth = False
c.window.transparent = False
c.scrolling.bar = 'overlay'
c.statusbar.show = 'never'
c.statusbar.position = 'top'

c.tabs.show = 'switching'
c.tabs.show_switching_delay = 10000
c.hints.border = '1px #0D0D0D #00020b'
c.completion.shrink = True
c.completion.scrollbar.width = 0
c.downloads.location.prompt = True
c.downloads.remove_finished = 1000
c.downloads.position = 'bottom'
c.zoom.levels = ['25%', '30%', '35%', '40%', '45%', '50%', '55%', '60%', '65%', '70%', '75%', '80%', '85%', '90%', '95%', '100%', '105%', '110%', '115%', '120%', '125%', '130%', '135%', '140%', '145%', '150%', '155%', '160%', '165%', '170%', '175%', '180%', '185%', '190%', '195%', '200%', '205%', '210%', '215%', '220%', '225%', '230%', '235%', '240%', '245%', '250%', '255%', '260%', '265%', '270%', '275%', '280%', '285%', '290%', '295%', '300%', '305%', '310%', '315%', '320%', '325%', '330%', '335%', '340%', '345%', '350%', '355%', '360%', '365%', '370%', '375%', '380%', '385%', '390%', '395%', '400%', '405%', '410%', '415%', '420%', '425%', '430%', '435%', '440%', '445%', '450%', '455%', '460%', '465%', '470%', '475%', '480%', '485%', '490%', '495%', '500%']
c.zoom.default = '100%'

c.editor.command = ['emacsclient', '-c', '-n', '--alternate-editor=\"\"', '--socket-name=\"/run/user/1000/emacs/server\"', '+{line}:{column}', '{file}']
c.url.default_page = 'file:///home/cf/Templates/html/startpage/backpage.html'
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}', '!': 'https://duckduckgo.com/?q=!{}', 'archwiki': 'https://duckduckgo.com/?q=!archwiki {}',  'stract': 'https://stract.com/search?ss=false&sr=N4IgNglg1gpgJiAXAbQLoBoRwgZ0rBFDEAIzAHsBjApNAXyA&q={}&optic=&gl=All'}
c.url.start_pages = 'file:///home/cf/Templates/html/startpage/backpage.html'

# Content Settings
c.content.site_specific_quirks.enabled = True
c.content.persistent_storage = 'ask'
c.content.plugins = False
c.content.print_element_backgrounds = True
c.content.prefers_reduced_motion = False
c.content.webgl = True
c.content.user_stylesheets = ['~/Templates/css/style.css', '~/Templates/css/cgpt.css']

## Content AdBlocking :content:adblock:
c.content.blocking.enabled = True
c.content.blocking.hosts.lists = ['https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts']
c.content.blocking.hosts.block_subdomains = True
c.content.blocking.adblock.lists = ['https://easylist.to/easylist/easylist.txt', 'https://easylist.to/easylist/easyprivacy.txt', 'https://raw.githubusercontent.com/CrusheerPL/AlleBlockV2/master/AlleBlockV2.txt']
c.content.blocking.whitelist = []
c.content.blocking.method = 'auto'

## Content Cookies :content:cookies:
c.content.cookies.accept = 'no-3rdparty'
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')
config.set('content.cookies.accept', 'all', 'devtools://*')

## Content Geolocation :content:geo:
config.set('content.geolocation', True, 'https://maps.google.com')
config.set('content.geolocation', False, 'https://www.google.com')
config.set('content.geolocation', False, 'https://www.qub.ca')
config.set('content.geolocation', False, 'https://www.tuango.ca')

## Content Headers :content:headers:
config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:133.0) Gecko/20100101 Firefox/133.0', 'https://accounts.google.com/*')

## Content Images :content:img:
config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')

## Content JavaScript :content:js:
c.content.javascript.clipboard = 'access'
config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')

## Content Access :content:access:
config.set('content.local_content_can_access_remote_urls', True, 'file:///home/cf/.local/share/qutebrowser/userscripts/*')
config.set('content.local_content_can_access_remote_urls', True, 'file:///home/cf/Templates/html/startpage/*')
config.set('content.local_content_can_access_file_urls', True, 'file:///home/cf/.local/share/qutebrowser/userscripts/*')
config.set('content.local_content_can_access_file_urls', True, 'file:///home/cf/Templates/html/startpage/*')

## Content Media :content:media
c.content.autoplay = False
c.content.media.audio_video_capture = True
config.set('content.media.audio_capture', True, 'https://www.messenger.com/*')
config.set('content.media.audio_capture', True, 'https://www.messenger.com/*/*')
config.set('content.media.audio_capture', True, 'https://www.facebook.com/*')
config.set('content.media.audio_capture', True, 'https://teams.microsoft.com/*')
config.set('content.media.video_capture', True, 'https://www.messenger.com')
config.set('content.media.video_capture', True, 'https://www.messenger.com/*/*')
config.set('content.media.video_capture', True, 'https://www.facebook.com')
config.set('content.media.video_capture', True, 'https://teams.microsoft.com')
config.set('content.media.audio_video_capture', True, 'https://teams.microsoft.com')

## Content Notifications :content:notify:
c.content.notifications.presenter = 'libnotify'
c.content.notifications.show_origin = True
config.set('content.notifications.enabled', False, 'https://www.facebook.com')
config.set('content.notifications.enabled', False, 'https://www.netflix.com')
config.set('content.notifications.enabled', False, 'https://www.reddit.com')
config.set('content.notifications.enabled', True, 'https://teams.live.com')
config.set('content.notifications.enabled', True, 'https://teams.microsoft.com')
config.set('content.notifications.enabled', False, 'https://www.tiktok.com')

## Content Protocol Handlers :content:proto:
config.set('content.register_protocol_handler', True, 'https://mail.google.com?extsrc=mailto&url=%25s')
config.set('content.register_protocol_handler', True, 'https://outlook.office.com?mailtouri=%25s')
config.set('content.register_protocol_handler', True, 'https://outlook.live.com?mailtouri=%25s')
config.set('content.register_protocol_handler', True, 'https://mail.proton.me#mailto=%25s')

## Theme Dark Mode :theme:dark:
c.colors.webpage.preferred_color_scheme = 'dark'
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.images = 'never'
c.colors.webpage.darkmode.policy.page = 'always'

## Theme Colors :theme:colors:
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
c.colors.statusbar.normal.fg = '#484848'
c.colors.statusbar.passthrough.fg = '#484848'
c.colors.statusbar.passthrough.bg = '#121212'
c.colors.statusbar.insert.bg = '#000000'
c.colors.statusbar.insert.fg = '#323232'
c.colors.statusbar.caret.fg = '#382020'
c.colors.statusbar.caret.bg = '#000000'
c.colors.statusbar.caret.selection.fg = '#3f2020'
c.colors.statusbar.caret.selection.bg = '#0b0000'
c.colors.prompts.bg = '#121212'
c.colors.prompts.border = '#000000'

c.colors.prompts.selected.bg = '#242424'
c.colors.prompts.selected.fg = '#f4f4f4'
c.colors.tabs.bar.bg = '#121212'
c.colors.tabs.odd.bg = '#121212'
c.colors.tabs.even.bg = '#121212'
c.colors.webpage.bg = '#121212'

## Theme Fonts :theme:font:
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

# Key Bindings :kbd:
#  c.bindings.key_mappings = {'<Ctrl-[>': '<Escape>', '<Ctrl-6>': '<Ctrl-^>', '<Ctrl-M>': '<Return>', '<Ctrl-J>': '<Return>', '<Ctrl-I>': '<Tab>', '<Enter>': '<Return>', '<Ctrl-Enter>': '<Ctrl-Return>'}
#  c.input.forward_unbound_keys = "all"

#  def bind_chained(key, *commands):
#      config.bind(key, ' ;; '.join(commands))
#  bind_chained('<Escape>', 'clear-keychain', 'search')

#  ## Normal Mode :kbd:norm:
#  ESC_BIND = 'clear-keychain ;; search ;; fullscreen --leave'

#  c.bindings.commands['normal'] = {
#  	# Navigation
#  	'<ctrl-v>': 'scroll-page 0 0.5',
#  	'<alt-v>': 'scroll-page 0 -0.5',
#  	'<ctrl-shift-v>': 'scroll-page 0 1',
#  	'<alt-shift-v>': 'scroll-page 0 -1',

#  	# commands
#  	'<alt-x>': 'cmd-set-text :',
#  	'<ctrl-x>b': 'cmd-set-text -s :buffer',
#  	'<ctrl-x>k': 'tab-close',
#  	'<Ctrl-x><Ctrl-c>': 'quit',

#  	# searching
#  	'<ctrl-s>': 'cmd-set-text /',
#  	'<ctrl-r>': 'cmd-set-text ?',

#  	# hinting
#  	'<alt-s>': 'hint all',

#  	# history
#  	# FIXME maybe this should be <C-b> <C-n>? Or would that be too confusing?
#  	'<ctrl-]>': 'forward',
#  	'<ctrl-[>': 'back',

#  	# tabs
#  	'<ctrl-tab>': 'tab-next',
#  	'<ctrl-shift-tab>': 'tab-prev',

#  	# open links
#  	'<ctrl-l>': 'cmd-set-text -s :open',
#  	'<alt-l>': 'cmd-set-text -s :open -t',

#  	# editing
#  	'<ctrl-f>': 'fake-key <Right>',
#  	'<ctrl-b>': 'fake-key <Left>',
#  	'<ctrl-a>': 'fake-key <Home>',
#  	'<ctrl-e>': 'fake-key <End>',
#  	'<ctrl-n>': 'fake-key <Down>',
#  	'<ctrl-p>': 'fake-key <Up>',
#  	'<alt-f>': 'fake-key <Ctrl-Right>',
#  	'<alt-b>': 'fake-key <Ctrl-Left>',
#  	'<ctrl-d>': 'fake-key <Delete>',
#  	'<alt-d>': 'fake-key <Ctrl-Delete>',
#  	'<alt-backspace>': 'fake-key <Ctrl-Backspace>',
#  	'<ctrl-w>': 'fake-key <Ctrl-backspace>',
#  	'<ctrl-y>': 'insert-text {primary}',

#  	# Numbers
#  	# https://github.com/qutebrowser/qutebrowser/issues/4213
#  	'1': 'fake-key 1',
#  	'2': 'fake-key 2',
#  	'3': 'fake-key 3',
#  	'4': 'fake-key 4',
#  	'5': 'fake-key 5',
#  	'6': 'fake-key 6',
#  	'7': 'fake-key 7',
#  	'8': 'fake-key 8',
#  	'9': 'fake-key 9',
#  	'0': 'fake-key 0',

#  	# escape hatch
#  	'<ctrl-H>': 'cmd-set-text -s :help',
#  	'<ctrl-g>': ESC_BIND,
#  }

#  c.bindings.commands['command'] = {
#  	'<ctrl-s>': 'search-next',
#  	'<ctrl-r>': 'search-prev',

#  	'<ctrl-p>': 'completion-item-focus prev',
#  	'<ctrl-n>': 'completion-item-focus next',

#  	'<alt-p>': 'command-history-prev',
#  	'<alt-n>': 'command-history-next',

#  	# escape hatch
#  	'<ctrl-g>': 'leave-mode',
#  }

#  c.bindings.commands['hint'] = {
#  	# escape hatch
#  	'<ctrl-g>': 'leave-mode',
#  }

#  c.bindings.commands['caret'] = {
#  	# escape hatch
#  	'<ctrl-g>': 'leave-mode',
#  }

# config.bind('.', 'cmd-repeat-last')
# config.bind(',,', 'jseval --quiet --file ~/.config/qutebrowser/userscripts/toggle_visibility.js')
# config.bind(',.', 'jseval --quiet --file ~/.config/qutebrowser/userscripts/iiie.js')
# config.bind('td', 'jseval --quiet --file ~/.config/qutebrowser/userscripts/iie2.js')
# config.bind('<?', 'set content.user_stylesheets \'["~/Templates/css/style.css", "~/Templates/css/glassy.css"]\'')
# config.bind('>?', 'set content.user_stylesheets \'["~/Templates/css/style.css", "~/Templates/css/cgpt.css"]\'')
# config.bind(',b', ':set statusbar.show in-mode')
# config.bind(',B', ':set statusbar.show never')
# config.bind(',d', 'set downloads.location.prompt true')
# config.bind(',D', 'set downloads.location.prompt false')
# config.bind(',m', 'spawn --detach mpv {url}')
# config.bind(',M', 'hint links spawn --detach mpv {hint-url}')
# config.bind(',R', ':spawn --detach st -e readit -c -l en')
# config.bind(',U', 'hint links spawn umpv {hint-url}')
# config.bind(',l', 'spawn ytcl {url};;cmd-later 100 spawn ytln {url}')
# config.bind(',rf', 'spawn --detach st -e readit -c -l fr')
# config.bind(',rs', 'hint --rapid links spawn rssadd {hint-url}')
# config.bind(',ta', 'cmd-set-text -s :spawn --userscript taskadd')
# config.bind(',th', ':spawn --userscript taskadd due:eod pri:H')
# config.bind(',tt', 'fake-key <Ctrl+c>;;yank selection;;spawn tts "$(xclip -selection clipboard -o)"')
# config.bind(',uM', 'hint --rapid links spawn umpv {hint-url}')
# config.bind(',um', 'spawn umpv {url}')
# config.bind(',yd', 'spawn ydl {url}')
# config.bind(',yt', 'spawn --detach mpv {url}')
# config.bind(',yu', 'hint links spawn --detach ydl {hint-url}')
# config.bind('0', 'hint links userscript append_hint_url')
# config.bind('1', 'zoom 100%')
# config.bind('2', 'zoom 185%')
# config.bind('3', 'zoom 150%')
# config.bind('4', 'zoom 125%')
# config.bind('5', 'zoom 85%')
# config.bind('6', 'quickmark-load qai')
# config.bind('7', 'hint --rapid links spawn ydl {hint-url}')
# config.bind('8', 'spawn ydl {url}')
# config.bind('9', 'hint links spawn ydl {hint-url}')

# config.bind(';D', 'hint --rapid links spawn ydl {hint-url}')
# config.bind(';M', 'hint links spawn mpv {hint-url}')
# config.bind(';N', 'hint --rapid links spawn mpv {hint-url}')
# config.bind(';l', 'hint links spawn ytln {hint-url}')

# config.bind('<Alt+Shift+j>', 'zoom-out')
# config.bind('<Alt+Shift+k>', 'zoom-in')
# config.bind('<Alt+c>', ':fake-key <Ctrl+c>;;yank selection')
# config.bind('<Alt+w>', ':fake-key <Ctrl+c>;;yank selection')

# config.bind('<Ctrl+->', 'zoom-out')
# config.bind('<Ctrl+=>', 'zoom-in')
# config.bind('<Ctrl+0>', 'zoom 100%')
# config.bind('-', 'zoom-out')
# config.bind('=', 'zoom-in')
# config.bind('+', "zoom 100%")
# config.bind('<Ctrl+a>', 'mode-enter insert;;fake-key <Ctrl+a>;;fake-key <Ctrl+c>;;mode-leave')
# config.bind('<Ctrl+i>', 'fake-key <Tab>')
# config.bind('<Ctrl+Alt+i>', 'fake-key <Backtab>')
# config.bind('<Alt+w>', 'fake-key <Ctrl+c>;;yank selection')
# config.bind('<Ctrl+c>', 'fake-key <Ctrl+c>;;yank selection')
# config.bind('<Ctrl+Alt+Shift+e>', 'config-edit')
# config.bind('<Ctrl+e>', 'mode-enter insert;;fake-key <End>')
# config.bind('<Ctrl+d>', 'scroll-page 0 0.9')
# config.bind('<Ctrl+u>', 'scroll-page 0 -0.9')
# config.bind('<Space>', 'scroll-page 0 0.6')
# config.bind('<Backspace>', 'scroll-page 0 -0.6')
# config.bind('N', 'forward')
# config.bind('P', 'back')
# config.bind('<Ctrl+n>', 'fake-key <down>')
# config.bind('<Ctrl+p>', 'fake-key <up>')
# config.bind('n', 'fake-key <down>')
# config.bind('p', 'fake-key <up>')
# config.bind('<Alt+Backspace>', 'back')
# config.bind('EE', 'fake-key <ctrl+c>;;yank selection;;spawn sleep 0.3;;spawn --detach st -e seledit')
# config.bind('TT', 'tab-only')
# config.bind('UU', 'edit-text {url}')
# config.bind('WE', 'spawn wikilocale {url} ;; cmd-later 500 open {clipboard}')
# config.bind('Y', 'fake-key <Ctrl+c>;;yank selection')
# config.bind('d', 'scroll-page 0 0.4;;fake-key <down>;;fake-key <down>')
# config.bind('u', 'scroll-page 0 -0.4;;fake-key <up>;;fake-key <up>')
# config.bind('tt', 'fake-key <Ctrl+c>;;yank selection;;spawn tts "$(xclip -selection clipboard -o)"')
# config.bind('<Ctrl+g>', 'fake-key <Escape>')
# config.bind('gG', ':tab-give 1')
# config.bind('gT', 'cmd-set-text :tab-take -k')

# Caret Mode :kbd:caret:
# config.bind('EE', 'fake-key <ctrl+c>;;yank selection;;spawn sleep 0.3;;spawn --detach st -e seledit', mode='caret')
# config.bind('d', 'fake-key <down>', mode='caret')
# config.bind('u', 'fake-key <up>', mode='caret')
# config.bind('j', 'move-to-next-line;;scroll-page 0 0.03', mode='caret')
# config.bind('k', 'move-to-prev-line;;scroll-page 0 -0.03', mode='caret')
# config.bind('<Ctrl+n>', 'move-to-next-line', mode='caret')
# config.bind('<Ctrl+p>', 'move-to-prev-line', mode='caret')
# config.bind('tt', 'fake-key <Ctrl+c>;;yank selection;;spawn tts "$(xclip -selection clipboard -o)" ', mode='caret')
# config.bind('<Ctrl+a>', 'fake-key <Home>', mode='caret')
# config.bind('<Ctrl+e>', 'fake-key <End>', mode='caret')
# config.bind('<Ctrl+f>', 'fake-key <Right>', mode='caret')
# config.bind('<Ctrl+b>', 'fake-key <Left>', mode='caret')
# config.bind('<Ctrl+w>', 'fake-key <Ctrl+x>', mode='caret')
# config.bind('<Ctrl+d>', 'fake-key <Delete>', mode='caret')
# config.bind('<Alt+w>', 'yank selection;;fake-key <Ctrl+c>', mode='caret')
# config.bind('<Alt+a>', 'fake-key <Ctrl+Home>', mode='caret')
# config.bind('<Alt+f>', 'fake-key <Ctrl+Right>', mode='caret')
# config.bind('<Alt+b>', 'fake-key <Ctrl+Left>', mode='caret')
# config.bind('<Alt+e>', 'fake-key <Ctrl+End>', mode='caret')
# config.bind('<Alt+d>', 'fake-key <Ctrl+Right>;;fake-key <Ctrl+Left>;;fake-key <Ctrl+x>', mode='caret')
# config.bind('<Ctrl+g>', 'mode-leave', mode='caret')
# config.bind('tt', 'fake-key <Ctrl+c>;;yank selection;;spawn tts "$(xclip -selection clipboard -o)" ', mode='caret')
# config.bind('u', 'scroll-page 0 -0.4', mode='caret')

## Command Mode :kbd:cmd:

# config.bind('<Alt+c>', 'fake-key <Ctrl+c>', mode='command')
# config.bind('<Alt+w>', 'fake-key <Ctrl+c>', mode='command')
# config.bind('<Ctrl+y>', 'fake-key <Ctrl+v>', mode='command')
# config.bind('<Alt+v>', 'fake-key <Ctrl+v>', mode='command')
# config.bind('<Alt+p>', 'insert-text {primary}', mode='command')
# config.bind('<Ctrl+,>', 'command-accept --rapid', mode='command')
# config.bind('<Ctrl+.>', 'command-repeat', mode='command')
# config.bind('<Ctrl+n>', ':completion-item-focus next', mode='command')
# config.bind('<Ctrl+p>', ':completion-item-focus prev', mode='command')
# config.bind('<Alt+m>', 'fake-key <Home>', mode='command')
# config.bind('<Ctrl+a>', 'fake-key <Home>', mode='command')
# config.bind('<Ctrl+e>', 'fake-key <End>', mode='command')
# config.bind('<Escape>', 'mode-leave', mode='command')
# config.bind('<Ctrl+g>', 'mode-leave', mode='command')
# config.bind('<Ctrl+h>', 'fake-key <Backspace>', mode='command')
# config.bind('<Ctrl+d>', 'fake-key <Delete>', mode='command')
# config.bind('<Alt+d>', 'fake-key <Ctrl+Delete>', mode='command')
# config.bind('<Alt+u>', 'fake-key <Ctrl+Shift+Home>;;fake-key <Ctrl+x>', mode='command')
# config.bind('<Ctrl+f>', 'fake-key <Right>', mode='command')             # forward-char
# config.bind('<Ctrl+b>', 'fake-key <Left>', mode='command')              # backward-char
# config.bind('<Alt+f>', 'fake-key <Ctrl+Right>', mode='command')             # forward-word
# config.bind('<Alt+b>', 'fake-key <Ctrl+Left>', mode='command')              # backward-word
# config.bind('<Ctrl+Shift+f>', 'fake-key <Shift+Right>', mode='command')     # mark-forward-char
# config.bind('<Ctrl+Shift+b>', 'fake-key <Shift+Left>', mode='command')      # mark-backward-char
# config.bind('<Ctrl+Shift+a>', 'fake-key <Shift+Home>', mode='command')      # mark-beginning-of-line
# config.bind('<Ctrl+Shift+e>', 'fake-key <Shift+End>', mode='command')       # mark-end-of-line
# config.bind('<Alt+Shift+f>', 'fake-key <Ctrl+Shift+Right>', mode='command') # mark-forward-word
# config.bind('<Alt+Shift+b>', 'fake-key <Ctrl+Shift+Left>', mode='command')  # mark-backward-word
# config.bind('<Alt+Shift+a>', 'fake-key <Ctrl+Shift+Home>', mode='command')  # mark-to-beginning-of-text
# config.bind('<Alt+Shift+e>', 'fake-key <Ctrl+Shift+End>', mode='command')   # mark-end-of-text
# config.bind('<Alt+Shift+h>', 'fake-key <Shift+Home>', mode='command')       # mark-beginning-of-line

## Insert Mode :kbd:ins:

# config.bind('<Escape>', 'mode-leave', mode='insert')
# config.bind('<Ctrl+g>', 'mode-leave', mode='insert')
# config.bind('<Ctrl+->', 'zoom-out', mode='insert')
# config.bind('<Ctrl+=>', 'zoom-in', mode='insert')
# config.bind('<Ctrl+Shift+e>', 'scroll-page 0 -0.4', mode='insert')
# config.bind('<Ctrl+Shift+y>', 'scroll-page 0 0.4', mode='insert')
# config.bind('<Alt+p>', 'insert-text {primary}', mode='insert')
# config.bind('<Alt+Shift+p>', 'insert-text {primary}', mode='insert')
# config.bind('<Tab>', 'fake-key <space>;;fake-key <space>;;fake-key <space>;;fake-key <space>', mode='insert')
# config.bind('<Ctrl+Alt+Space>', 'fake-key <Home>;;fake-key <Shift+End>;;fake-key <Ctrl+c>;;fake-key <End>;;fake-key <Return>;;fake-key <Ctrl+v>', mode='insert') # duplicate-line
# config.bind('<Ctrl+o>', 'fake-key <Shift+Return>;;fake-key <Up>;;fake-key <End>', mode='insert')
# config.bind('<Alt+o>', 'fake-key <Home>;;fake-key <Shift+Return>;;fake-key <Up>', mode='insert')
# config.bind('<Alt+Shift+o>', 'fake-key <End>;;fake-key <Shift+Return>', mode='insert')
# config.bind('<Ctrl+a>', 'fake-key <Home>', mode='insert')      # move-to-beginning-of-line
# config.bind('<Ctrl+e>', 'fake-key <End>', mode='insert')       # end-of-line
# config.bind('<Ctrl+f>', 'fake-key <Right>', mode='insert')     # forward-char
# config.bind('<Ctrl+b>', 'fake-key <Left>', mode='insert')      # backward-char
# config.bind('<Ctrl+n>', 'fake-key <Down>', mode='insert')      # forward-line
# config.bind('<Ctrl+p>', 'fake-key <Up>', mode='insert')        # previous-line
# config.bind('<Ctrl+d>', 'fake-key <Delete>', mode='insert')    # delete-char
# config.bind('<Ctrl+h>', 'fake-key <Backspace>', mode='insert') # backward-delete-char
# config.bind('<Alt+b>', 'fake-key <Ctrl+Left>', mode='insert')  # backward-word
# config.bind('<Alt+f>', 'fake-key <Ctrl+Right>', mode='insert') # forward-word
# config.bind('<Alt+a>', 'fake-key <Ctrl+Home>', mode='insert') # move-to-text-start
# config.bind('<Alt+e>', 'fake-key <Ctrl+End>', mode='insert')  # move-to-end-of-text
# config.bind('<Alt+i>', 'fake-key <Home>;;fake-key <Ctrl+Right>;;fake-key <Ctrl+Left>', mode='insert') # back-to-indentation
# config.bind('<Alt+d>', 'fake-key <Ctrl+Right>;;fake-key <Ctrl+Left>;;fake-key <Ctrl+x>', mode='insert')
# config.bind('<Alt+c>', 'fake-key <Ctrl+c>', mode='insert')  # copy (st)
# config.bind('<Alt+v>', 'fake-key <Ctrl+v>', mode='insert')  # paste (st)
# config.bind('<Ctrl+y>', 'fake-key <Ctrl+v>', mode='insert') # yank
# config.bind('<Alt+w>', 'fake-key <Ctrl+c>', mode='insert')  # kill-ring-save
# config.bind('<Alt+y>', 'fake-key <Home>;;fake-key <Shift+End>;;fake-key <Ctrl+c>;;fake-key <End>', mode='insert') # copy-whole-line
# config.bind('<Ctrl+Alt+k>', 'fake-key <Shift+End>;;fake-key <Ctrl+x>', mode='insert') # kill-end-of-line
# config.bind('<Ctrl+Alt+w>', 'fake-key <Ctrl+Home>;;fake-key <Shift+End>;;fake-key <Ctrl+c>', mode='insert') # copy-whole-text
# config.bind('<Ctrl+Alt+m>', 'fake-key <Shift+End>;;fake-key <Ctrl+c>', mode='insert') # copy-forward-line
# config.bind('<Ctrl+Alt+p>', 'fake-key <Shift+Home>;;fake-key <Ctrl+c>', mode='insert') # copy-previous-line
# config.bind('<Ctrl+Shift+f>', 'fake-key <Shift+Right>', mode='insert')     # mark-forward-char
# config.bind('<Ctrl+Shift+b>', 'fake-key <Shift+Left>', mode='insert')      # mark-backward-char
# config.bind('<Ctrl+Shift+a>', 'fake-key <Shift+Home>', mode='insert')      # mark-beginning-of-line
# config.bind('<Ctrl+Shift+e>', 'fake-key <Shift+End>', mode='insert')       # mark-end-of-line
# config.bind('<Alt+Shift+f>', 'fake-key <Ctrl+Shift+Right>', mode='insert') # mark-forward-word
# config.bind('<Alt+Shift+b>', 'fake-key <Ctrl+Shift+Left>', mode='insert')  # mark-backward-word
# config.bind('<Alt+Shift+a>', 'fake-key <Ctrl+Shift+Home>', mode='insert')  # mark-to-beginning-of-text
# config.bind('<Alt+Shift+e>', 'fake-key <Ctrl+Shift+End>', mode='insert')   # mark-end-of-text
# config.bind('<Alt+Shift+h>', 'fake-key <Shift+Home>', mode='insert')       # mark-beginning-of-line
# config.bind('<Ctrl+l>', 'fake-key <Shift+End>', mode='insert')             # mark-end-of-line
# config.bind('<Ctrl+Shift+l>', 'fake-key <Shift+End>;;fake-key <Ctrl+x>', mode='insert') # kill-end-of-line

# config.bind('<Alt+Shift+@>', 'fake-key <Ctrl+Shift+Right>', mode='insert')                    # mark-word
# config.bind('<Ctrl+\'>', 'fake-key <Ctrl+Shift+Right>', mode='insert')                        # mark-word
# config.bind('<Ctrl+;>', 'fake-key <Ctrl+Shift+Left>', mode='insert')                          # mark-backward-word
# config.bind('<Alt+Space>', 'fake-key <Home>;;fake-key <Ctrl+Shift+End>', mode='insert')       # mark-whole-line
# config.bind('<Ctrl+Space>', 'fake-key <Ctrl+Shift+Right>', mode='insert')                     # mark-word
# config.bind('<Ctrl+Shift+Space>', 'fake-key <Ctrl+Shift+Left>', mode='insert')                # mark-previous-word

# config.bind('<Ctrl+Alt+Shift+a>', 'fake-key <Ctrl+a>', mode='insert') # select all
# config.bind('<Ctrl+Alt+a>', 'fake-key <Ctrl+a>', mode='insert')       # select-all

# config.bind('<Ctrl+Shift+n>', 'fake-key <Shift+Down>', mode='insert') # mark-forward-line
# config.bind('<Ctrl+Shift+p>', 'fake-key <Shift+Up>', mode='insert')   # mark-previous-line
# config.bind('<Ctrl+Shift+j>', 'fake-key <Shift+Down>', mode='insert') # mark-forward-line
# config.bind('<Ctrl+Shift+k>', 'fake-key <Shift+Up>', mode='insert')   # mark-previous-line

# config.bind('<Ctrl+k>', 'fake-key <Shift+End>;;fake-key <Ctrl+c>;;fake-key <Delete>', mode='insert') # kill-line
# config.bind('<Ctrl+w>', 'fake-key <Ctrl+c>;;fake-key <Ctrl+Backspace>', mode='insert')        # kill-backward-word
# config.bind('<Ctrl+u>', 'fake-key <Shift+Home>;;fake-key <Ctrl+x>', mode='insert')            # unix-rubout
# config.bind('<Alt+u>', 'fake-key <Ctrl+Shift+Home>;;fake-key <Ctrl+x>', mode='insert')        # kill-to-beginning-of-text
# config.bind('<Ctrl+Alt+k>', 'fake-key <Ctrl+Shift+End>;;fake-key <Ctrl+x>', mode='insert')    # kill-to-end-of-text
# config.bind('<Ctrl+Shift+h>', 'fake-key <Ctrl+Shift+Left>;;fake-key <Ctrl+c>', mode='insert') # copy-backward-word
# config.bind('<Alt+d>', 'fake-key <Ctrl+Right>;;fake-key <Ctrl+Shift+Left>;;fake-key <Ctrl+x>', mode='insert') # kill-word

# config.bind('<Ctrl+i>', 'fake-key <Tab>', mode='insert')
# config.bind('<Ctrl+Alt+i>', 'fake-key <Backtab>', mode='insert')
# config.bind('<Ctrl+m>', 'fake-key <Shift+Return>', mode='insert')
# config.bind('<Ctrl+j>', 'fake-key <Shift+Return>', mode='insert')

## Passthrough Mode :kbd:passthrough:

# config.bind('<Ctrl+->', 'zoom-out', mode='passthrough')
# config.bind('<Ctrl+=>', 'zoom-in', mode='passthrough')
# config.bind('<Escape>', 'mode-leave', mode='passthrough')
# config.bind('<Ctrl+g>', 'mode-leave', mode='passthrough')

# config.bind('<Alt+Shift+p>', 'insert-text {primary}', mode='passthrough')
# config.bind('<Tab>', 'fake-key <Tab>', mode='passthrough')
# config.bind('<Ctrl+Alt+Space>', 'fake-key <Home>;;fake-key <Ctrl+Shift+End>;;fake-key <Ctrl+c>;;fake-key <End>;;fake-key <Return>;;fake-key <Ctrl+v>', mode='passthrough') # duplicate-line

# config.bind('<Ctrl+o>', 'fake-key <Shift+Return>;;fake-key <Up>;;fake-key <End>', mode='passthrough')
# config.bind('<Alt+o>', 'fake-key <Home>;;fake-key <Shift+Return>;;fake-key <Up>;;fake-key <Home>', mode='passthrough')
# config.bind('<Alt+Shift+o>', 'fake-key <End>;;fake-key <Shift+Return>', mode='passthrough')

# config.bind('<Ctrl+a>', 'fake-key <Home>', mode='passthrough')      # move-to-beginning-of-line
# config.bind('<Ctrl+e>', 'fake-key <End>', mode='passthrough')       # end-of-line
# config.bind('<Ctrl+f>', 'fake-key <Right>', mode='passthrough')     # forward-char
# config.bind('<Ctrl+b>', 'fake-key <Left>', mode='passthrough')      # backward-char
# config.bind('<Ctrl+n>', 'fake-key <Down>', mode='passthrough')      # forward-line
# config.bind('<Ctrl+p>', 'fake-key <Up>', mode='passthrough')        # previous-line
# config.bind('<Ctrl+d>', 'fake-key <Delete>', mode='passthrough')    # delete-char
# config.bind('<Ctrl+h>', 'fake-key <Backspace>', mode='passthrough') # backward-delete-char
# config.bind('<Alt+b>', 'fake-key <Ctrl+Left>', mode='passthrough')  # backward-word
# config.bind('<Alt+f>', 'fake-key <Ctrl+Right>', mode='passthrough') # forward-word
# config.bind('<Alt+a>', 'fake-key <Ctrl+Home>', mode='passthrough') # move-to-text-start
# config.bind('<Alt+e>', 'fake-key <Ctrl+End>', mode='passthrough')  # move-to-end-of-text
# config.bind('<Alt+i>', 'fake-key <Home>;;fake-key <Ctrl+Right>;;fake-key <Ctrl+Left>', mode='passthrough') # back-to-indentation

# config.bind('<Alt+c>', 'fake-key <Ctrl+c>', mode='passthrough')  # copy (st)
# config.bind('<Alt+v>', 'fake-key <Ctrl+v>', mode='passthrough')  # paste (st)
# config.bind('<Ctrl+y>', 'fake-key <Ctrl+v>', mode='passthrough') # yank
# config.bind('<Alt+w>', 'fake-key <Ctrl+c>;;yank selection', mode='passthrough')  # kill-ring-save
# config.bind('<Alt+y>', 'fake-key <Home>;;fake-key <Shift+End>;;fake-key <Ctrl+c>;;fake-key <End>', mode='passthrough') # copy-whole-line

# config.bind('<Ctrl+Alt+k>', 'fake-key <Shift+End>;;fake-key <Ctrl+x>', mode='passthrough') # kill-end-of-line
# config.bind('<Ctrl+Alt+w>', 'fake-key <Ctrl+Home>;;fake-key <Shift+End>;;fake-key <Ctrl+c>', mode='passthrough')
# config.bind('<Ctrl+Alt+m>', 'fake-key <Shift+End>;;fake-key <Ctrl+c>', mode='passthrough') # copy-forward-line
# config.bind('<Ctrl+Alt+p>', 'fake-key <Shift+Home>;;fake-key <Ctrl+c>', mode='passthrough') # copy-previous-line

## selection
# config.bind('<Ctrl+Shift+f>', 'fake-key <Shift+Right>', mode='passthrough')     # mark-forward-char
# config.bind('<Ctrl+Shift+b>', 'fake-key <Shift+Left>', mode='passthrough')      # mark-backward-char
# config.bind('<Ctrl+Shift+a>', 'fake-key <Shift+Home>', mode='passthrough')      # mark-beginning-of-line
# config.bind('<Ctrl+Shift+e>', 'fake-key <Shift+End>', mode='passthrough')       # mark-end-of-line

# config.bind('<Alt+Shift+f>', 'fake-key <Ctrl+Shift+Right>', mode='passthrough') # mark-forward-word
# config.bind('<Alt+Shift+b>', 'fake-key <Ctrl+Shift+Left>', mode='passthrough')  # mark-backward-word
# config.bind('<Alt+Shift+a>', 'fake-key <Ctrl+Shift+Home>', mode='passthrough')  # mark-to-beginning-of-text
# config.bind('<Alt+Shift+e>', 'fake-key <Ctrl+Shift+End>', mode='passthrough')   # mark-end-of-text
# config.bind('<Alt+Shift+h>', 'fake-key <Shift+Home>', mode='passthrough')       # mark-beginning-of-line
# config.bind('<Ctrl+l>', 'fake-key <Shift+End>', mode='passthrough')             # mark-end-of-line
# config.bind('<Ctrl+Shift+l>', 'fake-key <Shift+End>;;fake-key <Ctrl+x>', mode='passthrough') # kill-end-of-line

# config.bind('<Alt+Shift+@>', 'fake-key <Ctrl+Shift+Right>', mode='passthrough')               # mark-word
# config.bind('<Ctrl+\'>', 'fake-key <Ctrl+Shift+Right>', mode='passthrough')                   # mark-word
# config.bind('<Ctrl+;>', 'fake-key <Ctrl+Shift+Left>', mode='passthrough')                     # mark-backward-word
# config.bind('<Alt+Space>', 'fake-key <Home>;;fake-key <Ctrl+Shift+End>', mode='passthrough')  # mark-whole-line
# config.bind('<Ctrl+Space>', 'fake-key <Ctrl+Shift+Right>', mode='passthrough')                # mark-word
# config.bind('<Ctrl+Shift+Space>', 'fake-key <Ctrl+Shift+Left>', mode='passthrough')           # mark-previous-word

# config.bind('<Ctrl+Alt+Shift+a>', 'fake-key <Ctrl+a>', mode='passthrough') # select all
# config.bind('<Ctrl+Alt+a>', 'fake-key <Ctrl+a>', mode='passthrough')       # select-all

# config.bind('<Ctrl+Shift+n>', 'fake-key <Shift+Down>', mode='passthrough') # mark-forward-line
# config.bind('<Ctrl+Shift+p>', 'fake-key <Shift+Up>', mode='passthrough')   # mark-previous-line
# config.bind('<Ctrl+Shift+j>', 'fake-key <Shift+Down>', mode='passthrough') # mark-forward-line
# config.bind('<Ctrl+Shift+k>', 'fake-key <Shift+Up>', mode='passthrough')   # mark-previous-line

# config.bind('<Ctrl+k>', 'fake-key <Shift+End>;;fake-key <Ctrl+c>;;fake-key <Delete>', mode='passthrough') # kill-line
# config.bind('<Ctrl+w>', 'fake-key <Ctrl+c>;;fake-key <Ctrl+Backspace>', mode='passthrough')        # kill-backward-word
# config.bind('<Ctrl+u>', 'fake-key <Shift+Home>;;fake-key <Ctrl+x>', mode='passthrough')            # unix-rubout
# config.bind('<Alt+u>', 'fake-key <Ctrl+Shift+Home>;;fake-key <Ctrl+x>', mode='passthrough')        # kill-to-beginning-of-text
# config.bind('<Ctrl+Alt+k>', 'fake-key <Ctrl+Shift+End>;;fake-key <Ctrl+x>', mode='passthrough')    # kill-to-end-of-text
# config.bind('<Ctrl+Shift+h>', 'fake-key <Ctrl+Shift+Left>;;fake-key <Ctrl+c>', mode='passthrough') # copy-backward-word
# config.bind('<Alt+d>', 'fake-key <Ctrl+Right>;;fake-key <Ctrl+Shift+Left>;;fake-key <Ctrl+x>', mode='passthrough') # kill-word

# config.bind('<Ctrl+i>', 'fake-key <Tab>', mode='passthrough')
# config.bind('<Ctrl+Alt+i>', 'fake-key <Backtab>', mode='passthrough')
# config.bind('<Ctrl+Return>', 'fake-key <Ctrl+Return>', mode='passthrough')
# config.bind('<Ctrl+Return>', 'fake-key <Shift+Return>', mode='passthrough')
# config.bind('<Ctrl+m>', 'fake-key <Shift+Return>', mode='passthrough')

## Prompt Mode :kbd:prompt:
config.bind('<Escape>', 'mode-leave', mode='prompt')
config.bind('<Ctrl+y>', 'prompt-accept', mode='prompt')
config.bind('<Ctrl+w>', 'rl-filename-rubout', mode='command')

## testing :kbd:test:
config.bind('<Alt+Return>', 'fake-key <Ctrl+Return>', mode='passthrough')
config.bind('<Alt+Return>', 'fake-key <Ctrl+Return>', mode='insert')
config.bind('<Alt+Return>', 'fake-key <Ctrl+Return>', mode='command')
config.bind('<Alt+c>', 'yank selection', mode='insert')
config.bind('<Alt+c>', 'yank selection', mode='passthrough')
config.bind('<Alt+p>', 'insert-text {primary}', mode='insert')
config.bind('<Alt+p>', 'insert-text {primary}', mode='passthrough')
config.bind('<Alt+y>', 'insert-text {primary}', mode='insert')
config.bind('<Alt+y>', 'insert-text {primary}', mode='passthrough')

## Readline Command :kbd:rl:cmd:
# config.bind('<Ctrl+b>', 'rl-backward-char', mode='command')
# config.bind('<Ctrl+h>', 'rl-backward-delete-char', mode='command')
# config.bind('<Alt+b>', 'rl-backward-word', mode='command')
# config.bind('<Ctrl+a>', 'rl-beginning-of-line', mode='command')
# config.bind('<Ctrl+h>', 'rl-delete-char', mode='command')
# config.bind('<Ctrl+e>', 'rl-end-of-line', mode='command')
# config.bind('<Ctrl+f>', 'rl-forward-char', mode='command')
# config.bind('<Alt+Backspace>', 'rl-backward-kill-word', mode='command')
# config.bind('<Alt+f>', 'rl-forward-word', mode='command')
# config.bind('<Alt+p>', 'insert-text {primary}', mode='command')
# config.bind('<Ctrl+k>', 'rl-kill-line', mode='command')
# config.bind('<Alt+d>', 'rl-kill-word', mode='command')
# config.bind('<Ctrl+u>', 'rl-rubout', mode='command')
# config.bind('<Alt+u>', 'rl-unix-line-discard', mode='command')
# config.bind('<Ctrl+y>', 'rl-yank', mode='command')

## Readline Prompt :kbd:rl:prompt:
# config.bind('<Ctrl+b>', 'rl-backward-char', mode='prompt')
# config.bind('<Ctrl+h>', 'rl-backward-delete-char', mode='prompt')
# config.bind('<Alt+b>', 'rl-backward-word', mode='prompt')
# config.bind('<Ctrl+a>', 'rl-beginning-of-line', mode='prompt')
# config.bind('<Ctrl+h>', 'rl-delete-char', mode='prompt')
# config.bind('<Ctrl+e>', 'rl-end-of-line', mode='prompt')
# config.bind('<Ctrl+f>', 'rl-forward-char', mode='prompt')
# config.bind('<Alt+Backspace>', 'rl-backward-kill-word', mode='prompt')
# config.bind('<Alt+f>', 'rl-forward-word', mode='prompt')
# config.bind('<Alt+p>', 'insert-text {primary}', mode='prompt')
# config.bind('<Ctrl+k>', 'rl-kill-line', mode='prompt')
# config.bind('<Alt+d>', 'rl-kill-word', mode='prompt')
# config.bind('<Ctrl+u>', 'rl-rubout', mode='prompt')
# config.bind('<Alt+u>', 'rl-unix-line-discard', mode='prompt')
# config.bind('<Ctrl+y>', 'rl-yank', mode='prompt')

c.bindings.key_mappings = {'<Ctrl-[>': '<Escape>', '<Ctrl-6>': '<Ctrl-^>', '<Ctrl-M>': '<Return>', '<Ctrl-J>': '<Return>', '<Ctrl-I>': '<Tab>', '<Enter>': '<Return>', '<Ctrl-Enter>': '<Ctrl-Return>'}

c.input.forward_unbound_keys = "all"

def bind_chained(key, *commands):
    config.bind(key, ' ;; '.join(commands))
bind_chained('<Escape>', 'clear-keychain', 'search', 'mode-leave')

## Normal Mode :kbd:norm:
ESC_BIND = 'clear-keychain ;; search ;; fullscreen --leave ;; mode-leave'

# ==== Normal Mode ====
c.bindings.commands['normal'] = {
    # General
    ',,': 'jseval --quiet --file ~/.config/qutebrowser/userscripts/toggle_visibility.js',
    ',.': 'jseval --quiet --file ~/.config/qutebrowser/userscripts/iiie.js',
    '<?': 'set content.user_stylesheets \"\";;reload',
    '>?': 'set content.user_stylesheets \'["~/Templates/css/style.css", "~/Templates/css/cgpt.css"]\'',
    ',b': ':set statusbar.show in-mode',
    ',B': ':set statusbar.show never',
    ',d': 'set downloads.location.prompt true',
    ',D': 'set downloads.location.prompt false',
    ',m': 'spawn --detach mpv {url}',
    ',M': 'hint links spawn --detach mpv {hint-url}',
    ',R': ':spawn --detach st -e readit -c -l en',
    ',U': 'hint links spawn umpv {hint-url}',
    ',l': 'spawn ytcl {url};;cmd-later 100 spawn ytln {url}',
    ',rf': 'spawn --detach st -e readit -c -l fr',
    ',rs': 'hint --rapid links spawn rssadd {hint-url}',
    ',ta': 'cmd-set-text -s :spawn --userscript taskadd',
    ',th': ':spawn --userscript taskadd due:eod pri:H',
    ',tt': 'fake-key <Ctrl+c>;;yank selection;;spawn tts "$(xclip -selection clipboard -o)"',
    ',uM': 'hint --rapid links spawn umpv {hint-url}',
    ',um': 'spawn umpv {url}',
    ',yd': 'spawn ydl {url}',
    ',yt': 'spawn --detach mpv {url}',
    ',yu': 'hint links spawn --detach ydl {hint-url}',
    ';D': 'hint --rapid links spawn ydl {hint-url}',
    ';M': 'hint links spawn mpv {hint-url}',
    ';N': 'hint --rapid links spawn mpv {hint-url}',
    ';l': 'hint links spawn ytln {hint-url}',
    '<alt-J>': 'zoom-out',
    '<alt-K>': 'zoom-in',
    '<alt-Y>': 'yank {url:title}',

    '<alt+c>': 'fake-key <Ctrl+c>;;yank selection',
    '<alt+w>': 'fake-key <Ctrl+c>;;yank selection',
    '<ctrl-->': 'zoom-out',
    '<ctrl-=>': 'zoom-in',
    '<ctrl-0>': 'zoom 100%',
    '<ctrl-a>': 'mode-enter insert;;fake-key <Ctrl+a>;;fake-key <Ctrl+c>;;mode-leave',
    '<ctrl-i>': 'fake-key <Tab>',
    '<ctrl-alt-i>': 'fake-key <Backtab>',
    '<ctrl-c>': 'fake-key <Ctrl+c>;;yank selection',
    '<ctrl-alt-E>': 'config-edit',
    '<ctrl-e>': 'mode-enter insert;;fake-key <End>',
    '<Space>': 'scroll-page 0 0.6',
    '<Backspace>': 'scroll-page 0 -0.6',

    'N': 'forward',
    'P': 'back',
    'EE': 'fake-key <ctrl+c>;;yank selection;;spawn sleep 0.3;;spawn --detach st -e seledit',
    'TT': 'tab-only',
    'UU': 'edit-text {url}',
    'WE': 'spawn wikilocale {url} ;; cmd-later 500 open {clipboard}',
    'Y': 'fake-key <Ctrl+c>;;yank selection',
    'd': 'scroll-page 0 0.4;;fake-key <down>;;fake-key <down>',
    'u': 'scroll-page 0 -0.4;;fake-key <up>;;fake-key <up>',
    'tt': 'fake-key <Ctrl+c>;;yank selection;;spawn tts "$(xclip -selection clipboard -o)"',
    '<Ctrl+g>': 'fake-key <Escape>',
    'gG': ':tab-give 1',
    'gT': 'cmd-set-text :tab-take -k',
    '.': 'cmd-repeat-last',

    # Navigation
    '<ctrl-v>': 'scroll-page 0 0.45',
    '<alt-v>': 'scroll-page 0 -0.45',
    '<ctrl-shift-v>': 'scroll-page 0 0.95',
    '<alt-shift-v>': 'scroll-page 0 -0.95',

    '-': 'zoom-out',
    '=': 'zoom-in',
    '+': 'zoom 100%',

    'd': 'scroll-page 0 0.45',
    'u': 'scroll-page 0 -0.45',
    'U': 'undo',
    'F': 'forward',
    'l': 'back',
    'n': 'fake-key <down>',
    'p': 'fake-key <up>',

    # Tabs
    '<ctrl-tab>': 'tab-next',
    '<ctrl-shift-tab>': 'tab-prev',
    '<ctrl-x>k': 'tab-close',
    '<ctrl-x><ctrl-c>': 'write-quit',
    '<ctrl-q>': 'write-quit',

    # Search
    '<ctrl-s>': 'cmd-set-text /',
    '<ctrl-r>': 'cmd-set-text ?',

    # Hinting
    '<alt-s>': 'hint all',

    # History
    '<alt-x>': 'cmd-set-text :',
    '<ctrl-x>b': 'cmd-set-text -s :buffer',

    # Open Links
    '<ctrl-l>': 'cmd-set-text -s :open',
    '<alt-l>': 'cmd-set-text -s :open -t',

    '<ctrl-f>': 'fake-key <Right>',
    '<ctrl-b>': 'fake-key <Left>',
    '<ctrl-a>': 'fake-key <Home>',
    '<ctrl-e>': 'fake-key <End>',
    '<ctrl-n>': 'fake-key <Down>',
    '<ctrl-p>': 'fake-key <Up>',
    '<alt-b>': 'fake-key <Ctrl+Left>',
    '<ctrl-d>': 'fake-key <Delete>',
    '<alt-d>': 'fake-key <Ctrl+Delete>',
    '<alt-space>': 'forward',
    '<alt-backspace>': 'back',
    '<ctrl-w>': 'tab-close',
    '<ctrl-y>': 'insert-text {primary}',

    # Numbers
    '0': 'hint links userscript append_hint_url',
    '1': 'zoom 100%',
    '2': 'zoom 185%',
    '3': 'zoom 150%',
    '4': 'zoom 125%',
    '5': 'zoom 85%',
    '6': 'quickmark-load qai',
    '7': 'hint --rapid links spawn ydl {hint-url}',
    '8': 'spawn ydl {url}',
    '9': 'hint links spawn ydl {hint-url}',

    # Escape / Misc
    '<ctrl-H>': 'cmd-set-text -s :help',
    '<ctrl-g>': 'clear-keychain ;; search ;; fullscreen --leave',
    '<ctrl-alt-p>': 'mode-enter passthrough',

}

# ==== Caret Mode ====
c.bindings.commands['caret'] = {
    # Navigation
    'j': 'move-to-next-line;;scroll-page 0 0.03',
    'k': 'move-to-prev-line;;scroll-page 0 -0.03',
    '<Ctrl+n>': 'move-to-next-line',
    '<Ctrl+p>': 'move-to-prev-line',
    'd': 'fake-key <down>',
    'u': 'fake-key <up>',

    # Editing / Yank
    'EE': 'fake-key <ctrl+c>;;yank selection;;spawn sleep 0.3;;spawn --detach st -e seledit',
    'tt': 'fake-key <Ctrl+c>;;yank selection;;spawn tts "$(xclip -selection clipboard -o)" ',
    '<ctrl-a>': 'fake-key <Home>',
    '<ctrl-e>': 'fake-key <End>',
    '<ctrl-f>': 'fake-key <Right>',
    '<ctrl-b>': 'fake-key <Left>',
    '<ctrl-w>': 'fake-key <Ctrl+x>',
    '<ctrl-d>': 'fake-key <Delete>',
    '<alt-w>': 'yank selection;;fake-key <Ctrl+c>',
    '<alt-a>': 'fake-key <Ctrl+Home>',
    '<alt-f>': 'fake-key <Ctrl+Right>',
    '<alt-b>': 'fake-key <Ctrl+Left>',
    '<alt-e>': 'fake-key <Ctrl+End>',
    '<alt-d>': 'fake-key <Ctrl+Right>;;fake-key <Ctrl+Left>;;fake-key <Ctrl+x>',

    # Escape
    '<Ctrl+g>': 'mode-leave',
}

# ==== Command Mode ====
c.bindings.commands['command'] = {
    # Navigation
    '<ctrl-n>': ':completion-item-focus next',
    '<ctrl-p>': ':completion-item-focus prev',

    # History
    '<alt-p>': 'command-history-prev',
    '<alt-n>': 'command-history-next',

    # Readline / Editing
    '<ctrl-b>': 'rl-backward-char',
    '<ctrl-h>': 'rl-backward-delete-char',
    '<alt-b>': 'rl-backward-word',
    '<ctrl-a>': 'rl-beginning-of-line',
    '<ctrl-e>': 'rl-end-of-line',
    '<ctrl-f>': 'rl-forward-char',
    '<alt-Backspace>': 'rl-backward-kill-word',
    '<alt-f>': 'rl-forward-word',
    '<ctrl-k>': 'rl-kill-line',
    '<alt-d>': 'rl-kill-word',
    '<ctrl-u>': 'rl-rubout',
    '<alt-u>': 'rl-unix-line-discard',
    '<ctrl-y>': 'rl-yank',

    # Editing / Misc
    '<alt-p>': 'insert-text {primary}',
    '<alt-c>': 'fake-key <Ctrl+c>;;yank selection',
    '<alt-v>': 'fake-key <Ctrl+v> --global',
    '<ctrl-,>': 'command-accept --rapid',
    '<ctrl-.>': 'command-repeat',
    '<ctrl-h>': 'fake-key <Backspace>',
    '<ctrl-d>': 'fake-key <Delete>',
    '<alt-d>': 'fake-key <Ctrl+Delete>',
    '<alt-u>': 'fake-key <Ctrl+Shift+Home>;;fake-key <Ctrl+x>',
    '<alt-m>': 'fake-key <Home>',
    '<ctrl-f>': 'fake-key <Right>',
    '<ctrl-b>': 'fake-key <Left>',
    '<escape>': 'mode-leave',
    '<ctrl-g>': 'mode-leave',
    '<ctrl-w>': 'fake-key <Ctrl+Shift+left>;;yank selection;;fake-key <Ctrl+x> --global',
    '<ctrl-shift-f>': 'fake-key <Shift+Right>',
    '<ctrl-shift-b>': 'fake-key <Shift+Left>',
    '<ctrl-shift-a>': 'fake-key <Shift+Home>',
    '<ctrl-shift-e>': 'fake-key <Shift+End>',
    '<alt-shift-f>': 'fake-key <Ctrl+Shift+Right>',
    '<alt-shift-b>': 'fake-key <Ctrl+Shift+Left>',
    '<alt-shift-a>': 'fake-key <Ctrl+Shift+Home>',
    '<alt-shift-e>': 'fake-key <Ctrl+Shift+End>',
    '<alt-shift-h>': 'fake-key <Shift+Home>',
}

# ==== Insert Mode ====
c.bindings.commands['insert'] = {

    # Navigation
    '<ctrl-a>': 'fake-key <Home>',
    '<ctrl-e>': 'fake-key <End>',
    '<ctrl-f>': 'fake-key <Right>',
    '<ctrl-b>': 'fake-key <Left>',
    '<ctrl-n>': 'fake-key <Down>',
    '<ctrl-p>': 'fake-key <Up>',

    # Editing
    '<ctrl-d>': 'fake-key <Delete>',
    '<ctrl-h>': 'fake-key <Backspace>',
    '<ctrl-w>': 'fake-key <Ctrl+Shift+left>;;fake-key <Ctrl+x>',
    '<alt-b>': 'fake-key <Ctrl+Left>',
    '<alt-f>': 'fake-key <Ctrl+Right>',
    '<alt-a>': 'fake-key <Ctrl+Home>',
    '<alt-e>': 'fake-key <Ctrl+End>',
    '<alt-i>': 'fake-key <Home>;;fake-key <Ctrl+Right>;;fake-key <Ctrl+Left>',
    '<alt-d>': 'fake-key <Ctrl+Right>;;fake-key <Ctrl+Left>;;fake-key <Ctrl+x>',
    '<alt-c>': 'fake-key <Ctrl+c>',
    '<alt-v>': 'fake-key <Ctrl+v>',
    '<ctrl-y>': 'fake-key <Ctrl+v>',
    '<alt-w>': 'fake-key <Ctrl+c>',
    '<alt-y>': 'fake-key <Home>;;fake-key <Shift+End>;;fake-key <Ctrl+c>;;fake-key <End>',
    '<alt-p>': 'insert-text {primary}',

    # Kill / Yank / Misc
    '<ctrl-alt-k>': 'fake-key <Shift+End>;;fake-key <Ctrl+x>',
    '<ctrl-alt-w>': 'fake-key <Ctrl+Home>;;fake-key <Shift+End>;;fake-key <Ctrl+c>',
    '<ctrl-alt-m>': 'fake-key <Shift+End>;;fake-key <Ctrl+c>',
    '<ctrl-alt-p>': 'fake-key <Shift+Home>;;fake-key <Ctrl+c>',
    '<ctrl-shift-h>': 'fake-key <Ctrl+Shift+Left>;;fake-key <Ctrl+c>',
    '<alt-u>': 'fake-key <Ctrl+Shift+Home>;;fake-key <Ctrl+x>',
    '<alt-d>': 'fake-key <Ctrl+Right>;;fake-key <Ctrl+Shift+Left>;;fake-key <Delete>',
    '<ctrl-k>': 'fake-key <Shift+End>;;fake-key <Ctrl+x>',
    '<ctrl-w>': 'fake-key <Ctrl+Shift+Left>;;fake-key <Ctrl+x>',
    '<ctrl-u>': 'fake-key <Shift+Home>;;fake-key <Ctrl+x>',
    '<ctrl-o>': 'fake-key <Shift+Return>;;fake-key <Up>;;fake-key <End>',
    '<alt-o>': 'fake-key <Home>;;fake-key <Shift+Return>;;fake-key <Up>;;fake-key <Home>',
    '<alt-shift-o>': 'fake-key <Home>;;fake-key <Backspace>',

    # Mark / Selection
    '<ctrl-shift-f>': 'fake-key <Shift+Right>',
    '<ctrl-shift-b>': 'fake-key <Shift+Left>',
    '<ctrl-shift-a>': 'fake-key <Shift+Home>',
    '<ctrl-shift-e>': 'fake-key <Shift+End>',
    '<alt-shift-f>': 'fake-key <Ctrl+Shift+Right>',
    '<alt-shift-b>': 'fake-key <Ctrl+Shift+Left>',
    '<alt-shift-a>': 'fake-key <Ctrl+Shift+Home>',
    '<alt-shift-e>': 'fake-key <Ctrl+Shift+End>',
    '<alt-shift-h>': 'fake-key <Shift+Home>',
    '<ctrl-shift-l>': 'fake-key <Shift+End>;;fake-key <Ctrl+x>',
    '<alt-shift-@>': 'fake-key <Ctrl+Shift+Right>',
    '<ctrl-space>': 'fake-key <Ctrl+Shift+Right>',
    '<ctrl-alt-space>': 'fake-key <Ctrl+Shift+Left>',
    '<ctrl-alt-shift-a>': 'fake-key <Ctrl+a>',
    '<ctrl-\'>': 'fake-key <Ctrl+Shift+Right>',
    '<ctrl-;>': 'fake-key <Ctrl+Shift+Left>',
    '<alt-space>': 'fake-key <Home>;;fake-key <Ctrl+Shift+End>',
    '<ctrl-alt-a>': 'fake-key <Ctrl+Shift+Home>',
    '<ctrl-alt-e>': 'fake-key <Ctrl+Shift+End>',
    '<ctrl-shift-n>': 'fake-key <Shift+Down>',
    '<ctrl-shift-p>': 'fake-key <Shift+Up>',
    '<ctrl-shift-j>': 'fake-key <Shift+Down>',
    '<ctrl-shift-k>': 'fake-key <Shift+Up>',
    '<escape>': 'mode-leave',
    '<ctrl-g>': ESC_BIND,
    '<ctrl-->': 'zoom-out',
    '<ctrl-0>': 'zoom 100%',
    '<ctrl-=>': 'zoom-in',
    '<ctrl-+>': 'zoom 100%',
}

# ==== Passthrough Mode ====
c.bindings.commands['passthrough'] = c.bindings.commands['insert'].copy()

# ==== Prompt Mode ====
c.bindings.commands['prompt'] = {
    '<Escape>': 'mode-leave',
    '<ctrl-y>': 'prompt-accept',
    '<ctrl-w>': 'rl-filename-rubout',
    '<ctrl-b>': 'rl-backward-char',
    '<ctrl-h>': 'rl-backward-delete-char',
    '<alt-b>': 'rl-backward-word',
    '<ctrl-a>': 'rl-beginning-of-line',
    '<ctrl-e>': 'rl-end-of-line',
    '<ctrl-f>': 'rl-forward-char',
    '<alt-Backspace>': 'rl-backward-kill-word',
    '<alt-f>': 'rl-forward-word',
    '<alt-p>': 'insert-text {primary}',
    '<ctrl-k>': 'rl-kill-line',
    '<alt-d>': 'rl-kill-word',
    '<ctrl-u>': 'rl-rubout',
    '<alt-u>': 'rl-unix-line-discard',
    '<ctrl-y>': 'rl-yank',
}

# ==== Hint Mode ====
c.bindings.commands['hint'] = {
    '<escape>': 'mode-leave',
    '<ctrl-g>': ESC_BIND,
}
