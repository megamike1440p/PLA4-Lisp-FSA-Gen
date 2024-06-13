;Student Name: Whitten, Michael
;File Name: part1.lsp
;Project 4
;This is a basis for how to process an FSA in lisp. This code is used as a string with the hardcoded values replaced in lisp-fsa-gen.py
(defun fsa (input-list)
  (let ((test-string input-list)
        (alphabet-list '(x y z a))
        (transition-list '((0 0 x) (0 1 y) (1 2 x) (2 2 x) (2 3 y) (3 3 x) (3 4 z) (4 4 x) (4 1 a)))
        (current-state 0)
        (accept-state '(1 3))
        (current-index 0)
        (valid-string t))
    (dolist (current-token input-list)
      (unless (member current-token alphabet-list)
        (print "invalid token in string")
        (setq valid-string nil)
        (return)
      )
      (let ((valid-transition nil))
        (dolist (current-transition transition-list)
            ;if this
          (when (and (eql (first current-transition) current-state) (eql (third current-transition) current-token))
            ;then this
            (setq current-state (second current-transition))
            (setq valid-transition t)
          )
        )
        (unless valid-transition
          (print "invalid transition")
          (setq valid-string nil)
          (return)))
      (setq current-index (1+ current-index)))
    (if valid-string
        (if (member current-state accept-state)
            (print "valid string")
            (print "invalid string"))
        (print "invalid string"))))

(defun demo ()
  (setq fp (open "theString.txt" :direction :input))
  (let ((input-list (read fp)))
    (fsa input-list)))
(demo)