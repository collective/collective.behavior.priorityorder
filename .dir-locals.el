((python-mode .
              (
               (eval .
                     (let ((local-path (dir-locals-find-file ".")))
                       (setenv "PYTHONPATH"
                               (shell-command-to-string
                                (concat
                                 (concat
                                  (if (stringp local-path) (file-name-directory local-path) (car local-path))
                                  "../../bin/zopepy") " -c \"import sys; print ':'.join(sys.path)\"")))))

               (eval .
                     (let ((local-path (dir-locals-find-file "."))
                           (path (if (stringp local-path)
                                     (file-name-directory local-path) (car local-path))))
                       (setq python-shell-virtualenv-path
                             (concat path "../.."
                              ;;(if (file-exists-p (concat path "../../bin/python"))
                              ;;    "../.."
                              ;;  "../../../Python-2.7")
                              ))))
               ;; (eval .
               ;;       (setq python-shell-virtualenv-path
               ;;                 "../.."
               ;;             ))
               (eval .
                     (setq python-shell-interpreter "python2"))
               )))
