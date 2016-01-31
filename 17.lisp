;;one two three four five six seven eight nine ten eleven twelve thirteen bla bla bla

(defun generate-numbers ()
  (let ((result "one") (txt nil))
    (dotimes (x 1001)
      (when (> x 1)
        (setf txt (format nil "~r" x))
        (setf result (concatenate 'string result txt))
        ))
    (print result)
    result))
(generate-numbers)
