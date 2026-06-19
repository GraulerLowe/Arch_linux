;;===============================
;;Configuración de emacs
;;===============================


;; ===============================
;; 1. Optimización de arranque
;; ===============================
(setq gc-cons-threshold (* 50 1000 1000))

(add-hook 'emacs-startup-hook
          (lambda ()
            (setq gc-cons-threshold (* 2 1000 1000))))

;; ===============================
;; 2. Configuración de Paquetes (Idempotencia)
;; ===============================
(require 'package)
(setq package-archives '(("melpa" . "https://melpa.org/packages/")
                         ("gnu" . "https://elpa.gnu.org/packages/")))
(package-initialize)

;; Instalar use-package si no existe
(unless (package-installed-p 'use-package)
  (package-refresh-contents)
  (package-install 'use-package))

(require 'use-package)
;; Forzar que todos los paquetes se instalen automáticamente
(setq use-package-always-ensure t)

;; ===============================
;; 3. Interfaz y UI
;; ===============================
(menu-bar-mode -1)
(tool-bar-mode -1)
(scroll-bar-mode -1)
(global-font-lock-mode t)
(setq inhibit-startup-screen t)
(global-hl-line-mode t)
(global-display-line-numbers-mode)
(column-number-mode t)
(show-paren-mode t)
(setq-default indent-tabs-mode nil)
(setq-default tab-width 4)
(setq make-backup-files nil)
(setq auto-save-default nil)
(setq ring-bell-function 'ignore)

;; Scrolling fluido
(setq scroll-margin 5
      scroll-conservatively 101
      scroll-step 1
      fast-but-imprecise-scrolling t)

;; Transparencia (Hyprland)
;;(set-frame-parameter nil 'alpha-background 90)
;;(add-to-list 'default-frame-alist '(alpha-background . 90))

;; ===============================
;; 4. Paquetes Visuales y Temas
;; ===============================
(use-package doom-themes
  :config
  (load-theme 'doom-xcode t))

(use-package doom-modeline
  :init (doom-modeline-mode 1))

(use-package nyan-mode
  :config (nyan-mode 1))

(use-package all-the-icons)

(use-package dashboard
  :config
  (dashboard-setup-startup-hook)
  (setq dashboard-startup-banner "/home/grauler/Imágenes/meiko_solanin.jpg")
  (setq initial-buffer-choice (lambda () (get-buffer-create dashboard-buffer-name))))

;; ===============================
;; 5. Herramientas de Desarrollo 
;; ===============================

;; Auto-completado global
(use-package company
  :config
  (global-company-mode t))

;; C++ y LSP 
(use-package lsp-mode
  :hook ((c++-mode . lsp)
         (c-mode . lsp)
         (rust-mode . lsp))
  :commands lsp
  :config
  (setq lsp-idle-delay 0.1))

(use-package lsp-ui :commands lsp-ui-mode)
(setq dired-listing-switches "-alh")
;; Manejo de proyectos
(use-package projectile
  :config (projectile-mode +1))

(use-package magit
  :bind (("C-x g" . magit-status)))
(with-eval-after-load 'magit-mode
  (add-hook 'after-save-hook 'magit-after-save-refresh-status t))

(use-package flycheck
  :init (global-flycheck-mode))

(use-package yasnippet
  :config (yas-global-mode 1))

;; Terminal integrada
(use-package vterm)

;; Explorador de archivos
(use-package treemacs
  :bind ([f8] . treemacs))

;; ===============================
;; 6. Atajos de teclado y fuentes
;; ===============================
(global-set-key (kbd "C-c C-c") (lambda () (interactive) (find-file "~/.emacs.d/init.el")))
(global-set-key (kbd "C-c t") 'vterm)

;; Configuración de fuente (Ajusta el nombre si no tienes Ubuntu Mono)
(set-face-attribute 'default nil :family "Ubuntu Mono" :height 120)
(add-to-list 'default-frame-alist '(font . "Ubuntu Mono-12"))

(use-package ivy
  :ensure t
  :config
  (ivy-mode 1))

;; ===============================
;; 7. Custom-set (Generado por Emacs)
;; ===============================
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-safe-themes
   '("4780d7ce6e5491e2c1190082f7fe0f812707fc77455616ab6f8b38e796cbffa9"
     default))
 '(ein:jupyter-server-use-subcommand "server")
 '(package-selected-packages
   '(cargo-mode company creamsody-theme dashboard django-mode
                doom-modeline doom-themes easy-theme-preview ein
                exec-path-from-shell flycheck flycheck-rust ivy
                javap-mode lsp-java lsp-mode magit nyan-mode org
                rust-mode treemacs vterm yuck-mode)))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
