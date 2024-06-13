#*********************************************************************************************************
#   Student Name: Whitten, Michael
#   File Name: fsa.py
#   Project 4
#
#Tokenizes an FSA and generates a lisp program to test the string
#*********************************************************************************************************
import sys

class FileReader:
    def read_file(self, file_name):
        with open(file_name) as f:
            content = f.readline()
        return content

    def read(self, fsa_file):
        fsa_content = self.read_file(fsa_file)
        tokens = fsa_content.split(';')
        return tokens

def generate_lisp(tokens):
    num_states = int(tokens[0])
    alphabet = " ".join(map(str, tokens[1].split(',')))
    transitions = " ".join(map(lambda t: f"{t.replace(':', ' ')}", tokens[2].split(',')))
    start_state = int(tokens[3])
    accept_states = " ".join(map(str, tokens[4].split(',')))
    lisp_code = f""";Student Name: Whitten, Michael
;File Name: part2.lsp
;Project 4
;Automatically generated when lisp-fsa-gen.py is run
(defun fsa (input-list)
    (let ((test-string input-list)
    (alphabet-list '({alphabet}))
    (transition-list '({transitions}))
    (current-state {start_state})
    (accept-state '({accept_states}))
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
            (when (and (eql (first current-transition) current-state) (eql (third current-transition) current-token))
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
(demo)"""
    return lisp_code

def main():
    file_reader = FileReader()
    fsa_file = str(sys.argv[1])
    tokens = file_reader.read(fsa_file)
    lisp_code = generate_lisp(tokens)
    with open('part2.lsp', 'w') as f:
        f.write(lisp_code)

if __name__ == "__main__":
    main()