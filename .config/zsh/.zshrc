#!/usr/bin/env zsh
# -*- mode: sh; -*- vim: ft=sh:ts=2:sw=2:et:
# Time-stamp: <2025-08-12 22:28:23 cf>
# Box: cf [Linux 6.15.8-zen1-1-zen x86_64 GNU/Linux]
#        __       _          _ _
#   ___ / _|  ___| |__   ___| | |
#  / __| |_  / __| '_ \ / _ \ | |
# | (__|  _| \__ \ | | |  __/ | |
#  \___|_|   |___/_| |_|\___|_|_|
#
#                      cf. [zshrc] ❯⟩

autoload -U colors && colors

RESET="%{$reset_color%}"
GRAY="%{$fg[gray]%}"
BLUE="%{$fg[blue]%}"
RED="%{$fg[red]%}"
YELLOW="%{$fg[yellow]%}"
GREEN="%{$fg[green]%}"
WHITE="%{$fg[white]%}"

#PS1="%B%{$fg[red]%}[%{$fg[yellow]%}%n%{$fg[green]%}@%{$fg[blue]%}%M%{$fg[red]%}] %{$fg[magenta]%}%~%{$fg[$(if [ $? -eq 0 ]; then echo white; else echo red; fi)]%}  %{$reset_color%}%b"
# PS1="%B%{$fg[magenta]%} %~%{$fg[$(if [ $? -eq 0 ]; then echo white; else echo red; fi)]%}  %{$reset_color%}%b "
# PS1="%B%{$fg[magenta]%} %~%{$fg[$(if [ $? -eq 0 ]; then echo white; else echo red; fi)]%} ❱ %{$reset_color%}%b "

setopt prompt_subst

precmd() {
  if (( $? != 0 )); then
    PROMPT_SYMBOL_COLOR="$RED"
  else
    PROMPT_SYMBOL_COLOR="$RESET"
  fi
}

# ❯
if tty | grep -q "tty" ; then
  PS1='%B%{$fg[magenta]%}%~%{$reset_color%} ${PROMPT_SYMBOL_COLOR}>%{$reset_color%}%b '
else
  PS1='%B%{$fg[magenta]%}%~%{$reset_color%} ${PROMPT_SYMBOL_COLOR}⟩%{$reset_color%}%b '
fi

setopt autocd
stty stop undef

HISTSIZE=100000
SAVEHIST=100000
HISTFILE="$HOME/.cache/zsh/history"

# HISTORY_IGNORE='(clear|pwd|exit|* —help|[bf]g *|less *|cd ..|cd -)'

setopt BANG_HIST                 # Perform textual history expansion, csh-style, treating the character ‘!’ specially.
setopt EXTENDED_HISTORY          # Write the history file in the ':start:elapsed;command' format.
setopt INC_APPEND_HISTORY        # Write to the history file immediately, not when the shell exits.
setopt SHARE_HISTORY             # Share history between all sessions.
setopt HIST_EXPIRE_DUPS_FIRST    # Expire a duplicate event first when trimming history.
setopt HIST_IGNORE_DUPS          # Do not record an event that was just recorded again.
setopt HIST_IGNORE_ALL_DUPS      # Delete an old recorded event if a new event is a duplicate.
setopt HIST_FIND_NO_DUPS         # Do not display a previously found event.
setopt HIST_IGNORE_SPACE         # Do not record an event starting with a space.
setopt HIST_SAVE_NO_DUPS         # Do not write a duplicate event to the history file.
setopt HIST_VERIFY               # Do not execute immediately upon history expansion.
setopt HIST_REDUCE_BLANKS        # Remove superfluous blanks from each command line being added to the history list.
setopt APPEND_HISTORY            # append to history file
setopt HIST_NO_STORE             # Don't store history commands
setopt HIST_NO_FUNCTIONS         # Don't store function definitions

# typeset -g session_cmd_count=0
# job_count() {
#     (( ${#jobstates} > 0 )) && echo "${BLUE}${#jobstates}j"
# }

# exit_status() {
#     (( $? < 0 )) && echo "${RED}$?"
# }

# funcline_count() {
#     if (( $? == 0 )); then
#         local line_count=$(wc -l <<< "$last_command" 2>/dev/null | tr -d '[:space:]')
#         [[ -n "$line_count" && "$line_count" -gt 0 ]] && echo "${line_count}"
#     fi
# }

# positional_count() {
#     (( $# > 0 )) && echo ":$#"
# }

# cmd_count() {
#     [[ -n "$CMDCOUNT" ]] && echo "${GRAY}cmd:${GREEN}${CMDCOUNT}"
# }

# session_cmd_count=0
# precmd() {
#     (( session_cmd_count++ ))
# }

# hist_count() {
#     [[ "$session_cmd_count" -gt 0 ]] && echo "${YELLOW}${session_cmd_count}"
# }

# : ${prev_lines:=0}
# : ${prev_columns:=0}
# terminal_width() {
#     lines="$LINES"
#     columns="$COLUMNS"
#     if [ "$lines" -ne "$prev_lines" ] && [ "$columns" -ne "$prev_columns" ]; then
#         echo "${WHITE}${lines}${GRAY}:${WHITE}${columns}"
#         prev_lines="$LINES"
#         prev_columns="$COLUMNS"
#     else
#         echo "0"
#     fi
# }

# preexec() {
#     command_start_time=$(date +%s%3N)  # Capture start time in milliseconds
# }

# precmd() {
#     command_end_time=$(date +%s%3N)    # Capture end time in milliseconds
#     LAST_EXECUTION_TIME=$((command_end_time - command_start_time))
# }

# exec_time() {
#     local d_ms=$((LAST_EXECUTION_TIME % 1000))
#     if (( LAST_EXECUTION_TIME > 1000 )); then
#         echo "0"
#         # echo "${GREEN}${d_ms}"  # Short
#     elif (( LAST_EXECUTION_TIME > 5000)); then
#         echo "${YELLOW}${d_ms}" # Average
#     else
#         echo "${RED}${d_ms}"    # Long
#     fi
# }

# dspcnt() {
#     out="$1"
#     [[ -n "$out" && "$out" != "0" ]] && echo "${GRAY}[${RESET}${out}${GRAY}]"
# }

# prmptcnt() {
#     local cnt=""
#     cnt+=$(dspcnt "$(exec_time)")
#     cnt+=$(dspcnt "$(job_count)")
#     cnt+=$(dspcnt "$(exit_status)")
#     cnt+=$(dspcnt "$(positional_count)")
#     cnt+=$(dspcnt "$(cmd_count)")
#     cnt+=$(dspcnt "$(hist_count)")
#     cnt+="$(dspcnt ${GREEN}$(date +%H)${GRAY}:${YELLOW}$(date +%M)${GRAY}:${RED}$(date +%S))"
#     cnt+=$(dspcnt "$(terminal_width)")
#     echo -n "$cnt"
# }
# setopt prompt_subst
# PS4='%{$fg[gray][%}$(prmptcnt)%{$fg[gray]]%}'
# [ -f ".rprompt" ] && RPROMPT='$(prmptcnt)' || RPROMPT=""
# rpr() {
#     [ -f ".rprompt" ] && rm .rprompt >/dev/null || touch .rprompt >/dev/null
#     source .zshrc >/dev/null
# }

# path check
export PATH="$(echo "$PATH" | awk -v RS=: -v ORS=: '!a[$1]++' | sed 's/:$//')"

# load extra configs
SH_CONFIG="${XDG_CONFIG_HOME:-$HOME/.config}/shell"
for j in "$SH_CONFIG"/{aliases,aliasrc,functions,shortcutrc,shortcutenvrc,zshnameddirrc,ytaliases} ; do
    [ -f "$j" ] && source "$j" >/dev/null 2>&1
done

ralias() { gpg2 --quiet --no-tty --for-your-eyes-only --decrypt "$(pass ralias)" 2>/dev/null | source /dev/stdin ; }

ZDOTDIR="${XDG_CONFIG_HOME:-$HOME/.config}/zsh"
# Base comp dir init
fpath=($ZDOTDIR $fpath)

# Load zsh completion
autoload -U compinit
zstyle ':completion:*' menu select
zmodload zsh/complist
compinit
_comp_options+=(globdots)

# function for dsurfraw -e|--elvi option
_dsrfraw_elvi_completion() {
    local -a elvis
    elvis=(
        ${(f)"$(sr -elvi | cut -d'-' -f1 | sed 's/\t//g' | tr -d ' ' | awk 'nr > 1')"}
    )
    _describe 'values' elvis
}
compdef _dsrfraw_elvi_completion dsurfraw
compdef _mpv vlb
compdef _man ve
compdef _exifjpg exifjpg

# vi binds
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
alias help=run-help

# Wikiman plugin
source /usr/share/wikiman/widgets/widget.zsh
bindkey '^X^_' _wikiman_widget

#  emacs() {
#      if [[ $# -eq 0 ]]; then
#          setsid -f /usr/local/bin/emacs # "emacs" is function, will cause recursion
#          return
#      fi
#      args=($*)
#      for ((i=0; i <= ${#args}; i++)); do
#          local a=${args[i]}
#          if [[ ${a:0:1} == '-' && ${a} != '-c' && ${a} != '--' ]]; then
#              (
#                  [ -t 1 ] && devour /usr/local/bin/emacs ${args[*]}
#              ) || {
#                  setsid -f /usr/local/bin/emacs ${args[*]} >/dev/null 2>&1
#              }
#              return
#          fi
#      done
#      ( [ -t 1 ] && devour emacsclient -c -a "" ${args[*]} ) || {
#          setsid -f /usr/local/bin/emacsclient \
#                 -s ${EMACS_SOCKET_NAME:-"$XDG_RUNTIME_DIR/emacs/server"} \
#                 -cn --alternate-editor="" ${args[*]} >/dev/null 2>&1
#      }
#  }
[ -z "$(pidof -xs emacs)" ] && setsid -f /usr/local/bin/emacs -f server-start >/dev/null 2>&1

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
    tmp="$(mktemp -uq)"
    trap 'rm -f $tmp >/dev/null 2>&1 && trap - HUP INT QUIT TERM PWR EXIT' HUP INT QUIT TERM PWR EXIT
    lf -last-dir-path="$tmp" "$@"
    if [ -f "$tmp" ]; then
        dir="$(cat "$tmp")"
        [ -d "$dir" ] && [ "$dir" != "$(pwd)" ] && cd "$dir"
    fi
}

# bind lfcfd to ctrl-x ctrl-o outside emacs
[[ -z "$INSIDE_EMACS" ]] && bindkey -s '^X^o' '^ulfcd\n'
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

copy_lbuffer() {
  emulate -L zsh
  ( [ -n "$LBUFFER" ] && echo "$LBUFFER" | xclip -in -selection clipboard 2>/dev/null ) || true
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
zle -N copy_lbuffer
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
    aln=$(grep -rn "${al}=" ~/.config/(shell|zsh) | grep -vE '[~#]' | awk -F ':' '{print $1, $2}')
    f=$(echo "$fnl" | awk '{print $1}')
    l=$(echo "$fnl" | awk '{print $2}')
    devour emacsclient -s "$EMACS_SOCKET_NAME" -a "" -c "+${l}" "$f" || true
}

is_fn_type() {
    fn="$1"
    fnl=$(grep -rn "${fn}() " ~/.config/(shell|zsh) | grep -vE '[~#]' | awk -F ':' '{print $1, $2}' )
    f=$(echo "$fnl" | awk '{print $1}')
    l=$(echo "$fnl" | awk '{print $2}')
    devour emacsclient -s "$EMACS_SOCKET_NAME" -a "" -c "+${l}" "$f" || true
}

is_file_type() {
    devour emacsclient -s "$EMACS_SOCKET_NAME" -a "" -c "$(is_file_type "$t")" || true
}

emtype() {
    t=$(get_last_arg)
    wt=$(type -w "$t" | awk '{print $2}')
    case "$wt" in
        'alias') is_alias_type "$t" || return 1 ;;
        'function') is_fn_type "$t" || return 1 ;;
        *) if ! is_file_type "$t" ; then
               devour emacsclient -s "$EMACS_SOCKET_NAME" -a "" -c -n "$t"  || true
           else
               return 1
           fi
           ;;
    esac
    return
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
   dwmswallow $WINDOWID
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

# __fzfmenu__() {
#   local cmd="fd -tf --max-depth=1"
#   eval $cmd | ~/.local/bin/fzfmenu
# }
# __fzf-menu__() {
#   LBUFFER="${LBUFFER}$(__fzfmenu__)"
#   local ret=$?
#   zle reset-prompt
#   return $ret
# }
# zle     -N    __fzf-menu__
# bindkey -M emacs '^T^G' __fzf-menu__
# bindkey -M vicmd '^T^G' __fzf-menu__
# bindkey -M viins '^T^G' __fzf-menu__

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
    find ~/.config/{mpv,lf,nsxiv,nvim,shell,x11,zathura,picom,ncmpcpp,newsboat,mpd,ytfzf,zsh,yazi} ~/.local/src/{dwm,st,dmenu,dwmblocks} ~/Templates/{nix,dwm,dwmblocks,xmouseless,st,dotfiles} ~/.local/bin -type f | \
        grep -vE '[#~]' | fzf --multi --print0 |\
        while IFS= read -r -d '' f; do
            if [ -f "$f" ] || [ -d "$f" ]; then
                emc "$f" || { echo "failed to open $f" >&2 ; return 1 ; }
                echo "$f" | grep -Eq '(alias|zsh|functions)' && { zle -I; source "$f" 2>/dev/null ; continue; }
            fi
        done
    return 0
}
zle -N cfg-edit
bindkey '^X^F' cfg-edit

fzf-rsync () { "$HOME/.local/bin/fzhsync" "$@" || return 1 ; return  0 ; }
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

# editzshrc() {
#     $EDITOR /home/cf/.config/zsh/.zshrc
#     zle -I; source /home/cf/.config/zsh/.zshrc
# }
# zle -N editzshrc
# bindkey '^X^Z' editzshrc

editzshrc() {
   ( $EDITOR ~/.zshrc ; setsid -f "$TERMINAL" >/dev/null 2>&1 ; exit ) || return 1
   zle -I ; exit ; zle accept-line 2>/dev/null || return 1
   return 0
}
zle -N editzshrc
bindkey '^X^Z' editzshrc

tmux-attach-to() {
    zle -I ; LBUFFER="tmux-attach" ; zle accept-line 2>/dev/null || return 1
}
zle -N tmux-attach-to
[[ -z "$TMUX" ]] && bindkey '^X^A' tmux-attach-to

primary_echo() {
    xa_listen -x
}
zle -N primary_echo
# ctrl-x ctrl-v
bindkey '^X^v' primary_echo

# swalminibuffer() {
#     xswal -t "minibuffer" || return 1 ;
#     return 0 ;
# }
# zle -N swalminibuffer
# ctrl-x ctrl-g when terminal is not in Emacs
# [[ -z "$INSIDE_EMACS" ]] && bindkey '^X^G' swalminibuffer

sshop() {
    emulate -L zsh
    t=$(grep -iE '^(host)\s? ' ~/.ssh/config| sed 's/^Host //;s/[[:space:]]//g' | fzf)
    ( [ -n "$t" ] && ssh "${t}" ) || return 1
    return 0
}
zle -N sshop
bindkey -M viins '^X^S' sshop
bindkey -M vicmd '^X^S' sshop
bindkey -M emacs '^X^S' sshop

# plugin sourcing
source /usr/share/nvm/init-nvm.sh

. "$HOME/.local/share/cargo/env"

# eval "$(zoxide init zsh)"
# eval "$(luarocks  path --bin)"

# yazi
export YAZI_CONFIG_HOME="$HOME/.config/yazi"
export YAZI_FILE_ONE="$(which file)"
export YAZI_ZOXIDE_OPTS="--recent"

y() {
    tmp="$(mktemp -t "yazi-cwd.XXXXXX")" cwd
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

dwmbar=$(pgrep dwmblock | xargs -r ps | grep ${GPG_TTY##*/} | awk '{print $1}')
DWMBLOCKS=${dwmbar:-"dwmblocks"}
export DWMBLOCKS
export DOT="$HOME/.dotf"

# Pre-export the current cmdline
preexec() { export LAST_CMD="$1" ; }

export PATH="$PATH:$HOME/.nix-profile/bin:/nix/var/nix/profiles/default/bin"

# Fast syntax highlighting
source /usr/share/zsh/plugins/fast-syntax-highlighting/fast-syntax-highlighting.plugin.zsh 2>/dev/null
