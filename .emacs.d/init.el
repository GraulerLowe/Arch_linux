;; Desactivar la barra de menú
(menu-bar-mode -1)

;; Desactivar la barra de herramientas
(tool-bar-mode -1)

;; Desactivar la barra de desplazamiento
(scroll-bar-mode -1)

;; Activar el resaltado de sintaxis
(global-font-lock-mode t)

;; Barra de Tutorial de emacs
(setq inhibit-startup-screen t)

;; Activar el resaltado de líneas activas
(global-hl-line-mode t)

;; Mostrar números de línea
(global-display-line-numbers-mode)

;; Mostrar número de columna
(column-number-mode t)

;; Mostrar corchetes coincidentes
(show-paren-mode t)

;; Utilizar espacios en lugar de tabuladores
(setq-default indent-tabs-mode nil)

;; Definir el ancho de tabulación
(setq-default tab-width 4)

;; Desactivar los archivos de respaldo
(setq make-backup-files nil)

;; Desactivar los archivos de autoguardado
(setq auto-save-default nil)

;; Desactivar el sonido de advertencia
(setq ring-bell-function 'ignore)

;; Cambiar el color de fondo
(set-face-background 'default "#011220")
;;(set-face-background 'fringe "#011220")
(set-face-background 'mode-line "#011220")
;;(set-face-background 'mode-line-inactive "#011220")
(set-face-background 'minibuffer-prompt "#011220")

;; Cambiar el color de fondo de las líneas de número
(set-face-background 'line-number "#011220")
(set-face-background 'line-number-current-line "#011220")

;; Ajustar el tamaño de la fuente
(set-face-attribute 'default nil :height 110)

(require 'package)
(setq package-archives '(("melpa" . "https://melpa.org/packages/")
                         ("gnu" . "https://elpa.gnu.org/packages/")))

(load-theme 'catppuccin :no-confirm)
;;(setq doom-theme 'catppuccin)
(setq catppuccin-flavor 'mocha) ;; or 'latte, 'macchiato, or 'mo>
;;(catppuccin-reload)

;; Habilitar el auto-completado
(require 'company)
(add-hook 'after-init-hook 'global-company-mode)

;; Configurar el atajo de teclado para abrir el archivo de confi>
(global-set-key (kbd "C-c C-c") (lambda () (interactive) (find-file "~/.emacs.d/init.el")))

(use-package doom-modeline
  :ensure t
  :init (doom-modeline-mode 1))

(use-package ivy
  :ensure t
  :config
  (ivy-mode 1))

;; Manejo de proyectos
(use-package projectile
  :ensure t
  :config
  (projectile-mode +1))

(use-package yasnippet
  :ensure t
  :config (yas-global-mode 1))

(add-to-list 'load-path "~/.emacs.d/nyan-mode")
(require 'nyan-mode)
(nyan-mode 1)

(use-package magit
  :ensure t
  :bind (("C-x g" . magit-status)))

(use-package flycheck
  :ensure t
  :init (global-flycheck-mode))

(use-package all-the-icons
  :ensure t)

;; Instalar y configurar neotree
(use-package neotree
  :ensure t
  :config
  (setq neo-theme (if (display-graphic-p) 'icons 'arrow)) ; Usa iconos si está en modo gráfico
  (global-set-key [f8] 'neotree-toggle)) ; Asigna la tecla F8 para activar/desactivar neotree 

(set-frame-font "Noto Sans Mono-12" nil t)


;; Atajo de teclado para abrir una terminal
(global-set-key (kbd "C-c t") 'ansi-term)

;;Dashboard
(require 'dashboard)
(dashboard-setup-startup-hook)
(setq initial-buffer-choice (lambda () (get-buffer-create dashboard-buffer-name)))
(setq dashboard-startup-banner "/home/graulerlowe/Imágenes/Images/fondo/ramona_writting.png")



(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages
   '(all-the-icons all-the-icons-completion all-the-icons-ibuffer
                   all-the-icons-nerd-fonts auto-complete
                   catppuccin-theme company dashboard doom-modeline
                   doom-themes exotica-theme haskell-emacs magit
                   material-theme night-owl-theme nyan-mode
                   org-dashboard racket-mode)))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
