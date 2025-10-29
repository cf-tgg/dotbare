#!/usr/bin/env zsh
# -*- mode: sh; -*- vim: ft=sh:ts=2:sw=2:et:
# Time-stamp: <2025-10-26 00:21:31 cf>
# Box: cf [Linux 6.15.8-zen1-1-zen x86_64 GNU/Linux]
#        __       _          _ _
#   ___ / _|  ___| |__   ___| | |
#  / __| |_  / __| '_ \ / _ \ | |
# | (__|  _| \__ \ | | |  __/ | |
#  \___|_|   |___/_| |_|\___|_|_|
#
#                      cf. [zshrc] ❯⟩

autoload -U colors

setopt prompt_subst

#PS1="%B%{$fg[red]%}[%{$fg[yellow]%}%n%{$fg[green]%}@%{$fg[blue]%}%M%{$fg[red]%}] %{$fg[magenta]%}%~%{$fg[$(if [ $? -eq 0 ]; then echo white; else echo red; fi)]%}  %{$reset_color%}%b"

# Display exit code of last commandline
precmd() {
  if (( $? != 0 )); then
    PROMPT_SYMBOL_COLOR="%{$fg[red]%}"
  else
    PROMPT_SYMBOL_COLOR="%{$reset_color%}"
  fi
}

# Prompt ❯❯
# PS1='%B%{$fg[white]%}[%n@%{$fg[red]%}%M %{$fg[white]%}%~]${PROMPT_SYMBOL_COLOR}$%{$reset_color%}%b '

if tty | grep -q tty >/dev/null 2>&1 ; then
  PS1='%B%{$fg[magenta]%}%~%{$reset_color%} ${PROMPT_SYMBOL_COLOR}>%{$reset_color%}%b '
else
  PS1='%B%{$fg[magenta]%}%~%{$reset_color%} ${PROMPT_SYMBOL_COLOR}⟩%{$reset_color%}%b '
fi

setopt autocd
stty stop undef

# OPTIONS
setopt ALWAYS_TO_END          # When completing a word, move the cursor to the end of the word
setopt APPEND_HISTORY         # this is default, but set for share_history
setopt AUTO_CD                # cd by typing directory name if it's not a command
setopt AUTO_LIST              # automatically list choices on ambiguous completion
setopt AUTO_MENU              # automatically use menu completion
# setopt AUTO_PUSHD             # Make cd push each old directory onto the stack
setopt COMPLETEINWORD         # If unset, the cursor is set to the end of the word
# setopt CORRECT_ALL            # autocorrect commands
setopt EXTENDED_GLOB          # treat #, ~, and ^ as part of patterns for filename generation
setopt EXTENDED_HISTORY       # save each command's beginning timestamp and duration to the history file
setopt GLOB_DOTS              # dot files included in regular globs
setopt HASH_LIST_ALL          # when command completion is attempted, ensure the entire  path is hashed
setopt HIST_EXPIRE_DUPS_FIRST # # delete duplicates first when HISTFILE size exceeds HISTSIZE
setopt HIST_FIND_NO_DUPS      # When searching history don't show results already cycled through twice
setopt HIST_IGNORE_DUPS       # Do not write events to history that are duplicates of previous events
setopt HIST_IGNORE_SPACE      # remove command line from history list when first character is a space
setopt HIST_REDUCE_BLANKS     # remove superfluous blanks from history items
setopt HIST_VERIFY            # show command with history expansion to user before running it
setopt HISTIGNORESPACE        # remove commands from the history when the first character is a space
setopt INC_APPEND_HISTORY     # save history entries as soon as they are entered
setopt INTERACTIVECOMMENTS    # allow use of comments in interactive code (bash-style comments)
setopt LONGLISTJOBS           # display PID when suspending processes as well
setopt NO_BEEP                # silence all bells and beeps
setopt NOCASEGLOB             # global substitution is case insensitive
setopt NONOMATCH              ## try to avoid the 'zsh: no matches found...'
setopt NOSHWORDSPLIT          # use zsh style word splitting
setopt NOTIFY                 # report the status of backgrounds jobs immediately
setopt NUMERIC_GLOB_SORT      # globs sorted numerically
setopt PROMPT_SUBST           # allow expansion in prompts
# setopt PUSHD_IGNORE_DUPS      # Don't push duplicates onto the stack
setopt SHARE_HISTORY          # share history between different instances of the shell

HISTSIZE=100000
SAVEHIST=100000
HISTFILE="${XDG_CACHE_HOME:-$HOME/.cache}/zsh/history"
HISTORY_IGNORE='(clear|pwd|exit|* —help|[bf]g *|less *|cd ..|cd -)'

# setopt BANG_HIST                 # Perform textual history expansion, csh-style, treating the character ‘!’ specially.
# setopt EXTENDED_HISTORY          # Write the history file in the ':start:elapsed;command' format.
# setopt INC_APPEND_HISTORY        # Write to the history file immediately, not when the shell exits.
# setopt SHARE_HISTORY             # Share history between all sessions.
# setopt HIST_EXPIRE_DUPS_FIRST    # Expire a duplicate event first when trimming history.
# setopt HIST_IGNORE_DUPS          # Do not record an event that was just recorded again.
# setopt HIST_IGNORE_ALL_DUPS      # Delete an old recorded event if a new event is a duplicate.
# setopt HIST_FIND_NO_DUPS         # Do not display a previously found event.
# setopt HIST_IGNORE_SPACE         # Do not record an event starting with a space.
# setopt HIST_SAVE_NO_DUPS         # Do not write a duplicate event to the history file.
# setopt HIST_VERIFY               # Do not execute immediately upon history expansion.
# setopt HIST_REDUCE_BLANKS        # Remove superfluous blanks from each command line being added to the history list.
# setopt APPEND_HISTORY            # append to history file
# setopt HIST_NO_STORE             # Don't store history commands
# # setopt HIST_NO_FUNCTIONS         # Don't store function definitions

# path check
export PATH="$(echo "$PATH" | awk -v RS=: -v ORS=: '!a[$1]++' | sed 's/:$//')"

# load extra configs
for f in "${XDG_CONFIG_HOME:-$HOME/.config}/shell"/{aliases,aliasrc,functions,shortcutrc,shortcutenvrc,zshnameddirrc,ytaliases} ; do
   if [ -f "$f" ]; then
       source "$f" >/dev/null 2>&1
   fi
   unset f
done
ralias() { gpg2 -d "$(pass rals)" | source /dev/stdin >/dev/null 2>&1 ; }

# Ensure emacs is running the server
# [ -e "$EMACS_SOCKET_NAME" ] || EMACS_SOCKET_NAME=${EMACS_SERVER_FILE:-"$XDG_RUNTIME_DIR/emacs/server"}
# [ -z "$(pidof -xs emacs)" ] && emacs -f server-start >/dev/null 2>&1

# Completion
[ -z "$ZDOTDIR" ] && ZDOTDIR="${XDG_CONFIG_HOME:-$HOME/.config}/zsh"

# Base comp dir init
fpath=(
    $ZDOTDIR
    /usr/local/share/zsh/site-functions
    /usr/share/zsh/site-functions
    /usr/share/zsh/functions/Calendar
    /usr/share/zsh/functions/Chpwd
    /usr/share/zsh/functions/Completion
    /usr/share/zsh/functions/Completion/Base
    /usr/share/zsh/functions/Completion/Linux
    /usr/share/zsh/functions/Completion/Unix
    /usr/share/zsh/functions/Completion/X
    /usr/share/zsh/functions/Completion/Zsh
    /usr/share/zsh/functions/Exceptions
    /usr/share/zsh/functions/MIME
    /usr/share/zsh/functions/Math
    /usr/share/zsh/functions/Misc
    /usr/share/zsh/functions/Newuser
    /usr/share/zsh/functions/Prompts
    /usr/share/zsh/functions/TCP
    /usr/share/zsh/functions/VCS_Info
    /usr/share/zsh/functions/VCS_Info/Backends
    /usr/share/zsh/functions/Zftp
    /usr/share/zsh/functions/Zle
    /usr/share/zsh/plugins/fast-syntax-highlighting
)

# Load zsh completion
autoload -U compinit
zstyle ':completion:*' menu select
zmodload zsh/complist
compinit
_comp_options+=(globdots)

# function for dsurfraw -e|--elvi option
compdef _mpv vlb
compdef _man ve
compdef _dsurfraw dsurfraw
compdef _exifjpg exifjpg
compdef _tts tts
compdef _tailscale tailscale

# vi bindings
bindkey -v
export KEYTIMEOUT=1
source <(fzf --zsh)

### Modules

autoload -Uz surround
zle -N delete-surround surround
zle -N add-surround surround
zle -N change-surround surround
bindkey -a cs change-surround
bindkey -a ds delete-surround
bindkey -a ys add-surround
bindkey -a Y vi-yank-eol
bindkey -M visual S add-surround

autoload -Uz run-help
alias help='run-help'
# Wikiman plugin
[ -f "/usr/share/wikiman/widgets/widget.zsh" ] && {
    source /usr/share/wikiman/widgets/widget.zsh
    bindkey '^X^_' _wikiman_widget
}

autoload -Uz add-zsh-hook
DIRSTACKFILE="${XDG_CACHE_HOME:-$HOME/.cache}/zsh/dirs"
if [[ -f "$DIRSTACKFILE" ]] && (( ${#dirstack} == 0 )); then
	dirstack=("${(@f)"$(< "$DIRSTACKFILE")"}")
	[[ -d "${dirstack[1]}" ]] && cd -- "${dirstack[1]}"
fi
chpwd_dirstack() {
	print -l -- "$PWD" "${(u)dirstack[@]}" > "$DIRSTACKFILE"
}
add-zsh-hook -Uz chpwd chpwd_dirstack

DIRSTACKSIZE='20'

setopt AUTO_PUSHD PUSHD_SILENT PUSHD_TO_HOME

## Remove duplicate entries
setopt PUSHD_IGNORE_DUPS

## This reverts the +/- operators.
setopt PUSHD_MINUS

# Use vim keys in tab completion menu
bindkey -M menuselect 'h' vi-backward-char
bindkey -M menuselect 'k' vi-up-line-or-history
bindkey -M menuselect 'l' vi-forward-char
bindkey -M menuselect 'j' vi-down-line-or-history
bindkey -M menuselect 'b' vi-backward-char
bindkey -M menuselect 'p' vi-up-line-or-history
bindkey -M menuselect 'f' vi-forward-char
bindkey -M menuselect 'n' vi-down-line-or-history

bindkey -v '^?' backward-delete-char
bindkey -v '^H' backward-delete-char

# Edit line in vim with ctrl-e
autoload edit-command-line; zle -N edit-command-line
bindkey '^X^E' edit-command-line

bindkey -M vicmd '^[[P' vi-delete-char
bindkey -M vicmd '^X^E' edit-command-line
bindkey -M visual '^[[P' vi-delete

# Change cursor shape for different vi modes
function zle-keymap-select () {
    case $KEYMAP in
        vicmd) echo -ne '\e[1 q';;      # block
        viins|main) echo -ne '\e[5 q';; # beam
    esac
}
echo -ne '\e[5 q' #Beam preload
preexec() { echo -ne '\e[5 q' ; }

zle -N zle-keymap-select
zle-line-init() {
    zle -K viins
    echo -ne "\e[5 q"
}
zle -N zle-line-init

# Use lf to switch directories
lfcd () {
    tmp=$(mktemp -uq)
    trap 'rm -f $tmp >/dev/null 2>&1 && trap - HUP INT QUIT TERM PWR EXIT' HUP INT QUIT TERM PWR EXIT
    lf -last-dir-path="$tmp" "$@"
    if [ -f "$tmp" ]; then
        dir="$(cat "$tmp")"
        [ -d "$dir" ] && [ "$dir" != "$(pwd)" ] && cd "$dir"
    fi
}

# bind lfcd to ctrl-x ctrl-o outside emacs
[[ -z "$INSIDE_EMACS" ]] && bindkey -s '^X^O' '^ulfcd\n'
bindkey -s '^O' '^ulfcd\n'
bindkey -s '^X^H' '^ubc -lq\n'
bindkey -s '^X^W' '^ucd "$(dirname "$(fzf)")"\n'
bindkey '^[[P' delete-char
bindkey '^R' history-incremental-search-backward

# Alt-m spawns fzf-nova scripts
__fzf_nova__() {
    "$HOME/.local/src/fzf-nova/fzf-nova"
}
zle -N  __fzf_nova__
bindkey -M emacs '^[m' __fzf_nova__
bindkey -M vicmd '^[m' __fzf_nova__
bindkey -M viins '^[m' __fzf_nova__

# Attach to tmux nvim session
tmux-attach-nvim() {
   zle -I ; LBUFFER="switch-back-to-nvim" ; zle-accept-line 2>/dev/null || return 1
}
zle -N tmux-attach-nvim
bindkey -M viins '^X^N' tmux-attach-nvim
bindkey -M vicmd '^X^N' tmux-attach-nvim
bindkey -M emacs '^X^N' tmux-attach-nvim

toupper() {
     echo "$@" | tr abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
}

tolower() {
    echo "$@" | tr ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz
}

c_escape() {
    echo "$*" | sed 's/["\\]/\\\0/g'
}

sh_quote() {
    v=$(echo "$1" | sed "s/'/'\\\\''/g")
    test "x$v" = "x${v#*[!A-Za-z0-9_/.+-]}" || v="'$v'"
    echo "$v"
}

cleanws() {
    echo "$@" | sed 's/^ *//;s/[[:space:]][[:space:]]*/ /g;s/ *$//'
}

cleanws_lbuffer() {
  emulate -L zsh
  local buf=$(cleanws "${LBUFFER}")
  LBUFFER="$buf" || return 1
  return 0
}

copy_lbuffer() {
  emulate -L zsh
  local buf="${LBUFFER}"
  [ -n "$buf" ] || return
  export LBUF="$buf"
  if [ -n "$DISPLAY" ]; then
      if echo "$buf" | xclip -in -selection clipboard 2>/dev/null ; then
          [ -x "$(command -v notify-send)" ] && {
            notify-send -t 1000 "[copy_buffer]" "$buf"
          } || {
            redunst
            notify-send -t 1000 "[copy_buffer]" "$buf" || return 1
          }
      fi
  fi
  return 0
}
zle -N copy_lbuffer
bindkey -M viins '^[w' copy_lbuffer
bindkey -M vicmd '^[w' copy_lbuffer
bindkey -M emacs '^[w' copy_lbuffer

c_escape_lbuffer() {
  emulate -L zsh
  local buf=$(c_escape "${LBUFFER}")
  echo "$buf" | xclip -in -sel clip 2>/dev/null
  LBUFFER="$buf" || return 1
  return 0
}
zle -N c_escape_lbuffer
bindkey -M viins '^[\' c_escape_lbuffer
bindkey -M vicmd '^[\' c_escape_lbuffer
bindkey -M emacs '^[\' c_escape_lbuffer

get_last_arg() {
  emulate -L zsh
  local buf="${LBUFFER%"${LBUFFER##*[![:space:]]}"}"
  local -a words
  words=(${(z)buf})
  print -r -- "${words[-1]}"
}

strip_last_arg() {
  emulate -L zsh
  local buf="${LBUFFER%"${LBUFFER##*[![:space:]]}"}"
  local -a words
  words=(${(z)buf})
  local last="${words[-1]}"
  LBUFFER="${LBUFFER%"$last"}"
}

replace_lastarg_with() {
  emulate -L zsh
  strip_last_arg
  LBUFFER+="$1"
}

insert_lastarg_parens() {
  local arg="$(get_last_arg)"
  replace_lastarg_with "(${arg})"
}
zle -N insert_lastarg_parens
bindkey '^X\(' insert_lastarg_parens

insert_lastarg_singlequote() {
  local arg="$(get_last_arg)"
  replace_lastarg_with "'$arg'"
}
zle -N insert_lastarg_singlequote
bindkey "^X\'" insert_lastarg_singlequote

insert_lastarg_shell_escaped() {
  local arg="$(get_last_arg)"
  replace_lastarg_with "$(printf '%q' "$arg")"
}
zle -N insert_lastarg_shell_escaped
bindkey '^X^\\' insert_lastarg_shell_escaped

insert_lastarg_doublequote() {
  local arg="$(get_last_arg)"
  replace_lastarg_with "\"$arg\""
}
zle -N insert_lastarg_doublequote
bindkey '^X\"' insert_lastarg_doublequote

insert_lastarg_braced_var() {
  local arg="$(get_last_arg)"
  replace_lastarg_with '{"'"$arg"'"}'
}
zle -N insert_lastarg_braced_var
bindkey '^X\{' insert_lastarg_braced_var

quoted-lbuffer() {
    LBUFFER=$(printf "'%s'" "${LBUFFER}") || LBUFFER="${LBUFFER}"
    return
}
zle -N quoted-lbuffer
bindkey '^[q' quoted-lbuffer

unescape-lbuffer() {
    LBUFFER=$(printf '%s' "${LBUFFER}" | sed 's/\\//g;s/\\\\/\\/g;') || LBUFFER="${LBUFFER}"
    return
}
zle -N unescape-lbuffer
bindkey -M viins '^X^[\' unescape-lbuffer
bindkey -M vicmd '^X^[\' unescape-lbuffer
bindkey -M emacs '^X^[\' unescape-lbuffer

is_alias_type() {
    al="$1"
    aln=$(grep -rn "${al}='" ~/.config/(shell|zsh) | grep -vE '[~#]' | awk -F ':' '{print $1, $2}')
    f=$(echo "$fnl" | awk '{print $1}')
    l=$(echo "$fnl" | awk '{print $2}')
    devour emacsclient -c -s "$EMACS_SOCKET_NAME" --alternate-editor="" +${l} --file="$f" || true
}

is_fn_type() {
    fn="$1"
    fnl=$(grep -rn "${fn}() " ~/.config/(shell|zsh) | grep -vE '[~#]' | awk -F ':' '{print $1, $2}' )
    f=$(echo "$fnl" | awk '{print $1}')
    l=$(echo "$fnl" | awk '{print $2}')
    devour emacsclient -c -s "$EMACS_SOCKET_NAME" --alternate-editor="" +${l} --file="$f" || true
}

is_file_type() {
               []
 devour emacsclient -c -s "$EMACS_SOCKET_NAME" --alternate-editor="" "$(is_file_type "$t")" || true
}

emtype() {
    t=$(get_last_arg)
    wt=$(type -w "$t" | awk '{print $2}')
    case "$wt" in
        'alias') is_alias_type "$t" || return 1 ;;
        'function') is_fn_type "$t" || return 1 ;;
        *) ( [ ! -f "$t" ] 2>/dev/null && f="$t" ) || return 1 ;;
    esac
    [ -t 1 ] && devour emacsclient -s "$EMACS_SOCKET_NAME" --alternate-editor="" -cn "$t"  || true
    return 0
}
zle -N emtype
bindkey -M emacs '^[e' emtype
bindkey -M vicmd '^[e' emtype
bindkey -M viins '^[e' emtype

shell-escape-primary() {
    p=$(xclip -sel prim -o 2>/dev/null)
    [ -n "$p" ] || return 0
    LBUFFER=$(echo "${LBUFFER}" | sed "s/${p}//;s/ $//")
    escaped_psel=$(shell_escape -p 2>/dev/null)
    LBUFFER+=" ${escaped_psel}" || return 1
    return 0
}
zle -N shell-escape-primary
bindkey -M vicmd '^X^p' shell-escape-primary
bindkey -M viins '^X^p' shell-escape-primary
bindkey -M emacs '^X^p' shell-escape-primary

shell-escape-last-word() {
    t=${LBUFFER##* } || return 1
    j=$(shell_escape -ei "${t}")
    ( [ -n "$t" ] && [ -n "$j" ] ) || return 1
    LBUFFER=$(echo "${LBUFFER}" | sed "s/${t}//;s/ $//;" 2>/dev/null)
    LBUFFER+=" ${j}" || return 1
    return 0
}
zle -N shell-escape-last-word
bindkey -M vicmd '^[\' shell-escape-last-word
bindkey -M viins '^[\' shell-escape-last-word
bindkey -M emacs '^[\' shell-escape-last-word

# Ctrl-x + Enter swallows launched app
acceptandswallow() {
   xdotool key --clearmodifiers super+shift+space
   dwmswallow "$WINDOWID"
   zle accept-line
}
zle -N accept-line-swallow acceptandswallow
bindkey -M viins '^X^m' accept-line-swallow
bindkey -M vicmd '^X^m' accept-line-swallow
bindkey -M emacs '^X^m' accept-line-swallow

# fzf_history() { # Ctrl-h fuzzy history
#     zle -I; eval $(history -n | fzf +s | sed 's/ *[0-9]* *//')
# }
# zle -N fzf_history
# bindkey '^G' fzf_history

# Ctrl-k fuzzy kill processes
fzf_killps() {
    ( zle -I; ps -ef | sed 1d | fzf -m | awk '{print $2}' | xargs kill -${1:-9} 2>/dev/null ) || return 1
    return 0
}
zle -N fzf_killps
bindkey '^X^K' fzf_killps

# dwim Xselection paste
paste() {
    LBUFFER+=$(xclip -selection primary -o 2>/dev/null || xclip -selection clipboard -o 2>/dev/null || printf '%s' "$LAST_CMD" 2>/dev/null || return 1 ; )
    return
}
zle -N paste
bindkey '^[p' paste

open-line() {
    LBUFFER=$(printf '\n%s' "${LBUFFER}" || return 1 )
    return
}
zle -N open-line
bindkey '^[o' open-line

split-line() {
    LBUFFER=$(printf '%s\n' "${LBUFFER}" || return 1 )
    return
}
zle -N open-line
bindkey '^[+' split-line

# bindkey '^G' mpv_id
# fzf_cd() { # Ctrl-p fuzzy path navigator
#     zle -I; DIR=$(find ${1:-*} -path '*/\.*' -prune -o -type d -print 2>/dev/null | fzf) && cd "$DIR" ;
# }
# zle -N fzf_cd

__fzfmenu__() {
  local cmd="fd -tf --max-depth=1"
  eval $cmd | ~/.local/bin/fzfmenu
}
__fzf-menu__() {
  LBUFFER="${LBUFFER}$(__fzfmenu__)"
  local ret=$?
  zle reset-prompt
  return $ret
}
zle -N __fzf-menu__
bindkey -M emacs '^T^G' __fzf-menu__
bindkey -M vicmd '^T^G' __fzf-menu__
bindkey -M viins '^T^G' __fzf-menu__

# pick_torrent() LBUFFER="transmission-remote -t ${$({
#     for torrent in ${(f)"$(transmission-remote -l)"}; do
#         torrent_name=$torrent[73,-1]
#         [[ $torrent_name != (Name|) ]] && echo ${${${(s. .)torrent}[1]}%\*} $torrent_name
#     done
# } | fzf)%% *} -"
# zle -N pick_torrent
# bindkey '^t' pick_torrent

zle -N fzfbm
# ctrl-x ctrl-b
bindkey '^X^B' fzfbm

#  zle -N tmxzf
# ctrl-x ctrl-y
#  bindkey '^X^Y' tmxzf

cfg-edit() {
    emulate -L zsh ;
    find ~/.config/{mpv,lf,nsxiv,nvim,shell,x11,zathura,picom,ncmpcpp,newsboat,mpd,ytfzf,zsh,yazi} ~/.local/src/{dwm,st,dmenu,dwmblocks} ~/Templates/{nix,dwm,dwmblocks,xmouseless,st,dotfiles} ~/.local/bin -type f | \
        grep -vE '[#~]' | fzf --multi --print0 |\
        while IFS= read -r -d '' f; do
            if [ -f "$f" ] || [ -d "$f" ]; then
                emc "$f" || { echo "failed to open $f" >&2 ; return 1 ; }
                echo "$f" | grep -Eq '(alias|zsh|functions)' && {
                    zle -I ;
                    cat "$f" | source /dev/stdin 2>/dev/null
                }
            fi
        done  >/dev/null 2>&1
    return 0
}
zle -N cfg-edit
bindkey '^X^F' cfg-edit

fzf-rsync () { ( "$HOME/.local/bin/fzhsync" "$@" && return 0 ) || return 1 ; }
zle -N fzf-rsync
bindkey '^X^H' fzf-rsync

scrnshot-sync() {
    t=${1:-"dg3s"}
    ssh -f "$t" sh -c "{ exit \$? ; }" || {
        t=$(grep -i HostName "$HOME/.ssh/config" | awk '{print $2}' | fzf)
    }
    [ -n "$t" ] && maimsync -t "$t" -f || maimsync -f || return 1
    return 0
}
zle -N scrnshot-sync
bindkey -M viins '^X^R' scrnshot-sync
bindkey -M vicmd '^X^R' scrnshot-sync
bindkey -M emacs '^X^R' scrnshot-sync

editzshrc() {
    emulate -L zsh
    ( emacsclient -c -s "$EMACS_SOCKET_NAME" ~/.zshrc && cat ~/.zshrc | source /dev/stdin 2>/dev/null ) || return 1
    return 0
}
zle -N editzshrc
bindkey '^X^Z' editzshrc

tmux-attach-to() {
    zle -I ; LBUFFER="tmux-attach" ; zle accept-line 2>/dev/null || return 1
}
zle -N tmux-attach-to
[[ -z "$TMUX" ]] && bindkey '^X^A' tmux-attach-to

primary_echo() { ( xa_listen -x && return 0 ) || return 1 ; }
zle -N primary_echo
# ctrl-x ctrl-v
bindkey '^X^v' primary_echo

xswal-select() {  ( xswal -x && return 0 ) || return 1 ; }
zle -N xswal-select
# ctrl-x ctrl-g when terminal is not in Emacs
[[ -z "$INSIDE_EMACS" ]] && bindkey '^X^G' xswal-select

sshop() {
    grep -iE '^(host)\s? ' ~/.ssh/config | sed 's/^Host //;s/[[:space:]]//g' | fzf | xargs -r ssh
}
zle -N sshop
bindkey -M viins '^X^S' sshop
bindkey -M vicmd '^X^S' sshop
bindkey -M emacs '^X^S' sshop

# plugin sourcing
[ /usr/share/nvm/init-nvm.sh ] && source /usr/share/nvm/init-nvm.sh
[ -f "$HOME/.local/share/cargo/env" ] && . "$HOME/.local/share/cargo/env"

# eval "$(luarocks  path --bin)"

# yazi
if [ -x $(command -v yazi) ]; then
    # eval "$(zoxide init zsh)"
    export YAZI_CONFIG_HOME="$HOME/.config/yazi"
    export YAZI_FILE_ONE="$(which file)"
    export YAZI_ZOXIDE_OPTS="--recent"

    y() {
        local tmp="$(mktemp -t "yazi-cwd.XXXXXX")" cwd
        yazi "$@" --cwd-file="$tmp"
        if cwd="$(command cat -- "$tmp")" && [ -n "$cwd" ] && [ "$cwd" != "$PWD" ]; then
            builtin cd -- "$cwd" ;
        fi
        rm -f -- "$tmp" >/dev/null 2>&1
    }
    zle -N y
    bindkey -M vicmd '^X^Y' y
    bindkey -M viins '^X^Y' y
    bindkey -M emacs '^X^Y' y
fi

__fzf-cmd-menu__() {
   cat ~/Templates/sh/dwmcmds | fzf --delimiter="\t" --with-nth=1 --multi  | awk -F "\t" '{print $2}' |\
       while read -r cmd; do
           eval "$cmd" || continue
       done
}
zle -N __fzf-cmd-menu__
bindkey '^[d' __fzf-cmd-menu__
bindkey -M emacs '^[d' __fzf-cmd-menu__
bindkey -M viins '^[d' __fzf-cmd-menu__
bindkey -M vicmd '^[d' __fzf-cmd-menu__

# Emacs line-editing (not using `bindkey -e' makes for a hybrid vi-emacs keymap)
# bindkey -e

# basic cursor movement
bindkey '^A' beginning-of-line      # Ctrl-a
bindkey '^[a' beginning-of-line     # Meta-t
bindkey '^E' end-of-line            # Ctrl-e
bindkey '^B' backward-char          # Ctrl-b
bindkey '^F' forward-char           # Ctrl-f
bindkey '^[b' backward-word         # Meta-b
bindkey '^[f' forward-word          # Meta-f

# Deletion and killing text
bindkey '^D' delete-char            # Ctrl-d
bindkey '^H' backward-delete-char   # Ctrl-h (Backspace)
bindkey '^W' backward-kill-word     # Ctrl-w
bindkey '^[d' kill-word             # Meta-d

# bindkey '^[?' backward-kill-word     # Meta-Backspace
bindkey '^K' kill-line              # Ctrl-k
bindkey '^U' backward-kill-line     # Ctrl-u
bindkey '^Y' yank                   # Ctrl-y
bindkey '^[y' yank-pop              # Meta-y

# Text transposition and case modification
bindkey '^T' transpose-chars        # Ctrl-t
bindkey '^[t' transpose-words       # Meta-t

bindkey '^[u' up-case-word          # Meta-u
bindkey '^[l' down-case-word        # Meta-l
bindkey '^[c' capitalize-word       # Meta-c

# Undo/Redo
bindkey '^_' undo                   # Ctrl-_
bindkey '^[/' undo                  # Alternative undo

# Line clearing and insertion
bindkey '^L' clear-screen           # Ctrl-l
bindkey '^Q' quoted-insert          # Ctrl-q

# Command history navigation
bindkey '^P' up-line-or-history     # Ctrl-p
bindkey '^N' down-line-or-history   # Ctrl-n

bindkey '^[<' beginning-of-history  # Meta-<
bindkey '^[>' end-of-history        # Meta->

bindkey '^R' history-incremental-search-backward  # Ctrl-r
bindkey '^S' history-incremental-search-forward  # Ctrl-s
bindkey '^Z' undo

# bindkey '^[p' history-search-backward  # Meta-p
# bindkey '^[n' history-search-forward  # Meta-n

bindkey '^[.' insert-last-word       # Meta-.
bindkey '^G'  send-break             # Ctrl-g (Abort)

# Completion bindings
bindkey '^I' complete-word          # TAB
bindkey '^[?' list-choices          # M-?
bindkey '^[*' expand-word           # M-*
bindkey '^[!' expand-history        # M-!
bindkey '^[~' expand-tilde          # M-~
bindkey '^[/' quoted-insert         # M-/

bindkey '^[@'  set-mark                  # M-@
bindkey '^X^X' exchange-point-and-mark  # Ctrl-x Ctrl-x (exchange-point-and-mark)
bindkey '^X^E' edit-command-line        # Ctrl-x Ctrl-e (Edit command-line in $EDITOR)

# Ensure arrow keys work
#  bindkey "$terminfo[kcuu1]" up-line-or-history    # Up arrow
#  bindkey "$terminfo[kcud1]" down-line-or-history  # Down arrow
#  bindkey "$terminfo[kcuf1]" forward-char          # Right arrow
#  bindkey "$terminfo[kcub1]" backward-char         # Left arrow

# dash POSIX dotfiles + readline keymap
alias dash="ENV=~/.env rlwrap -n dash -i"

[ -e /etc/profile.d/nix.sh ] && . /etc/profile.d/nix.sh
[ "$NIX_PATH" = "nixpkgs=$HOME/.local/state/nix/profiles/channels/nixpkgs" ] || NIX_PATH="nixpkgs=$HOME/.local/state/nix/profiles/channels/nixpkgs"
export NIX_PATH
export PATH="$PATH:$HOME/.nix-profile/bin:/nix/var/nix/profiles/default/bin"

# dwm blocks statusbar
#  DWMBAR=$(xwininfo -root -tree | grep '("dwm" "dwm")' | awk '{print $1}')
#  export DWMBAR

#  ttys=$(w | grep -c "tty[1-9]" 2>/dev/null)
#  if [ $ttys -gt 1 ]; then
#      STATUSBAR="$XDG_RUNTIME_DIR/dwmblocks.pid"
#      export STATUSBAR
#      barpid=$(pgrep dwmblock | xargs -r ps | grep "${GPG_TTY##*/}" | awk '{print $1}')
#      [ -n "$barpid" ] && echo "$barpid" > "$STATUSBAR"
#  fi

# dwmbar=$(pgrep dwmblock | xargs -r ps | grep -E "${GPG_TTY##*/}" | tail -n 1 | awk '{print $1}')
# DWMBLOCKS=${dwmbar:-"dwmblocks"}
# export DWMBLOCKS
# export DOT="$HOME/.dotf"

# Pre-export the current cmdline
preexec() { export LAST_CMD="$1" ; }
colors

# Fast syntax highlighting
source /usr/share/zsh/plugins/fast-syntax-highlighting/fast-syntax-highlighting.plugin.zsh 2>/dev/null
