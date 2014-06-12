set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/vundle/
call vundle#rc()

Bundle 'gmarik/vundle'

Bundle 'Lokaltog/vim-easymotion'
Bundle 'Lokaltog/vim-powerline'
"Bundle 'airblade/vim-gitgutter'
"Bundle 'Townk/vim-autoclose'
"Bundle 'kien/ctrlp.vim'
Bundle 'tpope/vim-fugitive'
Bundle 'vim-scripts/indent-motion'
Bundle 'mileszs/ack.vim'
Bundle 'hrp/EnhancedCommentify'
Bundle 'greyblake/vim-preview'
Bundle 'charz/multi-cscope-db'
Bundle 'mattn/emmet-vim'
Bundle 'mfukar/robotframework-vim'
Bundle 'klen/python-mode'


set laststatus=2
set t_Co=256
let g:Powline_symbols='fancy'

let g:EasyMotion_leader_key=','

filetype plugin indent on 

set backspace=2
set ts=8
set sw=4
set ts=4
set et
set hls
set autoindent
set nu

syntax on
syntax enable
"set mouse=a

"
" pyhton-mode
"
let g:pymode_rope=1

