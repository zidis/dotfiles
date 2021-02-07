
" Set leader to space
	let mapleader = "\<Space>"

" Remap semicolon to colon
	nmap ; :

" Split navigation
	nnoremap <C-h> <C-w>h
	nnoremap <C-j> <C-w>j
	nnoremap <C-k> <C-w>k
	nnoremap <C-l> <C-w>l

" Normal mode
	inoremap kj <Esc>
	inoremap <Esc> <Nop>

" vim-plug installation
if empty(glob('~/.vim/autoload/plug.vim'))
  silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

" Plugins
	call plug#begin('~/.vim/plugged')
		Plug 'itchyny/lightline.vim'
		Plug 'scrooloose/nerdtree'
		Plug 'vim-syntastic/syntastic'
		Plug 'chrisbra/Colorizer'
		Plug 'junegunn/goyo.vim' 
		Plug 'tpope/vim-fugitive'
		Plug 'joshdick/onedark.vim'
	call plug#end()


" Plugin settings
	" Lightline
		let g:lightline = {
      	\ 'colorscheme': 'onedark',
      	\ }

	" NerdTree
		map <Leader>n :NERDTreeToggle<CR>
	
	" Colorizer
		map <leader>c :ColorToggle<CR>

	" Vimwiki
		let g:vimwiki_list = [{'path': '~\Google Drive\personal\personal.wiki',
                     \ 'syntax': 'markdown', 'ext': '.md'}]

	" Fugitive
		nnoremap <leader>gs :Gstatus<CR>
		nnoremap <leader>gc :Gcommit -v -q<CR>
		nnoremap <leader>gp :Git push origin master<CR>		
			
	" Goyo
		nnoremap <silent> <leader>z :Goyo<CR>


" Appearance						
	set ruler
	set number relativenumber
	set cursorline
	set laststatus=2
	set noshowmode

" General
	filetype plugin on
	syntax on
	set nocompatible
	set encoding=utf-8

" Search
	set hlsearch
	set incsearch
	set ignorecase 
	set smartcase

" Behavior	
	set tabstop=4
	set linebreak
	set wrap
	set splitbelow splitright

" Enable autocompletion:
	set wildmode=longest,list,full

" Disable auto commenting on new line
	autocmd FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o

" Spell check <leader>o
	map <leader>o :setlocal spell! spelllang=en_us<CR>
	map <leader>O :setlocal spell! spelllang=el_gr<CR>

" Disable bells/visualbells
	set belloff=all

" No extra files
	set nobackup
	set noswapfile
	set noundofile

" Miscellaneous
	map! <F2> <C-R>=strftime('%c')<CR>

	map <leader>vr :e ~/.vimrc<CR>
